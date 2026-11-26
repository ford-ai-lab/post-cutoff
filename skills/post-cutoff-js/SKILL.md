---
name: post-cutoff-js
description: What changed in popular JavaScript / TypeScript (npm) packages after 2025-06-01 - breaking changes, removed or renamed APIs, deprecations, new preferred APIs and minimum versions, quoted from upstream release notes with version, date and source link. Use before writing, editing or upgrading code that imports any of these packages, because your training data may describe an older API - ai, @angular/core, @anthropic-ai/sdk, astro, axios, @biomejs/biome, commander, drizzle-orm, esbuild, eslint, express, hono, jest, langchain, @langchain/core, mongoose, next, openai, playwright, postcss, prettier, prisma, puppeteer, react, react-router, rollup, storybook, stripe, @supabase/supabase-js, svelte, @sveltejs/kit, tailwindcss, @tanstack/react-query, typescript, typescript-eslint, vite, vitest, vue, webpack, wrangler, zod.
license: MIT
metadata:
  built: "2026-11-25"
  cutoff: "2025-06-01"
  author: "Ford (AI agent); with an accountable human operator"
---

# post-cutoff-js

Release-note digests for 41 JavaScript / TypeScript (npm) packages, covering releases published after **2025-06-01**.
Built **2026-11-25**. Anything released after that date is not here.

## When to use this

Before you write or change code that uses a package in the table below, and whenever an error
looks like an API that moved (unknown option, missing export, changed signature, unsupported
runtime version).

## How to use this

1. Find the version the project actually uses: package.json / the lockfile. Do not assume the latest.
2. Open the package's file from the table (one small file per package, in `references/`).
3. Apply only entries whose version is at or below the project's installed version. Entries above
   it describe an upgrade the project has not made; mention them only if the user is upgrading.
4. Sections in each file: Breaking changes, Removed or renamed, Deprecated, Minimum versions and
   platform support, New APIs and features, Coverage. Each group is headed by version, date and a
   source link.
5. If an entry matters to the code you are writing, open its source link and read the full note
   before relying on it. Entries are truncated quotes (marked `[…]`), not explanations.

## What these files are and are not

- Every entry is text quoted from the package's own changelog or release notes, picked by keyword
  rules. Nothing was written from memory and no model summarised it. Nobody reviewed it.
- The rules miss things. A file that lists no breaking changes does not prove there were none;
  "no details in release notes" means exactly that.
- Long changelogs are capped; each file says how many entries were left out.
- Releases before 2025-06-01 are not covered, and a package that is not in the table is not covered
  at all. In both cases read the package's own changelog.

## Packages

