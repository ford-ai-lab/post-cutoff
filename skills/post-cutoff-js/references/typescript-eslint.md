# typescript-eslint (npm): changes after 2025-06-01

- Latest stable on the registry: **8.74.0** (2026-11-23). Built 2026-11-25.
- 70 stable releases after the cut-off: 8.33.1 (2025-06-02) to 8.74.0 (2026-11-23).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 8.62.0 (2026-06-22) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8620-2026-06-22)
- remove redundant package.json "files"

## Deprecated
### 8.65.0 (2026-07-20) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8650-2026-07-20)
- eslint-plugin: [no-restricted-imports] deprecate extension rule
### 8.64.0 (2026-07-13) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8640-2026-07-13)
- eslint-plugin: [no-loop-func] support `using` / `await using` declarations and deprecate the rule
### 8.55.0 (2026-02-09) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8550-2026-02-09)
- utils: deprecate defaultOptions in favor of meta.defaultOptions
### 8.42.0 (2025-09-02) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8420-2025-09-02)
- deprecate tseslint.config()
### 8.34.0 (2025-06-09) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8340-2025-06-09)
- type-utils: deprecated getSourceFileOfNode function

## New APIs and features
### 8.74.0 (2026-11-23) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8740-2026-11-23)
- ast-spec: tighten types of `MethodDefinition`
- ast-spec: tighten types of `Property`
- eslint-plugin: [adjacent-overload-signatures] add `ignoreAccessors` option
### 8.73.0 (2026-11-16) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8730-2026-11-16)
- eslint-plugin: [consistent-type-imports] narrow report location
- eslint-plugin: [no-unsafe-class-instance-assignment] add rule
- typescript-estree: add projectService.EXPERIMENTAL_backend for TypeScript 7.1 native parser support over IPC
### 8.72.0 (2026-10-19) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8720-2026-10-19)
- eslint-plugin: lazy load rules
- eslint-plugin: [await-thenable] add `allowMixedPromiseArrays` option
- typescript-estree: error on abstract keyword that precedes export
### 8.71.0 (2026-09-28) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8710-2026-09-28)
- eslint-plugin: [no-unsafe-enum-assignment] add rule
### 8.70.0 (2026-09-07) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8700-2026-09-07)
- eslint-plugin: [no-generated-empty-object-type] add rule
- website: generate per-page social preview cards
### 8.69.0 (2026-08-31) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8690-2026-08-31)
- eslint-plugin: [no-misused-promises] add flagUnions option for checkConditionals
### 8.68.0 (2026-08-24) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8680-2026-08-24)
- eslint-plugin: [strict-void-return] add fix suggestions
- utils: support ESLint rule meta.languages
### 8.67.0 (2026-08-10) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8670-2026-08-10)
- typescript-eslint: export basic globs for using tseslint
### 8.66.0 (2026-08-03) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8660-2026-08-03)
- typescript-estree: handle import.defer() as ImportExpression
### 8.65.0 (2026-07-20) [source](https://github.com/typescript-eslint/typescript-eslint/blob/main/CHANGELOG.md#8650-2026-07-20)
- add warning when TS 7 is detected
- (51 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 70 releases; 41 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 8.72.2, 8.72.1, 8.71.2, 8.71.1, 8.70.1, 8.62.1, 8.61.1, 8.60.1, 8.59.4, 8.59.3, 8.59.2, 8.59.1 and 17 more.
- Sources: https://raw.githubusercontent.com/typescript-eslint/typescript-eslint/main/CHANGELOG.md; registry (npm) for dates.
