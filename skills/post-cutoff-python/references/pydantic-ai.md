# pydantic-ai (pypi): changes after 2025-06-01

- Latest stable on the registry: **2.75.0** (2026-11-25). Built 2026-11-25.
- 274 stable releases after the cut-off: 0.2.13 (2025-06-03) to 2.75.0 (2026-11-25).
- New major versions since the cut-off: 1.0.0 (2025-09-05), 2.0.0 (2026-06-23).
- Lines below are quoted from upstream release notes and sorted by keyword rules. Not reviewed by a person. Open the source link before relying on one.

## Breaking changes
### 2.73.0 (2026-11-24) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2730)
- Leave `init=False` evaluator fields out of [`Dataset`][pydantic_evals.dataset.Dataset] files and schemas, and stop `ClassVar` annotations breaking [`to_file()`][pydantic_evals.dataset.Dataset.to_file]
### 2.60.0 (2026-10-23) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2600)
- Keep tool returns shaped like media markers from breaking [`StepPersistence`][pydantic_ai_harness.step_persistence.StepPersistence] snapshots, and fix `SqliteMediaStore`, `DiskMediaStore`, `MongoMediaStore` and `S3MediaStore` […]
### 2.33.0 (2026-08-21) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2330)
- Here's a filtered list of the breaking changes for each version to help you upgrade Pydantic AI.
- See #11111 - A model request whose `thinking` effort level differs from the one in effect, like a run's first request with `thinking='low'`, emits a [`ModelSettingsDeltaEvent`][pydantic_ai.messages.ModelSettingsDeltaEvent], which […]
- Nothing was removed, but code that reads message history behaves differently, and some durable workflows record a different sequence of activities or steps
- See #8094 - Pydantic AI no longer records a [`RetryPromptPart`][pydantic_ai.messages.RetryPromptPart]. A tool retry is that call's [`ToolReturnPart`][pydantic_ai.messages.ToolReturnPart] with `outcome='retried'`, and a retry that […]
- See #9405 - A tool that joins the agent's tools mid-run emits a [`ToolAvailabilityDeltaEvent`][pydantic_ai.messages.ToolAvailabilityDeltaEvent], which a durability `event_stream_handler=` receives in an event-handler activity or […]

## Removed or renamed
### 2.73.0 (2026-11-24) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2730)
- Drop the unified settings Claude, Gemini and Grok models reject instead of sending them. A [`FallbackModel`][pydantic_ai.models.fallback.FallbackModel] that relied on the 400 to reach a later model now stays on the first model […]
### 2.71.0 (2026-11-19) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2710)
- Let [`Peers(network)`][pydantic_ai_harness.peers.Peers] join an [`InMemoryPeerNetwork`][pydantic_ai_harness.peers.InMemoryPeerNetwork] under the agent's `name`, and rename `PeerNetwork` to […]
### 2.69.0 (2026-11-17) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2690)
- Rename harness `subagents`, `filesystem` and `spend` packages to their capability names and align store, `ACP*` and `*Error` class names
- Rename `BubblewrapSandbox` to [`BubblewrappedWorkspace`][pydantic_ai_harness.bubblewrap_sandbox.BubblewrappedWorkspace] and clarify its docs
### 2.64.0 (2026-10-31) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2640)
- Remove unresolvable [`RealtimeEvent`][pydantic_ai.realtime.RealtimeEvent] from `pydantic_ai.agent.all`
### 2.60.0 (2026-10-23) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2600)
- Drop client-supplied [`TextContent.metadata`][pydantic_ai.messages.TextContent.metadata] from user prompts in [`sanitize_messages`][pydantic_ai.messages.sanitize_messages]
### 2.59.0 (2026-10-21) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2590)
- Remove shut-down Groq models `playai-tts`, `playai-tts-arabic`, `meta-llama/llama-guard-4-12b` and `meta-llama/llama-4-maverick-17b-128e-instruct`
### 2.54.0 (2026-10-03) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2540)
- Drop the [`SubAgents`][pydantic_ai_harness.subagents.SubAgents] `agent_folders` default-change warning: since v2.52.0 the `agents` folder is not loaded by default, so pass `agent_folders='agents'` to keep loading it

