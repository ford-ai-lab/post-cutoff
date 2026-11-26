# ruff (pypi): changes after 2025-06-01

- Latest stable on the registry: **0.17.6** (2026-11-19). Built 2026-11-25.
- 73 stable releases after the cut-off: 0.11.13 (2025-06-05) to 0.17.6 (2026-11-19).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 0.17.0 (2026-10-09) [source](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md#0170)
- Update the default and latest Python versions for 3.15
- Update the default rule set
- Update Rust crate quick-junit to 0.8.0
- \[`flake8-import-conventions`\] Add `datetime as dt` as a conventional alias (`ICN001`)
- Support Unicode dummy variable names
- Update to Unicode 17
- Always show unsafe and display-only fixes in the CLI
- Remove the Python dependency from conda-forge builds (conda-forge/ruff-feedstock
- Remove support for ruff-lsp
- The formatter, `unsorted-imports` (`I001`), `line-too-long` (`E501`), and `doc-line-too-long` (`W505`) now consistently ignore trailing pragma comments when computing line length. […]

## Coverage
- Release notes read for 7 releases; 1 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 0.17.6, 0.17.5, 0.17.4, 0.17.3, 0.17.2, 0.17.1.
- 66 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Source not reachable in this build: github_releases astral-sh/ruff: HTTP 403 cached
- Sources: https://raw.githubusercontent.com/astral-sh/ruff/main/CHANGELOG.md, https://github.com/astral-sh/ruff/releases; registry (pypi) for dates.
