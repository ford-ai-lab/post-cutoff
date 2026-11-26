# next (npm): changes after 2025-06-01

- Latest stable on the registry: **16.4.6** (2026-11-09). Built 2026-11-25.
- 113 stable releases after the cut-off: 14.2.30 (2025-06-12) to 16.4.6 (2026-11-09).
- New major versions since the cut-off: 16.0.0 (2025-10-22).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 16.0.0 (2025-10-22) [source](https://github.com/vercel/next.js/blob/canary/docs/01-app/02-guides/upgrading/version-16.mdx)
- Continue through the breaking changes below, run the relevant checks, and fix any remaining issues.
- Turbopack by default: Starting with Next.js 16, Turbopack is stable and used by default with `next dev` and `next build`
- Opting out of Turbopack: If you need to continue using Webpack, you can opt out with the `--webpack` flag. For example, to use Turbopack in development but Webpack for production builds
- Turbopack configuration location: The `experimental.turbopack` configuration is out of experimental.
- Resolve alias fallback: In some projects, client-side code may import files containing Node.js native modules. This will cause `Module not found: Can't resolve 'fs'` type of errors.
- Sass node_modules imports: Turbopack fully supports importing Sass files from `node_modules`. Note that while Webpack allowed the legacy tilde (`~`) prefix, Turbopack does not support this syntax.
- Turbopack File System Caching: Turbopack stores compiler artifacts on disk between runs, for significantly faster compile times across restarts. […]
- Version 15 introduced Async Request APIs as a breaking change, with temporary synchronous compatibility.
- Starting with Next.js 16, synchronous access is fully removed. These APIs can only be accessed asynchronously.
- `searchParams` in `page.js`
- Migrating types for async Request-time APIs: To help migrate to async `params` and `searchParams`, you can run `npx next typegen` to automatically generate these globally available types helpers
- `LayoutProps`
- (48 more in this category not shown; see the changelog.)

## Removed or renamed
### 16.0.0 (2025-10-22) [source](https://github.com/vercel/next.js/blob/canary/docs/01-app/02-guides/upgrading/version-16.mdx)
- Remove `unstable_` prefix from stabilized APIs
- Remove `experimental_ppr` Route Segment Config from pages and layouts
- These features were previously deprecated and are now removed
- AMP Support: AMP adoption has declined significantly, and maintaining this feature adds complexity to the framework. All AMP APIs and configurations have been removed
- `amp` configuration from your Next config file
- `next/amp` hook imports and usage (`useAmp`)
- `export const config = { amp: true }` from pages
- next lint Command: The `next lint` command has been removed. Use Biome or ESLint directly. `next build` no longer runs linting.
- (7 more in this category not shown; see the changelog.)

## Deprecated
### 16.0.0 (2025-10-22) [source](https://github.com/vercel/next.js/blob/canary/docs/01-app/02-guides/upgrading/version-16.mdx)
- Migrate from deprecated `middleware` convention to `proxy`
- The `next/legacy/image` component is deprecated. Use `next/image` instead
- The `images.domains` config is deprecated.
- Use `images.remotePatterns` instead for improved security

## Minimum versions and platform support
### 16.0.0 (2025-10-22) [source](https://github.com/vercel/next.js/blob/canary/docs/01-app/02-guides/upgrading/version-16.mdx)
- Requirement: Change / Details
- Node.js 20.9+: Minimum version now `20.9.0` (LTS); Node.js 18 no longer supported
- TypeScript 5+: Minimum version now `5.1.0`
- Browsers: Chrome 111+, Edge 111+, Firefox 111+, Safari 16.4+

## Coverage
- Release notes read for 1 releases; 1 had extractable items.
- 112 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Source not reachable in this build: github_releases vercel/next.js: HTTP 403 cached
- Sources: https://raw.githubusercontent.com/vercel/next.js/canary/docs/01-app/02-guides/upgrading/version-{major}.mdx, https://github.com/vercel/next.js/releases; registry (npm) for dates.
