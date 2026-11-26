# @angular/core (npm): changes after 2025-06-01

- Latest stable on the registry: **22.3.0** (2026-11-18). Built 2026-11-25.
- 139 stable releases after the cut-off: 18.2.14 (2025-09-10) to 22.3.0 (2026-11-18).
- New major versions since the cut-off: 21.0.0 (2025-11-19), 22.0.0 (2026-06-03).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 22.0.0 (2026-06-03) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2200-2026-06-03)
- This change will trigger the `nullishCoalescingNotNullable` and `optionalChainNotNullable` diagnostics on exisiting projects. You might want to disable those 2 diagnotiscs in your `tsconfig` temporarily.
- data prefixed attribute no-longer bind inputs nor outputs.
- The compiler will throw when there a when inputs, outputs or model are binding to the same input/outputs.
- `in` variables will throw in template expressions.
- compiler-cli
- Elements with multiple matching selectors will now throw at compile time.
- The second arguement of appRef.bootstrap does not accept `any` anymore. Make sure the element you pass is not nullable.
- * TypeScript versions older than 6.0 are no longer supported.
- Leave animations are no longer limited to the element being removed.
- Component with undefined `changeDetection` property are now `OnPush` by default. Specify `changeDetection: ChangeDetectionStrategy.Eager` to keep the previous behavior.
- change AnimationCallbackEvent.animationComplete signature
- `ChangeDetectorRef.checkNoChanges` was removed. In tests use `fixture.detectChanges()` instead.
### 21.1.6 (2026-02-25) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2116-2026-02-25)
- Angular now only applies known attributes from HTML in translated ICU content. Unknown attributes are dropped and not rendered.
- fix: fix LCP image detection with duplicate URLs
- compiler-cli
- fix: detect uninvoked functions in defer trigger expressions
- fix: block creation of sensitive URI attributes from ICU messages
### 21.0.0 (2025-11-19) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2100-2025-11-19)
- (test only) - `TestBed` now provides a fake `PlatformLocation` implementation that supports the Navigation API. This may break some tests, though we have not observed any failures internally. […]
- `ngComponentOutletContent` is now of type `Node[][] | undefined` instead of `any[][] | undefined`.
- NgModuleFactory has been removed, use NgModule instead.
- compiler-cli
- Previously hidden type issues in host bindings may show up in your builds. Either resolve the type issues or set `"typeCheckHostBindings": false` in the `angularCompilerOptions` section of your tsconfig.
- The Angular compiler now produces an error when the the `emitDeclarationOnly` TS compiler option is enabled as this mode is not supported.
- The server-side bootstrapping process has been changed to eliminate the reliance on a global platform injector.
- (36 more in this category not shown; see the changelog.)

## Deprecated
### 22.1.0 (2026-07-29) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2210-2026-07-29)
- `HttpClient.jsonp`, `HttpClientJsonpModule`, and related JSONP classes/functions are deprecated. Use standard HTTP requests instead.
- fix: skip transfer cache for uncacheable HTTP traffic
- feat: Add an error for --global-foo cases
- feat: Disable &apos;--global-&apos; error outside of g3
- feat: Namespace CSS variables to the app
- feat: Support css var namespacing in properties
- fix: permissive whitespace parsing in default never blocks
- fix: support foreign components defined outside top-level scope
### 22.0.1 (2026-06-10) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2201-2026-06-10)
- platform-server
- XHR support in `@angular/platform-server` is deprecated. Use standard `fetch` APIs instead. (cherry picked from commit
- fix: escape CSS string-terminating characters in escapeCssUrl
- fix: Limits date format string length
- (358 more in this category not shown; see the changelog.)

## Minimum versions and platform support
### 22.0.0 (2026-06-03) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2200-2026-06-03)
- feat: drop support for TypeScript 5.9
### 21.0.0 (2025-11-19) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2100-2025-11-19)
- fix: drop support for TypeScript 5.8

## New APIs and features
### 22.3.0 (2026-11-18) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2230-2026-11-18)
- feat: report unknown property bindings on explicit ng-template elements
- feat: add check for numeric CSS properties requiring units
- feat: port preprocessor serve tool
- feat: support synchronous WASM execution in preprocessor
- feat: add `scrollMargin` to `@defer` viewport options
- feat: expose `debugging` annotation
- feat: support increment/decrement operators in expressions
- feat: add `HttpClient.query()` method for HTTP QUERY requests
### 22.2.0 (2026-09-23) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2220-2026-09-23)
- feat: allow template to access private props
- feat: add strictUnclaimedEventNames option to catch misspelled output bindings
- feat: scope type-checking of keyed defer blocks
- feat: add ErrorBoundary programmatic APIs
- feat: add utility for testing directives
- feat: allow reading `Injector` from a view or content query
- feat: support annotations in WebMCP tool declarations
- feat: allow permanent hidden fields in signal forms
### 21.2.0 (2026-02-25) [source](https://github.com/angular/angular/blob/main/CHANGELOG.md#2120-2026-02-25)
- feat: add an 'outlet' injector option for ngTemplateOutlet
- feat: Add Location strategies to manage trailing slash on write
- (75 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 138 releases; 25 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 22.2.7, 22.2.6, 22.2.5, 22.2.4, 22.2.3, 22.2.2, 22.2.1, 22.1.8, 22.1.7, 22.1.6, 22.1.5, 22.1.4 and 101 more.
- 1 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/angular/angular/main/CHANGELOG.md; registry (npm) for dates.
