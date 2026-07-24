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
- How opencode appears to layer ambient instructions
- How `AGENTS.md`, `CLAUDE.md`, and configured `instructions` interact
- How ambient instructions differ from skills

## Canonical Boundary
This note is intentionally narrower than `config-and-instruction-loading.md`.

Use this note for:
- how to reason about ambient instruction placement inside opencode
- where to put repo norms versus additive instruction files versus skills

Use `config-and-instruction-loading.md` for:
- loader/discovery mechanics and merged-source debugging

Use `research/concepts/instruction-layering.md` for:
- the cross-tool concept model

## Why This Matters Here
- This repository relies heavily on durable instructions and on-demand skills.
- If instruction layering is fuzzy, it becomes hard to know which file actually shaped behavior.
- This is one of the highest-value advanced topics because it controls the harness without requiring plugins or deeper experimental hooks.

## Current Findings
- opencode appears to have a real instruction pipeline, not just a single prompt file.
- `AGENTS.md` seems to be first-class.
- `CLAUDE.md` appears to be treated as a compatibility fallback rather than a peer that always stacks.
- Configured `instructions` appear additive rather than nearest-file-wins.
- Skills are not ambient instructions; they are separate, on-demand procedural modules.

## Practical Layering Model

### 1. Global ambient instruction layer
Current source excerpts suggest:
- global `AGENTS.md` is checked first
- global `CLAUDE.md` can act as fallback
- the first matching global file wins

Practical takeaway:
- there is a top ambient layer, but it is not an uncontrolled pile of global files

### 2. Project ambient instruction layer
Current source excerpts suggest:
- project instruction files are searched upward from the current directory toward the worktree root
- first matching file type wins
- this prevents stacking every `AGENTS.md` or `CLAUDE.md` across ancestors

Practical takeaway:
- project ambient instructions appear intentionally bounded
- this reduces prompt sprawl and hidden inheritance

### 3. Configured `instructions` layer
Current source excerpts suggest:
- `instructions` from config are additive
- global and local config arrays can concatenate and deduplicate
- local files and globs can be injected this way
- remote URLs may also be possible, but that is not ideal for a local-first workflow

Practical takeaway:
- `instructions` is the more compositional layer
- unlike `AGENTS.md`, it can accumulate multiple extra files

### 4. Skills layer
Skills are not part of the same ambient instruction mechanism.

Current source excerpts suggest:
- skills are listed separately in the system prompt
- only skills that pass the agent permission filter are surfaced
- skills remain on-demand procedural help, not always-on ambient policy text

Practical takeaway:
- keep “always true” guidance in ambient instructions
- keep “use when relevant” procedures in skills

## Ambient Instructions vs Skills

### Ambient instructions are for:
- stable operating behavior
- safety norms
- communication style
- repo-wide expectations

### Skills are for:
- reusable procedures
- conditional workflows
- narrow task patterns

If a rule should apply all the time, it probably does **not** belong only in a skill.
If a procedure should only appear when needed, it probably does **not** belong in always-on instructions.

## Important Operational Detail
Current source excerpts suggest instructions are injected into the system prompt every turn.

Practical consequence:
- ambient instruction wording matters a lot
- every unnecessary line has recurring cost
- instruction bloat is more expensive than skill bloat

## Subagents and Delegation
Current source excerpts suggest subagents get their own fresh session and pass through the same instruction pipeline.

Practical takeaway:
- ambient instructions affect subagents too
- if a rule truly applies repo-wide, this is good
- if a rule is too broad or too wordy, it pollutes all agent contexts, not just the main thread

## Good Layering Strategy for This Repository

### Put in `AGENTS.md`
- stable identity and behavior
- durable safety norms
- communication defaults
- general work style

### Put in configured `instructions`
- modular local standards docs
- additional policy or conventions worth always loading
- documents you want composed additively rather than collapsed into one file

### Put in skills
- repeatable procedures
- bounded workflows
- task-specific checklists and routines

## Common Failure Modes
- stuffing procedures into always-on instructions
- hiding always-on policy inside skills
- forgetting that configured `instructions` accumulate additively
- assuming `AGENTS.md` and `CLAUDE.md` both stack everywhere
- letting ambient instructions become too large to inspect comfortably

## Local-First / Corporate Notes
- Remote instruction URLs should be treated cautiously or avoided.
- A local-first setup benefits from keeping ambient instruction sources inspectable and local.
- Since subagents also inherit the instruction pipeline, noisy or risky instructions scale their cost everywhere.

## Practical Heuristic for This Repository
When adding a new rule, ask:

1. Should this apply all the time?
2. Should this apply to subagents too?
3. Is this a stable norm or a reusable procedure?
4. Does this belong in `AGENTS.md`, configured `instructions`, or a skill?
5. Will this still make sense after a long interruption?

## Relationship to Other Notes
- `research/products/opencode/config-and-instruction-loading.md`
- `research/products/opencode/agents-permissions-and-skills-basics.md`
- `research/concepts/instruction-layering.md`
- `research/concepts/prompt-modularity-repository-architecture.md`
- `research/concepts/skill-systems.md`

## Open Questions
- How much ambient instruction is too much in practical daily use?
- Which existing rules in this repository belong in AGENTS versus skills versus future modular instruction files?
- Which parts of the instruction pipeline are stable public behavior versus implementation detail?

## References
- Context7 `/anomalyco/opencode` — instruction loader, prompt assembly, and skill-visibility excerpts.
