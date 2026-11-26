# ai (npm): changes after 2025-06-01

- Latest stable on the registry: **7.0.181** (2026-11-23). Built 2026-11-25.
- 789 stable releases after the cut-off: 4.3.17 (2025-07-07) to 7.0.181 (2026-11-23).
- New major versions since the cut-off: 5.0.0 (2025-07-31), 6.0.0 (2025-12-22), 7.0.0 (2026-06-25).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 7.0.0 (2026-06-25) [source](https://github.com/vercel/ai/blob/main/packages/ai/CHANGELOG.md#700)
- feat(ai): change type of experimental_context from unknown to generic
- chore(ai): remove deprecated `media` type part from `ToolResultOutput`
- feat(ai): make experimental_telemetry stable
- feat(ai): change naming nomenclature for `*TelemetryIntegration` to `*Telemetry`
- fix(ai): carry prepareStep message overrides forward across steps
- fix(ai): limit response messages in StepResult to messages created in that step
- feat(ai): remove/refactor event data sent via callbacks
- feat(provider): adding new 'custom' content type
- feat(ai): add support for uploading provider skills using the provider references abstraction
- fix(ai): remove experimental_customProvider
- feat(ai): rename `stepCountIs` to `isStepCount`
- refactor(ai/core): rename `ModelCallStreamPart` to `LanguageModelStreamPart` and align stream model call naming (`streamLanguageModelCall`, `experimental_streamLanguageModelCall`).
### 6.0.0 (2025-12-22) [source](https://github.com/vercel/ai/blob/main/packages/ai/CHANGELOG.md#600)
- ai SDK 6 beta
### 5.0.0 (2025-07-31) [source](https://github.com/vercel/ai/blob/main/packages/ai/CHANGELOG.md#500)
- chore(@ai-sdk/rsc): extract to separate package
- chore: rename reasoning to reasoningText etc
- chore (ai): remove automatic conversion of UI messages to model messages
- remove setting temperature to `0` by default
- feat (ui): typed tool parts in ui messages
- feat (ai): automatic tool execution error handling
- chore (provider,ai): tools have input/output instead of args,result
- chore (ai): change source ui message parts to source-url
- chore (ai): remove "data" UIMessage role
- refactoring (ai): restructure message metadata transfer
- chore (ai): remove exports of internal ui functions
- (79 more in this category not shown; see the changelog.)

## Removed or renamed
### 5.0.0 (2025-07-31) [source](https://github.com/vercel/ai/blob/main/packages/ai/CHANGELOG.md#500)
- remove `null` option from `DefaultSettingsMiddleware`
- remove setting defaults for `temperature` and `stopSequences` in `ai` to enable middleware changes

## Minimum versions and platform support
### 7.0.0 (2026-06-25) [source](https://github.com/vercel/ai/blob/main/packages/ai/CHANGELOG.md#700)
- Raise minimum supported Node.js version to 22. Supported versions: 22, 24, and 26.

## New APIs and features
### 6.0.0 (2025-12-22) [source](https://github.com/vercel/ai/blob/main/packages/ai/CHANGELOG.md#600)
- release: start 5.1 beta
### 5.0.0 (2025-07-31) [source](https://github.com/vercel/ai/blob/main/packages/ai/CHANGELOG.md#500)
- feat (core): Add finishReason field to NoObjectGeneratedError
- feat (ai): add content to generateText result
- feat (ai): add content to streamText result
- feat (ai): add filename to file ui parts

## Coverage
- Release notes read for 335 releases; 3 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 7.0.181, 7.0.180, 7.0.179, 7.0.178, 7.0.177, 7.0.176, 7.0.175, 7.0.174, 7.0.173, 7.0.172, 7.0.171, 7.0.170 and 320 more.
- 454 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/vercel/ai/main/packages/ai/CHANGELOG.md; registry (npm) for dates.
