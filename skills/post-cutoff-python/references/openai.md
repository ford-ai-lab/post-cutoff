# openai (pypi): changes after 2025-06-01

- Latest stable on the registry: **3.59.0** (2026-11-24). Built 2026-11-25.
- 190 stable releases after the cut-off: 1.83.0 (2025-06-02) to 3.59.0 (2026-11-24).
- New major versions since the cut-off: 2.0.0 (2025-09-30), 3.0.0 (2026-08-12).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 3.37.0 (2026-10-22) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3370-2026-10-22)
- api: This minor release includes a breaking change to Decisions types. In Live response models, question `instructions` can now be a string or a list of structured text, image, or JSON parts; […]
### 3.0.0 (2026-08-12) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#300-2026-08-12)
- api: HTTPX2 is now the default HTTP client, and `httpx` is no longer installed automatically. Applications using custom HTTPX clients, transports, or configuration objects must migrate to their HTTPX2 equivalents or use the […]
### 2.13.0 (2025-12-16) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#2130-2025-12-16)
- ci: add CI job to detect breaking changes with the Agents SDK
### 2.0.0 (2025-09-30) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#200-2025-09-30)
- api: `ResponseFunctionToolCallOutputItem.output` and `ResponseCustomToolCallOutput.output` now return `string | Array<ResponseInputText | ResponseInputImage | ResponseInputFile>` instead of `string` only. […]
### 1.100.3 (2025-08-20) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#11003-2025-08-20)
- internal/ci: setup breaking change detection
### 1.99.8 (2025-08-11) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#1998-2025-08-11)
- types: revert ChatCompletionMessageToolCallUnion breaking change
### 1.92.0 (2025-06-26) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#1920-2025-06-26)
- internal: add tests for breaking change detection

## Removed or renamed
### 2.37.0 (2026-05-15) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#2370-2026-05-13)
- Remove unnecessary client_id when using workload identity provider for auth

## Deprecated
### 3.1.0 (2026-08-14) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#310-2026-08-14)
- api: deprecate Sora video APIs

## Minimum versions and platform support
### 2.49.0 (2026-07-27) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#2490-2026-07-27)
- require Python 3.10 and automate version reviews
### 2.47.0 (2026-07-22) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#2470-2026-07-21)
- deps: require patched aiohttp on Python 3.10+

## New APIs and features
### 3.59.0 (2026-11-24) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3590-2026-11-24)
- api: add healthcare model IDs for Responses
### 3.58.0 (2026-11-23) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3580-2026-11-23)
- api: set and read agent session spending limits
### 3.57.0 (2026-11-20) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3570-2026-11-19)
- api: support Live WebRTC standby
### 3.56.0 (2026-11-19) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3560-2026-11-19)
- api: add gpt-live-1.1 to Live model choices
### 3.55.0 (2026-11-18) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3550-2026-11-18)
- api: add Live MCP server configuration
- api: hide Managed Agents session budget controls and events
### 3.54.0 (2026-11-17) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3540-2026-11-17)
- api: type Managed Agents budget events
### 3.53.0 (2026-11-17) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3530-2026-11-17)
- api: add 2-hour and 8-hour Responses background windows
- api: add the GPT-6.2 Astra Law Responses model identifier
- api: add the GPT-6.2 Astra model identifier
- api: add the GPT-6.2 Sol model identifier
### 3.52.0 (2026-11-16) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3520-2026-11-16)
- api: add schedule pause reasons
- api: deliver beta Agents session errors as stream events
### 3.51.0 (2026-11-13) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3510-2026-11-12)
- api: expand agent, image, Live, and external key support
### 3.50.0 (2026-11-12) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3500-2026-11-12)
- api: expose reasoning input transformations on responses
### 3.49.0 (2026-11-10) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3490-2026-11-10)
- api: add typed async function tools
### 3.48.0 (2026-11-09) [source](https://github.com/openai/openai-python/blob/main/CHANGELOG.md#3480-2026-11-09)
- api: add stream options for agent sessions
- api: recognize gpt-6-rosalind in beta Responses
- (237 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 193 releases; 145 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 3.55.1, 3.42.1, 3.36.1, 3.35.1, 3.26.1, 3.22.1, 3.19.2, 3.19.1, 3.16.2, 3.16.1, 3.14.1, 3.3.1 and 36 more.
- Sources: https://raw.githubusercontent.com/openai/openai-python/main/CHANGELOG.md; registry (pypi) for dates.
