# @biomejs/biome (npm): changes after 2025-06-01

- Latest stable on the registry: **2.6.9** (2026-11-24). Built 2026-11-25.
- 78 stable releases after the cut-off: 2.0.0 (2025-06-17) to 2.6.9 (2026-11-24).
- New major versions since the cut-off: 2.0.0 (2025-06-17).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 2.5.12 (2026-09-03) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#2512)
- Fixed #3515 and #10395, where Biome could corrupt Unicode characters while writing source received through standard input to standard output. Characters such as `⚠` and `✔` are now preserved.

## Removed or renamed
### 2.6.2 (2026-10-21) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#262)
- Removed the `javascript.parser.gritMetavariables` option. It was intended for internal use only and had no effect on how Biome parses JavaScript and TypeScript files. […]
### 2.2.0 (2025-08-14) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#220)
- Renamed `noAwaitInLoop` to `noAwaitInLoops`.
- Renamed `noConstantBinaryExpression` to `noConstantBinaryExpressions`.
- Renamed `noDestructuredProps` to `noSolidDestructuredProps`.
- Renamed `noImplicitCoercion` to `noImplicitCoercions`.
- Renamed `noReactPropAssign` to `noReactPropAssignments`.
- Renamed `noUnknownAtRule` to `noUnknownAtRules`.
- Renamed `noUselessBackrefInRegex` to `noUselessRegexBackrefs`.
- Renamed `useAdjacentGetterSetter` to `useGroupedAccessorPairs`.
- (7 more in this category not shown; see the changelog.)

## Deprecated
### 2.5.0 (2026-06-12) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#250)
- `noDeprecatedMediaType` (recommended)
### 2.4.0 (2026-02-15) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#240)
- `noDeprecatedImports`. The rule reports imports of deprecated symbols.
- `useDeprecatedDate`. The rule enforces use of GraphQL `@deprecated` directive with date.
### 2.3.0 (2025-10-24) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#230)
- Deprecated the option `files.experimentalScannerIgnores` in favour of force-ignore syntax in `files.includes`.

## New APIs and features
### 2.5.0 (2026-06-12) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#250)
- Added a new reporter called `concise`. When `--reporter=concise` is passed the commands `format`, `lint`, `check` and `ci`, the diagnostics are printed in a compact manner
- Added the `useKeyWithClickEvents` a11y lint rule for HTML files (`.html`, `.vue`, `.svelte`, `.astro`). This is a port of the existing JSX rule. […]
- Added new nursery lint rule `noUndeclaredClasses` for HTML, JSX, and SFC files (Vue, Astro, Svelte). The rule detects CSS class names used in `class="..."` (or `className`) attributes that are not defined in any `<style>` block […]
- Added new nursery lint rule `noUnusedClasses` for CSS. The rule detects CSS class selectors that are never referenced in any HTML or JSX file that imports the stylesheet. […]
- Added a `biome upgrade` command for standalone installations. It upgrades Homebrew installs with `brew upgrade biome`, updates manually installed binaries from the latest GitHub release, and tells npm users to upgrade with their […]
- Added the HTML version of the `useHeadingContent` rule. The rule now enforces that heading elements (`h1`-`h6`) have content accessible to screen readers in HTML, Vue, Svelte, and Astro files.
- Added the HTML version of the `useKeyWithMouseEvents` rule. The rule now enforces that `onmouseover` is accompanied by `onfocus` and `onmouseout` is accompanied by `onblur` in HTML, Vue, Svelte, and Astro files.
- Added the new assist action `useSortedTypeFields`, which sorts the fields of GraphQL object types, interface types and input object types alphabetically, e.g. `name, age, id` becomes `age, id, name`.
### 2.4.0 (2026-02-15) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#240)
- Added `ignore` option to the `useHookAtTopLevel` rule.
- Added the rule `useAnchorContent` for HTML to enforce that anchor elements have accessible content for screen readers. The rule flags empty anchors, anchors with only whitespace, and anchors where all content is hidden with […]
- Added the rule `useMediaCaption` to the HTML language. Enforces that `audio` and `video` elements have a `track` element with `kind="captions"` for accessibility. Muted videos are allowed without captions.
- Added support for multiple reporters, and the ability to save reporters on arbitrary files.
- The Biome CSS parser is now able to parse Vue SFC syntax such as `:slotted` and `:deep`. These pseudo functions are only correctly parsed when the CSS is defined inside `.vue` components. […]
- Added support for Cursor files. When Biome sees a Cursor JSON file, it will parse it with comments enabled and trailing commas enabled: `$PROJECT/.cursor/`
- Added JSON as a target language for GritQL pattern matching. You can now write Grit plugins for JSON files.
- Example patterns:: Match all key-value pairs
### 2.3.0 (2025-10-24) [source](https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md#230)
- Biome's resolver now supports `baseUrl` if specified in `tsconfig.json`.
- tsconfig.json
- (169 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 65 releases; 6 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 2.6.9, 2.6.8, 2.6.7, 2.6.6, 2.6.5, 2.6.4, 2.6.3, 2.5.15, 2.5.14, 2.5.13, 2.5.11, 2.5.10 and 47 more.
- 13 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/biomejs/biome/main/packages/@biomejs/biome/CHANGELOG.md; registry (npm) for dates.
