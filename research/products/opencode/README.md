# opencode Research

This branch stores product-specific research notes about opencode.

## Branch Role

This directory is for current opencode behavior, not for vendor-neutral theory.

Use it to answer:
- how opencode implements a capability today
- which config or runtime surfaces matter in practice
- which areas appear stable versus volatile

For cross-tool explanations, defer to:
- `../../concepts/`
- `../../capabilities/`
- `../../syntheses/`

## Reading Order
1. `foundations.md`
2. `config-and-instruction-loading.md`
3. `agents-permissions-and-skills-basics.md`
4. `references-and-external-context-basics.md`
5. `local-first-models-and-providers.md`
6. `permissions-and-agent-safety.md`
7. `memory-and-retrieval.md`
8. `session-control-and-recovery.md`
9. `mcp-and-tooling.md`
10. `config-surface-and-volatility-map.md`
11. `advanced-features-map.md`
12. `instruction-layering.md`
13. `system-prompt-control.md`

## Canonical Bridges Upward
- instruction theory -> `../../concepts/instruction-layering.md`
- prompt-repo structure -> `../../concepts/prompt-modularity-repository-architecture.md`
- context attachment -> `../../capabilities/context-attachments.md`
- retrieval systems -> `../../capabilities/retrieval-pipelines.md`
- sessions -> `../../capabilities/sessions.md`
- MCP -> `../../capabilities/mcp.md`
- vocabulary -> `../../syntheses/vocabulary.md`

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, selected source excerpts, repository note cross-check
- Stability: Low
- Recheck triggers:
  - config schema changes
  - release notes mention behavior changes
  - local behavior differs from docs
