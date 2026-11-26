"""Split normalised blocks into releases and pull digest items out of each release."""
import re
from dataclasses import dataclass, field

from . import classify as C

_PRE = r"(?:[-.]?(?:alpha|beta|rc|canary|dev|next|pre|preview|nightly|insiders|experimental|a|b|c|post)[-.]?\d*(?:[.-]\w+)*)"
_VER = re.compile(r"v?(\d+\.\d+(?:\.\d+){0,2}" + _PRE + r"?)(?=$|[\s(,:/—–\-\]])", re.I)
PRERELEASE = re.compile(r"\d" + _PRE + r"$|[-]\w", re.I)
_PENDING = re.compile(r"^(unreleased|main|master|latest changes|next|upcoming|in development|trunk)\b", re.I)
_MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}


@dataclass
class Release:
    version: str
    heading: str = ""
    date: str = ""            # ISO date, from the registry when known, else from the heading
    date_from: str = ""       # "registry" | "heading"
    source: str = ""          # link shown next to every item of this release
    blocks: list = field(default_factory=list)
    default_category: str = None
    items: list = field(default_factory=list)   # (category, text)
    has_text: bool = False
    raw: str = ""             # the upstream text this release was cut from (whole file or release body)
    untraced: int = 0         # items dropped by trace() because they could not be found in `raw`


def clean_heading(h):
    h = re.sub(r"<[^>]+>", "", h)
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
    h = h.replace("`", "").replace("*", "").replace("[", "").replace("]", "")
    return h.strip()


def heading_version(h, aliases):
    """Return the version a heading announces, or None. Only accepts a bare version or one
    prefixed by the package name / 'Version' / 'Release', so 'Python 3.9 dropped' is not a release."""
    t = clean_heading(h)
    names = "|".join(re.escape(a) for a in sorted(aliases, key=len, reverse=True) if a)
    prefix = re.compile(r"^(?:(?:version|release|ver\.?|what'?s new in|" + names + r")[\s@:-]*)*", re.I)
    rest = t[prefix.match(t).end():]
    m = _VER.match(rest)
    if not m or re.match(r"\s*(change ?log|series|\.x|and )", rest[m.end():], re.I):
        return None
    return m.group(1)


def heading_date(h):
    t = clean_heading(h)
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", t)
    if m:
        return m.group(0)
    m = re.search(r"([A-Za-z]{3,9})\.? (\d{1,2})(?:st|nd|rd|th)?,? (\d{4})", t)
    if m and m.group(1)[:3].lower() in _MONTHS:
        return f"{m.group(3)}-{_MONTHS[m.group(1)[:3].lower()]:02d}-{int(m.group(2)):02d}"
    m = re.search(r"(\d{1,2})(?:st|nd|rd|th)? ([A-Za-z]{3,9})\.?,? (\d{4})", t)
    if m and m.group(2)[:3].lower() in _MONTHS:
        return f"{m.group(3)}-{_MONTHS[m.group(2)[:3].lower()]:02d}-{int(m.group(1)):02d}"
    return ""


def slug(h):
    """GitHub's anchor for a Markdown heading (close approximation)."""
    t = re.sub(r"<[^>]+>", "", h)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[`*]", "", t).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def split_releases(blocks, aliases):
    """Every heading that announces a version starts a release, whatever its level."""
    releases, cur, seen = [], None, set()
    for b in blocks:
        if b[0] == "h":
            v = heading_version(b[2], aliases)
            if v and v not in seen:
                seen.add(v)
                cur = Release(version=v, heading=b[2], date=heading_date(b[2]))
                cur.date_from = "heading" if cur.date else ""
                cur.level = b[1]
                releases.append(cur)
                continue
            if v is None and _PENDING.match(clean_heading(b[2])):
                cur = None
                continue
            if v:      # repeated version heading (e.g. a table of contents): keep collecting
                continue
        if cur is not None:
            cur.blocks.append(b)
    return releases


_TRAIL = re.compile(r"(\s*\(?\[?(#\d+|[0-9a-f]{7,40}|`[0-9a-f]{7,40}`)\]?(\([^)]*\))?\)?[,;]?)+\s*\.?$")


_HTML = re.compile(r"</?(a|br|details|summary|sub|sup|img|p|div|span|kbd|b|i|em|strong|h\d|picture|source)\b[^>]*>", re.I)


def _strip_html(t):
    """Drop layout tags but keep anything inside backticks (`<Activity />` is an API name)."""
    parts = re.split(r"(`[^`]*`)", t)
    return "".join(x if x.startswith("`") else _HTML.sub("", x) for x in parts)


def clean_item(t):
    t = _strip_html(t)
    # changesets: "[#123](url) [`abc`](url) Thanks [@user](url)! - text"
    t = re.sub(r"^.{0,220}?Thanks .{0,160}?! - ", "", t)
    t = re.sub(r"^\[?`?[0-9a-f]{7,40}`?\]?(\([^)]*\))?:?\s+", "", t)          # leading commit hash
    t = re.sub(r"^`?#\d+ <[^>]+>`_:?\s*", "", t)                               # towncrier rst issue link
    t = re.sub(r"^\[?#\d+\]?(\([^)]*\))?:\s*", "", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)                                # images
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)                            # links -> text
    t = re.sub(r"\s*-\s*#\d+,\s*thanks @[\w-]+!?\s*$", "", t)
    t = re.sub(r"\(`\)", "", t)
    t = re.sub(r"\s+(by|thanks to|thanks) @[\w-]+( and @[\w-]+)*( in \S+)?", "", t, flags=re.I)
    t = re.sub(r"\s+in https://github\.com/\S+", "", t)
    t = re.sub(r"https://github\.com/\S+/(pull|issues|commit)/\S+", "", t)
    t = re.sub(r"\((closes|fixes|refs?|see|gh-?|pr )?\s*#?\d+(,\s*#?\d+)*\)", "", t, flags=re.I)
    t = re.sub(r"\(\s*(#\d+[,\s]*)+\)", "", t)
    t = re.sub(r"\s*\(\s*@[\w-]+(,?\s*(and\s+)?@[\w-]+)*(\s*(in\b|:)\s*[^)]*)?\)?\.?(?=$|\s)", "", t)   # (@user in #1)
    for _ in range(3):
        t = _TRAIL.sub("", t)
    t = re.sub(r"(?<=\s)\(\s*[,;]?\s*\)", "", t)
    t = t.replace("**", "").replace("__", "")
    t = re.sub(r"\s+", " ", t).strip(" -–—:;,")
    t = re.sub(r"\s+([.,;:])", r"\1", t)
    return t


