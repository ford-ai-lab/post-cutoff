# mongoose (npm): changes after 2025-06-01

- Latest stable on the registry: **9.13.1** (2026-11-24). Built 2026-11-25.
- 109 stable releases after the cut-off: 6.13.9 (2026-02-04) to 9.13.1 (2026-11-24).
- New major versions since the cut-off: 9.0.0 (2025-11-21).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 9.0.0 (2025-11-21) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#900--2025-11-21)
- BREAKING CHANGE: drop support for callback-based pre middleware, e.g. `next()` in `pre()` hooks
- BREAKING CHANGE: update to MongoDB Node driver v7
- BREAKING CHANGE: make UUID schema type return bson UUIDs
- BREAKING CHANGE: make findOne(null), find(null), etc. throw an error instead of returning first doc
- BREAKING CHANGE: disallow update pipelines by default, require updatePipeline option
- BREAKING CHANGE: call virtual ref function with subdoc, not top-level doc
- BREAKING CHANGE(types): make create() and insertOne() params more strict, remove generics to prevent type inference
- BREAKING CHANGE(types): make FilterQuery properties no longer resolve to any in TypeScript
- BREAKING CHANGE(types): change `this` to HydratedDocument for default() and required(), HydratedDocument | Query for validate()
- BREAKING CHANGE(types): make id a virtual in TypeScript rather than a property on Document base class
- BREAKING CHANGE(types): consolidate RootQuerySelector, Condition, etc. types with MongoDB driver's
- BREAKING CHANGE: asyncify update validators, SchemaType.prototype.doValidate(), save hooks for improved stack traces
- (6 more in this category not shown; see the changelog.)

## Deprecated
### 9.4.0 (2026-04-03) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#940--2026-04-03)
- feat(document): add $getChanges() alias, deprecate getChanges() #15959 techcodie
### 9.2.0 (2026-02-09) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#920--2026-02-09)
- feat(base): add `returnDocument` global option, deprecate `returnOriginal` and `new`

## New APIs and features
### 9.13.0 (2026-11-23) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#9130--2026-11-23)
- feat: upgrade MongoDB driver to 7.9 #16724 oscarmaia
- feat(schema+model+query): add defaultSort option to schemas, applies default sort to all queries unless sort explicitly specified
### 9.12.0 (2026-11-04) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#9120--2026-11-04)
- feat: upgrade to mongodb driver 7.8
### 9.11.0 (2026-10-05) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#9110--2026-10-05)
- feat: use MongoDB Node.js driver 7.7.x
- feat(query): add Query.prototype.findAndCount() for composable paginated queries #16508 #16504 lokeshllkumar
### 9.10.0 (2026-09-10) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#9100--2026-09-10)
- feat: upgrade mongodb driver -> 7.6.0
- feat(model): add Model.findAndCount() wrapper for limit+skip based pagination with countDocuments
- feat(schema): add Schema.prototype.queryHelper() to make it easier to define query helpers in TypeScript
- feat: support middleware skip option for cursors and custom hooks #16350 #15883 #8768 AbdelrahmanHafez
- types: support for type narrowing when using projection in find and findOne
### 9.9.0 (2026-07-30) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#990--2026-07-30)
- types: add discriminator key to each member of embedded discriminator enum
### 9.8.0 (2026-07-20) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#980--2026-07-20)
- feat(schema): add `strictRead` option to filter or throw on unknown fields during document hydration #16345 #4279 GourabSingha
- feat: upgrade MongoDB Node.js driver to 7.5
### 9.7.0 (2026-06-09) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#970--2026-06-09)
- feat: add Node.js TracingChannel support for APM instrumentation #16275 #16105 logaretm
- feat(model): add standard schema adapter for models
### 9.6.0 (2026-04-28) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#960--2026-04-28)
- feat: upgrade mongodb node driver to 7.2
- feat(schematype): support `allowNull` option to disallow null values even if not `required`
### 9.5.0 (2026-04-20) [source](https://github.com/Automattic/mongoose/blob/master/CHANGELOG.md#950--2026-04-20)
- feat(debug): add `timestamp` option to debug output #16216 rejunp
- (39 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 99 releases; 30 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 9.12.4, 9.12.3, 9.12.2, 9.12.1, 9.11.5, 9.11.4, 9.11.3, 9.11.2, 9.11.1, 9.10.4, 9.10.3, 9.10.2 and 57 more.
- 12 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/Automattic/mongoose/master/CHANGELOG.md; registry (npm) for dates.
