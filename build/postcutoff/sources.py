"""Where release notes come from. Every source returns Release objects (see parse.py).

Source kinds in packages.json:
  {"kind": "changelog", "url": "<raw file url>", "format": "md"|"rst"}
      one file with a heading per version.
  {"kind": "per_version", "url": "<raw url with {version} {major} {minor} {mm}>", "format": ...,
   "default": "breaking"|"new"|null}
      one file per release (pandas, NumPy, Django, TypeScript, Next.js upgrade guides).
  {"kind": "github_releases", "repo": "owner/name"}
      GitHub Releases API. Unauthenticated works within rate limits; GITHUB_TOKEN raises them.
Registry metadata (npm, PyPI) supplies the publish date of every version and is fetched for all packages.
"""
import os
import re
import urllib.parse

from .fetch import FetchError
from .normalise import to_blocks, _rst_inline
from .parse import Release, split_releases, slug


def is_prerelease(v):
    return not re.fullmatch(r"\d+(\.\d+){1,3}", v)


def vkey(v):
    k = [int(x) for x in re.findall(r"\d+", v)[:4]]
    return tuple(k + [0] * (3 - len(k)))


def registry_dates(fetcher, ecosystem, name):
    """Return {version: ISO date} from the package registry."""
    if ecosystem == "npm":
        doc = fetcher.get_json("https://registry.npmjs.org/" + urllib.parse.quote(name, safe="@"))
        return {v: t[:10] for v, t in doc.get("time", {}).items() if v not in ("created", "modified")}
    doc = fetcher.get_json(f"https://pypi.org/pypi/{name}/json")
    out = {}
    for v, files in doc.get("releases", {}).items():
        times = [f["upload_time_iso_8601"][:10] for f in files if not f.get("yanked")]
        if times:
            out[v] = min(times)
    return out


def human_url(raw_url):
    m = re.match(r"https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.*)", raw_url)
    if not m:
        return raw_url
    return f"https://github.com/{m.group(1)}/{m.group(2)}/blob/{m.group(3)}/{urllib.parse.quote(m.group(4))}"


def lookup_date(dates, version):
    for v in (version, version + ".0", version + ".0.0", re.sub(r"\.0$", "", version)):
        if v in dates:
            return v, dates[v]
    return version, ""


def from_changelog(fetcher, src, aliases, dates):
    fmt = src.get("format", "md")
    text = fetcher.get(src["url"])
    page = human_url(src["url"])
    releases = split_releases(to_blocks(text, fmt), aliases)
    for r in releases:
        _, d = lookup_date(dates, r.version)
        if d:
            r.date, r.date_from = d, "registry"
        r.raw = text if fmt != "rst" else text + "\n" + _rst_inline(text)
        r.source = page + ("#" + slug(r.heading) if fmt == "md" and src["url"].endswith((".md", ".mdx")) else "")
    return releases


def from_per_version(fetcher, src, aliases, dates, cutoff):
    """Try the URL template for every stable registry version published after the cut-off."""
    fmt = src.get("format", "md")
    releases, tried = [], set()

    def url_for(v):
        parts = (v.split(".") + ["0", "0"])[:3]
        return src["url"].format(version=v, major=parts[0], minor=parts[1], mm=f"{parts[0]}.{parts[1]}")

    # a file shared by a whole series (version-16.mdx, "TypeScript 5.9.md") belongs to the first
    # release of that series, and only counts if that first release is after the cut-off
    for v in sorted((v for v in dates if not is_prerelease(v)), key=vkey):
        url = url_for(v)
        if url in tried:
            continue
        tried.add(url)
        if dates[v] <= cutoff:
            continue
        try:
            text = fetcher.get(url.replace(" ", "%20"))
        except FetchError as e:
            if e.status == 404:
                continue
            raise
        r = Release(version=v, heading="", date=dates[v], date_from="registry", source=human_url(url))
        r.default_category = src.get("default")
        r.raw = text if fmt != "rst" else text + "\n" + _rst_inline(text)
        r.blocks = [b for b in to_blocks(text, fmt)]
        releases.append(r)
    return releases


