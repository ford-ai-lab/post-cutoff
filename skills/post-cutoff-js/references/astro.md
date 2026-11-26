# astro (npm): changes after 2025-06-01

- Latest stable on the registry: **7.4.13** (2026-11-18). Built 2026-11-25.
- 169 stable releases after the cut-off: 4.16.19 (2025-08-19) to 7.4.13 (2026-11-18).
- New major versions since the cut-off: 6.0.0 (2026-03-10), 7.0.0 (2026-06-22).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 7.0.0 (2026-06-22) [source](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#700)
- Upgrade to Vite v8
- Makes `'jsx'` the default value for `compressHTML`
- Adds background dev server management for AI coding agents.
- Removes the `@astrojs/db` package as it is no longer maintained.
- Replaces the Go compiler with a Rust-based version.
- Makes Sätteri the default Markdown processor
- Enables advanced routing by default.
- Removes deprecated APIs exported from `astro:transitions`.

## Removed or renamed
### 7.0.0 (2026-06-22) [source](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#700)
- Removes the setting `experimental.queuedRendering`. The new rendering engine is now stable and replaces the old one.
- The construction of the queue has been removed, instead now Astro uses a streaming approach where components are rendered and flushed as they are encountered.
- The node polling feature has been removed because it doesn't yield concrete savings.

## Minimum versions and platform support
### 7.4.2 (2026-10-21) [source](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#742)
- Bumps the minimum supported Node.js version to 22.23.4, which includes the fixes from the October 2026 Node.js security releases
### 7.4.0 (2026-10-15) [source](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#740)
- Increases the minimum Node.js version to 22.22.0

## New APIs and features
### 7.4.0 (2026-10-15) [source](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#740)
- Adds a new `--timings` flag to `astro build` to help you find what slows down your builds
- Adds a new optional `getFontProperties()` callback to font providers
- Adds a `fetch()` function to the font provider `init()` context
- Adds `experimental.redirectPage`, letting you provide your own `src/pages/3xx.astro` in place of the redirect page Astro generates in static builds.
- Adds a `notFound()` handler to `astro/fetch` and `astro/hono` that renders the custom 404 page when no route matches, including a prerendered `404.astro`
- Adds support for separate `build` and `runtime` image services
- Allows integrations to control where Astro writes client, server, and prerender build output.
- Lets custom prerenderers report the images used on prerendered pages
### 7.3.0 (2026-09-03) [source](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#730)
- Adds `--ignore-lock` flag to `astro preview`, allowing multiple preview servers to run simultaneously on different ports. This is useful for E2E testing workflows (e.g., Playwright) that need to run several preview servers at […]
- Adds a `logger` parameter to image services hooks
- Adds `logger` to the context object passed to cache providers
### 7.2.0 (2026-08-06) [source](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#720)
- Adds the `astro preview --background` flag to start preview servers as background processes.
- Adds support for paths relative to your project root in `logger.entrypoint`
- Widens the `AstroPrerenderer` `render()` return type so prerenderers can report incremental-build metadata
- Adds `session: false` in `astro.config` to opt out of session support. Projects that do not set `session: false` see no behavior change.
- Adds experimental support for incremental static builds with `experimental.incrementalBuild`.
- Adds the optional `digest` property to content collection entries.
### 7.1.0 (2026-07-16) [source](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md#710)
- Adds a new `deferRender` option to the `glob()` content loader
- (10 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 51 releases; 6 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 7.4.13, 7.4.12, 7.4.11, 7.4.10, 7.4.9, 7.4.8, 7.4.7, 7.4.6, 7.4.5, 7.4.4, 7.4.3, 7.4.1 and 33 more.
- 118 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/withastro/astro/main/packages/astro/CHANGELOG.md; registry (npm) for dates.
