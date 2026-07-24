# opencode: Local-First Models and Providers

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current providers docs excerpts
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - provider config changes
  - local backend support changes
  - auth storage or provider policy changes

## Scope
- How opencode appears to configure providers
- What local-first usage looks like in practice
- Why provider understanding matters before more advanced product features

## Canonical Boundary
This note is for **current opencode provider behavior and local-first fit**.

For the reusable routing concept, see:
- `research/capabilities/model-routing.md`

## Why This Matters Here
- This environment values local-first behavior and controlled network exposure.
- Before going deeper into advanced opencode features, it helps to know how the harness reaches models at all.

## Current Findings
- opencode appears to support multiple provider backends through config.
- It can work with custom or OpenAI-compatible endpoints.
- Current docs explicitly mention local-style backends such as:
  - Ollama
  - LM Studio
  - llama.cpp via local server
- Provider config appears able to define:
  - display name
  - base URL
  - auth settings
  - headers
  - model list
  - model token limits

## What a Provider Appears To Be
A provider is the configured path from opencode to a model backend.

Practical examples:
- hosted SaaS API
- approved internal endpoint
- local OpenAI-compatible server on `127.0.0.1`

This means provider configuration is not just cosmetic. It determines where requests go and what models are available.

## Practical Local-First Model
For this repository, a local-first provider setup likely means:

1. prefer a local model server or approved internal endpoint
2. point opencode at that endpoint through provider config
3. define only the models you actually want available
4. keep limits and auth explicit

That keeps routing understandable.

## Common Provider Fields Seen in Docs
Current docs excerpts show provider config can include:
- npm adapter package
- provider display name
- `options.baseURL`
- `options.apiKey`
- custom headers
- model entries
- model limits for context and output

Practical takeaway:
- provider config is both routing and capability declaration

## Why This Is Foundational
Before studying advanced agent behavior, it helps to know:
- which model is actually being called
- whether it is local or remote
- what token limits are realistic
- whether credentials or headers are involved

Otherwise, later performance or behavior questions can get misdiagnosed as prompt issues when they are really backend issues.

## Local Backends Explicitly Worth Knowing

### Ollama
Seems supported and often discussed as a local-first option.

### LM Studio
Relevant because it matches the user's stated interests.

### llama.cpp server
Represents a more manual local OpenAI-compatible path.

These all reinforce that opencode can act as a front end to local model infrastructure rather than requiring only hosted APIs.

## Practical Boundary Rules

### Use provider config for:
- backend routing
- auth and headers
- model availability
- explicit context/output limits

### Do not bury provider assumptions in prompts
If a workflow depends on a specific model/backend shape, it is better surfaced in config or documentation than hidden in prompt text.

## Local-First / Corporate Notes
- A localhost endpoint is easier to reason about than a public API.
- Explicit `baseURL` and explicit models are preferable to vague auto-discovery when control matters.
- Any `apiKey`, headers, or auth storage still deserve review, even if the model host is internal.
- If a provider config points to a remote endpoint, that should be treated as a network boundary decision, not as a neutral default.

## Relevance to This Repository
When evaluating a provider setup, the main recurring questions are:

1. Is the backend local, internal, or external?
2. Which models are intentionally exposed to opencode?
3. Are token limits explicit and believable?
4. Are credentials stored or injected in a way that matches local policy?
5. Would troubleshooting be easy after a long interruption?

## Relationships to Other Notes
- `research/concepts/context-engineering.md`
- `research/capabilities/model-routing.md`

## Open Questions
- Which local provider path is simplest to maintain on a locked-down Windows laptop?
- How much provider detail belongs in durable notes versus per-machine setup notes?
- Which provider choices are good enough for daily harness work versus only experimentation?

## References
- Context7 `/anomalyco/opencode` — providers docs excerpts for custom providers and local OpenAI-compatible backends.
