# commander (npm): changes after 2025-06-01

- Latest stable on the registry: **15.1.0** (2026-11-07). Built 2026-11-25.
- 5 stable releases after the cut-off: 14.0.1 (2025-09-12) to 15.1.0 (2026-11-07).
- New major versions since the cut-off: 15.0.0 (2026-05-29).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 15.0.0 (2026-05-29) [source](https://github.com/tj/commander.js/blob/master/CHANGELOG.md#1500-2026-05-29)
- *Breaking:* migrated Commander implementation from CommonJS to ESM
- *Breaking:* removed deprecated export of `commander/esm.mjs`
- Commander 15 is ESM only, but this does not mean you need to migrate to ESM to use it. Importing ESM from CommonJS is supported by Node.js, and Bun, and Deno. […]
- If you have problems using Commander 15 in your environment, one option is stay on Commander 14 for now. Commander 14 will get security updates until May 2027 and things will hopefully improve for your setup in the meantime.

## Deprecated
### 15.1.0 (2026-11-07) [source](https://github.com/tj/commander.js/blob/master/CHANGELOG.md#1510-2026-11-07)
- undeprecate `InvalidOptionArgumentError`
- `cmd.storeOptionsAsProperties()`
- `cmd.combineFlagAndOptionalValue()`
### 14.0.3 (2026-01-31) [source](https://github.com/tj/commander.js/blob/master/CHANGELOG.md#1403-2026-01-31)
- clarify typing for deprecated callback parameter to `.outputHelp()`

## Minimum versions and platform support
### 15.0.0 (2026-05-29) [source](https://github.com/tj/commander.js/blob/master/CHANGELOG.md#1500-2026-05-29)
- *Breaking:* Commander 15 requires Node.js v22.12.0 or higher (for `require(esm)`).

## New APIs and features
### 15.0.0 (2026-05-29) [source](https://github.com/tj/commander.js/blob/master/CHANGELOG.md#1500-2026-05-29)
- show excess command-arguments in error message
### 14.0.3 (2026-01-31) [source](https://github.com/tj/commander.js/blob/master/CHANGELOG.md#1403-2026-01-31)
- Release Policy document

## Coverage
- Release notes read for 5 releases; 3 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 14.0.2, 14.0.1.
- Sources: https://raw.githubusercontent.com/tj/commander.js/master/CHANGELOG.md; registry (npm) for dates.
