#!/usr/bin/env python3
"""Make a packages.json for build.py from a project's own dependency files.

    python3 build/from_manifest.py package.json requirements.txt pyproject.toml > my-packages.json
    python3 build/build.py --packages my-packages.json --out my-pack

Packages already configured in build/packages.json keep their hand-checked sources. Anything else
gets no sources here, and build.py then looks for a changelog through the registry's repository
link (see postcutoff/sources.py: discover). Private packages need a source entry written by hand.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def names(path):
    base = os.path.basename(path)
    if base == "package.json":
        d = json.load(open(path))
        return "npm", sorted({**d.get("dependencies", {}), **d.get("devDependencies", {})})
    if base == "pyproject.toml":
        import tomllib
        d = tomllib.load(open(path, "rb"))
        deps = list(d.get("project", {}).get("dependencies", []))
        for group in d.get("project", {}).get("optional-dependencies", {}).values():
            deps += group
        deps += list(d.get("tool", {}).get("poetry", {}).get("dependencies", {}))
    else:                                   # requirements.txt style
        deps = [l.split("#")[0].strip() for l in open(path) if l.strip() and not l.startswith(("-", "#"))]
    out = {re.split(r"[\s\[<>=!~;@(]", d, maxsplit=1)[0].lower() for d in deps}
    return "pypi", sorted(n for n in out if n and n != "python")


def main():
    known = {(p["ecosystem"], p["name"]): p for p in json.load(open(os.path.join(HERE, "packages.json")))["packages"]}
    cutoff = json.load(open(os.path.join(HERE, "packages.json")))["cutoff"]
    pkgs = []
    for path in sys.argv[1:]:
        eco, found = names(path)
        for n in found:
            pkgs.append(known.get((eco, n), {"name": n, "ecosystem": eco, "sources": []}))
    json.dump({"cutoff": cutoff, "packages": pkgs}, sys.stdout, indent=1)


if __name__ == "__main__":
    main()
