# Pi Providers and Programmatic Surfaces

## Freshness
- Last verified: 2026-07-28
- Verified against: Pi docs index, usage docs, custom-model docs, custom-provider docs, RPC docs
- Product version: current docs snapshot
- Stability: Low-Medium
- Recheck triggers:
  - provider API support changes
  - RPC protocol changes
  - custom-provider extension surface changes

## Scope
- Pi's provider/model configuration surfaces
- custom models and custom providers
- non-interactive, RPC, and SDK usage surfaces

## Canonical Boundary
This note owns Pi's provider-routing and programmatic entry surfaces.

It is not the main home for:
- package ecosystem comparison
- session internals
- general model-routing concepts

## Why This Matters Here
- Replacing a harness depends on whether providers, local endpoints, gateways, and automation entrypoints can be expressed cleanly.

## Current Findings
- Pi documents built-in support for many providers and custom-model/provider extension points.
- Pi supports custom providers through extensions and custom models through `models.json`.
- Pi exposes interactive, print/JSON, RPC, and SDK/programmatic usage modes.

## Provider and Model Surfaces

Pi home/docs describe built-in provider support for multiple vendors and local endpoints, with model switching during a session.

Documented configuration surfaces include:
- `--provider`
- `--model`
- `--api-key`
- `--thinking`
- `--models`
- `--list-models`
- `~/.pi/agent/models.json`

## Custom Models

Pi documents `models.json` for:
- local OpenAI-compatible servers such as Ollama/LM Studio/vLLM-style endpoints
- provider overrides
- custom model metadata
- compatibility flags
- thinking-level maps
- model overrides for built-in providers

## Custom Providers

Pi documents custom providers through `pi.registerProvider()` in extensions.

Documented uses include:
- proxies and gateways
- self-hosted/private endpoints
- OAuth/SSO integrations
- custom streaming APIs

Provider extensions can:
- override built-in provider base URLs or headers
- register new providers and models
- add OAuth flows for `/login`
- implement custom `streamSimple` behavior

## Modes of Use

Pi documents four main modes:
- interactive TUI
- print mode (`-p` / `--print`)
- JSON event-stream mode (`--mode json`)
- RPC mode (`--mode rpc`)

The docs also describe an SDK/programmatic surface and direct `AgentSession` use for Node.js/TypeScript users.

## RPC Surface

Pi RPC mode is documented as JSON over stdin/stdout with:
- prompt submission
- streaming event output
- model changes
- thinking-level changes
- session inspection and switching
- bash execution
- compaction control
- extension-UI request/response protocol

## Resource Loading for Programmatic Runs

Non-interactive modes still respect resource-loading and project-trust rules, with fallback behavior controlled by settings and `--approve`/`--no-approve`.

## Relationships to Other Notes
- `research/products/pi/foundations.md`
- `research/products/pi/config-and-instruction-loading.md`
- `research/products/pi/extension-ecosystem-and-core-gaps.md`
- `research/capabilities/model-routing.md`

## Repository Relevance
- This note captures whether Pi can be driven through local/custom providers and whether it exposes non-TUI integration surfaces for external tooling.

## Open Questions
- Which current provider and model-routing requirements in this repository need custom-provider extensions versus `models.json` only?

## References
- [Using Pi](https://pi.dev/docs/latest/usage) — CLI/provider flags and mode overview.
- [Custom Models](https://pi.dev/docs/latest/models) — `models.json` behavior.
- [Custom Providers](https://pi.dev/docs/latest/custom-provider) — extension-based provider registration.
- [RPC Mode](https://pi.dev/docs/latest/rpc) — headless JSON protocol.
- [Pi documentation index](https://pi.dev/docs/latest) — SDK and JSON mode entry points.
