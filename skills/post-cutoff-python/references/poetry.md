# poetry (pypi): changes after 2025-06-01

- Latest stable on the registry: **2.5.2** (2026-11-21). Built 2026-11-25.
- 15 stable releases after the cut-off: 2.1.4 (2025-08-05) to 2.5.2 (2026-11-21).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Deprecated
### 2.3.0 (2026-01-18) [source](https://github.com/python-poetry/poetry/blob/main/CHANGELOG.md#230---2026-01-18)
- Deprecate `poetry.utils._compat.metadata`, which is sometimes used in plugins, in favor of `importlib.metadata`.
### 2.2.0 (2025-09-14) [source](https://github.com/python-poetry/poetry/blob/main/CHANGELOG.md#220---2025-09-14)
- Deprecate table values and values that are not valid SPDX expressions for `[project.license]`.

## Minimum versions and platform support
### 2.3.0 (2026-01-18) [source](https://github.com/python-poetry/poetry/blob/main/CHANGELOG.md#230---2026-01-18)
- Drop support for Python 3.9.

## New APIs and features
### 2.5.0 (2026-09-19) [source](https://github.com/python-poetry/poetry/blob/main/CHANGELOG.md#250---2026-09-19)
- Add an `installer.builtin-uninstall` setting to uninstall packages with a built-in uninstaller instead of invoking `pip uninstall`.
- Add official support for Python 3.15.
- Add Python 3.15 to the automatically generated classifiers.
### 2.4.0 (2026-05-03) [source](https://github.com/python-poetry/poetry/blob/main/CHANGELOG.md#240---2026-05-03)
- Add `solver.min-release-age` setting to require package releases to be a certain number of days old before they are considered during dependency resolution.
- Add `solver.min-release-age-exclude` to exclude selected packages from age filtering.
- Add `solver.min-release-age-exclude-source` to exclude all packages from selected package indexes from age filtering.
- Allow `findpython>=0.8`.
### 2.3.0 (2026-01-18) [source](https://github.com/python-poetry/poetry/blob/main/CHANGELOG.md#230---2026-01-18)
- Add support for exporting `pylock.toml` files with `poetry-plugin-export`.
- Add support for specifying build constraints for dependencies.
- Add support for publishing artifacts whose version is determined dynamically by the build-backend.
- Add support for editable project plugins.
- Check `requires-poetry` before any other validation.
- Validate the content of `project.readme` when running `poetry check`.
- Add the option to clear all caches by making the cache name in `poetry cache clear` optional.
- Automatically update the cache for packages where the locked files differ from cached files.
### 2.2.0 (2025-09-14) [source](https://github.com/python-poetry/poetry/blob/main/CHANGELOG.md#220---2025-09-14)
- Add support for nesting dependency groups.
- Add support for PEP 735 dependency groups.
- Add support for PEP 639 license clarity.
- (11 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 15 releases; 6 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 2.5.1, 2.4.3, 2.4.2, 2.4.1, 2.3.4, 2.3.3, 2.3.1, 2.2.1, 2.1.4.
- Sources: https://raw.githubusercontent.com/python-poetry/poetry/main/CHANGELOG.md; registry (pypi) for dates.
