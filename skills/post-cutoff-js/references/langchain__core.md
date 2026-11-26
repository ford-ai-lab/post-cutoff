# @langchain/core (npm): changes after 2025-06-01

- Latest stable on the registry: **1.5.1** (2026-11-24). Built 2026-11-25.
- 113 stable releases after the cut-off: 0.3.58 (2025-06-11) to 1.5.1 (2026-11-24).
- New major versions since the cut-off: 1.0.0 (2025-10-17).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 1.0.0 (2025-10-17) [source](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-core/CHANGELOG.md#100)
- Backward compatible: Content blocks can be loaded lazily with no breaking changes to existing code
- Backward Compatibility: This release maintains backward compatibility with existing code. Content blocks are loaded lazily, so no changes are required to existing applications.
- New Features: To take advantage of new features like content blocks and middleware
- Update to `@langchain/core@next`
- Use the new `contentBlocks` property to access rich content
- For middleware and `createAgent`, install `langchain@next`

## Deprecated
### 1.5.0 (2026-11-20) [source](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-core/CHANGELOG.md#150)
- Standardize finish reason on `message-finish` events and final `AIMessage`s. Provider integrations set `finish_reason` (raw provider value), `normalized_finish_reason` (`stop | length | tool_call | content_filter | refusal | […]
### 1.1.25 (2026-02-17) [source](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-core/CHANGELOG.md#1125)
- Deprecated `addLangChainErrorFields` in favor of `LangChainError` subclasses

## New APIs and features
### 1.4.0 (2026-11-11) [source](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-core/CHANGELOG.md#140)
- feat(core): add decision models
### 1.3.0 (2026-10-22) [source](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-core/CHANGELOG.md#130)
- feat: stream tool-call args as `tool-call-delta` slices
### 1.2.0 (2026-06-17) [source](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-core/CHANGELOG.md#120)
- feat(core): add OpenAI-compatible stream event conversion
### 1.1.0 (2025-11-24) [source](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-core/CHANGELOG.md#110)
- allow to concat system messages
### 1.0.0 (2025-10-17) [source](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-core/CHANGELOG.md#100)
- Standard content blocks: A new unified API for accessing modern LLM features across all providers
- New `contentBlocks` property: Provides provider-agnostic access to reasoning traces, citations, built-in tools (web search, code interpreters, etc.), and other advanced LLM features
- Type-safe: Full TypeScript support with type hints for all content block types
- Enhanced Message API: Improvements to the core message types
- Structured content: Better support for multimodal content with the new content blocks API
- Provider compatibility: Consistent message format across all LLM providers
- Rich metadata: Enhanced metadata support for tracking message provenance and transformations

## Coverage
- Release notes read for 96 releases; 7 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 1.5.1, 1.4.2, 1.4.1, 1.3.7, 1.3.6, 1.3.5, 1.3.4, 1.3.3, 1.3.2, 1.3.1, 1.2.20, 1.2.19 and 77 more.
- 17 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Sources: https://raw.githubusercontent.com/langchain-ai/langchainjs/main/libs/langchain-core/CHANGELOG.md; registry (npm) for dates.
