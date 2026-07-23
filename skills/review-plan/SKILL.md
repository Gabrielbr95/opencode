---
name: review-plan
description: Model-invoked. The proportional review procedure for planning artifacts. Loads when reviewing spec, tasks, decisions, architecture, or overall plan readiness.
---

# Review Plan
**Triggered by:** A planning pass being completed, a planning subtask being handed off for critique, or the user requesting review of `plan/*` artifacts.

## Procedure

### Stage 1: Internal Consistency
1. Start with the claimed scope, touched planning artifacts, and immediately relevant related sections. Do not reread every durable file unless the review reveals uncertainty or contradiction.
2. Check whether `plan/spec.md`, `plan/tasks.md`, `plan/decisions.md`, and `plan/architecture.md` agree where they overlap.
3. Check whether terminology is used consistently across the touched artifacts.
4. Check for stale references, contradictory scope statements, or tasks that no longer match the stated objective.

### Stage 2: Planning Quality
1. **Proportional Review:** Match review depth to the tier, work type, and consequence. Do not demand a fully expanded plan when the current workflow only needs the next slice to be actionable.
2. **Actionability:** Is the next execution slice clear enough to start safely?
3. **Decision Discipline:** Are major decisions surfaced for user approval? Are minor reversible choices being over-documented?
4. **Task Shape:** Does `plan/tasks.md` show the full path clearly without forcing unnecessary detail everywhere?
5. **YAGNI Check:** Is the plan drifting into unnecessary contract detail or speculative structure that does not materially reduce risk?

## Output
- If reviewing your own planning artifacts: Fix the issues immediately before presenting the plan as ready.
- If reviewing a subagent or another draft: Return **PASS** or **FAIL**. If FAIL, provide a terse bulleted list of strictly required fixes. No stylistic nitpicks.
- A PASS means the plan is coherent enough for the current objective and boundary. It does not require every later slice to be fully detailed unless the user explicitly asked for that.
