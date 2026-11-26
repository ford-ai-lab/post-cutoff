# react-router (npm): changes after 2025-06-01

- Latest stable on the registry: **8.5.3** (2026-11-24). Built 2026-11-25.
- 52 stable releases after the cut-off: 6.30.2 (2025-11-13) to 8.5.3 (2026-11-24).
- New major versions since the cut-off: 8.0.0 (2026-06-17).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 8.4.0 (2026-09-15) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v840)
- ⚠️ This contains some breaking changes to exported `UNSAFE_` contexts, so please review carefully if you are using those unsafe exports
### 8.0.0 (2026-06-17) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v800)
- Remove the `future.v8_trailingSlashAwareDataRequests` flag
- Update `tsconfig.json` `target`/`lib` from `ES2020 -> ES2022`
- Switch the published packages in `packages/` to ESM-only.
- Remove deprecated `data` parameter in favor of `loaderData` for `meta` APIs (to align with `Route.ComponentProps`)
- Remove `future.v8_passThroughRequests` flag - the raw incoming `request` is now always passed through to `loader`/`action`. Use `url` for the normalized URL without React Router-specific implementation details (`.data` suffixes […]
- Remove internal `hasErrorBoundary` field added to `router.routes` when using a data router
- Remove `react-router-dom` package
- Remove `future.v8_middleware` flag — middleware is always enabled in v8
- Update minimum React version to 19.2.7
### 7.15.0 (2026-05-05) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v7150)
- ⚠️ This is a breaking change if you have already opted into the unstable version - you will need to update your code accordingly
### 7.14.0 (2026-04-02) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#7140)
- UNSTABLE RSC FRAMEWORK MODE BREAKING CHANGE - Existing route module exports remain unchanged from stable v7 non-RSC mode, but new exports are added for RSC mode. […]
### 7.12.0 (2026-01-07) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#7120)
- Data: `/a/b/c.data`: `/a/b/c` ⚠️
### 7.10.0 (2025-12-02) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#7100)
- ⚠️ This is a breaking change if you have begun using `fetcher.unstable_reset()`
### 7.8.0 (2025-08-07) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#780)
- ⚠️ This may cause some type errors to show up in your code for unguarded `match.data` accesses - you should properly guard for `undefined` values in those scenarios.
- ⚠️ This is a breaking change if you've adopted the `staticHandler` `unstable_respond` API
- ⚠️ This is a breaking change if you have adopted middleware and are using a custom server with a `getLoadContext` function
- ⚠️ This is a breaking change if you have adopted the `unstable_getContext` prop

## Removed or renamed
### 8.5.2 (2026-11-18) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v852)
- The error is still logged with `console.error`; only the second, uncaught throw is removed
### 8.0.0 (2026-06-17) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v800)
- `hasErrorBoundary` is no longer accepted on `RouteObject` (`IndexRouteObject`/`NonIndexRouteObject`), `DataRouteObject`, `<Route>` JSX props, or as a key in `lazy` route definitions.
- The `future.v8_middleware` flag has been removed; middleware is now always enabled
- `getLoadContext` functions in custom servers must return a `RouterContextProvider` — returning a plain object is no longer supported
- The `MiddlewareEnabled` type (previously exported as `UNSAFE_MiddlewareEnabled`) has been removed since the conditional it gated is now unconditional
### 7.15.0 (2026-05-05) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v7150)
- Remove `unstable_subResourceIntegrity` from the runtime `FutureConfig` type; the flag is now controlled by the top-level `subResourceIntegrity` option in `react-router.config.ts`
- This includes adding back the optimization that was removed in `7.6.0`
### 7.8.0 (2025-08-07) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#780)
- The API has been renamed to `unstable_generateMiddlewareResponse` for clarity

## Deprecated
### 8.5.0 (2026-10-19) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v850)
- Deprecate React Router's view transition APIs in favor of React's `<ViewTransition>` component, available in React 19.3 and later
- Deprecate the `viewTransition` props/options, `useViewTransitionState`, and `NavLink`'s `isTransitioning` render prop and `transitioning` class
### 8.4.0 (2026-09-15) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v840)
- Deprecate the `createStaticRouter({ branches })` option
- `createStaticRouter` now caches route branches internally, ignores `branches`, and logs a deprecation warning when the option is provided
- The deprecated `EntryContext.branches` property remains available for compatibility but is always an empty array
### 7.15.1 (2026-05-14) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v7151)
- This should allow you to consolidate usages of the following hooks which will likely be deprecated and removed in a future major version
### 7.10.0 (2025-12-02) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#7100)
- The `match.shouldLoad` API is now marked deprecated in favor of these more powerful alternatives
### 7.8.0 (2025-08-07) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#780)
- `@deprecated` warnings have been added to the existing `data` properties to point users to new `loaderData` properties, in preparation for removing the `data` properties in a future major release

## Minimum versions and platform support
### 8.0.0 (2026-06-17) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v800)
- Update minimum Node version to 22.22.0

## New APIs and features
### 8.1.0 (2026-06-29) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v810)
- Return route metadata from server request, client navigation, and client fetcher instrumentations
### 8.0.0 (2026-06-17) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v800)
- Bump dependencies
### 7.17.0 (2026-06-04) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v7170)
- Ship a subset of the official documentation inside the `react-router` package
### 7.16.0 (2026-05-28) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v7160)
- Stabilize `future.unstable_trailingSlashAwareDataRequests` as `future.v8_trailingSlashAwareDataRequests`
### 7.15.0 (2026-05-05) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#v7150)
- Stabilize `unstable_defaultShouldRevalidate` as `defaultShouldRevalidate` on `<Link>`, `<Form>`, `useLinkClickHandler`, `useSubmit`, `fetcher.submit`, and `setSearchParams`
- Stabilize the instrumentation APIs. `unstable_instrumentations` is now `instrumentations` and `unstable_pattern` is now `pattern`
- Stabilize `unstable_mask` as `mask` on `<Link>`, `useLinkClickHandler`, and `useNavigate`, and rename the corresponding `Location.unstable_mask` field to `Location.mask`
- Stabilize the `unstable_normalizePath` option on `staticHandler.query` and `staticHandler.queryRoute` as `normalizePath`
- Stabilize `future.unstable_passThroughRequests` as `future.v8_passThroughRequests`
- Stabilize `unstable_url` as `url` on `loader`, `action`, and `middleware` function args
- Stabilize `unstable_useTransitions` as `useTransitions` on `<BrowserRouter>`, `<HashRouter>`, `<HistoryRouter>`, `<MemoryRouter>`, `<Router>`, `<RouterProvider>`, `<HydratedRouter>`, and `useLinkClickHandler`
### 7.13.0 (2026-01-23) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#7130)
- Add `crossOrigin` prop to `Links` component
### 7.12.0 (2026-01-07) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#7120)
- Add additional layer of CSRF protection by rejecting submissions to UI routes from external origins. If you need to permit access to specific external origins, you can specify them in the `react-router.config.ts` config […]
### 7.11.0 (2025-12-17) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#7110)
- Stabilize `<HydratedRouter onError>`/`<RouterProvider onError>`
### 7.10.0 (2025-12-02) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#7100)
- Stabilize `fetcher.reset()`
- Stabilize the `dataStrategy` `match.shouldRevalidateArgs`/`match.shouldCallHandler()` APIs.
### 7.9.0 (2025-09-12) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#790)
- Stabilize middleware and context APIs.
### 7.8.0 (2025-08-07) [source](https://github.com/remix-run/react-router/blob/main/packages/react-router/CHANGELOG.md#780)
- Add `nonce` prop to `Links` & `PrefetchPageLinks`
- (2 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 40 releases; 17 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 8.5.3, 8.5.1, 8.3.1, 8.3.0, 8.2.0, 8.0.1, 7.18.0, 7.14.2, 7.14.1, 7.13.2, 7.13.1, 7.10.1 and 11 more.
- 12 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/remix-run/react-router/main/packages/react-router/CHANGELOG.md; registry (npm) for dates.
