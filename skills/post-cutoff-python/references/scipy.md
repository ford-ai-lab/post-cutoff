# scipy (pypi): changes after 2025-06-01

- Latest stable on the registry: **1.18.1** (2026-08-21). Built 2026-11-25.
- 8 stable releases after the cut-off: 1.16.0 (2025-06-22) to 1.18.1 (2026-08-21).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 1.18.0 (2026-06-19) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.18.0-notes.rst)
- The output of `scipy.stats.rankdata` is now always of a floating point dtype -- the result dtype of the input and a Python `float`.
- The behavior of the `residuals` returned by `scipy.linalg.lstsq` has been changed. For `lapack_driver == "gelsy"` or the system being either underdetermined or square, empty residuals are still returned. […]
- The 2nd output object of `scipy.stats.contingency.crosstab` when kwarg `sparse=True` is now a sparse array holding the counts instead of a sparse matrix. […]
- `scipy.stats.obrientransform` now returns a tuple of arrays instead of a single `ndarray`.
- `scipy.stats.multinomial` now returns NaNs when the category probability (`p`) rows/arrays do not sum to unity. This is an expiration of the deprecated behavior of adjusting the final element in the `p` array to compensate. […]
- The `iprint` and `disp` parameters of `scipy.optimize.fmin_l_bfgs_b` have been removed, following the expiry of their deprecation.
- For `scipy.linalg.{sqrtm, logm, signm}`, `disp` (and `sqrtm` `blocksize`) parameters were removed (expired deprecations).
- The deprecated `atol` argument of `scipy.optimize.nnls` has been removed.
- For 2D input, the return type of `scipy.linalg.bandwidth` has changed from `(int, int)` to `(np.int64, np.int64)`.
- The second return type of `scipy.linalg.cho_factor` changed from `bool` to `NDArray[np.bool]`.
- The second return type of `scipy.interpolate.splint` changed from a 1D `float64` array to `None` when `full_output=True`.
- The types of the `k` and `n` attributes of the `BinomTestResult` object returned by `scipy.stats.binomtest` have changed from `int` to `np.float64`.
### 1.17.1 (2026-02-23) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.17.1-notes.rst)
- BUG: linalg solve behavior change breaking downstream tests
### 1.17.0 (2026-01-10) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.17.0-notes.rst)
- The resulting shapes for `transform.Rotation.from_euler` / `from_davenport` have changed to make them consistent with broadcasting rules. […]
### 1.16.0 (2025-06-22) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.16.0-notes.rst)
- Several of the `scipy.linalg` functions for solving a linear system (e.g. `~scipy.linalg.solve`) documented that the RHS argument must be either 1-D or 2-D but did not always raise an error when the RHS argument had more the two […]
- `scipy.stats.bootstrap` now explicitly broadcasts elements of `data` to the same shape (ignoring `axis`) before performing the calculation.
- Several submodule names are no longer available via `from scipy.signal import *`, but may still be imported directly, as detailed at `<
- (1 more in this category not shown; see the changelog.)

## Removed or renamed
### 1.17.0 (2026-01-10) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.17.0-notes.rst)
- `~scipy.sparse.dia_array.tocsr` is approximately three times faster and some unnecessary copy operations have been removed from sparse format interconversions more broadly.
- `scipy.stats.find_repeats` has been removed. Please use `numpy.unique`/`numpy.unique_counts` instead.
- `scipy.linalg` functions for Toeplitz matrices no longer ravel n-d input arguments; instead, multidimensional input is treated as a batch.
- The `seed` and `rand` functions from `scipy.linalg.interpolative` have been removed. Use the `rng` argument instead.
- Complex inputs to `scipy.spatial.distance.cosine` and `scipy.spatial.distance.correlation` now raise an error.
- Support for object arrays and longdoubles has been removed from `scipy.signal.correlate`, `scipy.signal.convolve`, `scipy.signal.lfilter`, and `scipy.signal.sosfilt`.
- `kulczynski1` and `sokalmichener` have been removed from `scipy.spatial.distance`.
- `kron` has been removed from `scipy.linalg`. Please use `numpy.kron`.
### 1.16.0 (2025-06-22) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.16.0-notes.rst)
- `scipy.sparse.conjtransp` has been removed. Use `.T.conj()` instead.
- The `quadrature='trapz'` option has been removed from `scipy.integrate.quad_vec`, and `scipy.stats.trapz` has been removed. Use `trapezoid` in both instances instead.
- `scipy.special.comb` and `scipy.special.perm` now raise when `exact=True` and arguments are non-integral.
- Support for inference of the two sets of measurements from the single argument `x` has been removed from `scipy.stats.linregress`. The data must be specified separately as `x` and `y`.
- Support for NumPy masked arrays has been removed from `scipy.stats.power_divergence` and `scipy.stats.chisquare`.
- A significant number of functions from non-public namespaces (e.g., `scipy.sparse.base`, `scipy.interpolate.dfitpack`) were cleaned up. They were previously already emitting deprecation warnings.
- (5 more in this category not shown; see the changelog.)

## Deprecated
### 1.18.0 (2026-06-19) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.18.0-notes.rst)
- passing `lwork` parameter to `scipy.linalg.qr` has been deprecated. The functionality was rarely used; the function computes the optimal size of the work arrays automatically, therefore users should simply remove their uses of […]
- The sparse construction functions `kron`, `kronsum` and `block_diag` choose return type `sparray` or `spmatrix` depending on the type of the sparse input arrays. When no inputs are sparse, the output is chosen to be `spmatrix`. […]
- A `FutureWarning` is now issued for calling `{r}matvec` on column vectors with `LinearOperator`. Identical behavior can be achieved (and extended to batch dimensions) via `{r}matmat`.
- `scipy.linalg` functions are now stricter--using non-LAPACK dtypes is deprecated. When the deprecations expire, this will effectively limit the dtypes allowed in linear algebra functions to: integers (upcast to float), and […]
- `scipy.spatial.minkowsi_distance`, `scipy.spatial.minkowsi_distance_p`, and `scipy.spatial.distance_matrix` have been deprecated in favor of other superior functions.
- `scipy.spatial.tsearch` has been deprecated because it duplicates functionality more conveniently provided within the `Delaunay` class proper.
- The following functions have been deprecated because they were deemed not practically useful: `scipy.interpolate.pade`, `scipy.interpolate.lagrange`, and `scipy.interpolate.approximate_taylor_polynomial`.
- Setting `spmatrix=True` for the `scipy.io` readers `mmio`, `FFM`, `hb`, and `matlab/_mio` is now deprecated, including when set as the default value.
### 1.17.0 (2026-01-10) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.17.0-notes.rst)
- A new `variant` parameter of `scipy.stats.anderson_ksamp` allows the user to select between three different variants of the statistic, superseding the `midrank` parameter which allowed toggling between two. […]
- The `scipy.odr` module is deprecated in v1.17.0 and will be completely removed in v1.19.0. Users are suggested to use the `odrpack` package instead.
- The default dype behavior of `scipy.sparse.diags` and `scipy.sparse.diags_array` will change in v1.19.0.
- In v1.19.0, `scipy.linalg.hankel` will no longer ravel multidimensional inputs and instead will treat them as a batch.
- (10 more in this category not shown; see the changelog.)

## Minimum versions and platform support
### 1.18.0 (2026-06-19) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.18.0-notes.rst)
- This release requires Python 3.12-3.14 and NumPy 2.0.0 or greater.
### 1.17.0 (2026-01-10) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.17.0-notes.rst)
- This release requires Python 3.11-3.14 and NumPy 1.26.4 or greater.
### 1.16.0 (2025-06-22) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.16.0-notes.rst)
- This release requires Python 3.11-3.13 and NumPy 1.25.2 or greater.

## New APIs and features
### 1.18.0 (2026-06-19) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.18.0-notes.rst)
- SciPy now supports three different build modes for BLAS and LAPACK LP64/ILP64 support, and machinery is provided for downstream `cython_lapack` consumers to gracefully handle LP64/ILP64 backend builds. […]
- Remaining Fortran to C translations have been completed---an experimental Fortran-free build option is now available to developers for testing purposes. Developer feedback is welcome on Fortran-free builds.
- `scipy.signal.whittaker_henderson` now provides access to Whittaker-Henderson smoothing of a discrete signal.
- A large number of `scipy.stats` functions now support lazy arrays and JAX JIT. Array API support has been improved substantially in SciPy, with at least 21 functions gaining new support in this release. […]
- Added ILP64 support to `scipy.linalg.expm` and `scipy.linalg.sqrtm`.
- Added ILP64 BLAS/LAPACK support to SuperLU and PROPACK extensions.
- Support for n-dimensional linear operators has been added to `scipy.sparse.linalg.LinearOperator`, and `LinearOperator` now has a new `rdot` method.
- Support for the `nan_policy` keyword argument has been added to: `scipy.stats.obrientransform`, `scipy.stats.boxcox`, `scipy.stats.boxcox_normmax`, `scipy.stats.yeojohnson`, `scipy.stats.yeojohnson_normmax` […]
### 1.17.0 (2026-01-10) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.17.0-notes.rst)
- Many SciPy functions have gained native support for batching of N-dimensional array input and additional support for the array API standard. An overall summary of the latter is now available in a `set of tables`.
- In `scipy.sparse`, `coo_array` now supports indexing. This includes integers, slices, arrays, `np.newaxis`, `Ellipsis`, in 1D, 2D and the relatively new nD. […]
- In `scipy.spatial`, `transform.Rotation` and `transform.RigidTransform` have been extended to support N-D arrays. `geometric_slerp` now has support for extrapolation.
- `scipy.stats` has gained the matrix t and logistic distributions and many performance and accuracy improvements.
- Initial support for 64-bit integer (ILP64) BLAS and LAPACK libraries has been added, including for MKL and Apple Accelerate. Please report any issues with ILP64 you encounter.
- Added `scipy.sparse.linalg.funm_multiply_krylov`, a restarted Krylov method for evaluating `y = f(tA) b`.
- ENH: Implement all relevant methods for `sparse.dia_array`
- ENH: add `weights` param to `stats.quantile` similarly to...
### 1.16.0 (2025-06-22) [source](https://github.com/scipy/scipy/blob/main/doc/source/release/1.16.0-notes.rst)
- Improved experimental support for the Python array API standard, including new support in `scipy.signal`, and additional support in `scipy.stats` and `scipy.special`. […]
- `scipy.optimize` now uses the new Python implementation from the PRIMA package for COBYLA. The PRIMA implementation fixes many bugs in the old Fortran 77 implementation with a better performance on average.
- (15 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 8 releases; 4 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 1.18.1, 1.16.3, 1.16.2, 1.16.1.
- Sources: https://raw.githubusercontent.com/scipy/scipy/main/doc/source/release/{version}-notes.rst; registry (pypi) for dates.
