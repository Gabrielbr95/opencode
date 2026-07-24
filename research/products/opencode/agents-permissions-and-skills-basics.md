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
- The basic relationship between agents, permissions, and skills in opencode
- What seems foundational before studying more advanced features

## Why This Matters Here
- This repository already uses agent roles and skills heavily.
- The main practical question is not “what advanced feature exists?” but “who is doing what, under which permissions, with which reusable procedures?”

## Current Findings
- opencode appears to treat agents, permissions, and skills as separate layers.
- That separation is useful:
  - agents = workers
  - permissions = runtime control
  - skills = on-demand procedural help
- This is a good foundation for a controllable harness.

## Agents: Practical Model
Agents appear to be named workers with configurable fields such as:
- model
- description
- prompt/system text
- mode
- steps
- permissions

The docs and source excerpts also suggest:
- built-in agents exist
- custom agents can be defined in config or loaded from markdown files
- some modes are primary-facing while others are subagent-facing

Practical takeaway:
- agents define **who the worker is**
- they do not by themselves define what is allowed

## Permissions: Practical Model
Permissions appear to be the runtime enforcement layer.

Key ideas found in docs/spec:
- rules can allow, ask, or deny
- per-agent overrides exist
- rule matching is pattern-based
- the last matching rule appears to win in newer rule-based evaluation logic

Practical takeaway:
- permissions are where autonomy should be tightened first
- if an agent feels unsafe or too broad, permissions are usually the first lever to inspect

## Skills: Practical Model
Skills appear to be reusable procedural modules discovered from skill directories or configured sources.

Important distinction:
- skills are not ambient instructions
- they are loaded on demand when relevant

Another useful detail from current source excerpts:
- the system prompt only appears to list skills that pass the agent's permission filter

Practical takeaway:
- skills are part of the available capability surface
- permissions can shape which skills an agent effectively sees or uses

## Clean Mental Model

### Agent
Who is acting.

### Permission
What that actor may do.

### Skill
Reusable procedure the actor may load if allowed.

That is probably the simplest durable mental model for this repository.

## Practical Guidance for This Repository

### Start with permissions before advanced delegation
If a role feels too broad, tighten permissions before inventing more roles.

### Use skills to reduce prompt bloat
If a procedure is reusable but not always relevant, prefer a skill over adding more ambient instructions.

### Keep agent roles narrow and understandable
Avoid many overlapping agents without a clear difference in:
- responsibility
- permission envelope
- expected use case

## Product Drift Warning
There appears to be some drift between:
- current docs/config shapes
- newer v2 spec direction

Areas likely to drift:
- singular vs plural config keys
- permission shape details
- command vs skill emphasis

So this note should be read as a current practical snapshot, not a permanent contract.

## Relationship to General Concepts
- `research/concepts/agent-architectures.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`
- `research/concepts/skill-systems.md`

## Open Questions
- Which built-in agents are durable enough to depend on long-term?
- What is the safest sensible default permission profile for this environment?
- Which skill patterns work best without causing skill sprawl?

## References
- Context7 `/anomalyco/opencode` — current docs/source/spec excerpts for agents, permissions, and skills.
