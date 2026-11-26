# jest (npm): changes after 2025-06-01

- Latest stable on the registry: **30.5.2** (2026-09-18). Built 2026-11-25.
- 18 stable releases after the cut-off: 30.0.0 (2025-06-10) to 30.5.2 (2026-09-18).
- New major versions since the cut-off: 30.0.0 (2025-06-10).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 30.0.0 (2025-06-10) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3000)
- `[jest-config]` [BREAKING] Add `mts` and `cts` to default `moduleFileExtensions` config
- `[jest-config]` [BREAKING] Update `testMatch` and `testRegex` default option for supporting `mjs`, `cjs`, `mts`, and `cts`
- `[@jest/core]` [BREAKING] Changed `--filter` to accept an object with shape `{ filtered: Array<string> }` to match documentation
- `[@jest/core, @jest/test-sequencer]` [BREAKING] Exposes `globalConfig` & `contexts` to `TestSequencer` (#14535, &
- `[@jest/environment]` [BREAKING] Remove deprecated `jest.genMockFromModule()`
- `[@jest/environment]` [BREAKING] Remove unnecessary defensive code
- `[jest-environment-jsdom]` [BREAKING] Upgrade JSDOM to v22
- `[expect, @jest/expect]` [BREAKING] Add type inference for function parameters in `CalledWith` assertions
- `[@jest/fake-timers]` [BREAKING] Upgrade `@sinonjs/fake-timers` to v13 (#14544 &
- `[jest-runtime]` [BREAKING] Make it mandatory to pass `globalConfig` to the `Runtime` constructor
- `[jest-runtime]` [BREAKING] Use `vm.compileFunction` over `vm.Script`
- `[jest-snapshot]` [BREAKING] Add support for Error causes in snapshots
- (16 more in this category not shown; see the changelog.)

## Removed or renamed
### 30.0.0 (2025-06-10) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3000)
- `[*]` Renamed `globalsCleanupMode` to `globalsCleanup` and `--waitNextEventLoopTurnForUnhandledRejectionEvents` to `--waitForUnhandledRejections`
- Remove `invalid/wrong` test case assertions for `ObjectContaining`.

## Deprecated
### 30.5.0 (2026-08-28) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3050)
- `[jest-runtime]` Emit the JSON-without-import-attribute deprecation warning once per test file instead of once per worker, so it is no longer silently swallowed for every file after the first

## Minimum versions and platform support
### 30.5.0 (2026-08-28) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3050)
- `[jest-runtime]` Allow `require()` of ESM-marked files on Node < 24.9 via transform fallback
### 30.4.0 (2026-05-07) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3040)
- `[jest-runtime]` Support `require()` of ES modules on Node v24.9+
- `[jest-runtime]` Extend the `.js`-with-ESM-syntax fallback to `require()` on Node v24.9+ - falls back to `require(esm)` when the CJS parser rejects ESM syntax
### 30.0.0 (2025-06-10) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3000)
- `[*]` [BREAKING] Drop support for Node.js versions 14, 16, 19, 21 and 23
- `[*]` [BREAKING] Drop support for `typescript@4.3`, minimum version is now `5.4`

## New APIs and features
### 30.5.0 (2026-08-28) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3050)
- `[@jest/expect-utils, jest-mock]` Add `mockFn.whenCalledWith(...args)` for configuring return values per argument list, with first-class asymmetric-matcher support
- `[@jest/expect-utils]` Export `AsymmetricMatcher` and `FunctionParameters` types (previously private to `expect`)
- `[jest-circus, jest-core, jest-jasmine2, jest-test-result, jest-types]` `--collectTests` now expands `test.each`/`describe.each` cases and reports per-status counts (skipped/todo via the new `wouldRun` flag for selected tests) […]
- `[jest-circus, jest-environment, jest-runtime, jest-types]` Add describe-level retries via `jest.retryTimes(..., {entireDescribe: true})`
- `[jest-circus, jest-message-util, jest-reporters, jest-types]` Add `retryMessages` to `AssertionResult` and export `formatErrorStack`, so the retry log renders nested `cause` and `AggregateError` sections with code frames instead […]
- `[jest-circus, jest-types]` Add `unhandledErrorsDetailed` to `Circus.RunResult`, so an unhandled rejection reports its `cause` chain and `AggregateError` entries with code frames instead of a pre-serialized stack
- `[jest-haste-map]` Replace `NodeWatcher` and `FSEventsWatcher` with `@parcel/watcher` for the non-watchman watch path
- `[jest-resolve]` Bump `unrs-resolver` to 1.12.1, remove `jest-pnp-resolver` and unnecessary checks
### 30.4.0 (2026-05-07) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3040)
- `[babel-jest]` Support collecting coverage from `.mts`, `.cts` (and other) files
- `[jest-circus, jest-cli, jest-config, jest-core, jest-jasmine2, jest-types]` Add `--collect-tests` flag to discover and list tests without executing them
- `[jest-config, jest-runner, jest-worker]` Add `workerGracefulExitTimeout` config option to control how long workers are given to exit before being force-killed
- `[jest-config]` Add support for `jest.config.mts` as a valid configuration file
- `[jest-config, jest-core, jest-reporters, jest-runner]` `verbose` and `silent` can now be set per-project; the project-level value overrides the global value for that project's tests
- `[@jest/fake-timers]` Accept `Temporal.Duration` in `jest.advanceTimersByTime()` and `jest.advanceTimersByTimeAsync()`
- `[@jest/fake-timers]` Accept `Temporal.Instant` and `Temporal.ZonedDateTime` in `jest.setSystemTime()` and `useFakeTimers({now})`
- `[@jest/fake-timers]` Support faking `Temporal.Now.*`
### 30.3.0 (2026-03-10) [source](https://github.com/jestjs/jest/blob/main/CHANGELOG.md#3030)
- `[jest-config]` Add `defineConfig` and `mergeConfig` helpers for type-safe Jest config
- `[jest-fake-timers]` Add `setTimerTickMode` to configure how timers advance
- (68 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 18 releases; 12 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 30.5.1, 30.4.2, 30.1.3, 30.1.2, 30.1.1, 30.0.2.
- Sources: https://raw.githubusercontent.com/jestjs/jest/main/CHANGELOG.md; registry (npm) for dates.
