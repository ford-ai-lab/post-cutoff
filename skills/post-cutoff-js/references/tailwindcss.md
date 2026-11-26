# tailwindcss (npm): changes after 2025-06-01

- Latest stable on the registry: **4.3.5** (2026-11-06). Built 2026-11-25.
- 23 stable releases after the cut-off: 3.4.18 (2025-10-01) to 4.3.5 (2026-11-06).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Removed or renamed
### 4.1.15 (2025-10-20) [source](https://github.com/tailwindlabs/tailwindcss/blob/main/CHANGELOG.md#4115---2025-10-20)
- Remove the `postinstall` script from oxide ([#19149])(
### 4.1.13 (2025-09-04) [source](https://github.com/tailwindlabs/tailwindcss/blob/main/CHANGELOG.md#4113---2025-09-03)
- Drop warning from browser build
- Drop exact duplicate declarations when emitting CSS

## Deprecated
### 4.2.0 (2026-02-18) [source](https://github.com/tailwindlabs/tailwindcss/blob/main/CHANGELOG.md#420---2026-02-18)
- Deprecate `start-*` and `end-*` utilities in favor of `inset-s-*` and `inset-e-*` utilities

## New APIs and features
### 4.3.0 (2026-05-08) [source](https://github.com/tailwindlabs/tailwindcss/blob/main/CHANGELOG.md#430---2026-05-08)
- Add `@container-size` utility
- Add `scrollbar-{auto,thin,none}` utilities for `scrollbar-width`, and `scrollbar-thumb-*` / `scrollbar-track-*` color utilities for `scrollbar-color`
- Add `scrollbar-gutter-*` utilities
- Add `zoom-*` utilities
- Add `tab-*` utilities
- Allow using `@variant` with stacked variants (e.g. `@variant hover:focus { … }`)
- Allow using `@variant` with compound variants (e.g. `@variant hover, focus { … }`)
- Support `--default(…)` in `--value(…)` and `--modifier(…)` for functional `@utility` definitions
### 4.2.0 (2026-02-18) [source](https://github.com/tailwindlabs/tailwindcss/blob/main/CHANGELOG.md#420---2026-02-18)
- Add mauve, olive, mist, and taupe color palettes to the default theme
- Add `@tailwindcss/webpack` package to run Tailwind CSS as a webpack plugin
- Add `pbs-*` and `pbe-*` utilities for `padding-block-start` and `padding-block-end`
- Add `mbs-*` and `mbe-*` utilities for `margin-block-start` and `margin-block-end`
- Add `scroll-pbs-*` and `scroll-pbe-*` utilities for `scroll-padding-block-start` and `scroll-padding-block-end`
- Add `scroll-mbs-*` and `scroll-mbe-*` utilities for `scroll-margin-block-start` and `scroll-margin-block-end`
- Add `border-bs-*` and `border-be-*` utilities for `border-block-start` and `border-block-end`
- Add `inline-*`, `min-inline-*`, `max-inline-*` utilities for `inline-size`, `min-inline-size`, and `max-inline-size`
### 4.3.4 (2026-11-02) [source](https://github.com/tailwindlabs/tailwindcss/blob/main/CHANGELOG.md#434---2026-11-02)
- Add `@tailwindcss/turbopack`, a Turbopack loader for using Tailwind CSS with Next.js
### 4.3.1 (2026-06-12) [source](https://github.com/tailwindlabs/tailwindcss/blob/main/CHANGELOG.md#431---2026-06-12)
- Add `--silent` option to suppress output in `@tailwindcss/cli`
- (3 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 23 releases; 6 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 4.3.5, 4.3.3, 4.3.2, 4.2.4, 4.2.3, 4.2.2, 4.2.1, 4.1.18, 4.1.17, 4.1.16, 4.1.14, 4.1.12 and 5 more.
- Sources: https://raw.githubusercontent.com/tailwindlabs/tailwindcss/main/CHANGELOG.md; registry (npm) for dates.
