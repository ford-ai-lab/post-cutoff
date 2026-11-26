# openai (npm): changes after 2025-06-01

- Latest stable on the registry: **7.64.0** (2026-11-24). Built 2026-11-25.
- 161 stable releases after the cut-off: 5.0.2 (2025-06-02) to 7.64.0 (2026-11-24).
- New major versions since the cut-off: 6.0.0 (2025-09-30), 7.0.0 (2026-07-27).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 7.44.0 (2026-10-26) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7440-2026-10-25)
- api: expand Live Decision item and question types. Breaking change in a minor release. Live Decision item events now include messages and function/custom-tool calls and outputs. […]
### 7.43.0 (2026-10-22) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7430-2026-10-22)
- api: Breaking change in a minor release. A Live response's Decisions question `instructions` can now be a string or an array of text, image, or JSON parts. […]
### 6.16.0 (2026-01-09) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#6160-2026-01-09)
- ci: add breaking change detection workflow
### 6.0.0 (2025-09-30) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#600-2025-09-30)
- api: `ResponseFunctionToolCallOutputItem.output` and `ResponseCustomToolCallOutput.output` now return `string | Array<ResponseInputText | ResponseInputImage | ResponseInputFile>` instead of `string` only. […]
### 5.14.0 (2025-08-20) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#5140-2025-08-20)
- internal/ci: setup breaking change detection

## Deprecated
### 7.5.0 (2026-08-17) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#750-2026-08-17)
- api: deprecate Sora video APIs

## Minimum versions and platform support
### 7.0.0 (2026-07-27) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#700-2026-07-27)
- require Node.js 22 and codify version support

## New APIs and features
### 7.64.0 (2026-11-24) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7640-2026-11-24)
- api: add healthcare model IDs for Responses
### 7.63.0 (2026-11-23) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7630-2026-11-23)
- api: add spending limits to agent sessions
### 7.62.0 (2026-11-20) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7620-2026-11-19)
- api: support Live WebRTC standby
### 7.61.0 (2026-11-19) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7610-2026-11-19)
- api: add gpt-live-1.1 to Live model choices
### 7.60.0 (2026-11-18) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7600-2026-11-18)
- api: add Live MCP server configuration
- api: add standalone CSAM moderation types
- api: hide Managed Agents session budget controls and events
### 7.59.0 (2026-11-17) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7590-2026-11-17)
- api: type Managed Agents budget events
### 7.58.0 (2026-11-17) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7580-2026-11-17)
- api: add 2-hour and 8-hour Responses background windows
- api: add schedule pause reasons
- api: add the GPT-6.2 Astra Law Responses model identifier
- api: add the GPT-6.2 Astra model identifier
- api: add the GPT-6.2 Sol model identifier
### 7.57.0 (2026-11-13) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7570-2026-11-13)
- api: update Agents, Live, Images, and admin types
### 7.56.0 (2026-11-12) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7560-2026-11-12)
- api: type reasoning input transformations on responses
### 7.55.0 (2026-11-10) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7550-2026-11-10)
- api: add typed async function tools
### 7.54.0 (2026-11-09) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7540-2026-11-08)
- api: recognize gpt-6-rosalind in beta Responses
### 7.53.0 (2026-11-06) [source](https://github.com/openai/openai-node/blob/master/CHANGELOG.md#7530-2026-11-06)
- agents: deliver session errors as stream events
- (232 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 170 releases; 138 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 7.45.1, 7.30.1, 6.43.0, 6.39.1, 6.30.1, 6.15.0, 6.9.1, 6.8.1, 6.0.1, 5.23.2, 5.23.1, 5.22.1 and 20 more.
- Sources: https://raw.githubusercontent.com/openai/openai-node/master/CHANGELOG.md; registry (npm) for dates.
