# pytest-asyncio (pypi): changes after 2025-06-01

- Latest stable on the registry: **1.5.0** (2026-11-12). Built 2026-11-25.
- 7 stable releases after the cut-off: 1.1.0 (2025-07-16) to 1.5.0 (2026-11-12).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 1.3.0 (2025-11-10) [source](https://github.com/pytest-dev/pytest-asyncio/blob/main/docs/reference/changelog.rst)
- Support for Python 3.9

## Deprecated
### 1.4.0 (2026-05-26) [source](https://github.com/pytest-dev/pytest-asyncio/blob/main/docs/reference/changelog.rst)
- Overriding the *event_loop_policy* fixture is deprecated. Use the `pytest_asyncio_loop_factories` hook instead.
- Only import `asyncio.AbstractEventLoopPolicy` for type checking to avoid raising a DeprecationWarning.

## New APIs and features
### 1.5.0 (2026-11-12) [source](https://github.com/pytest-dev/pytest-asyncio/blob/main/docs/reference/changelog.rst)
- A `fixture-scope` value for `asyncio_default_fixture_loop_scope`. With it, an asynchronous fixture without `loop_scope` uses its `scope` as its loop scope. This is the behavior of an unset option in pytest-asyncio 1.x.
### 1.4.0 (2026-05-26) [source](https://github.com/pytest-dev/pytest-asyncio/blob/main/docs/reference/changelog.rst)
- Added the `pytest_asyncio_loop_factories` hook to parametrize asyncio tests with custom event loop factories.
- Added dependency on `sphinx-tabs >= 3.5` to organize documentation examples into tabs.
### 1.3.0 (2025-11-10) [source](https://github.com/pytest-dev/pytest-asyncio/blob/main/docs/reference/changelog.rst)
- Support for pytest 9
### 1.2.0 (2025-09-12) [source](https://github.com/pytest-dev/pytest-asyncio/blob/main/docs/reference/changelog.rst)
- `--asyncio-debug` CLI option and `asyncio_debug` configuration option to enable asyncio debug mode for the default event loop.
- A `pytest.UsageError` for invalid configuration values of `asyncio_default_fixture_loop_scope` and `asyncio_default_test_loop_scope`.
- Compatibility with the `Pyright` type checker
### 1.1.0 (2025-07-16) [source](https://github.com/pytest-dev/pytest-asyncio/blob/main/docs/reference/changelog.rst)
- Propagation of ContextVars from async fixtures to other fixtures and tests on Python 3.10 and older
- Cancellation of tasks when the `loop_scope` ends
- Warning when the current event loop is closed by a test
- Added runtime dependency on backports.asyncio.runner for use with Python 3.10 and older
### 1.4.1 (2026-10-25) [source](https://github.com/pytest-dev/pytest-asyncio/blob/main/docs/reference/changelog.rst)
- Declared support for Python 3.15

## Coverage
- Release notes read for 6 releases; 6 had extractable items.
- 1 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/pytest-dev/pytest-asyncio/main/docs/reference/changelog.rst; registry (pypi) for dates.