## Deprecated
### 2.73.0 (2026-11-24) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2730)
- Warn with [`DeprecatedModelWarning`][pydantic_ai.exceptions.DeprecatedModelWarning] when a request targets a model Anthropic or OpenAI has deprecated
### 2.71.0 (2026-11-19) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2710)
- Add `auth` to [`StackOne`][pydantic_ai_harness.stackone.StackOne], deprecating `api_key`, to match the other hosted MCP capabilities
- Deprecate `DEPRECATED_ANTHROPIC_MODELS`, which Pydantic AI no longer uses
### 2.69.0 (2026-11-17) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2690)
- Make [`Advisor`][pydantic_ai_harness.advisor.Advisor] accept `native=` and `local=` like the other [`NativeOrLocalTool`][pydantic_ai.capabilities.NativeOrLocalTool] capabilities, deprecating `mode`
- Rename the `DockerSandbox` harness capability to [`DockerContainer`][pydantic_ai_harness.docker_container.DockerContainer], keeping `DockerSandbox` as a deprecated alias
### 2.68.0 (2026-11-12) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2680)
- Give sub-agent task-control events the `Event` suffix and past-participle names, with `agent_name` and `parent_task_id` fields, keeping the old names as deprecated aliases
- Rename harness [`CapabilityEvent`][pydantic_ai.messages.CapabilityEvent] fields to `*_count`, `*_name`, `duration_ms` and `previous_item`, keeping the old names as deprecated aliases
### 2.62.0 (2026-10-27) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2620)
- Build Harness [`SystemReminders`][pydantic_ai_harness.system_reminders.SystemReminders] on request-scoped system prompts and deprecate `cache_ttl`
- Add [`CodeMode(monty_sandbox=...)`][pydantic_ai_harness.CodeMode], which takes a remote Monty URL or a function that builds the pool, and deprecate `monty_sandbox_url`
### 2.61.0 (2026-10-24) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2610)
- Deprecate [`google_multi_speaker`][pydantic_ai.realtime.google.GoogleRealtimeModelSettings.google_multi_speaker] on [`GoogleRealtimeModel`][pydantic_ai.realtime.google.GoogleRealtimeModel], which no Gemini Live model supports
### 2.60.0 (2026-10-23) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2600)
- Deprecate [`RetryPromptPart`][pydantic_ai.messages.RetryPromptPart] in favor of [`ToolReturnPart(outcome='retried')`][pydantic_ai.messages.ToolReturnPart] and [`RetryFeedbackPart`][pydantic_ai.messages.RetryFeedbackPart]. […]
- Deprecate [`OpenAIDecisionsProvider`][pydantic_ai.providers.openai_decisions.OpenAIDecisionsProvider] and let [`OpenAIDecisionsModel`][pydantic_ai.models.openai_decisions.OpenAIDecisionsModel] take […]
- (4 more in this category not shown; see the changelog.)

## Minimum versions and platform support
### 2.55.0 (2026-10-09) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2550)
- Require Python 3.11 or newer in every package; Python 3.10 installs resolve to 2.54.0 and earlier
### 1.0.0 (2025-09-05) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v100-2025-09-04)
- See #2725 - Drop support for Python 3.9

