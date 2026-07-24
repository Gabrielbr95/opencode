# opencode: System Prompt Control

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current source excerpts, local `customize-opencode` skill guidance already present in this repository workflow
- Product version: current docs/source snapshot; exact installed local version not verified
- Stability: Low
- Recheck triggers:
  - plugin hook changes
  - request/prompt assembly changes
  - experimental hook changes
  - local runtime behavior differs from source reading

## Scope
- How much control over opencode's system prompt appears available
- Which parts of the earlier note are confirmed, corrected, or still unknown
- What the most plausible control levers are before considering a fork or harness switch

## Why This Matters Here
- This repository already invests heavily in instructions, agents, and skills.
- If opencode's baked prompt layers are large or rigid, they affect token cost, controllability, and maintainability.
- This is an advanced topic, but it is now grounded by the foundation notes instead of being treated as a speculative hack in isolation.

## Current Findings
- opencode does assemble important parts of the system prompt in code on each model request.
- Ambient instructions are injected every turn.
- Skills and MCP instructions are also added from code-driven system-prompt assembly.
- Standard customization surfaces shape the final prompt strongly, but they do **not** appear to expose a normal declarative "rewrite the whole system prompt" feature.
- A confirmed advanced lever does exist: the plugin hook `experimental.chat.system.transform`.
- The existence of the hook is confirmed; the practical safety and usefulness of using it in this exact setup is still untested locally.

## What Is Confirmed

### 1. Important parts of the system prompt are generated in code
Current source excerpts show that each model request builds a `system` payload from multiple pieces, including:
- environment/system context
- ambient instructions
- MCP instructions
- skill instructions/listing

This confirms the old note's main idea: the prompt is not just one static editable file.

### 2. Ambient instruction files are injected every turn
Current source excerpts confirm that `instruction.system()` is included in system prompt construction each request.

Practical consequence:
- `AGENTS.md` and configured instructions are persistent levers
- any noise here has recurring cost

### 3. Subagents inherit the same ambient instruction pipeline
Current source excerpts show subagents get fresh sessions that go through the same prompt-building path.

Practical consequence:
- broad instruction changes affect the whole harness, not just the main thread

### 4. Skill visibility is part of the generated prompt surface
Current source excerpts confirm that available skills are formatted into the system prompt, and that denied skills do not appear there.

Practical consequence:
- reducing visible skills can reduce prompt surface area
- skill permissions are one indirect prompt-control lever

### 5. A plugin hook exists to transform the system prompt
Current source excerpts confirm `experimental.chat.system.transform` is triggered during LLM request preparation.

The hook receives mutable output shaped like:
- `{ system }`

and plugins mutate that output in place.

This is the strongest confirmed control lever found so far.

## What the Earlier Note Got Right
- The core prompt is not fully controlled by normal text files alone.
- Standard repo-level customization mainly shapes layers around a code-built prompt assembly process.
- `experimental.chat.system.transform` is a real hook worth investigating.
- Experimental hooks deserve stability caution.

## What Needed Correction or Nuance

### 1. “Standard configuration cannot touch the core prompt” was too absolute
That claim is directionally right but too broad.

Why:
- current request-prep source suggests `agent.prompt` can replace the provider default system header
- ambient instructions also directly affect the prompt every turn

More accurate wording:
- standard surfaces can shape important prompt layers
- but they do not appear to provide a clean normal feature for fully rewriting the entire assembled system prompt

### 2. “Fixed token cost the user cannot reduce” was too absolute
That also needs nuance.

Some prompt surface can be reduced by:
- trimming ambient instructions
- denying or removing unnecessary skills from visibility
- reducing MCP usage/instructions
- changing agent prompt/header behavior

More accurate wording:
- some recurring prompt cost is user-shapeable
- the deepest generated layers are not obviously removable through normal config alone

### 3. The sample plugin implementation was not actually confirmed
The existence of the hook is confirmed.
The exact best mutation strategy for this repository is **not** yet verified in a live run.

So the old sample should not be treated as known-good code.

## Best Confirmed Control Levers, Ranked

### 1. Ambient instruction discipline
Lowest-risk and already proven.

Examples:
- tighten `AGENTS.md`
- move procedures out of always-on instructions and into skills
- avoid additive instruction sprawl

### 2. Skill visibility control
Confirmed indirect lever.

Examples:
- remove unused skills
- deny irrelevant skills for specific agents

### 3. MCP restraint
If MCP instructions are part of the system prompt, unnecessary MCP integration likely adds recurring prompt surface.

### 4. Agent prompt shaping
Custom agent prompt/header behavior appears to affect the request header, though not necessarily the whole assembled system structure.

### 5. `experimental.chat.system.transform`
Strongest direct lever found, but also highest-risk lever before forking.

## What Is Still Unknown
- Whether using `experimental.chat.system.transform` is practical and stable enough in real day-to-day use.
- What the safest minimal transform strategy is for this repository.
- How much token reduction is actually achievable without breaking tool affordances or system clarity.
- Whether a live local run would reveal undocumented constraints in the hook contract.

## Practical Interpretation for This Repository
Do **not** jump straight to system-prompt surgery.

Use this order first:
1. clean up ambient instructions
2. control skill visibility
3. avoid unnecessary MCP surface
4. only then consider plugin-level system transform work

This keeps the boring levers in play before reaching for the sharp one.

## Cautious Next Spike
If this topic becomes worth testing, the next honest step is a small local spike whose only purpose is to answer:

> Can `experimental.chat.system.transform` safely and predictably reduce or reshape the assembled system prompt in this setup?

That spike should verify only:
- the actual runtime shape of `system`
- whether the hook fires per request as expected
- whether a minimal transform survives restart and basic use
- whether token/control benefit is material enough to justify maintenance cost

Do **not** start by writing a complex trimming plugin.

## Local-First / Corporate Notes
- Plugin-based prompt surgery is code, not harmless configuration.
- Experimental hooks imply re-audit cost on upgrades.
- Any solution that depends on version-sensitive prompt internals is a maintenance commitment.
- For a solo maintainer with long interruption gaps, this should remain an exception path, not the default workflow pattern.

## Relationship to Other Notes
- `research/products/opencode/instruction-layering.md`
- `research/products/opencode/advanced-features-map.md`
- `research/products/opencode/config-surface-and-volatility-map.md`
- `research/products/opencode/permissions-and-agent-safety.md`

## Open Questions
- Is plugin-level system-prompt transformation worth the maintenance burden here?
- How much control can be gained from boring levers alone before any plugin work is needed?
- Would a small transform plugin meaningfully outperform simpler instruction and skill cleanup?

## References
- Context7 `/anomalyco/opencode` — prompt assembly, instruction injection, subagent session creation, skill filtering, and plugin-trigger excerpts.
