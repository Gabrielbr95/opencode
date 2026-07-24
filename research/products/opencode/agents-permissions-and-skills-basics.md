# opencode: Agents, Permissions, and Skills Basics

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, v2 spec excerpts
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - permission schema changes
  - agent config changes
  - skill discovery changes
  - current docs and spec drift further apart

## Scope
- the basic structural relationship between agents, permissions, and skills in opencode
- the smallest product mental model needed before narrower branch notes

## Canonical Boundary
This note is for the **basic structural mental model**:
- agent = who acts
- permission = what is allowed
- skill = reusable procedure the actor may load

For runtime safety posture and stricter operational interpretation, see:
- `research/products/opencode/permissions-and-agent-safety.md`

## Why This Matters Here
- This repository uses agent roles and skills heavily.
- The useful product question is the separation between worker identity, permission envelope, and reusable procedure.

## Current Findings
- opencode appears to treat agents, permissions, and skills as separate layers.
- agents look like named workers with their own model/prompt/mode/permission envelope.
- permissions look like runtime enforcement rules with allow/ask/deny style outcomes.
- skills look like on-demand procedural modules rather than ambient instructions.

## Product Mental Model

### Agent
Who is acting.

### Permission
What that actor may do.

### Skill
Reusable procedure the actor may load if available and allowed.

## Observed Product Details

### Agents
Current docs/source excerpts suggest agents can carry fields such as:
- model
- description
- prompt/system text
- mode
- steps
- permissions

### Permissions
Current docs/spec excerpts suggest:
- rules can allow, ask, or deny
- per-agent overrides exist
- rule matching is pattern-based

### Skills
Current source excerpts suggest:
- skills are discovered from skill directories or configured sources
- they are not ambient instructions
- visible/usable skills are shaped by the permission envelope

## Relationships to Other Notes
- `research/products/opencode/foundations.md`
- `research/products/opencode/permissions-and-agent-safety.md`
- `research/products/opencode/instruction-layering.md`
- `research/concepts/agent-architectures.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`
- `research/concepts/skill-systems.md`

## Relevance to This Repository
- This note is the shortest product-level bridge between the opencode branch overview and narrower notes on permissions, instruction placement, and customization.
- It should stay a simple model, not a second home for branch roadmap or safety policy.

## Open Questions
- Which built-in agents are durable enough to depend on long-term?
- What is the safest sensible default permission profile for this environment?
- Which skill patterns work best without causing skill sprawl?

## References
- Context7 `/anomalyco/opencode` — current docs/source/spec excerpts for agents, permissions, and skills.
