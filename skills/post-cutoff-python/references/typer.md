# typer (pypi): changes after 2025-06-01

- Latest stable on the registry: **0.29.2** (2026-11-18). Built 2026-11-25.
- 42 stable releases after the cut-off: 0.16.1 (2025-08-18) to 0.29.2 (2026-11-18).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 0.27.0 (2026-07-15) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0270-2026-07-15)
- 💥 Update metavar printing. PR
### 0.26.0 (2026-05-26) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0260-2026-05-26)
- ➖ Vendor Click and streamline Typer's functionality and code base. PR
### 0.23.0 (2026-02-11) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0230-2026-02-11)
- ♻️ When printing error tracebacks with Rich, default to not showing locals, which are sometimes verbose. PR
### 0.22.0 (2026-02-11) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0220-2026-02-11)
- 💥 Make `typer-slim` a shallow wrapper around `typer`, always requiring `rich` and `shellingham`. PR

## Removed or renamed
### 0.29.0 (2026-11-09) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0290-2026-11-09)
- `click_type` has been removed from `typer.Option()` and `typer.Argument()`. New ways to provide custom types will be provided with Pydantic, with much more flexibility.
### 0.26.0 (2026-05-26) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0260-2026-05-26)
- This also means that Click-specific functionality is no longer supported, like extracting the Click app and adding Click-specific plug-ins, or customizing the field types with Click-specific types.

## Minimum versions and platform support
### 0.29.2 (2026-11-18) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0292-2026-11-18)
- 💥 Drop support for Python 3.10. PR
### 0.24.0 (2026-02-16) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0240-2026-02-16)
- ➖ Drop support for Python 3.9. PR
### 0.21.0 (2025-12-25) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0210-2025-12-25)
- ➖ Drop support for Python 3.8. PR
- ➖ Drop support for Python 3.8 in CI. PR
### 0.19.2 (2025-09-23) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0192-2025-09-23)
- 🔥 Drop support for Python 3.7. PR
### 0.19.1 (2025-09-20) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0191-2025-09-20)
- Note: this is the last version to support Python 3.7, going forward Typer will require Python 3.8+. And soon Python 3.8 will also be dropped as Python 3.8 reached it's end of life almost a year ago.

## New APIs and features
### 0.29.0 (2026-11-09) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0290-2026-11-09)
- ✨ Use Pydantic for parameter validation. PR
### 0.25.0 (2026-04-26) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0250-2026-04-26)
- 🚸 Don't truncate code lines in traceback when formatted with Rich. PR
### 0.20.0 (2025-10-20) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0200-2025-10-20)
- ✨ Enable command suggestions on typo by default. PR
### 0.19.0 (2025-09-20) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0190-2025-09-20)
- ✨ Support `typing.Literal` to define a set of predefined choices. PR
- ✨ Allow setting an environment variable to `None` in `CliRunner.invoke`. PR
### 0.17.0 (2025-08-30) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0170-2025-08-30)
- ⚡️ Lazy-load `rich_utils` to reduce startup time. PR
### 0.27.1 (2026-08-03) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0271-2026-08-03)
- ✨ Make `epilog` formatting consistent with other parts of the help string. PR
### 0.26.4 (2026-05-30) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0264-2026-05-30)
- 📝 Update AI Library Skill to avoid verbose code for CLI Options. PR
### 0.25.1 (2026-04-30) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0251-2026-04-30)
- 🔧 Add Typer Library Skill for Agents. PR
### 0.23.2 (2026-02-16) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0232-2026-02-16)
- ✅ Monkeypatch console width to allow running `pytest` directly. PR
### 0.20.1 (2025-12-19) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0201-2025-12-19)
- ✨ Add support for standard tracebacks via the env `TYPER_STANDARD_TRACEBACK`. PR
### 0.17.3 (2025-08-30) [source](https://github.com/fastapi/typer/blob/master/docs/release-notes.md#0173-2025-08-30)
- ✨ Allow annotated parsing with a subclass of `Path`. PR

## Coverage
- Release notes read for 42 releases; 20 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 0.29.1, 0.28.0, 0.27.3, 0.27.2, 0.26.8, 0.26.7, 0.26.6, 0.26.5, 0.26.3, 0.26.2, 0.26.1, 0.24.2 and 10 more.
- Sources: https://raw.githubusercontent.com/fastapi/typer/master/docs/release-notes.md; registry (pypi) for dates.
