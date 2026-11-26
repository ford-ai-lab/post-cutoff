#!/usr/bin/env python3
"""Build the post-cutoff skill folders.

    python3 build/build.py                         # all packages, cut-off from packages.json
    python3 build/build.py --only react,pandas     # some packages
    python3 build/build.py --cutoff 2025-01-01     # another cut-off
    python3 build/build.py --offline               # from cache only

Standard library only. No model is called (see postcutoff/summarise.py for the hook).
"""
import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from postcutoff import parse, render, sources, summarise  # noqa: E402
from postcutoff.fetch import Fetcher  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = {"npm": "post-cutoff-js", "pypi": "post-cutoff-python"}
LABEL = {"npm": "JavaScript / TypeScript (npm)", "pypi": "Python (PyPI)"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--packages", default=os.path.join(HERE, "packages.json"))
    ap.add_argument("--cutoff")
    ap.add_argument("--out", default=os.path.join(HERE, "..", "skills"))
    ap.add_argument("--cache", default=os.path.join(HERE, ".cache"))
    ap.add_argument("--only", default="")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--date", help="build date stamp (default: today, UTC)")
    args = ap.parse_args()

    cfg = json.load(open(args.packages))
    default_list = os.path.abspath(args.packages) == os.path.join(HERE, "packages.json")
    cutoff = args.cutoff or cfg["cutoff"]
    built = args.date or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    only = {x for x in args.only.split(",") if x}
    fetcher = Fetcher(args.cache, offline=args.offline)
    hook = summarise.load()
    all_stats = []
    log = lambda m: print(m, flush=True)

    for pkg in cfg["packages"]:
        if only and pkg["name"] not in only:
            continue
        log(f"{pkg['ecosystem']:4} {pkg['name']}")
        dates, releases, problems = sources.collect(fetcher, pkg, cutoff, log)
        summarised, untraced = False, 0
        for r in releases:
            parse.extract(r)
            summarised = summarise.apply(hook, pkg, r) or summarised
            untraced += parse.trace(r)      # runs after the hook too: a summariser cannot add claims
        md, stats = render.render(pkg, dates, releases, problems, cutoff, built, summarised)
        stats["ecosystem"] = pkg["ecosystem"]
        stats["file"] = "references/" + render.file_name(pkg["name"])
        stats["bytes"] = len(md.encode())
        stats["untraced_dropped"] = untraced
        stats["items"] = sum(len(r.items) for r in releases)
        ref_dir = os.path.join(args.out, SKILLS[pkg["ecosystem"]], "references")
        os.makedirs(ref_dir, exist_ok=True)
        open(os.path.join(ref_dir, render.file_name(pkg["name"])), "w").write(md)
        c = stats["counts"]
        log(f"    -> {stats['file']} {stats['bytes']} bytes; latest {stats['latest']}; "
            f"breaking {c['breaking']}, removed {c['removed']}, deprecated {c['deprecated']}, "
            f"minver {c['minver']}, new {c['new']}" + (f"; PROBLEMS {problems}" if problems else ""))
        all_stats.append(stats)

    if not only:
        for eco, skill in SKILLS.items():
            rows = [s for s in all_stats if s["ecosystem"] == eco]
            write_skill(os.path.join(args.out, skill), skill, eco, rows, cutoff, built)
        json.dump({"built": built, "cutoff": cutoff, "packages": all_stats},
                  open(os.path.join(HERE if default_list else args.out, "build-report.json"), "w"), indent=1)
    usable = sum(1 for s in all_stats if s["usable"])
    log(f"\nSUMMARY built={built} cutoff={cutoff} packages={len(all_stats)} "
        f"with_usable_notes={usable} without={len(all_stats) - usable} "
        f"http_requests={fetcher.requests} "
        f"items_extracted={sum(s['items'] for s in all_stats)} "
        f"items_dropped_untraceable={sum(s['untraced_dropped'] for s in all_stats)} "
        f"total_bytes={sum(s['bytes'] for s in all_stats)} max_bytes={max(s['bytes'] for s in all_stats)}")
    for s in all_stats:
        if not s["usable"]:
            log(f"  no items: {s['ecosystem']} {s['name']}: {s['status']}"
                + (f" ({'; '.join(s['problems'])})" if s["problems"] else ""))


def write_skill(path, skill, eco, rows, cutoff, built):
    tmpl = open(os.path.join(HERE, "SKILL.template.md")).read()
    table = ["| Package | File | Latest (date built) | Breaking | Removed/renamed | Deprecated | New |",
             "|---|---|---|---|---|---|---|"]
    for s in sorted(rows, key=lambda s: s["name"].lstrip("@").lower()):
        c = s["counts"]
        note = "" if s["usable"] else " (no details in release notes)"
        table.append(f"| `{s['name']}` | [{s['file']}]({s['file']}){note} | {s['latest'] or '?'} | "
                     f"{c['breaking']} | {c['removed']} | {c['deprecated']} | {c['new']} |")
    ordered = [s["name"] for s in sorted(rows, key=lambda s: s["name"].lstrip("@").lower())]
    names = ", ".join(ordered)
    fixed = len(tmpl.split("description: ")[1].split("\n")[0]) - len("{{NAMES}}") + 60
    while len(names) + fixed > 1000:          # the Agent Skills spec caps description at 1024 characters
        ordered.pop()
        names = ", ".join(ordered) + " and others listed in the skill"
    manifest = {"npm": "package.json / the lockfile", "pypi": "pyproject.toml, requirements.txt or the lockfile"}[eco]
    text = (tmpl.replace("{{SKILL}}", skill).replace("{{LABEL}}", LABEL[eco]).replace("{{CUTOFF}}", cutoff)
            .replace("{{BUILT}}", built).replace("{{NAMES}}", names).replace("{{TABLE}}", "\n".join(table))
            .replace("{{MANIFEST}}", manifest).replace("{{COUNT}}", str(len(rows))))
    os.makedirs(path, exist_ok=True)
    open(os.path.join(path, "SKILL.md"), "w").write(text)


if __name__ == "__main__":
    main()
