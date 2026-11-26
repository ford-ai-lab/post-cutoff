# mypy (pypi): changes after 2025-06-01

- Latest stable on the registry: **2.4.1** (2026-10-28). Built 2026-11-25.
- 17 stable releases after the cut-off: 1.16.1 (2025-06-16) to 2.4.1 (2026-10-28).
- New major versions since the cut-off: 2.0.0 (2026-05-06).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 2.0 (2026-05-06) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-20)
- Mypy used to bundle stubs for a few packages in versions 0.812 and earlier. To navigate the transition, mypy used to report missing types for these packages even if `--ignore-missing-imports` was set. […]
- Contributed by Shantanu in PR 18372.
### 1.20 (2026-03-31) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-120)
- Remove prohibit_none_typevar_overlap (Shantanu, PR 20864)
- The `--force-uppercase-builtins` flag was deprecated and has been a no-op since mypy 1.17.0. Since mypy has dropped support for Python 3.9, the `--force-union-syntax` flag is no longer necessary.
- Contributed by Marc Mueller and.
### 1.17 (2025-07-14) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-117)
- Remove inconsistencies in operator handling (Ivan Levkivskyi, PR 19250)
- Mypy now requires `--python-version 3.9` or greater. Support for targeting Python 3.8 is fully removed now. Since 3.8 is an unsupported version, mypy will default to the oldest supported version (currently 3.9) if you still try […]
- This change is necessary because typeshed stopped supporting Python 3.8 after it reached its End of Life in October 2024.

## Deprecated
### 1.17 (2025-07-14) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-117)
- Mypy only supports Python 3.9+. The `--force-uppercase-builtins` flag is now deprecated as unnecessary, and a no-op. It will be removed in a future version.
- Contributed by Marc Mueller

## Minimum versions and platform support
### 2.0 (2026-05-06) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-20)
- Mypy no longer supports type checking code with `--python-version 3.9`. Use `--python-version 3.10` or newer.
### 1.20 (2026-03-31) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-120)
- Mypy no longer supports running with Python 3.9, which has reached end of life. When running mypy with Python 3.10+, it is still possible to type check code that needs to support Python 3.9 with the `--python-version 3.9` […]
- Mypy now supports t-strings that were introduced in Python 3.14.

## New APIs and features
### 2.4 (2026-10-01) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-24)
- Add support for PEP 661 sentinels (Edgar Ramírez Mondragón, PR 21647)
- Add the `am_send` slot and use `PyIter_Send` for `await` and `yield from` (Jukka Lehtosalo, PR 21979)
### 2.2 (2026-07-08) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-22)
- Add `librt.strings.toupper` and `librt.strings.tolower` codepoint primitives (Vaggelis Danias, PR 21553)
- Add `librt.strings.isidentifier` codepoint primitive (Vaggelis Danias, PR 21522)
- Add `librt.strings.isalpha` codepoint primitive (Vaggelis Danias, PR 21521)
- Add `librt.strings.isalnum` codepoint primitive (Vaggelis Danias, PR 21509)
- Add `librt.strings.isdigit` codepoint primitive (Vaggelis Danias, PR 21504)
- Add `librt.strings.isspace` char primitive (Vaggelis Danias, PR 21462)
- Add Python version checks to native parser (Kevin Kannammalil, PR 21539)
- Allow nativeparse to parse source code directly (bzoracler, PR 21260)
### 2.1 (2026-05-11) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-21)
- Enable incremental self-compilation (Vaggelis Danias, PR 21369)
### 2.0 (2026-05-06) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-20)
- Expose `--num-workers` and `--native-parser` (Ivan Levkivskyi, PR 21387)
- Add suggestions for misspelled module imports (Kevin Kannammalil, PR 20695)
### 1.20 (2026-03-31) [source](https://github.com/python/mypy/blob/master/CHANGELOG.md#mypy-120)
- Add some additional narrowing test cases (Shantanu, PR 20598)
- Add more tests for narrowing logic (Shantanu, PR 20672)
- Add --warn-unreachable to more tests (Shantanu, PR 20977)
- Add support for Python 3.14 t-strings (PEP 750) (Neil Schemenauer and Brian Schubert, PR 20850)
- Add implicit module dependency if using t-string (Jukka Lehtosalo, PR 20900)
- (15 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 15 releases; 9 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 2.4.1, 2.3.1, 2.3, 1.20.2, 1.19, 1.17.1.
- 2 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/python/mypy/master/CHANGELOG.md; registry (pypi) for dates.