def from_github_releases(fetcher, src, aliases, dates, cutoff):
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    releases = []
    for page in range(1, 11):
        data = fetcher.get_json(
            f"https://api.github.com/repos/{src['repo']}/releases?per_page=100&page={page}", headers)
        if not data:
            break
        for rel in data:
            if rel.get("draft"):
                continue
            tag = rel.get("tag_name") or ""
            prefix = src.get("tag_prefix")
            if prefix is not None and not tag.startswith(prefix):
                continue
            m = re.search(r"\d+\.\d+(\.\d+)*\S*$", tag)
            if not m:
                continue
            r = Release(version=m.group(0), heading=rel.get("name") or tag,
                        date=(rel.get("published_at") or "")[:10], date_from="github",
                        source=rel.get("html_url") or "")
            r.raw = rel.get("body") or ""
            r.blocks = to_blocks(r.raw, "md")
            releases.append(r)
        if (data[-1].get("published_at") or "9999")[:10] <= cutoff:
            break
    return releases


_CANDIDATES = [("CHANGELOG.md", "md"), ("HISTORY.md", "md"), ("CHANGES.md", "md"), ("History.md", "md"),
               ("CHANGES.rst", "rst"), ("CHANGELOG.rst", "rst"), ("NEWS.rst", "rst"), ("docs/changelog.md", "md")]


def discover(fetcher, pkg):
    """Sources for a package nobody configured: follow the registry's repository link, look for a
    changelog file in the usual places, then fall back to GitHub Releases."""
    repo = ""
    try:
        if pkg["ecosystem"] == "npm":
            doc = fetcher.get_json("https://registry.npmjs.org/" + urllib.parse.quote(pkg["name"], safe="@"))
            r = doc.get("repository") or {}
            urls = [r.get("url", "") if isinstance(r, dict) else str(r), doc.get("homepage") or ""]
            sub = r.get("directory", "") if isinstance(r, dict) else ""
        else:
            info = fetcher.get_json(f"https://pypi.org/pypi/{pkg['name']}/json").get("info", {})
            urls = list((info.get("project_urls") or {}).values()) + [info.get("home_page") or ""]
            sub = ""
    except FetchError:
        return []
    for u in urls:
        m = re.search(r"github\.com[/:]([\w.-]+)/([\w.-]+?)(?:\.git)?(?:[/#]|$)", u or "")
        if m:
            repo = f"{m.group(1)}/{m.group(2)}"
            break
    if not repo:
        return []
    found = []
    for base in ([sub + "/"] if sub else []) + [""]:
        for name, fmt in _CANDIDATES:
            url = f"https://raw.githubusercontent.com/{repo}/HEAD/{base}{name}"
            try:
                fetcher.get(url)
            except FetchError:
                continue
            found.append({"kind": "changelog", "url": url, "format": fmt})
            break
        if found:
            break
    return found + [{"kind": "github_releases", "repo": repo}]


def collect(fetcher, pkg, cutoff, log):
    """Return (dates, releases_after_cutoff, problems). Earlier sources win for a given version."""
    aliases = {pkg["name"], pkg["name"].split("/")[-1], pkg["name"].lstrip("@").replace("/", "-")}
    aliases |= set(pkg.get("aliases", []))
    problems = []
    try:
        dates = registry_dates(fetcher, pkg["ecosystem"], pkg["name"])
    except FetchError as e:
        dates = {}
        problems.append(f"registry: {e}")
    by_version = {}
    if not pkg.get("sources"):
        pkg["sources"] = discover(fetcher, pkg)
        log(f"    discovered: {[s.get('url') or s.get('repo') for s in pkg['sources']] or 'nothing'}")
    for src in pkg["sources"]:
        try:
            if src["kind"] == "changelog":
                rels = from_changelog(fetcher, src, aliases, dates)
            elif src["kind"] == "per_version":
                rels = from_per_version(fetcher, src, aliases, dates, cutoff)
            elif src["kind"] == "github_releases":
                rels = from_github_releases(fetcher, src, aliases, dates, cutoff)
            else:
                raise ValueError("unknown source kind " + src["kind"])
        except FetchError as e:
            problems.append(f"{src['kind']} {src.get('repo') or src.get('url')}: HTTP {e.status} {e.reason}".strip())
            continue
        kept = 0
        for r in rels:
            if is_prerelease(r.version) or not r.date or r.date <= cutoff:
                continue
            key = vkey(r.version)
            if key not in by_version:
                by_version[key] = r
                kept += 1
        log(f"    {src['kind']}: {len(rels)} releases parsed, {kept} stable after {cutoff}")
    return dates, [by_version[k] for k in sorted(by_version, reverse=True)], problems
