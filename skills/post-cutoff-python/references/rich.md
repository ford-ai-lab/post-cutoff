# rich (pypi): changes after 2025-06-01

- Latest stable on the registry: **15.0.0** (2026-04-12). Built 2026-11-25.
- 8 stable releases after the cut-off: 14.1.0 (2025-07-25) to 15.0.0 (2026-04-12).
- New major versions since the cut-off: 15.0.0 (2026-04-12).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 15.0.0 (2026-04-12) [source](https://github.com/Textualize/rich/blob/master/CHANGELOG.md#1500---2026-04-12)
- Breaking change: Dropped support for Python3.8

## Removed or renamed
### 14.1.0 (2025-07-25) [source](https://github.com/Textualize/rich/blob/master/CHANGELOG.md#1410---2025-06-25)
- Removed `typing_extensions` from runtime dependencies

## New APIs and features
### 14.3.0 (2026-01-24) [source](https://github.com/Textualize/rich/blob/master/CHANGELOG.md#1430---2026-01-24)
- Added support for some multi-codepopint glyphs (will fix alignment issues for these characters)
- Added support for `UNICODE_VERSION` environment variable
- Added `last_render_height` property to LiveRender
- Expose locals_max_depth and locals_overflow in traceback.install
- Added `Segment.split_lines_terminator`
### 14.1.0 (2025-07-25) [source](https://github.com/Textualize/rich/blob/master/CHANGELOG.md#1410---2025-06-25)
- Added padding property to Syntax which returns a tuple of four integers
- Added `TTY_INTERACTIVE` environment variable to force interactive mode off or on

## Coverage
- Release notes read for 8 releases; 3 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 14.3.4, 14.3.3, 14.3.2, 14.3.1, 14.2.0.
- Sources: https://raw.githubusercontent.com/Textualize/rich/master/CHANGELOG.md; registry (pypi) for dates.
