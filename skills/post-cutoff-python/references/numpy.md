# numpy (pypi): changes after 2025-06-01

- Latest stable on the registry: **2.5.5** (2026-11-15). Built 2026-11-25.
- 18 stable releases after the cut-off: 2.3.0 (2025-06-07) to 2.5.5 (2026-11-15).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 2.5.5 (2026-11-15) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.5.5-notes.rst)
- Casting a structured void dtype or subarray dtype to `numpy.dtypes.StringDType` now raises a `TypeError` instead of interpreting the raw bytes of each element as UTF-8.
### 2.5.0 (2026-06-21) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.5.0-notes.rst)
- linalg.eig and linalg.eigvals now always return complex arrays: Previously, the return values depended on whether the eigenvalues happen to lie on the real line (which, for a general, non-symmetric matrix, is not guaranteed).
- MSVC support: NumPy now requires minimum MSVC 19.35 toolchain version on Windows platforms. This corresponds to Visual Studio 2022 version 17.5 Preview 2 or newer.
- Cython support: NumPy's Cython headers (accessed via `cimport numpy`) now require Cython 3.0 or newer to build. If you try to compile a project that depends on NumPy's Cython headers using Cython 0.29 or older, you will see a […]
- numpy.where no longer truncates Python integers: Previously, if the `x` or `y` argument of `numpy.where` was a Python integer that was out of range of the output type, it would be silently truncated. […]
- Default memory allocator change: NumPy now uses `PyMem_RawMalloc` and `PyMem_RawFree` as the default memory allocator, instead of system's `malloc` and `free` directly.
- from_dlpack raises BufferError instead of RuntimeError: `np.from_dlpack` now raises `BufferError` instead of `RuntimeError` when the incoming DLPack tensor has an unsupported device, dtype, or exceeds the maximum number of […]
- Corrections to the BTPE binomial sampler: Two independent errors in the Stirling series of the acceptance/rejection step of the BTPE algorithm used by `numpy.random.Generator.binomial` have been corrected
- The third and fourth error terms were added rather than subtracted. This sign error was inherited from section 5.3 of the original 1988 paper by Kachitvichyanukul & Schmeiser, which incorrectly adds all four terms.
- The leading coefficient had a digit-swap typo (`13680` instead of `13860`) that was introduced in the initial implementation.
- datetime64/timedelta64 arithmetic raises on overflow: Addition, subtraction, and integer multiplication of `datetime64` and `timedelta64` values now raise `OverflowError` when the result would overflow `int64` or land on the […]

## Removed or renamed
### 2.5.3 (2026-09-06) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.5.3-notes.rst)
- `MaskedArray._fill_value` would become stale when ufuncs that change dtype left the result holding a fill_value typed for the old dtype. […]
### 2.5.0 (2026-06-21) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.5.0-notes.rst)
- Distutils has been removed
- `numpy.distutils` has been removed
- Passing `None` as dtype to `np.finfo` will now raise a `TypeError` (deprecated since 1.25)
- `numpy.cross` no longer supports 2-dimensional vectors. (Deprecated since 2.0)
- `numpy._core.numerictypes.maximum_sctype` has been removed. (deprecated since 2.0)
- `numpy.row_stack` has been removed in favor of `numpy.vstack`. (deprecated since 2.0)
- `get_array_wrap` has been removed. (deprecated since 2.0)
- `recfromtxt` and `recfromcsv` have been removed from `numpy.lib._npyio` in favor of `numpy.genfromtxt`. (deprecated since 2.0)
### 2.3.0 (2025-06-07) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.3.0-notes.rst)
- Remove deprecated macros like `NPY_OWNDATA` from Cython interfaces in favor of `NPY_ARRAY_OWNDATA` (deprecated since 1.7)
- Remove `numpy/npy_1_7_deprecated_api.h` and C macros like `NPY_OWNDATA` in favor of `NPY_ARRAY_OWNDATA` (deprecated since 1.7)
- Remove alias `generate_divbyzero_error` to `npy_set_floatstatus_divbyzero` and `generate_overflow_error` to `npy_set_floatstatus_overflow` (deprecated since 1.10)
- Remove `np.tostring` (deprecated since 1.19)
- Raise on `np.conjugate` of non-numeric types (deprecated since 1.13)
- (28 more in this category not shown; see the changelog.)

