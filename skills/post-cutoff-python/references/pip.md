# pip (pypi): changes after 2025-06-01

- Latest stable on the registry: **26.3** (2026-11-02). Built 2026-11-25.
- 11 stable releases after the cut-off: 25.2 (2025-07-30) to 26.3 (2026-11-02).
- New major versions since the cut-off: 26.0 (2026-01-31).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 26.3 (2026-11-02) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Block unexpected imports during installation, warn about unsafe imports afterward, and improve recovery from interrupted installations.
### 26.2 (2026-07-29) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Newly published packages will no longer be immediately visible to pip if the index uses caching. To install a newly published package, use `--refresh-package`.
- Drop support for detecting legacy, non-`405`, `virtualenv`
- Constraints files, including `PIP_CONSTRAINT`, no longer affect isolated build environments. Use `--build-constraint` or the `PIP_BUILD_CONSTRAINT` environment variable to constrain build dependencies instead.
### 26.0 (2026-01-31) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Remove support for non-bare project names in egg fragments. Affected users should use the Direct URL requirement syntax.
### 25.3 (2025-10-25) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Remove support for the legacy `setup.py develop` editable method in setuptools editable installs; setuptools >= 64 is now required.
- Remove the deprecated `--global-option` and `--build-option`. `--config-setting` is now the only way to pass options to the build backend.
- Deprecate the `PIP_CONSTRAINT` environment variable for specifying build constraints.
- Remove support for non-standard legacy wheel filenames.
- Remove support for the deprecated `setup.py bdist_wheel` mechanism. Consequently, `--use-pep517` is now always on, and `--no-use-pep517` has been removed.
### 25.2 (2025-07-30) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Remove warning when cloning from a Git reference that does not look like a commit hash.
- Remove vendored typing-extensions.

## Deprecated
### 26.1 (2026-04-26) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Emit a deprecation warning when pip imports an unexpected module after installation of a distribution has started.

## Minimum versions and platform support
### 26.1 (2026-04-26) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Drop support for Python 3.9.

## New APIs and features
### 26.3 (2026-11-02) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Show build backend warnings for local source directories and log them at debug level for other sources.
- Add support for selecting extras in pylock.toml files with `-r pylock.toml[extra1,extra2]`.
- Allow `--group` to select non-default groups from local pylock files, e.g. `--group pylock.toml:docs`.
- Support `--no-binary` with `-r pylock.toml`. Before, pip would get the sdist from the index instead of the locked URL, or fail if no wheel were available in the lock file.
- Speed up installing a wheel with console scripts by not resolving every `PATH` entry.
- Clarify the warning for `~`-prefixed leftover distribution directories.
- Allow pip itself to be built with flit-core 4.
### 26.2 (2026-07-29) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Declare support for Python 3.15
- Support self-referential extras officially. pip has supported this by accident since version 21.2.
- Add `--only-deps` flag to instruct pip to select only the dependencies of supplied packages. It cannot be used with `--no-deps`, `-r`, `--group`, or `--requirements-from-script`.
- Cache simple responses in accordance to their `Cache-Control` header instead of always revalidating on every request. To refresh cached package index responses and ensure newly published packages are found, use `--refresh-package […]
- Add `--no-require-hashes` to disable automatic enablement of `--require-hashes` when encountering a requirement with hashes.
- Honor `--only-final` when sourcing requirements with `-r pylock.toml`.
- Add support for `pylock.toml` `upload-time` field, so `--uploaded-prior-to` works with `-r pylock.toml`.
- Better error messages in case of conflicts with requirements from `-r pylock.toml`.
### 26.1 (2026-04-26) [source](https://github.com/pypa/pip/blob/main/NEWS.rst)
- Add experimental support to read requirements from standardized pylock.toml files (`-r pylock.toml`).
- Allow `--uploaded-prior-to` to accept a duration in days (e.g., `P3D` for 3 days ago).
- Speed up dependency resolution when there are complex conflicts.
- (31 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 11 releases; 6 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 26.2.2, 26.2.1, 26.1.2, 26.1.1, 26.0.1.
- Sources: https://raw.githubusercontent.com/pypa/pip/main/NEWS.rst; registry (pypi) for dates.
