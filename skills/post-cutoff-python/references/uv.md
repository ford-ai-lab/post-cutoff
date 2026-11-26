# uv (pypi): changes after 2025-06-01

- Latest stable on the registry: **0.13.10** (2026-11-24). Built 2026-11-25.
- 152 stable releases after the cut-off: 0.7.10 (2025-06-03) to 0.13.10 (2026-11-24).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 0.13.0 (2026-10-09) [source](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md#0130)
- Use Python 3.15 as the default stable version
- Honor `--require-hashes` in included constraints files
- Prefer native Python on Windows ARM64
- Reject editable requirements in included constraints files
- Omit the distutils startup patch on Python 3.10 and later
- Treat requirement-file option values as single paths
- Use `tar-codec` for tar archives by default
- Reject `uv build --clear` output directories that contain a build source
- output directory contained the source. Now, uv rejects these output directories, including equivalent paths reached through symlinks, before clearing any build output.
- Select an output directory that does not contain any build sources, or omit `--clear`.

## Minimum versions and platform support
### 0.13.9 (2026-11-17) [source](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md#0139)
- Raise the minimum supported Rust version to 1.98

## New APIs and features
### 0.13.0 (2026-10-09) [source](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md#0130)
- Add CPython 3.15.0
### 0.13.10 (2026-11-24) [source](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md#01310)
- Validate that dependency requirements in `uv.lock` match the locked package versions (astral-sh/uv
- Explain why `uv.lock` needs to be updated when `--locked` rejects it (astral-sh/uv
- Report dependencies whose package entries are missing from `uv.lock` (astral-sh/uv
### 0.13.8 (2026-11-12) [source](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md#0138)
- Add CPython 3.16.0a2
### 0.13.6 (2026-10-27) [source](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md#0136)
- Accept an empty `UV_RUN_RECURSION_DEPTH` as zero and report invalid values consistently
- Explain how to add project metadata when `uv init` finds a `pyproject.toml` without a `[project]` table
- Add CPython 3.11.18, 3.12.16, 3.13.18, 3.14.10, and 3.15.2
### 0.13.5 (2026-10-22) [source](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md#0135)
- Report incompatible self-dependencies directly in resolution errors
- Add CPython 3.15.1, 3.14.9, and 3.13.17
### 0.13.2 (2026-10-19) [source](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md#0132)
- Report all installed packages in `uv workspace metadata`, including packages outside the selected resolution
- Include supported environment restrictions when exporting `pylock.toml`
- Retry dropped GET and HEAD requests when fetching package and index data
- Preserve encoding declarations in wheel data scripts that require shell launchers
- Show causes and hints when `uv python find --script` cannot discover an interpreter, including with `-q`
- Print valid ksh activation instructions and support non-relocatable environments under OpenBSD-derived ksh
- Allow PEP 508 direct URLs, including Mercurial and extensionless archive URLs, in uv-build's `[build-system].requires` validation
- Add PyPy 3.11.17 and 3.12.15
- (4 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 11 releases; 8 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 0.13.7, 0.13.4, 0.13.3.
- 141 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Source not reachable in this build: github_releases astral-sh/uv: HTTP 403 cached
- Sources: https://raw.githubusercontent.com/astral-sh/uv/main/CHANGELOG.md, https://github.com/astral-sh/uv/releases; registry (pypi) for dates.