## Deprecated
### 2.5.0 (2026-06-21) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.5.0-notes.rst)
- Many expired deprecations, see below
- Many new deprecations, see below
- `numpy.char.chararray` is deprecated. Use an `ndarray` with a string or bytes dtype instead.
- `numpy.take` now correctly checks if the result can be cast to the provided `out=out` under the same-kind rule. A `DeprecationWarning` is given now when this check fails. […]
- The `numpy.char.[as]array` functions are deprecated. Use an `numpy.[as]array` with a string or bytes dtype instead.
- Setting the dtype attribute is deprecated because mutating an array is unsafe if an array is shared, especially by multiple threads. As an alternative, you can create a view with a new dtype via `array.view(dtype=new_dtype)`.
- Setting the `shape` attribute is deprecated because mutating an array is unsafe if an array is shared, especially by multiple threads. As an alternative, you can create a new view via `np.reshape` or `np.ndarray.reshape`. […]
- Using the `generic` unit in `numpy.timedelta64` is deprecated since this can lead to unexpected behavior such as non-transitive comparison, see gh-28287 for details. […]
### 2.3.0 (2025-06-07) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.3.0-notes.rst)
- The `numpy.typing.mypy_plugin` has been deprecated in favor of platform-agnostic static type inference. Please remove `numpy.typing.mypy_plugin` from the `plugins` section of your mypy configuration. […]
- The `numpy.typing.NBitBase` type has been deprecated and will be removed in a future version.
- But in NumPy 2.2.0, `float64` and `complex128` were changed to concrete subtypes, causing static type-checkers to reject `x: np.float64 = f(np.complex128(42j))`.
- So instead, the better approach is to use `typing.overload`
- (6 more in this category not shown; see the changelog.)

## Minimum versions and platform support
### 2.5.0 (2026-06-21) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.5.0-notes.rst)
- Numpy 2.5.0 is a transitional release. It drops support for Python 3.11, marking the end of distutils, and expires a large number of deprecations made in the 2.0.x release. […]
- NumPy now supports the stable ABI for free-threaded Python as described in `803`.
### 2.3.0 (2025-06-07) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.3.0-notes.rst)
- The minimum supported version was updated from 8.4.0 to 9.3.0, primarily in order to reduce the chance of platform-specific bugs in old GCC versions from causing issues.

## New APIs and features
### 2.5.0 (2026-06-21) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.5.0-notes.rst)
- Many static typing improvements
- Improved support for free threading
- Support for descending sorts.
- It is now possible to register user-dtypes for dlpack export and import via `numpy.dtypes.register_dlpack_dtype`. This functionality is meant to be used with care by user-dtype authors.
- Pixi package definitions: Pixi package definitions have been added for different kinds of from-source builds of NumPy. These can be used in downstream Pixi workspaces via the `pixi-build` feature.
- numpy.ndarray now supports structural pattern matching: `numpy.ndarray` and its subclasses now have the `Py_TPFLAGS_SEQUENCE` flag set, enabling structural pattern matching (PEP 634) with `match`/`case` statements. […]
### 2.3.0 (2025-06-07) [source](https://github.com/numpy/numpy/blob/main/doc/source/release/2.3.0-notes.rst)
- Interactive examples in the NumPy documentation.
- Building NumPy with OpenMP Parallelization.
- Preliminary support for Windows on ARM.
- Improved support for free threaded Python.
- Improved annotations.
- The type parameter of `np.dtype` now defaults to `typing.Any`. This way, static type-checkers will infer `dtype: np.dtype` as `dtype: np.dtype[Any]`, without reporting an error.
- Static type-checkers now interpret: `_: np.ndarray as: npt.NDArray[typing.Any]`.
- NumPy now registers its pkg-config paths with the pkgconf_ PyPI package: The pkgconf_ PyPI package provides an interface for projects like NumPy to register their own paths to be added to the pkg-config search path. […]
- (3 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 18 releases; 4 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 2.5.4, 2.5.2, 2.5.1, 2.4.6, 2.4.5, 2.4.4, 2.4.3, 2.4.2, 2.4.1, 2.3.5, 2.3.4, 2.3.3 and 2 more.
- Sources: https://raw.githubusercontent.com/numpy/numpy/main/doc/source/release/{version}-notes.rst; registry (pypi) for dates.