def shorten(t, limit):
    if len(t) <= limit:
        return t
    cut = t[:limit]
    dot = max(cut.rfind(". "), cut.rfind("; "))
    if dot > limit * 0.55:
        return cut[:dot + 1].rstrip() + " […]"
    return cut[:cut.rfind(" ")].rstrip(" ,;:") + " […]"


_NOT_A_CHANGE = re.compile(r"codemod|upgrade manually|coding agent|^install|getting started|introduction|overview|"
                           r"^summary|table of contents|acknowledg|contributors|^notes?$|^other\b|^general$|"
                           r"^miscellaneous", re.I)


def extract(release, limit=230):
    """Fill release.items with (category, text). Text is upstream's wording, cleaned and truncated."""
    items, seen = [], set()
    stack = []                       # (level, category or None, is_item_heading)
    paras_under = 0

    def add(cat, text):
        text = shorten(clean_item(text), limit)
        if cat and cat != C.SKIP and len(text) >= 12 and text.lower() not in seen:
            seen.add(text.lower())
            items.append((cat, text))

    def context(default=None):
        for _, cat, _ in reversed(stack):
            if cat:
                return cat
        return default

    blocks = release.blocks
    for i, b in enumerate(blocks):
        if b[0] == "h":
            release.has_text = True
            title = clean_heading(b[2])
            while stack and stack[-1][0] >= b[1]:
                stack.pop()
            parent = context(release.default_category)
            own = C.heading_category(title)
            is_item = False
            if own is None and not _NOT_A_CHANGE.search(title) and parent in (C.BREAKING, C.REMOVED, C.DEPRECATED, C.NEW, C.MINVER):
                # e.g. NumPy / Django / TypeScript notes: each change is its own sub-heading
                nxt = blocks[i + 1] if i + 1 < len(blocks) else None
                text = title + (": " + nxt[1] if nxt and nxt[0] == "p" else "")
                add(C.MINVER if C.item_category(text, None) == C.MINVER else parent, text)
                is_item = True
            stack.append((b[1], own, is_item))
            paras_under = 0
            continue
        release.has_text = release.has_text or len(b[1]) > 20
        ctx = context()
        if b[0] == "li":
            text = clean_item(b[1])
            add(C.item_category(text, ctx), b[1])
        elif b[0] == "li2":              # nested bullet: kept only when it is itself a change of contract
            cat = C.item_category(clean_item(b[1]), None)
            if cat in (C.BREAKING, C.REMOVED, C.DEPRECATED, C.MINVER):
                add(cat, b[1])
        else:
            paras_under += 1
            if stack and stack[-1][2]:
                continue                 # already quoted with its heading
            own = stack[-1][1] if stack else None
            if own in (C.BREAKING, C.REMOVED, C.DEPRECATED, C.MINVER) and paras_under <= 2:
                add(own, b[1])
            elif C._MINVER.search(b[1]) or C._MINVER2.search(b[1]):
                add(C.MINVER, b[1])
    release.items = items
    return release


def _norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


_INDEX_CACHE = {}


def _index(raw):
    key = id(raw)
    if key not in _INDEX_CACHE:
        _INDEX_CACHE.clear()                 # one upstream file at a time
        words, pos = _norm(raw).split(), {}
        for i, w in enumerate(words):
            pos.setdefault(w, []).append(i)
        _INDEX_CACHE[key] = (raw, words, pos)
    return _INDEX_CACHE[key][1:]


def is_traceable(text, raw, share=0.85):
    """True when the item's words occur in the upstream text, in order and close together.
    Cleaning only deletes things (links, hashes, credits), so a genuine quote always passes."""
    words = _norm(text.replace("[…]", "")).split()
    if not words:
        return False
    raw_words, pos = _index(raw)
    if any(w not in pos for w in words) and sum(w in pos for w in words) < share * len(words):
        return False
    k = min(range(len(words)), key=lambda i: len(pos.get(words[i], ())) or 10 ** 9)
    for p in pos.get(words[k], [])[:400]:
        lo, hi = max(0, p - 3 * k - 12), p + 3 * (len(words) - k) + 12
        j, hit = lo, 0
        for w in words:
            try:
                j = raw_words.index(w, j, hi) + 1
                hit += 1
            except ValueError:
                pass
        if hit >= share * len(words):
            return True
    return False


def trace(release):
    """Guard against anything that is not upstream's wording. Returns the number of items dropped."""
    kept = [(c, t) for c, t in release.items if is_traceable(t, release.raw)]
    release.untraced = len(release.items) - len(kept)
    release.items = kept
    return release.untraced
