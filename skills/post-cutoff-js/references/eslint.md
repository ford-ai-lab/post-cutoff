# eslint (npm): changes after 2025-06-01

- Latest stable on the registry: **10.15.0** (2026-11-13). Built 2026-11-25.
- 40 stable releases after the cut-off: 9.29.0 (2025-06-13) to 10.15.0 (2026-11-13).
- New major versions since the cut-off: 10.0.0 (2026-02-06).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 10.0.0 (2026-02-06) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v1000---february-6-2026)
- feat!: estimate rule-tester failure location (ST-DDT)
- feat!: replace `chalk` with `styleText` and add `color` to `ResultsMeta` (루밀LuMir)
- feat!: enable JSX reference tracking (Pixel998)
- feat!: add `name` to configs (Kirk Waiblinger)
- fix!: remove deprecated `SourceCode` methods (Pixel998)
- feat!: update dependency minimatch to v10 (renovate[bot])
- fix!: stricter rule tester assertions for valid test cases (唯然)
- fix!: Remove deprecated rule context methods (Nicholas C. Zakas)
- feat!: remove eslintrc support (Francesco Trotta)
- feat!: Use `ScopeManager#addGlobals()` (Milos Djermanovic)
- fix!: add `uniqueItems: true` in `no-invalid-regexp` option (Tanuj Kanti)
- feat!: Program range span entire source text (Pixel998)
- (9 more in this category not shown; see the changelog.)

## Minimum versions and platform support
### 10.0.3 (2026-03-06) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v1003---march-6-2026)
- chore: eslint-config-eslint require Node `^20.19.0 || ^22.13.0 || >=24` (Milos Djermanovic)
### 10.0.0 (2026-02-06) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v1000---february-6-2026)
- feat!: Require Node.js `^20.19.0 || ^22.13.0 || >=24` (Milos Djermanovic)

## New APIs and features
### 10.15.0 (2026-11-13) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v10150---november-13-2026)
- feat: check proto and assignment targets in `func-names` (Lê Văn Xuân Hoàn)
- feat: recognize string and computed keys in `accessor-pairs` descriptors (Lê Văn Xuân Hoàn)
- feat: handle TS type assertions in `no-invalid-this` (Valentin)
- feat: check individual specifier importKind in `no-shadow` (Lê Văn Xuân Hoàn)
- feat: update error location to head for `default-case` (Tanuj Kanti)
### 10.14.0 (2026-10-30) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v10140---october-30-2026)
- feat: fix property descriptor handling in `func-name-matching` (xbinaryx)
### 10.13.0 (2026-10-16) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v10130---october-16-2026)
- feat: report references inside IIFEs in `no-use-before-define` (Irfan fandi)
- feat: add `globalThis` to `no-obj-calls` (synthex-byte)
- feat: check `yield*` expressions in `no-unsafe-optional-chaining` (xbinaryx)
### 10.12.0 (2026-10-02) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v10120---october-2-2026)
- feat: handle astral letters in `new-cap` (sary)
- feat: allow `SourceCode#getText()` to accept tokens and comments (electrohyun)
### 10.11.0 (2026-09-18) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v10110---september-18-2026)
- feat: object-shorthand handle quoted properties for `ignoreConstructors` (Pavel)
- feat: report unsafe labeled `continue` in `no-unsafe-finally` rule (electrohyun)
- feat: only exempt `new-cap` built-ins that reference the global (sethamus)
### 10.10.0 (2026-09-04) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v10100---september-4-2026)
- feat: add `d` and `v` flags to `no-unexpected-multiline` (Gihyeon Jeong / 정기현)
- feat: check `Object.prototype` property names in `new-cap` (crimsonjay0)
- feat: no-extra-bind false negatives with class fields and static blocks (synthex-byte)
### 10.9.0 (2026-08-21) [source](https://github.com/eslint/eslint/blob/main/CHANGELOG.md#v1090---august-21-2026)
- feat: handle underflow in no-loss-of-precision (Rithish S)
- (65 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 40 releases; 28 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 10.9.1, 10.8.1, 10.4.1, 10.2.1, 10.0.2, 10.0.1, 9.39.5, 9.39.4, 9.39.3, 9.39.2, 9.39.1, 9.30.1.
- Sources: https://raw.githubusercontent.com/eslint/eslint/main/CHANGELOG.md; registry (npm) for dates.