| Package | File | Latest (date built) | Breaking | Removed/renamed | Deprecated | New |
|---|---|---|---|---|---|---|
| `ai` | [references/ai.md](references/ai.md) | 7.0.181 | 103 | 2 | 0 | 5 |
| `@angular/core` | [references/angular__core.md](references/angular__core.md) | 22.3.0 | 60 | 0 | 370 | 93 |
| `@anthropic-ai/sdk` | [references/anthropic-ai__sdk.md](references/anthropic-ai__sdk.md) | 1.14.0 | 6 | 1 | 4 | 202 |
| `astro` | [references/astro.md](references/astro.md) | 7.4.13 | 8 | 3 | 0 | 28 |
| `axios` | [references/axios.md](references/axios.md) | 1.21.1 | 1 | 0 | 1 | 28 |
| `@biomejs/biome` | [references/biomejs__biome.md](references/biomejs__biome.md) | 2.6.9 | 1 | 16 | 4 | 187 |
| `commander` | [references/commander.md](references/commander.md) | 15.1.0 | 4 | 0 | 4 | 2 |
| `drizzle-orm` | [references/drizzle-orm.md](references/drizzle-orm.md) | 0.45.4 | 1 | 0 | 0 | 4 |
| `esbuild` | [references/esbuild.md](references/esbuild.md) | 0.28.2 | 0 | 0 | 0 | 6 |
| `eslint` | [references/eslint.md](references/eslint.md) | 10.15.0 | 21 | 0 | 0 | 83 |
| `express` | [references/express.md](references/express.md) | 5.3.0 | 1 | 0 | 1 | 1 |
| `hono` | [references/hono.md](references/hono.md) (no details in release notes) | 4.13.22 | 0 | 0 | 0 | 0 |
| `jest` | [references/jest.md](references/jest.md) | 30.5.2 | 28 | 2 | 1 | 86 |
| `langchain` | [references/langchain.md](references/langchain.md) | 1.6.8 | 0 | 0 | 0 | 8 |
| `@langchain/core` | [references/langchain__core.md](references/langchain__core.md) | 1.5.1 | 6 | 0 | 2 | 11 |
| `mongoose` | [references/mongoose.md](references/mongoose.md) | 9.13.1 | 18 | 0 | 2 | 57 |
| `next` | [references/next.md](references/next.md) | 16.4.6 | 60 | 15 | 4 | 0 |
| `openai` | [references/openai.md](references/openai.md) | 7.64.0 | 5 | 0 | 1 | 250 |
| `playwright` | [references/playwright.md](references/playwright.md) | 1.65.1 | 30 | 1 | 2 | 78 |
| `postcss` | [references/postcss.md](references/postcss.md) | 8.5.33 | 0 | 0 | 1 | 1 |
| `prettier` | [references/prettier.md](references/prettier.md) | 3.10.1 | 0 | 1 | 0 | 3 |
| `prisma` | [references/prisma.md](references/prisma.md) (no details in release notes) | 7.10.1 | 0 | 0 | 0 | 0 |
| `puppeteer` | [references/puppeteer.md](references/puppeteer.md) | 25.19.0 | 4 | 0 | 0 | 24 |
| `react` | [references/react.md](references/react.md) | 19.3.1 | 0 | 0 | 0 | 44 |
| `react-router` | [references/react-router.md](references/react-router.md) | 8.5.3 | 18 | 8 | 8 | 20 |
| `rollup` | [references/rollup.md](references/rollup.md) | 4.68.8 | 0 | 1 | 1 | 30 |
| `storybook` | [references/storybook.md](references/storybook.md) | 10.6.9 | 2 | 3 | 6 | 154 |
| `stripe` | [references/stripe.md](references/stripe.md) | 23.2.0 | 112 | 7 | 5 | 0 |
| `@supabase/supabase-js` | [references/supabase__supabase-js.md](references/supabase__supabase-js.md) | 2.119.2 | 0 | 0 | 1 | 24 |
| `svelte` | [references/svelte.md](references/svelte.md) | 5.59.2 | 0 | 0 | 0 | 31 |
| `@sveltejs/kit` | [references/sveltejs__kit.md](references/sveltejs__kit.md) | 3.4.0 | 83 | 0 | 4 | 101 |
| `tailwindcss` | [references/tailwindcss.md](references/tailwindcss.md) | 4.3.5 | 0 | 3 | 1 | 21 |
| `@tanstack/react-query` | [references/tanstack__react-query.md](references/tanstack__react-query.md) | 5.108.4 | 0 | 0 | 0 | 3 |
| `typescript` | [references/typescript.md](references/typescript.md) | 7.0.2 | 21 | 0 | 29 | 18 |
| `typescript-eslint` | [references/typescript-eslint.md](references/typescript-eslint.md) | 8.74.0 | 0 | 1 | 5 | 69 |
| `vite` | [references/vite.md](references/vite.md) | 8.3.8 | 14 | 0 | 6 | 129 |
| `vitest` | [references/vitest.md](references/vitest.md) (no details in release notes) | 5.1.2 | 0 | 0 | 0 | 0 |
| `vue` | [references/vue.md](references/vue.md) | 3.5.46 | 0 | 0 | 0 | 1 |
| `webpack` | [references/webpack.md](references/webpack.md) | 5.113.0 | 0 | 5 | 4 | 234 |
| `wrangler` | [references/wrangler.md](references/wrangler.md) | 4.168.0 | 0 | 15 | 7 | 392 |
| `zod` | [references/zod.md](references/zod.md) (no details in release notes) | 4.6.7 | 0 | 0 | 0 | 0 |
