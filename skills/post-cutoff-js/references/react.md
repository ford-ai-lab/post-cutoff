# react (npm): changes after 2025-06-01

- Latest stable on the registry: **19.3.1** (2026-10-14). Built 2026-11-25.
- 31 stable releases after the cut-off: 19.0.1 (2025-12-03) to 19.3.1 (2026-10-14).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## New APIs and features
### 19.3.0 (2026-09-09) [source](https://github.com/facebook/react/blob/main/CHANGELOG.md#1930-september-9-2026)
- `<ViewTransition />`: Adds `<ViewTransition />` and `addTransitionType` APIs to power View Transition animations in React
- Fragment Refs: Add Refs to `<Fragment />` to support composable platform behavior
- `browser()`: a new `react-dom` API that returns a usable which errors during server rendering and resolves in the browser. `use(browser())` inside a `<Suspense>` boundary marks a subtree as browser-only without reporting a […]
- Enable Trusted Types API integration
- Added a DEV-only warning when a component appears to have been unblocked by calling `use()` conditionally
- Add `credentialless` as a recognized boolean attribute for iframes
- Add support for `onFullscreenChange` and `onFullscreenError` events
- Add `nonce` to rendered import maps
### 19.2.0 (2025-10-01) [source](https://github.com/facebook/react/blob/main/CHANGELOG.md#1920-october-1st-2025)
- `<Activity>`: A new API to hide and restore the UI and internal state of its children.
- `useEffectEvent` is a React Hook that lets you extract non-reactive logic into an Effect Event.
- `cacheSignal` (for RSCs) lets your know when the `cache()` lifetime is over.
- React Performance tracks appear on the Performance panel’s timeline in your browser developer tools
- Added resume APIs for partial pre-rendering with Web Streams: `resume`: to resume a prerender to a stream.
- Added resume APIs for partial pre-rendering with Node Streams: `resumeToPipeableStream`: to resume a prerender to a stream.
- Updated `prerender` APIs to return a `postponed` state that can be passed to the `resume` APIs.
- Add Node Web Streams (`prerender`, `renderToReadableStream`) to server-side-rendering APIs for Node.js
### 19.2.5 (2026-04-08) [source](https://github.com/facebook/react/blob/main/CHANGELOG.md#1925-march-18-2026)
- Add more cycle protections
### 19.2.4 (2026-01-26) [source](https://github.com/facebook/react/blob/main/CHANGELOG.md#1924-jan-26-2026)
- Add more DoS mitigations to Server Actions, and harden Server Components
- (26 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 24 releases; 11 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 19.2.7, 19.2.6, 19.2.2, 19.2.1, 19.1.8, 19.1.7, 19.1.3, 19.1.2, 19.1.1, 19.0.7, 19.0.6, 19.0.2 and 1 more.
- 7 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/facebook/react/main/CHANGELOG.md; registry (npm) for dates.
