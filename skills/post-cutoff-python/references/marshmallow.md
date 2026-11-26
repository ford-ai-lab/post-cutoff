# marshmallow (pypi): changes after 2025-06-01

- Latest stable on the registry: **4.4.0** (2026-11-04). Built 2026-11-25.
- 13 stable releases after the cut-off: 3.26.2 (2025-12-22) to 4.4.0 (2026-11-04).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Minimum versions and platform support
### 4.4.0 (2026-11-04) [source](https://github.com/marshmallow-code/marshmallow/blob/dev/CHANGELOG.rst)
- Drop support for Python 3.10.
### 4.1.0 (2025-11-01) [source](https://github.com/marshmallow-code/marshmallow/blob/dev/CHANGELOG.rst)
- Drop support for Python 3.9.

## New APIs and features
### 4.3.0 (2026-04-03) [source](https://github.com/marshmallow-code/marshmallow/blob/dev/CHANGELOG.rst)
- Add `pre_load` and `post_load` parameters to `marshmallow.fields.Field` for field-level pre- and post-processing.
### 4.1.0 (2025-11-01) [source](https://github.com/marshmallow-code/marshmallow/blob/dev/CHANGELOG.rst)
- Add `len` implementation to `missing` so that it can be used with `validate.Length <marshmallow.validate.Length>`. Thanks for the PR.
### 4.2.3 (2026-03-25) [source](https://github.com/marshmallow-code/marshmallow/blob/dev/CHANGELOG.rst)
- Allow `required` to be set on `marshmallow.fields.Contant`. Thanks for the report and for the PR.
- Add `ipaddress.*` to `marshmallow.Schema.TYPE_MAPPING`. Thanks for the suggestion and for the PR.

## Coverage
- Release notes read for 13 releases; 4 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 4.3.1, 4.2.4, 4.2.2, 4.2.1, 4.2.0, 4.1.2, 4.1.1, 4.0.1, 3.26.2.
- Sources: https://raw.githubusercontent.com/marshmallow-code/marshmallow/dev/CHANGELOG.rst; registry (pypi) for dates.
