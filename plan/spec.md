# Specification

## Objective
Use the completed research base and revised `workflow.md` to align the harness's operational layer so `AGENTS.md`, `agents/*`, and later the key workflow skills reflect the intended way of working without adding unnecessary ceremony.

## Core Requirements
- Preserve the current tier as **POC** and keep the workflow alignment effort proportional to that tier.
- Treat `workflow.md` as the conceptual source of truth, `plan/*` as durable project truth, `AGENTS.md` and `agents/*` as role/ownership definitions, and `skills/*` as reusable procedures.
- Re-anchor the plan around the implementation/alignment phase before making durable prompt changes.
- Inspect `AGENTS.md` and all files under `agents/*` before changing workflow skills.
- Align the primary session-owner behavior in `agents/generalist.md` with the revised workflow, especially around clarification, tier/mode choice, planning vs execution boundaries, delegation limits, and solo-maintainable pragmatism.
- Align `agents/reviewer.md` so review intensity is proportional to tier, work type, and durable-write risk rather than blindly maximal.
- Preserve the current strengths of the agent layer: small prompts, clear roles, and strong default ownership by the primary agent.
- Defer procedural detail to skills instead of bloating ambient or role prompts.
- Keep durable changes to prompts, skills, rules, or config reviewable and traceable as high-value internal mutations.
- Prefer the smallest boring alignment slice that improves clarity, leverage, or safety.

## Out of Scope (Crucial)
- No broad rewrite of the harness architecture.
- No expansion into new research topics before the current alignment pass is scoped and executed.
- No skill edits until the agent layer has been inspected and the next skill targets are explicitly identified.
- No enterprise-style governance, large multi-agent redesign, or prompt proliferation unless clearly justified by observed problems.

## User Interaction
The user directs a phased alignment pass. The agent first updates the durable plan, then reviews and refines the agent-layer prompts, surfaces the planned execution order for approval, and only after that proceeds to targeted prompt edits and later skill alignment work.
