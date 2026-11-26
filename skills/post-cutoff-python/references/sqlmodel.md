# sqlmodel (pypi): changes after 2025-06-01

- Latest stable on the registry: **0.0.50** (2026-11-13). Built 2026-11-25.
- 26 stable releases after the cut-off: 0.0.25 (2025-09-17) to 0.0.50 (2026-11-13).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 0.0.45 (2026-09-21) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0045-2026-09-21)
- ✨ Use UTC datetimes by default. PR
- `datetime` fields now use `UTCDateTime`, a custom type based on `DateTime(timezone=True)`. It requires aware datetime parameters, normalizes them to UTC, and returns aware UTC values from database reads, including on SQLite and […]
- Existing databases are not changed automatically. To retain naive storage, use `NaiveDatetime` or an explicit `Field(sa_type=DateTime(timezone=False))`. Explicit SQLAlchemy types retain their existing behavior. […]
### 0.0.31 (2025-12-28) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0031-2025-12-28)
- ➖ Drop support for Pydantic v1. PR

## Minimum versions and platform support
### 0.0.50 (2026-11-13) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0050-2026-11-13)
- 💥 Drop support for Python 3.10. PR
### 0.0.35 (2026-02-20) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0035-2026-02-20)
- ➖ Drop support for Python 3.9. PR
### 0.0.30 (2025-12-26) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0030-2025-12-26)
- ➖ Drop support for Python 3.8. PR
- ➖ Drop support for Python 3.8 in CI and docs. PR
### 0.0.28 (2025-12-23) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0028-2025-12-23)
- 📌 Pin FastAPI in tests to 0.125.0 while dropping support for Python 3.8. PR
### 0.0.25 (2025-09-17) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0025-2025-09-17)
- ⬆️ Drop support for Python 3.7, require Python 3.8 or above. PR

## New APIs and features
### 0.0.48 (2026-10-06) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0048-2026-10-06)
- ✨ Add support for SQLAlchemy 2.1. PR
### 0.0.47 (2026-09-23) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0047-2026-09-23)
- ✨ Add direct support for PostgreSQL, MySQL, and MariaDB, include in CI tests. PR
### 0.0.42 (2026-08-28) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0042-2026-08-28)
- 🏷️ Allow `Discriminator` type for `discriminator` parameter in `Field`. PR
### 0.0.39 (2026-06-25) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0039-2026-06-25)
- ✨ Add SQLModel Agent Library Skill, install with `uvx library-skills`. PR
### 0.0.25 (2025-09-17) [source](https://github.com/fastapi/sqlmodel/blob/main/docs/release-notes.md#0025-2025-09-17)
- ✨ Add overload for `exec` method to support `insert`, `update`, `delete` statements. PR

## Coverage
- Release notes read for 26 releases; 11 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 0.0.49, 0.0.46, 0.0.44, 0.0.43, 0.0.41, 0.0.40, 0.0.38, 0.0.37, 0.0.36, 0.0.34, 0.0.33, 0.0.32 and 3 more.
- Sources: https://raw.githubusercontent.com/fastapi/sqlmodel/main/docs/release-notes.md; registry (pypi) for dates.
