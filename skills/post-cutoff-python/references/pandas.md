# pandas (pypi): changes after 2025-06-01

- Latest stable on the registry: **3.1.1** (2026-11-04). Built 2026-11-25.
- 12 stable releases after the cut-off: 2.3.0 (2025-06-05) to 3.1.1 (2026-11-04).
- New major versions since the cut-off: 3.0.0 (2026-01-21).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 3.1.0 (2026-10-22) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.1.0.rst)
- Datetime/timedelta resolution for numeric input: In pandas 3.0, the default `unit` when creating `datetime64` or `timedelta64` data was changed from nanoseconds to microseconds for many cases (e.g. […]
- `Index.values` and `Index.array` now return read-only arrays for all dtypes, so an `Index` can no longer be silently corrupted by mutating the returned array in place (previously this left the Index displaying the new value while […]
- `DataFrame` arithmetic, comparison, and logical operations with an extension-dtype `Series`, `Index`, or array along the default `axis="columns"` now follow the same rules as the operation between two `Series` (`axis=0` already […]
- `Timedelta` and `to_timedelta` now raise on strings with trailing characters after an `hh:mm:ss` field, such as the AM/PM marker in `"3:25:00 PM"`. […]
- `Timestamp`, `to_datetime`, and `read_csv` with `parse_dates` now return the standard library `datetime.timezone.utc` rather than `dateutil.tz.tzutc()` when a non-ISO-8601 string carries a zero UTC offset (e.g. […]
- `infer_freq` on quarter-start data now reports the equivalent anchor from the first calendar quarter, e.g. `QS-JAN` instead of `QS-OCT`
- `read_csv` and `read_table` now raise `ValueError` when `delimiter=None` is passed together with `sep`, as they already did for any other pair of both; previously the `delimiter` was silently ignored. […]
- `testing.assert_frame_equal` with `check_freq=True` now also checks the `freq` of `DatetimeIndex` and `TimedeltaIndex` *columns*; previously only the `freq` of the index was checked
- `testing.assert_series_equal` with `check_index=False` no longer checks the `freq` attribute of a `DatetimeIndex` or `TimedeltaIndex`, as `freq` is an attribute of the index
- `DataFrameGroupBy.sum` and `DataFrameGroupBy.mean` on float dtypes with sorted grouping keys may differ from prior versions in the last few floating-point digits, due to a faster summation algorithm that does not use Kahan […]
- `DataFrameGroupBy.sum` and `DataFrameGroupBy.prod` on `ArrowDtype` decimal columns now return the maximum decimal precision (`decimal128(38, scale)` or `decimal256(76, scale)`) instead of a precision inferred from the group […]
- `DataFrame.select_dtypes` now raises `TypeError` when a Python class that does not name a dtype, such as `decimal.Decimal`, `datetime.date` or `Timestamp`, is passed to `include` or `exclude`. […]
### 3.0.0 (2026-01-21) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.0.0.rst)
- Datetime/timedelta resolution inference: Prior to pandas 3.0, whenever converting a sequence of strings, stdlib `datetime` objects, `np.datetime64` objects, or integers to a `datetime64` / `timedelta64` dtype, this would always […]
- The new default resolution when parsing strings is microseconds, falling back to nanoseconds when the precision of the string requires it.
- The resolution of the input is preserved for stdlib `datetime` objects (i.e. microseconds) or `np.datetime64`/`np.timedelta64` objects (i.e. the unit, capped to the supported range of seconds to nanoseconds; […]
- For integer input, the resolution used to interpret the integer value is used as the resulting resolution (or capped to the supported range of seconds to nanoseconds). […]
- Time zones are now represented by standard library zoneinfo instead of pytz by default: pandas now uses `zoneinfo` from the standard library (or `datetime.timezone` for fixed offsets) as the default timezone representation, for […]
- concat no longer ignores sort when all objects have a DatetimeIndex: When all objects passed to `concat` have a `DatetimeIndex`, passing `sort=False` will now result in the non-concatenation axis not being sorted. […]
- `Series.apply` and `DataFrame.apply` with a list-like or dict-like `func` argument.
- `Series.shift`, `DataFrame.shift`, `SeriesGroupBy.shift`, `DataFrameGroupBy.shift` with the `periods` argument a list of length greater than 1.
- `DataFrame.join` with `other` a list of one or more Series or DataFrames and `how="inner"`, `how="left"`, or `how="right"`.
- `Series.str.cat` with `others` a Series or DataFrame.
- Changed behavior of pd.offsets.Day to always represent calendar-day: In previous versions of pandas, `offsets.Day` represented a fixed span of 24 hours, disregarding Daylight Savings Time transitions. […]
- `pd.offsets.Day(n)` no longer compares as equal to `pd.offsets.Hour(24*n)`
- (45 more in this category not shown; see the changelog.)

## Removed or renamed
### 3.0.0 (2026-01-21) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.0.0.rst)
- Enforced deprecation of aliases `M`, `Q`, `Y`, etc. in favour of `ME`, `QE`, `YE`, etc. for offsets
- Renamed the following offset aliases
- `DataFrameGroupBy.idxmin`, `DataFrameGroupBy.idxmax`, `SeriesGroupBy.idxmin`, and `SeriesGroupBy.idxmax` will now raise a `ValueError` when a group has all NA values, or when used with `skipna=False` and any NA value is […]
- `concat` no longer ignores empty objects when determining output dtypes
- `concat` with all-NA entries no longer ignores the dtype of those entries when determining the result dtype
- `read_excel`, `read_json`, `read_html`, and `read_xml` no longer accept raw string or byte representation of the data. That type of data must be wrapped in a `StringIO` or `BytesIO`
- `to_datetime` with a `unit` specified no longer parses strings into floats, instead parses them the same way as without `unit`
- `SeriesGroupBy.agg` no longer pins the name of the group to the input passed to the provided `func`
- (119 more in this category not shown; see the changelog.)

## Deprecated
### 3.1.0 (2026-10-22) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.1.0.rst)
- PDEP-8: https://pandas.pydata.org/pdeps/0008-inplace-methods-in-pandas.html
- The `inplace` keyword is deprecated (and will eventually be removed) for all methods that do not actually work "inplace".
- For most extension dtypes (e.g. `category`, `str`, or the nullable dtypes), `Series.values` and `Index.values` return the underlying `pandas.api.extensions.ExtensionArray`. […]
- `DatetimeTZDtype`: a `datetime64` array converted to UTC, dropping the timezone
- `PeriodDtype`: an object-dtype array of `Period` objects
- `IntervalDtype` (`Series` only): an object-dtype array of `Interval` objects
- This is now deprecated and emits a `pandas.errors.Pandas4Warning`. In pandas 4.0, `.values` will return the ExtensionArray for these dtypes as well.
- Inferred frequencies will be returned as offsets: `infer_freq`, `DatetimeIndex.inferred_freq`, `TimedeltaIndex.inferred_freq`, and `Series.dt.freq` return a string such as `"D"`. […]
### 3.0.0 (2026-01-21) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.0.0.rst)
- pandas 3.0.0 updates the deprecation policy to clarify which deprecation warnings will be issued, using a new 3-stage policy: using `DeprecationWarning` initially, then switching to `FutureWarning` for broader visibility in the […]
- All warnings for upcoming changes in pandas will have the base class `pandas.errors.PandasChangeWarning`. Users may also use the following subclasses to control warnings.
- `pandas.errors.Pandas4Warning`: Warnings which will be enforced in pandas 4.0.
- `pandas.errors.Pandas5Warning`: Warnings which will be enforced in pandas 5.0.
- (109 more in this category not shown; see the changelog.)

## Minimum versions and platform support
### 3.1.0 (2026-10-22) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.1.0.rst)
- Some minimum supported versions of dependencies were updated. If installed, we now require
- +-----------------+---------------------+ | Package | New minimum version | +=================+=====================+ | numpy | 2.0.2 | +-----------------+---------------------+ | python-dateutil | 2.9.0 | […]
### 3.0.0 (2026-01-21) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.0.0.rst)
- pandas 3.0.0 supports Python 3.11 and higher.
- Some minimum supported versions of dependencies were updated. The following required dependencies were updated
- +-----------------+----------------------+ | Package | New Minimum Version | +=================+======================+ | numpy | 1.26.0 | +-----------------+----------------------+

## New APIs and features
### 3.1.0 (2026-10-22) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.1.0.rst)
- Filtering with a boolean mask in DataFrame.filter and Series.filter: `DataFrame.filter` and `Series.filter` now accept a boolean mask through the new `cond` keyword, keeping the rows (or columns with `axis=1`) where the mask is […]
- Faster read_csv, with parallel reads of large files: Reading CSV files with the default `engine="c"` is considerably faster in this release: tokenizing, type inference, and the conversion of integer, float, string and datetime […]
- Added `union_categories` parameter to `concat` to preserve categorical dtype by unioning categories when concatenating categoricals with different categories
- Added `Index.replace` method to support value replacement functionality similar to `Series.replace`
- `Series.to_json` now supports serializing custom ExtensionArrays (by correctly using the `_values_for_json` method of an ExtensionArray)
- `read_csv` now supports `dtype="complex64"` and `dtype="complex128"` with the C engine, enabling round-tripping of complex-number columns written by `DataFrame.to_csv`
- `read_excel` and `ExcelFile` now infer `engine` from a workbook object created by a supported engine's library, such as an `openpyxl.Workbook`, instead of raising
- Improved the precision of float parsing in `read_csv`
### 3.0.0 (2026-01-21) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v3.0.0.rst)
- Dedicated string data type by default: Historically, pandas represented string columns with NumPy `object` data type. This representation has numerous problems: it is not specific to strings (any Python object can be stored in an […]
- Inferred by default for string data (instead of object dtype)
- The `str` dtype can only hold strings (or missing values), in contrast to `object` dtype. (setitem with non string fails)
- The missing value sentinel is always `NaN` (`np.nan`) and follows the same missing value semantics as the other default dtypes.
- Consistent copy/view behaviour with Copy-on-Write: The new "copy-on-write" behaviour in pandas 3.0 brings changes in behavior in how pandas operates with respect to copies and views. A summary of the changes
- The result of *any* indexing operation (subsetting a DataFrame or Series in any way, i.e. including accessing a DataFrame column as a Series) or any method returning a new DataFrame or Series, always *behaves as if* it were a […]
- As a consequence, if you want to modify an object (DataFrame or Series), the only way to do this is to directly modify that object itself.
- Initial support for pd.col() syntax to create expressions: This release introduces `col` to refer to a DataFrame column by name and build up expressions.
### 2.3.0 (2025-06-05) [source](https://github.com/pandas-dev/pandas/blob/main/doc/source/whatsnew/v2.3.0.rst)
- Upcoming changes in pandas 3.0: pandas 3.0 will bring two bigger changes to the default behavior of pandas.
- Dedicated string data type by default: Historically, pandas represented string columns with NumPy `object` data type. This representation has numerous problems: it is not specific to strings (any Python object can be stored in an […]
- (113 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 12 releases; 7 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 3.1.1, 3.0.5, 3.0.1, 2.3.2, 2.3.1.
- Sources: https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/source/whatsnew/v{version}.rst; registry (pypi) for dates.
