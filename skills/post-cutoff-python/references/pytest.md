# pytest (pypi): changes after 2025-06-01

- Latest stable on the registry: **9.2.0** (2026-10-27). Built 2026-11-25.
- 10 stable releases after the cut-off: 8.4.0 (2025-06-02) to 9.2.0 (2026-10-27).
- New major versions since the cut-off: 9.0.0 (2025-11-08).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 9.2.0 (2026-10-27) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- `-c` now raises a usage error for a path that does not exist, is a directory, or is in a format pytest has no loader for. Such paths were previously either ignored or reported as an unhandled `FileNotFoundError`.
- The `indirect`, `ids` and `scope` arguments of `Metafunc.parametrize()` -- and therefore of `@pytest.mark.parametrize` -- are now keyword-only.
- Plugin import failures at startup are now reported and classified instead of escaping as a raw traceback with the accidental exit code `1`: a plugin that cannot be found -- via `-p`, `pytest_plugins` or `PYTEST_PLUGINS` -- exits […]
### 9.1.0 (2026-06-13) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- When using `--doctest-modules`, autouse fixtures with `module`, `package` or `session` scope that are defined inline in Python test modules (not plugins or conftests) will now possibly execute twice.
### 9.0.0 (2025-11-08) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- Fixed a bug where an invocation such as `pytest a/ a/b` would cause only tests from `a/b` to run, and not other tests under `a/`.
- Previously, pytest would assume it was running in a CI/CD environment if either of the environment variables `$CI` or `$BUILD_NUMBER` was defined; […]
- The non-public `config.args` attribute used to be able to contain `pathlib.Path` instances; now it can only contain strings.
- PytestRemovedIn9Warning deprecation warnings are now errors by default.
- But this will stop working when pytest `9.1` is released.
- If you have concerns about the removal of a specific feature, please add a comment to.
### 8.4.0 (2025-06-02) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- Async tests will now fail, instead of warning+skipping, if you don't have any suitable plugin installed.
- Tests will now fail, instead of raising a warning, if they return any value other than None.
- Test functions containing a yield now cause an explicit error. They have not been run since pytest 4.0, and were previously marked as an expected failure and deprecation warning.

## Removed or renamed
### 9.2.0 (2026-10-27) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- The private `_pytest.python.CallSpec2` name has been renamed to `CallSpec`. The old `CallSpec2` alias remains available for now and will be removed in pytest 10 or 11.
- Schedule *yield_fixture* decorator for removal in pytest 10 or 11.
- Similarly to the deprecation of class-scoped fixtures defined as instance methods in pytest 9.1, *all* higher-scoped fixtures (`module`, `package`, and `session`) defined as instance methods are now deprecated.
- Passing a non-string value to a `string`-typed ini option now emits a `pytest.PytestRemovedIn10Warning`. This affects `[tool.pytest.ini_options]` in `pyproject.toml`. […]
- Passing `bytes` to `TerminalReporter.write_line()` is now deprecated, pass a `str` instead.
### 9.1.0 (2026-06-13) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- Added a deprecation warning for class-scoped fixtures defined as instance methods (without `@classmethod`). Such fixtures set attributes on a different instance than the test methods use, leading to unexpected behavior. […]
- Calling `request.getfixturevalue()` during teardown to request a fixture that was not already requested is now deprecated and will become an error in pytest 10.
- Using non-`collections.abc.Collection` iterables (such as generators, iterators, or custom iterable objects) for the `argvalues` parameter in `@pytest.mark.parametrize` and `metafunc.parametrize` is now deprecated.
- The private `config.inicfg` attribute is now deprecated. Use `config.getini()` to access configuration values instead.
- Passing `baseid` to `pytest.FixtureDef` or `nodeid` strings to fixture registration APIs is now deprecated. These are internal pytest APIs that are used by some plugins.
- The method of configuring hooks using markers, deprecated since pytest 7.2, is now scheduled to be removed in pytest 10. See `hook-markers` for more details.
- The `--pastebin` option is now deprecated. The same functionality is now available in an external plugin, `pytest-pastebin`. See `pastebin-deprecated` for more details.
- The private `FixtureDef.has_location` attribute is now deprecated and will be removed in pytest 10. See `fixturedef-has-location-deprecated` for details.
### 9.0.0 (2025-11-08) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- `monkeypatch.syspath_prepend()` now issues a deprecation warning when the prepended path contains legacy namespace packages (those using `pkg_resources.declare_namespace()`). […]
- (2 more in this category not shown; see the changelog.)

