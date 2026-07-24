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
- Layering matters because it determines which instructions are always present, which are conditional, and where hidden prompt growth can occur.

## Motivation
- Instruction behavior is one of the easiest places for duplication, hidden overrides, and prompt bloat to accumulate.
- Product notes often need the same conceptual framing before they can talk about loader mechanics or tool-specific behavior.

## Problem Statement
- Real systems often combine global defaults, repo-level guidance, local overrides, and additive configured files.
- Without a clear model, it becomes hard to tell which rule actually shaped behavior, which rules stack, and which belong in skills instead.

## Key Concepts
- ambient instructions
- scope layers
- precedence
- additive includes
- fallback discovery
- skill boundary
- prompt-surface cost

## Principles vs Implementations
### Principles
- Ambient guidance and on-demand procedure are different layers.
- Precedence clarity matters more than any one filename convention.
- Additive layering increases reuse, but also increases hidden recurring prompt cost.
- Local overrides improve relevance, but can weaken inspectability when their authority is unclear.

### Implementations / Examples
- global + project + local instruction discovery
- first-match compatibility files
- additive configured instruction arrays
- subagent inheritance of the same instruction pipeline

## Common Patterns
- global + project + local scope layers
- first-match fallback files for compatibility
- additive instruction includes from config
- explicit separation between ambient instructions and on-demand skills
- loader debugging through “which source won?” inspection

## Advantages
- clearer behavior ownership
- less duplication than copy-pasted prompt fragments
- easier separation of stable repo norms from narrower local detail
- lower maintenance burden when the canonical home for a rule is clear

## Risks / Failure Modes
- prompt bloat from additive stacking
- hidden override behavior
- storing procedures in always-on instructions
- assuming compatibility files stack when they actually fallback

## Tradeoffs
- More layering gives more control, but also more debugging burden.
- More additive composition improves reuse, but increases hidden prompt cost.
- More local overrides improve local relevance, but can weaken inspectability.

## Relationships to Other Notes
- `../concepts/prompt-modularity-repository-architecture.md`
- `../concepts/skill-systems.md`
- `../products/opencode/config-and-instruction-loading.md`
- `../products/opencode/instruction-layering.md`
- `../products/opencode/system-prompt-control.md`

## Relevance to This Repository
- This note is the canonical concept-level home for layered instruction systems.
- Product notes that discuss opencode instruction behavior should defer here for the durable idea, then add only product-specific loader or prompt-assembly details.
- The repository's long-gap maintainability depends heavily on keeping ambient rules inspectable and distinct from on-demand procedure.

## Open Questions
- Which repo rules genuinely need ambient presence in every turn and every subagent?
- When does a modular instruction file clarify the system, and when does it only add another hidden layer?

## References
- `../concepts/prompt-modularity-repository-architecture.md` — durable principles for layering, override clarity, and prompt modularity.
- `../products/opencode/config-and-instruction-loading.md` — product mechanics for merged config plus instruction discovery.
- `../products/opencode/instruction-layering.md` — product-specific note on how ambient instructions, configured includes, and skills differ in opencode.
