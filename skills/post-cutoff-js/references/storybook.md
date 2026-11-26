# storybook (npm): changes after 2025-06-01

- Latest stable on the registry: **10.6.9** (2026-11-25). Built 2026-11-25.
- 120 stable releases after the cut-off: 7.6.21 (2025-12-17) to 10.6.9 (2026-11-25).
- New major versions since the cut-off: 10.0.0 (2025-10-28).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 10.4.0 (2026-05-14) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1040)
- Svelte: Fix Vite 8 + Vitest breaking rolldown deps scanner
- Vitest: Fix agent detection breaking runs

## Removed or renamed
### 10.3.0 (2026-03-18) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1030)
- Manifest: Rename `experimentalComponentsManifest` → `componentsManifest`, default to `true`
### 10.1.0 (2025-11-26) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1010)
- Core: Rename `Listbox` component to `ActionList` and use it in `TagsFilterPanel`
- Remove yarn esbuild pnp plugin

## Deprecated
### 10.6.0 (2026-09-02) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1060)
- Vue: Deprecate vue-docgen-api
### 10.3.6 (2026-04-29) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1036)
- ESLint: Update deprecated @storybook/test reference to storybook/test
### 10.2.4 (2026-02-02) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1024)
- Manager: Remove deprecated `active` prop warning in ZoomButton
### 10.1.0 (2025-11-26) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1010)
- Angular: Replace deprecated import of ApplicationConfig
### 10.0.0 (2025-10-28) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1000)
- Core: Fix Node 24 deprecation warning
- Core: Mark pnp support as deprecated

## New APIs and features
### 10.6.0 (2026-09-02) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1060)
- Angular: Add an in-process docgen analyzer, replacing Compodoc under the flag
- CLI: Add `storybook skills` command
- CLI: Allow esbuild builds for Storybook-owned pnpm dlx
- Core: Add additionnal field for component API in manifest
- Core: Add security token to instance registry record
- Core: Add storybook/internal/tools SDK skeleton
- Core: Allow token-only WebSocket upgrade without Origin
- Icons: Add missing @storybook/icons to the toolbar icon map
### 10.5.0 (2026-07-10) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1050)
- Addon Vitest: Add an initialGlobals option to pin a project's globals
- Angular: Add versioned `@types/node` to packages installed during `storybook init`
- Angular: Introduce @storybook/angular-vite package
- CLI: Add `storybook ai <tool>` MCP passthrough behind `STORYBOOK_FEATURE_AI_CLI`
- CLI: Add telemetry for the `storybook ai <command>` passthrough
- CLI: Allow -p shorthand to --port for ai command
- Controls: Add label to Object JSON control
- Core: Add ai-review observability
### 10.4.0 (2026-05-14) [source](https://github.com/storybookjs/storybook/blob/next/CHANGELOG.md#1040)
- A11y: Add aria-live announcements via @react-aria/live-announcer
- Addon-Docs: Add Reset story button to re-render stories in docs
- (136 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 106 releases; 40 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 10.6.9, 10.6.8, 10.6.7, 10.6.5, 10.6.4, 10.6.3, 10.6.2, 10.6.1, 10.5.10, 10.5.9, 10.5.8, 10.5.7 and 54 more.
- 14 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/storybookjs/storybook/next/CHANGELOG.md; registry (npm) for dates.