## Deprecated
### 9.1.0 (2026-06-13) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- `pytest.raises`, `pytest.warns` and `pytest.deprecated_call` now uses `ParamSpec` for the type hint to the (old and not recommended) callable overload, instead of `Any`. […]
- Marked `yield_fixture` as deprecated to type checkers using the `deprecated` decorator. Note it `has originally been deprecated` in pytest 6.2 already.

## Minimum versions and platform support
### 9.0.0 (2025-11-08) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- Support for Python 3.9 is dropped following its end of life.
### 8.4.0 (2025-06-02) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- We dropped support for Python 3.8 following its end of life (2024-10-07).

## New APIs and features
### 9.2.0 (2026-10-27) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- `Full diff:` now contains a legend explaining the `+` & `-` symbols in diff output.
- When `strict_markers` is enabled, marker names used in `-m` expressions are now validated against registered markers.
- Added the `parametrize_long_str_id_strategy` configuration option to control how long `str`/`bytes` parameter values are handled in auto-generated test IDs. […]
- A `RecursionError` whose recursion origin cannot be located now shows only the first and last 10 stack frames, matching what pytest already did when locating the origin failed outright. […]
- The line numbers of a module's statements are now computed once per traceback instead of once per traceback entry, which noticeably speeds up rendering failures raised from large test modules.
- The cached rewritten modules in `pycache` are now invalidated by a hash of the source instead of its modification time, using the checked-hash pyc format from `552`.
- The `pytest_plugins` variable and the `PYTEST_PLUGINS` environment variable now also accept entry point names of installed plugins (e.g. […]
- Warnings emitted while importing plugins through `-p`, `PYTEST_PLUGINS`, or entry point autoloading are now captured, filtered, and reported like other warnings.
### 9.1.0 (2026-06-13) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- Added `pytest.register_fixture()` to register fixtures using an imperative interface.
- Added `--report-chars` long CLI option.
- Added `--max-warnings` command-line option and `max_warnings` configuration option to fail the test run when the number of warnings exceeds a given threshold -- by.
- Added the `assertion_text_diff_style` configuration option, allowing string equality failures to be rendered as separate `Left:` and `Right:` blocks instead of `ndiff` output.
- Added support for `datetime.datetime` and `datetime.timedelta` comparisons with `pytest.approx`. An explicit `abs` or `rel` tolerance as a `datetime.timedelta` is required and relative tolerance is not supported for datetime […]
- `pytest.warns` now shows "Regex pattern did not match" instead of "DID NOT WARN" when warnings were emitted but the `match` pattern did not match.
- Improved output of `--fixtures-per-test` by excluding internal-implementation fixtures generated by `@pytest.mark.parametrize` and similar.
- Improved the readability of "DID NOT RAISE" error messages by using the exception type's name instead of its `repr`.
### 9.0.0 (2025-11-08) [source](https://github.com/pytest-dev/pytest/blob/main/doc/en/changelog.rst)
- Support for subtests has been added.
- Added support for native TOML configuration files.
- (78 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 10 releases; 4 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 9.1.1, 9.0.3, 9.0.2, 9.0.1, 8.4.2, 8.4.1.
- Sources: https://raw.githubusercontent.com/pytest-dev/pytest/main/doc/en/changelog.rst; registry (pypi) for dates.
