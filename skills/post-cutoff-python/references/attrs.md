# attrs (pypi): changes after 2025-06-01

- Latest stable on the registry: **26.1.0** (2026-03-19). Built 2026-11-25.
- 2 stable releases after the cut-off: 25.4.0 (2025-10-06) to 26.1.0 (2026-03-19).
- New major versions since the cut-off: 26.1.0 (2026-03-19).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 26.1.0 (2026-03-19) [source](https://github.com/python-attrs/attrs/blob/main/CHANGELOG.md#2610---2026-03-19)
- Field aliases are now resolved *before* calling `field_transformer`, so transformers receive fully populated `Attribute` objects with usable `alias` values instead of `None`. […]
### 25.4.0 (2025-10-06) [source](https://github.com/python-attrs/attrs/blob/main/CHANGELOG.md#2540---2025-10-06)
- Class-level `kw_only=True` behavior is now consistent with `dataclasses`.

## New APIs and features
### 25.4.0 (2025-10-06) [source](https://github.com/python-attrs/attrs/blob/main/CHANGELOG.md#2540---2025-10-06)
- Added support for Python 3.14 and PEP 749.
- Added a new experimental way to inspect classes

## Coverage
- Release notes read for 2 releases; 2 had extractable items.
- Sources: https://raw.githubusercontent.com/python-attrs/attrs/main/CHANGELOG.md; registry (pypi) for dates.
