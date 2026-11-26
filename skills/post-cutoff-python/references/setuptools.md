# setuptools (pypi): changes after 2025-06-01

- Latest stable on the registry: **84.2.1** (2026-10-20). Built 2026-11-25.
- 12 stable releases after the cut-off: 75.3.3 (2026-01-14) to 84.2.1 (2026-10-20).
- New major versions since the cut-off: 81.0.0 (2026-02-06), 82.0.0 (2026-02-08), 83.0.0 (2026-07-04), 84.0.0 (2026-08-08).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 84.0.0 (2026-08-08) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- `Compiler.spawn` is deprecated in favor of the new `Compiler.call`. `call` raises native `subprocess` exceptions; `spawn` remains as a shim that emits a `DeprecationWarning` and translates them to `DistutilsExecError`. […]
- Building an extension with a `MACOSX_DEPLOYMENT_TARGET` lower than the interpreter's configured value now raises `compilers.errors.PlatformError` instead of `distutils.errors.DistutilsPlatformError` (the macOS deployment-target […]
- The compilers now define their own exception vocabulary instead of borrowing distutils' framework errors. Language-agnostic exceptions (`Error`, `UnknownFileType`, and a new `PlatformError`) live at `distutils.compilers.errors` […]
- `customize_compiler` now asserts that the compiler-related config variables (`CC`, `CXX`, `CFLAGS`, etc.) resolve to strings, raising `AssertionError` if any are unexpectedly `None` rather than failing later with a less clear […]
### 83.0.0 (2026-07-04) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- Synced with pypa/distutils@d7633fbed including removal of dry_run support (pypa/distutils
### 82.0.0 (2026-02-08) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- `pkg_resources` has been removed from Setuptools. Most common uses of `pkg_resources` have been superseded by the importlib.resources and importlib.metadata projects. […]
### 81.0.0 (2026-02-06) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- Removed support for the --dry-run parameter to setup.py. This one feature by its nature threads through lots of core and ancillary functionality, adding complexity and friction. […]

## Deprecated
### 84.0.0 (2026-08-08) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- Newline-separated `keywords` and `platforms`, which are invalid and corrupt the generated metadata (pypa/setuptools#4887), are now handled forgivingly: each line is treated as a separate item and a deprecation warning is emitted. […]
- `Extension` is now a dataclass, exposing type annotations for its constructor arguments so subclasses (e.g. in Setuptools) can inherit them without redeclaring each parameter. Passing unknown keyword arguments is now deprecated. […]

## Minimum versions and platform support
### 83.0.0 (2026-07-04) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- Require Python 3.10 or later.

## New APIs and features
### 84.2.0 (2026-10-19) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- Added support for building abi3t extensions and abi3.abi3t wheels on Python 3.15 and newer. See `803` and the Python 3.15 "What's New" entry for more details.
- Updated vendored packaging version to 26.3, which adds support for the `abi3t` tag from `803`.
### 84.1.0 (2026-10-19) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- `setuptools.archive_util` now raises the new `UnsafeMember` exception when an archive member would be extracted outside of the extraction directory, where previously such a member was silently skipped. […]
### 84.0.0 (2026-08-08) [source](https://github.com/pypa/setuptools/blob/main/NEWS.rst)
- The C compiler modules now emit log messages through their own `compilers.C.*` loggers instead of the distutils root logger, part of decoupling the compilers package from distutils. […]
- The C compilers gained a `Compiler.call` method -- a thin wrapper over `subprocess.check_call` (with macOS deployment-target env injection) that is the modern replacement for `Compiler.spawn`. […]
- The compilers no longer depend on `distutils.util`, `distutils.version`, `distutils.compat`, or `distutils._macos_compat`. The platform-identification helpers (`get_platform`/`get_host_platform`/`is_mingw`) now live in […]
- The compilers now read their build configuration from the standard library's `sysconfig` instead of `distutils.sysconfig`. Per-compiler customization -- previously `distutils.sysconfig.customize_compiler` -- has moved into […]

## Coverage
- Release notes read for 12 releases; 6 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 84.2.1, 82.0.1, 80.10.2, 80.10.1, 75.3.4, 75.3.3.
- Sources: https://raw.githubusercontent.com/pypa/setuptools/main/NEWS.rst; registry (pypi) for dates.
