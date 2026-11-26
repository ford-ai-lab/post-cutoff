---
name: {{SKILL}}
description: What changed in popular {{LABEL}} packages after {{CUTOFF}} - breaking changes, removed or renamed APIs, deprecations, new preferred APIs and minimum versions, quoted from upstream release notes with version, date and source link. Use before writing, editing or upgrading code that imports any of these packages, because your training data may describe an older API - {{NAMES}}.
license: MIT
metadata:
  built: "{{BUILT}}"
  cutoff: "{{CUTOFF}}"
  author: "Ford (AI agent); with an accountable human operator"
---

# {{SKILL}}

Release-note digests for {{COUNT}} {{LABEL}} packages, covering releases published after **{{CUTOFF}}**.
Built **{{BUILT}}**. Anything released after that date is not here.

## When to use this

Before you write or change code that uses a package in the table below, and whenever an error
looks like an API that moved (unknown option, missing export, changed signature, unsupported
runtime version).

## How to use this

1. Find the version the project actually uses: {{MANIFEST}}. Do not assume the latest.
2. Open the package's file from the table (one small file per package, in `references/`).
3. Apply only entries whose version is at or below the project's installed version. Entries above
   it describe an upgrade the project has not made; mention them only if the user is upgrading.
4. Sections in each file: Breaking changes, Removed or renamed, Deprecated, Minimum versions and
   platform support, New APIs and features, Coverage. Each group is headed by version, date and a
   source link.
5. If an entry matters to the code you are writing, open its source link and read the full note
   before relying on it. Entries are truncated quotes (marked `[…]`), not explanations.

## What these files are and are not

- Every entry is text quoted from the package's own changelog or release notes, picked by keyword
  rules. Nothing was written from memory and no model summarised it. Nobody reviewed it.
- The rules miss things. A file that lists no breaking changes does not prove there were none;
  "no details in release notes" means exactly that.
- Long changelogs are capped; each file says how many entries were left out.
- Releases before {{CUTOFF}} are not covered, and a package that is not in the table is not covered
  at all. In both cases read the package's own changelog.

## Packages

{{TABLE}}
