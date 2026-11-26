"""Write one small Markdown reference file per package."""
import re

from . import classify as C
from .sources import vkey

CAPS = {C.BREAKING: 24, C.REMOVED: 14, C.DEPRECATED: 12, C.MINVER: 6, C.NEW: 18}
THIN = "no details in release notes"


def file_name(pkg_name):
    return re.sub(r"[^a-z0-9._-]+", "__", pkg_name.lower().lstrip("@")) + ".md"


def _majors(dates, cutoff):
    """First stable release of every major line published after the cut-off (registry facts)."""
    first = {}
    for v, d in dates.items():
        if re.fullmatch(r"\d+(\.\d+){1,3}", v) and d > cutoff:
            k = vkey(v)
            if k[0] not in first or k < vkey(first[k[0]]):
                first[k[0]] = v
    older = {vkey(v)[0] for v, d in dates.items() if re.fullmatch(r"\d+(\.\d+){1,3}", v) and d <= cutoff}
    return [(first[m], dates[first[m]]) for m in sorted(first) if m not in older and m > 0]


def render(pkg, dates, releases, problems, cutoff, built, summarised=False):
    """Return (markdown, stats)."""
    stable = {v: d for v, d in dates.items() if re.fullmatch(r"\d+(\.\d+){1,3}", v)}
    latest = max(stable, key=vkey) if stable else None
    after = sorted((v for v, d in stable.items() if d > cutoff), key=vkey)
    out = [f"# {pkg['name']} ({pkg['ecosystem']}): changes after {cutoff}", ""]
    if latest:
        out.append(f"- Latest stable on the registry: **{latest}** ({stable[latest]}). Built {built}.")
    else:
        out.append(f"- Registry metadata unavailable. Built {built}.")
    if after:
        out.append(f"- {len(after)} stable releases after the cut-off: {after[0]} ({stable[after[0]]}) "
                   f"to {after[-1]} ({stable[after[-1]]}).")
    majors = _majors(dates, cutoff)
    if majors:
        out.append("- New major versions since the cut-off: " + ", ".join(f"{v} ({d})" for v, d in majors) + ".")
    out.append("- Lines below are quoted from upstream release notes and sorted by keyword rules"
               + ("; then compressed by a model" if summarised else "") + ". Not reviewed by a person."
               " Open the source link before relying on one.")
    out.append("")
    counts = {c: 0 for c in C.CATEGORIES}
    shown = 0
    for cat in C.CATEGORIES:
        groups = [(r, [t for c, t in r.items if c == cat]) for r in releases]
        groups = [(r, ts) for r, ts in groups if ts]
        total = sum(len(ts) for _, ts in groups)
        counts[cat] = total
        if not total:
            continue
        if cat == C.NEW:    # feature releases first, then newest first
            groups.sort(key=lambda g: (vkey(g[0].version)[2] != 0, [-x for x in vkey(g[0].version)]))
        out.append(f"## {C.TITLES[cat]}")
        left = CAPS[cat]
        for r, ts in groups:
            if left <= 0:
                break
            take = ts[:min(left, 8 if cat != C.BREAKING else 12)]
            out.append(f"### {r.version} ({r.date}) [source]({r.source})")
            out += [f"- {t}" for t in take]
            left -= len(take)
            shown += len(take)
        omitted = total - (CAPS[cat] - left)
        if omitted > 0:
            out.append(f"- ({omitted} more in this category not shown; see the changelog.)")
        out.append("")
    with_notes = [r for r in releases if r.items]
    thin = [r for r in releases if not r.items]
    covered = {vkey(r.version) for r in releases}
    missing = [v for v in after if vkey(v) not in covered]
    if not any(counts.values()):
        out.append("## Changes")
        if not releases:
            out.append(f"- {THIN}: no release notes for this package could be read by this build"
                       + (f" ({'; '.join(problems)})." if problems else "."))
        else:
            out.append(f"- {THIN}: {len(releases)} releases were read and none mentions a breaking change, "
                       "removal, deprecation or new API in words these rules recognise.")
        out.append("")
    out.append("## Coverage")
    if releases:
        out.append(f"- Release notes read for {len(releases)} releases; {len(with_notes)} had extractable items.")
    if thin:
        vs = [r.version for r in thin]
        out.append(f"- {THIN} (fixes only, or nothing these rules recognise): "
                   + ", ".join(vs[:12]) + (f" and {len(vs) - 12} more" if len(vs) > 12 else "") + ".")
    if missing and releases:
        out.append(f"- {len(missing)} other registry releases after the cut-off have no separate notes in these "
                   "sources (often patch releases).")
    for p in problems:
        out.append(f"- Source not reachable in this build: {p}")
    srcs = []
    for s in pkg["sources"]:
        srcs.append(s.get("url") or f"https://github.com/{s['repo']}/releases")
    out.append("- Sources: " + ", ".join(srcs) + f"; registry ({pkg['ecosystem']}) for dates.")
    out.append("")
    stats = {"name": pkg["name"], "latest": latest, "after": len(after), "releases_read": len(releases),
             "with_items": len(with_notes), "counts": counts, "shown": shown, "problems": problems,
             "usable": bool(with_notes), "majors": majors,
             "status": ("items" if with_notes else "source unreachable" if problems and not releases
                        else "no stable release after cut-off" if not after
                        else "notes read, nothing matched" if releases else "no notes found")}
    return "\n".join(out), stats
