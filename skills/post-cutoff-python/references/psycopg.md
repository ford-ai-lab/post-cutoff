# psycopg (pypi): changes after 2025-06-01

- Latest stable on the registry: **3.3.9** (2026-11-12). Built 2026-11-25.
- 14 stable releases after the cut-off: 3.2.10 (2025-09-08) to 3.3.9 (2026-11-12).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Minimum versions and platform support
### 3.3.0 (2025-12-01) [source](https://github.com/psycopg/psycopg/blob/master/docs/news.rst)
- Drop support for Python 3.8 and 3.9.

## New APIs and features
### 3.3.0 (2025-12-01) [source](https://github.com/psycopg/psycopg/blob/master/docs/news.rst)
- Add `template strings queries`.
- Add `Cursor.set_result()` and `Cursor.results()` to move across the result sets of queries executed through `~Cursor.executemany()` or `~Cursor.execute()` with multiple statements (`#1080, #1170`).
- Add `transaction-status` to report the status during and after a `~Connection.transaction()` block.
- Allow changing loaders using `~adapt.AdaptersMap.register_loader()` on `Cursor.adapters` after a query result has already been returned.
- Add `pq.PGconn.used_gssapi` attribute and `Capabilities.has_used_gssapi()` function.
- Add `ConnectionInfo.full_protocol_version` attribute, `Capabilities.has_full_protocol_version()` function.
### 3.3.6 (2026-09-18) [source](https://github.com/psycopg/psycopg/blob/master/docs/news.rst)
- Add support for Python 3.15.
### 3.2.12 (2025-10-26) [source](https://github.com/psycopg/psycopg/blob/master/docs/news.rst)
- Allow copy to pass different types per column, as long as the database can convert them. Regression introduced in 3.2.11.
### 3.2.10 (2025-09-08) [source](https://github.com/psycopg/psycopg/blob/master/docs/news.rst)
- Add support for Python 3.14.

## Coverage
- Release notes read for 14 releases; 4 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 3.3.9, 3.3.8, 3.3.7, 3.3.5, 3.3.4, 3.3.3, 3.3.2, 3.3.1, 3.2.13, 3.2.11.
- Sources: https://raw.githubusercontent.com/psycopg/psycopg/master/docs/news.rst; registry (pypi) for dates.
