# pydantic (pypi): changes after 2025-06-01

- Latest stable on the registry: **2.14.4** (2026-11-19). Built 2026-11-25.
- 26 stable releases after the cut-off: 1.10.23 (2025-09-13) to 2.14.4 (2026-11-19).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Deprecated
### 2.14.4 (2026-11-19) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v2144-2026-11-19)
- Don't mark subclasses of `@deprecated` classes as deprecated in JSON Schema
### 2.12.3 (2025-10-17) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v2123-2025-10-17)
- Raise a warning when an invalid after model validator function signature is raised Starting in 2.12.0, using class methods for *after* model validators raised an error, but the error wasn't raised concistently. […]

## Minimum versions and platform support
### 2.14.0 (2026-10-08) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v2140-2026-10-08)
- This release drops support for Python 3.9 and adds support for Python 3.15.

## New APIs and features
### 2.14.0 (2026-10-08) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v2140-2026-10-08)
- Add support for `multiple_of` constraint in `fraction` and `timedelta` core schemas
- Add `namespace` parameter to `create_model()`
- Add an `ordered-dict` core schema
- Add a `counter` core schema
### 2.13.0 (2026-04-13) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v2130-2026-04-13)
- Allow default factories of private attributes to take validated model data
### 2.12.0 (2025-10-07) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v2120-2025-10-07)
- Add `extra` parameter to the validate functions
- Add `exclude_computed_fields` serialization option
- Add `preverse_empty_path` URL options
- Add `union_format` parameter to JSON Schema generation
- Add `qualname` parameter for `create_model`
### 2.12.4 (2025-11-05) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v2124-2025-11-05)
- Add type inference for IP address types
- Add more `pydantic-core` builds for the three-threaded version of Python 3.14
### 2.12.3 (2025-10-17) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v2123-2025-10-17)
- Add `FieldInfo.asdict()` method, improve documentation around `FieldInfo` This also add back support for mutations on `FieldInfo` classes, that are reused as `Annotated` metadata. […]
### 1.10.24 (2025-09-25) [source](https://github.com/pydantic/pydantic/blob/main/HISTORY.md#v11024-2025-09-25)
- Add user warning when using Python 3.14 Pydantic V1 will *not* work with Python 3.14 and greater. A warning is now raised as no actual error show up when using it, but the core behavior will silently get broken at runtime.

## Coverage
- Release notes read for 23 releases; 7 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 2.14.3, 2.14.2, 2.14.1, 2.13.4, 2.13.3, 2.13.2, 2.13.1, 2.12.5, 2.12.2, 2.12.1, 2.11.10, 2.11.9 and 4 more.
- 4 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/pydantic/pydantic/main/HISTORY.md; registry (pypi) for dates.
