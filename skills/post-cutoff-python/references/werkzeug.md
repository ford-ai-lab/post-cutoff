# werkzeug (pypi): changes after 2025-06-01

- Latest stable on the registry: **3.1.9** (2026-09-27). Built 2026-11-25.
- 6 stable releases after the cut-off: 3.1.4 (2025-11-29) to 3.1.9 (2026-09-27).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 3.1.9 (2026-09-27) [source](https://github.com/pallets/werkzeug/blob/main/CHANGES.rst)
- The invalid `Range` suffix length `-0` is no longer accepted.
### 3.1.7 (2026-03-24) [source](https://github.com/pallets/werkzeug/blob/main/CHANGES.rst)
- `Request.host`, `get_host`, and `host_is_trusted` validate the characters of the value. An empty value is no longer allowed. A Unix socket server address is ignored. The `trusted_list` argument to `host_is_trusted` is optional.

## Coverage
- Release notes read for 6 releases; 2 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 3.1.8, 3.1.6, 3.1.5, 3.1.4.
- Sources: https://raw.githubusercontent.com/pallets/werkzeug/main/CHANGES.rst; registry (pypi) for dates.
