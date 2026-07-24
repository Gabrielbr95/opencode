# Instruction Layering

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - exact discovery filenames and precedence rules
  - vendor-specific additive include mechanisms

## Summary
- Many agent harnesses have an ambient instruction layer separate from per-task prompts and separate from on-demand skills.
- The durable idea is not a specific filename like `AGENTS.md`; it is the existence of a layered instruction pipeline with scope, precedence, and maintenance cost.
- Good instruction architecture keeps always-on guidance small, inspectable, and clearly separated from reusable procedures.

## Motivation
- Instruction behavior is one of the easiest places for duplication, hidden overrides, and prompt bloat to accumulate.
- A capability note reduces repetition across product notes that each implement layered instructions differently.

## Problem Statement
- Real systems often combine global defaults, repo-level guidance, local overrides, and additive configured files.
- Without a clear model, it becomes hard to tell which rule actually shaped behavior, which rules stack, and which belong in skills instead.

## Core Function
- Provide always-on behavior shaping through scoped instruction sources.
- Separate stable ambient guidance from volatile runtime context and from conditional procedures.

## Common Patterns
- Global + project + local scope layers.
- First-match fallback files for compatibility.
- Additive instruction includes from config.
- Explicit separation between ambient instructions and on-demand skills.
- Loader debugging through “which file won?” inspection.

## Typical Components
- instruction discovery rules
- precedence/override rules
- additive include mechanism
- compatibility fallback files
- debug path for inspecting effective instruction sources

## Portability
- Portable across tools:
  - layered ambient instructions exist as a general harness capability
  - precedence clarity matters more than any one file name
  - always-on guidance and on-demand procedure should stay separate
- Product-shaped:
  - file names
  - search order
  - whether layers stack or first-match
  - whether subagents inherit the same pipeline

## Advantages
- clearer behavior ownership
- less duplication than copy-paste prompt fragments
- easier repo-wide policy with narrower local overrides
- lower maintenance burden when rules have a canonical home

## Risks / Failure Modes
- prompt bloat from additive stacking
- hidden override behavior
- storing procedures in always-on instructions
- assuming compatibility files stack when they actually fallback

## Tradeoffs
- More layering gives more control, but also more debugging burden.
- More additive composition improves reuse, but increases hidden prompt cost.
- More local overrides improve relevance, but can weaken inspectability.

## Relationships to Other Notes
- `../concepts/prompt-modularity-repository-architecture.md`
- `../concepts/skill-systems.md`
- `../products/opencode/config-and-instruction-loading.md`
- `../products/opencode/instruction-layering.md`
- `../products/opencode/system-prompt-control.md`

## Practical Applications for This Repository
- Keep ambient rules small and durable.
- Put reusable procedures in skills instead of always-on instructions.
- Debug behavior by identifying the winning instruction source before editing anything.
- Treat additive instruction includes as recurring prompt cost, not free organization.

## Open Questions
- Which repo rules truly need to be ambient for every turn and every subagent?
- When is a new modular instruction file worth the extra inspection burden?

## References
- `../concepts/prompt-modularity-repository-architecture.md` — durable principles for layering, override clarity, and prompt modularity.
- `../products/opencode/config-and-instruction-loading.md` — concrete product implementation of merged config plus instruction discovery.
- `../products/opencode/instruction-layering.md` — product-specific note on how ambient instructions, configured includes, and skills differ in opencode.
