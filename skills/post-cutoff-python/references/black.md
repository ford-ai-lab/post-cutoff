# black (pypi): changes after 2025-06-01

- Latest stable on the registry: **26.10.1** (2026-10-10). Built 2026-11-25.
- 10 stable releases after the cut-off: 25.9.0 (2025-09-19) to 26.10.1 (2026-10-10).
- New major versions since the cut-off: 26.1.0 (2026-01-18).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 26.10.0 (2026-10-04) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-26100)
- Remove spurious target version warning when runtime version is included in a `--target-version` flag
- Remove unused `migrate-black` script
### 26.3.0 (2026-03-06) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-2630)
- Remove unused gallery script

## Minimum versions and platform support
### 25.12.0 (2025-12-08) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-25120)
- Black no longer supports running with Python 3.9
### 25.9.0 (2025-09-19) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-2590)
- Remove support for pre-python 3.7 `await/async` as soft keywords/variable names

## New APIs and features
### 26.10.0 (2026-10-04) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-26100)
- Add support for `NO_COLOR` environment variable to disable ANSI output
- Add validation for `--line-ranges` values
- Allow optional whitespace around comma-separated versions and `pyi` in the `X-Python-Variant` header
- Add outputs (`is_formatted`, `change_count`, `same_count`, `failure_count`) to GitHub Action runs
### 26.5.0 (2026-05-16) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-2650)
- Add support for unpacking in comprehensions (PEP 798) and for lazy imports (PEP 810), both new syntactic features in Python 3.15
- Python 3.15 is now supported. Compiled wheels are not yet provided for Python 3.15, so performance may be slower than on existing Python versions. Wheels will be provided once Python 3.15 is later in its release cycle.
- Add `SourceASTParseError` to distinguish source parse failures from internal safety errors, improving error reporting when Black's lenient parser accepts input that `ast.parse()` rejects
- Added documentation for doctest formatting tools and updated the integrations index to match
### 26.3.0 (2026-03-06) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-2630)
- Introduce winloop to be used when windows in use which enables blackd to run faster on windows when winloop is installed.
### 26.1.0 (2026-01-18) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-2610)
- `always_one_newline_after_import`: Always force one blank line after import statements, except when the line after the import is a comment or an import statement
- `fix_fmt_skip_in_one_liners`: Fix `# fmt: skip` behavior on one-liner declarations, such as `def foo(): return "mock" # fmt: skip`, where previously the declaration would have been incorrectly collapsed
- `fix_module_docstring_detection`: Fix module docstrings being treated as normal strings if preceded by comments
- `fix_type_expansion_split`: Fix type expansions split in generic functions
- `multiline_string_handling`: Make expressions involving multiline strings more compact
- `normalize_cr_newlines`: Add `\r` style newlines to the potential newlines to normalize file newlines both from and to
- `remove_parens_around_except_types`: Remove parentheses around multiple exception types in `except` and `except*` without `as`
- `remove_parens_from_assignment_lhs`: Remove unnecessary parentheses from the left-hand side of assignments while preserving magic trailing commas and intentional multiline formatting
### 25.12.0 (2025-12-08) [source](https://github.com/psf/black/blob/main/CHANGES.md#version-25120)
- Add `output-file` input to GitHub Action `psf/black` to write formatter output to a file for artifact capture and log cleanliness
- (8 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 10 releases; 8 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 26.5.1, 26.3.1.
- Sources: https://raw.githubusercontent.com/psf/black/main/CHANGES.md; registry (pypi) for dates.