## New APIs and features
### 2.73.0 (2026-11-24) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2730)
- Add `capabilities` to [`Agent.override`][pydantic_ai.agent.Agent.override] and export [`AgentInstructions`][pydantic_ai.capabilities.AgentInstructions] and [`SourcedInstruction`][pydantic_ai.capabilities.SourcedInstruction]. […]
- Add [`RealtimeSession.append_voice_instructions`][pydantic_ai.realtime.RealtimeSession.append_voice_instructions] for GPT-Live's voice model, and a Twilio Media Streams bridge example
### 2.71.0 (2026-11-19) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2710)
- Add [`StavProvider`][pydantic_ai.providers.stav.StavProvider] for the Stav European inference gateway
- Add Otari as an OpenAI-compatible gateway provider
- Add `grep_tool_result` and `unit='bytes'` reads for [`ToolOutputLimits`][pydantic_ai_harness.tool_output_limits.ToolOutputLimits] spills
- Add [`DeferredToolRequests.validated_args`][pydantic_ai.tools.DeferredToolRequests.validated_args] so an approver sees the arguments a deferred tool call will run with
### 2.70.0 (2026-11-17) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2700)
- Add [`huggingface_logprobs`][pydantic_ai.models.huggingface.HuggingFaceModelSettings.huggingface_logprobs] and [`huggingface_top_logprobs`][pydantic_ai.models.huggingface.HuggingFaceModelSettings.huggingface_top_logprobs] to […]
- Add [`CapabilityPart`][pydantic_ai.messages.CapabilityPart], a request part for what a capability tells the model, rendered by the framework before any model sees it
### 2.69.0 (2026-11-17) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2690)
- Add [`service_tier`][pydantic_ai.settings.ModelSettings.service_tier] support to [`GroqModel`][pydantic_ai.models.groq.GroqModel]
- Add [`minimax_model_profile`][pydantic_ai.profiles.minimax.minimax_model_profile] and use it for MiniMax models on Bedrock, [`OpenAICompatibleProvider`][pydantic_ai.providers.openai_compatible.OpenAICompatibleProvider] […]
### 2.68.0 (2026-11-12) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2680)
- Add [`OutputTokenLimitExceeded`][pydantic_ai.exceptions.OutputTokenLimitExceeded], and fall back to the next model in [`ModelFallback`][pydantic_ai.capabilities.ModelFallback] when a response is cut off at […]
- Add `DelegationTasks.discover()` and stop one damaged saved task from blocking `DelegationTasks.opened()`
- Add the [`RefineOutput`][pydantic_ai_harness.RefineOutput] harness capability
### 2.67.0 (2026-11-11) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2670)
- Add [`framing_announcement`][pydantic_ai.settings.ModelSettings.framing_announcement] setting and only announce the `<system>` voice tag once a conversation needs it
### 2.65.0 (2026-11-03) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2650)
- Add multimodal notes to [`AskUserAnswer`][pydantic_ai_harness.ask_user.AskUserAnswer]
### 2.64.0 (2026-10-31) [source](https://github.com/pydantic/pydantic-ai/blob/main/docs/changelog.md#v2640)
- Add [`output_speech_timestamps`][pydantic_ai.realtime.RealtimeModelSettings.output_speech_timestamps] to report word timing of realtime speech, on Azure AI Voice Live
- Add a [`first_event_timeout`][pydantic_ai.settings.ModelSettings.first_event_timeout] model setting so a stream that never starts can fall back
- Add agent artifact security scanning for [`Memory`][pydantic_ai_harness.memory.Memory] and [`Skills`][pydantic_ai_harness.skills.Skills] with [`ArtifactScanner`][pydantic_ai_harness.artifact_scanning.ArtifactScanner]
- (10 more in this category not shown; see the changelog.)

## Coverage
- Release notes read for 40 releases; 21 had extractable items.
- no details in release notes (fixes only, or nothing these rules recognise): 2.66.0, 2.63.0, 2.57.0, 2.56.0, 2.51.0, 2.50.0, 2.47.0, 2.44.0, 2.42.0, 2.38.0, 2.0.0, 1.0.1 and 7 more.
- 234 other registry releases after the cut-off have no separate notes in these sources (often patch releases).
- Source not reachable in this build: github_releases pydantic/pydantic-ai: HTTP 403 cached
- Sources: https://raw.githubusercontent.com/pydantic/pydantic-ai/main/docs/changelog.md, https://github.com/pydantic/pydantic-ai/releases; registry (pypi) for dates.
