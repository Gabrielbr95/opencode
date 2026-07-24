# opencode: Instruction Layering

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current source/docs excerpts
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - instruction loader changes
  - AGENTS/CLAUDE compatibility behavior changes
  - config instruction merge behavior changes

## Scope
- how opencode separates ambient instructions from skills
- what seems product-specific about `AGENTS.md`, `CLAUDE.md`, and additive `instructions`
- the narrow placement question inside opencode: ambient file vs additive instruction file vs skill

## Canonical Boundary
This note is intentionally narrower than `config-and-instruction-loading.md`.

Use this note for:
- the product-specific placement boundary between ambient instructions and skills
- the local effect of opencode's additive instruction surfaces

Use `config-and-instruction-loading.md` for:
- loader/discovery mechanics and precedence debugging

Use `research/concepts/instruction-layering.md` for:
- the cross-tool concept model

## Why This Matters Here
- This repository relies heavily on durable instructions and on-demand skills.
- In opencode, the practical maintenance problem is not only which instruction source wins, but which kinds of rules belong in ambient instruction layers at all.

## Current Findings
- opencode appears to have a real ambient instruction pipeline rather than one static prompt file.
- `AGENTS.md` appears first-class.
- `CLAUDE.md` appears to behave as compatibility fallback rather than as a peer that always stacks.
- configured `instructions` appear additive.
- skills are separate from the ambient instruction pipeline and stay on-demand.

## Product-Specific Layer Distinctions

### Ambient file layers
Current source excerpts suggest there are bounded global and project instruction file layers.

What matters here:
- they shape always-on behavior
- they affect subagents too
- they carry recurring prompt cost every turn

### Additive configured `instructions`
Configured instruction files appear more compositional than `AGENTS.md`.

What matters here:
- several files can accumulate
- they are a distinct prompt-growth surface
- they are useful when always-on modularity matters, but they are easy to overuse

### Skills
Skills are not part of the same ambient instruction mechanism.

What matters here:
- they package reusable procedure
- they remain conditional rather than always loaded
- they are a better home for narrow repeatable workflows than ambient policy text

## Narrow Placement Boundary Inside opencode

### Best fit for ambient instructions
- stable operating behavior
- safety norms
- communication defaults
- branch-wide expectations that should affect subagents too

### Best fit for additive configured instruction files
- always-on modular docs that are still meant to remain ambient
- branch-level material that benefits from explicit composition rather than one large file

### Best fit for skills
- reusable procedures
- bounded workflows
- task-specific routines that should not be injected every turn

## Main Failure Modes Seen From This Boundary
- procedures drifting into always-on instructions
- stable policy hidden only inside skills
- additive instruction sprawl that quietly inflates prompt surface
- confusing loader mechanics with placement decisions

## Relationships to Other Notes
- `research/products/opencode/config-and-instruction-loading.md`
- `research/products/opencode/agents-permissions-and-skills-basics.md`
- `research/concepts/instruction-layering.md`
- `research/concepts/prompt-modularity-repository-architecture.md`
- `research/concepts/skill-systems.md`

## Relevance to This Repository
- This note is the product-specific home for the ambient-vs-skill placement question in opencode.
- It should not become a second home for general instruction-layer theory or for loader precedence details already covered elsewhere.

## Open Questions
- How much ambient instruction remains understandable in daily use before prompt-surface cost becomes excessive?
- Which current repo rules belong in `AGENTS.md`, additive `instructions`, or skills?
- Which parts of this instruction pipeline are stable public behavior versus implementation detail?

## References
- Context7 `/anomalyco/opencode` — instruction loader, prompt assembly, and skill-visibility excerpts.
