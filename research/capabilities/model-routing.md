# Model Routing

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - config shape for provider declarations
  - fallback and routing-policy features

## Summary
- Provider and model routing is the capability that determines where requests go, which models are available, and which runtime constraints apply.
- The durable idea is not a specific config schema. It is the control-plane decision about backend trust, latency, cost, token limits, and operational fit.
- In a local-first environment, routing is also a network-boundary decision.

## Motivation
- Product notes often mix stable routing concepts with volatile provider config syntax.
- This note separates the reusable routing model from one product's current field names.

## Problem Statement
- When model behavior is surprising, the real cause may be backend choice, token limits, or network path rather than prompt quality.
- Systems need a clear way to reason about local, internal, and external backends without burying those assumptions in prompt text.

## Core Function
- Route requests to one or more model backends.
- Declare available models and practical constraints.
- Keep backend assumptions explicit and inspectable.

## Common Patterns
- single approved provider
- multiple providers with explicit model catalogs
- local vs internal vs external classification
- role-based model selection
- explicit token/context/output limits

## Typical Components
- provider registry
- model catalog
- auth and header settings
- base URL or adapter definition
- routing/selection policy
- operational limits and fallback assumptions

## Portability
- Portable across tools:
  - backend routing is a separate concern from prompt design
  - explicit model catalogs and limits reduce hidden assumptions
  - local/internal/external classification matters in controlled environments
- Product-shaped:
  - exact provider config format
  - auth storage details
  - automatic discovery versus explicit declaration
  - fallback behavior

## Advantages
- clearer debugging when behavior depends on backend choice
- better control over data path and network exposure
- easier reasoning about token limits and model suitability

## Risks / Failure Modes
- prompt issues blamed on the wrong backend
- vague or auto-discovered model availability
- hidden network boundaries
- credentials or headers handled opaquely

## Tradeoffs
- Fewer providers improve predictability but reduce flexibility.
- Local backends improve control but may increase maintenance burden.
- Rich routing policies improve optimization but can make debugging harder.

## Relationships to Other Notes
- `../concepts/agent-architectures.md`
- `../concepts/context-engineering.md`
- `../products/opencode/local-first-models-and-providers.md`
- `../products/opencode/config-surface-and-volatility-map.md`

## Practical Applications for This Repository
- Document whether a backend is local, internal, or external before optimizing prompts around it.
- Keep model availability explicit instead of assuming whatever the provider exposes.
- Treat provider config as control-plane infrastructure, not as a prompt detail.

## Open Questions
- What is the simplest provider setup that stays maintainable on this machine?
- Which routing choices are worth making durable versus leaving machine-local?

## References
- `../products/opencode/local-first-models-and-providers.md` — concrete product note on current provider surface and local-first backends.
- `../products/opencode/config-surface-and-volatility-map.md` — evidence that routing concepts are more stable than current config field naming.
