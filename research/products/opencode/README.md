# opencode Research

This branch is for fast-moving notes about opencode itself.

## Scope
- foundations
- configuration model
- agents and modes
- permissions
- skills
- references
- providers
- advanced features
- MCP integration
- instruction layering and repo customization

## Why This Branch Exists
opencode is the active harness in this repository, so product-specific learning here can directly improve day-to-day workflow.

## Branch Role in the Research Stack
This directory should answer:
- how opencode implements a capability today
- which exact behaviors or config surfaces are product-specific
- which parts look volatile and need rechecking

This directory should **not** be the main home for:
- durable concept definitions
- repository-wide policy
- cross-tool capability explanations that belong in `../../capabilities/`

## Suggested Reading Order
1. `foundations.md`
2. `config-and-instruction-loading.md`
3. `instruction-layering.md`
4. `agents-permissions-and-skills-basics.md`
5. `references-and-external-context-basics.md`
6. `local-first-models-and-providers.md`
7. `permissions-and-agent-safety.md`
8. `config-surface-and-volatility-map.md`
9. `session-control-and-recovery.md`
10. `memory-and-retrieval.md`
11. `mcp-and-tooling.md`
12. `advanced-features-map.md`
13. `system-prompt-control.md` *(advanced, verified hook exists, practical spike still unrun)*

## Capability Bridges
- `../../concepts/instruction-layering.md`
- `../../capabilities/context-attachments.md`
- `../../capabilities/retrieval-pipelines.md`
- `../../capabilities/model-routing.md`
- `../../capabilities/sessions.md`
- `../../capabilities/mcp.md`

## Suggested Next Notes
- `plugin-and-hook-customization.md`
- `custom-agents-and-role-shaping.md`
- `practical-safe-baseline.md`

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, selected source excerpts, repository note cross-check
- Stability: Low
- Recheck triggers:
  - config schema changes
  - release notes mention behavior changes
  - local behavior differs from docs
