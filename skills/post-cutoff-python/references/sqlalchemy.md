# sqlalchemy (pypi): changes after 2025-06-01

- Latest stable on the registry: **2.1.9** (2026-11-16). Built 2026-11-25.
- 27 stable releases after the cut-off: 2.0.42 (2025-07-29) to 2.1.9 (2026-11-16).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 2.0.54 (2026-09-15) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [change, platform] Binary wheels are no longer built for Python 3.7. PyPI now rejects wheel files whose filename does not begin with the normalized project name, and the packaging tools that can be installed on Python 3.7 do not […]

## Deprecated
### 2.1.5 (2026-10-16) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_21.rst)
- [deprecated, orm] Using the `_orm.Mapper.exclude_properties` or `_orm.Mapper.include_properties` parameters on a Declarative mapping to exclude attributes that are declared on the class, such as with `_orm.mapped_column`, is […]
### 2.0.45 (2025-12-09) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [change, tests] A noxfile.py has been added to allow testing with nox. This is a direct port of 2.1's move to nox, however leaves the tox.ini file in place and retains all test documentation in terms of tox. […]
### 2.0.44 (2025-10-10) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, orm] The way ORM Annotated Declarative interprets Python `695` type aliases in `Mapped[]` annotations has been refined to expand the lookup scheme. […]

## New APIs and features
### 2.1.0 (2026-09-24) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_21.rst)
- [feature, orm] Added `_orm.composite.column_template` parameter to `_orm.composite`. When the composite class is a dataclass, this parameter accepts a string template such as `"person_%s"`, containing exactly one `%s` […]
- [usecase, postgresql] PostgreSQL index reflection now reports so-called "invalid" indexes with `postgresql_invalid=True` in the Inspector's `dialect_options`. […]
### 2.1.7 (2026-11-03) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_21.rst)
- [feature, orm] Added `_orm.SessionTransaction.connections` and `_orm.SessionTransaction.bound_connection`, which return the connections a `_orm.SessionTransaction` has already acquired, without acquiring a new one. […]
### 2.1.6 (2026-10-21) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_21.rst)
- [usecase, engine] Added `make_url.keep_blank_values` and `URL.update_query_string.keep_blank_values` parameters, which when set to True retain query string parameters with blank values such as `key=` in the `URL.query` dictionary […]
### 2.1.5 (2026-10-16) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_21.rst)
- [feature, orm] Added the `_orm.Unmapped` annotation and the `_orm.unmapped_column` construct, providing a declarative-compatible approach to having "excluded" columns in a Declarative model, that is, columns that are part of the […]
### 2.0.53 (2026-09-14) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, sqlite, reflection] Implemented `_engine.Inspector.get_table_options` for the SQLite dialect, which previously raised `NotImplementedError`. […]
- [usecase, oracle] Added support for oracledb's new `terminate()` feature, which allows for clean termination of an Oracle database connection in an asyncio context where the connection's state has fallen out of the event loop […]
### 2.0.49 (2026-04-03) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, mssql] Enhanced the `aioodbc` dialect to expose the `fast_executemany` attribute of the pyodbc cursor. This allows the `fast_executemany` parameter to work with the `mssql+aioodbc` dialect. […]
### 2.0.47 (2026-02-24) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, engine] The connection object returned by `_engine.Engine.raw_connection` now supports the context manager protocol, automatically returning the connection to the pool when exiting the context.
### 2.0.46 (2026-01-21) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, mssql] Added support for the `IF EXISTS` clause when dropping indexes on SQL Server 2016 (13.x) and later versions. The `DropIndex.if_exists` parameter is now honored by the SQL Server dialect, allowing conditional […]
### 2.0.45 (2025-12-09) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, mysql] Added support for MySQL 8.0.1 + `FOR SHARE` to be emitted for the `Select.with_for_update` method, which offers compatibility with `NOWAIT` and `SKIP LOCKED`. […]
- [usecase, postgresql] Added support for reflection of collation in types for PostgreSQL. The `collation` will be set only if different from the default one for the type. Pull request courtesy Denis Laxalde.
### 2.0.44 (2025-10-10) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, asyncio] Generalize the terminate logic employed by the asyncpg dialect to reuse it in the aiomysql and asyncmy dialect implementation.
### 2.0.43 (2025-08-11) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, oracle] Extended `_oracle.VECTOR` to support sparse vectors. This update introduces `_oracle.VectorStorageType` to specify sparse or dense storage and added `_oracle.SparseVector`. Pull request courtesy Suraj Shaw.
- [usecase, engine] Added new parameter `create_engine.skip_autocommit_rollback` which provides for a per-dialect feature of preventing the DBAPI `.rollback()` from being called under any circumstances, if the connection is […]
### 2.0.42 (2025-07-29) [source](https://github.com/sqlalchemy/sqlalchemy/blob/main/doc/build/changelog/changelog_20.rst)
- [usecase, orm] Added `dataclass_metadata` argument to all ORM attribute constructors that accept dataclasses parameters, e.g. `mapped_column.dataclass_metadata`, `relationship.dataclass_metadata`, etc. […]
- [usecase, postgresql] Added support for PostgreSQL 14+ `_postgresql.JSONB` subscripting syntax. When connected to PostgreSQL 14 or later, JSONB columns now automatically use the native subscript notation `jsonb_col['key']` […]
- [usecase, sql] The `_sql.values` construct gains a new method `_sql.Values.cte`, which allows creation of a named, explicit-columns `CTE` against an unnamed `VALUES` expression, producing a syntax that allows column-oriented […]
- (1 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 27 releases; 13 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 2.1.9, 2.1.8, 2.1.4, 2.1.3, 2.1.2, 2.1.1, 2.0.58, 2.0.57, 2.0.56, 2.0.55, 2.0.52, 2.0.51 and 2 more.
- Sources: https://raw.githubusercontent.com/sqlalchemy/sqlalchemy/main/doc/build/changelog/changelog_21.rst, https://raw.githubusercontent.com/sqlalchemy/sqlalchemy/main/doc/build/changelog/changelog_20.rst; registry (pypi) for dates.
