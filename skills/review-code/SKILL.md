---
name: review-code
description: Model-invoked. The proportional 2-stage review procedure for implementation work. Loads when verifying completed code changes.
---

# Review Code
**Triggered by:** An implementation task being completed, a coding subagent returning work, or the user requesting review of code.

## Procedure
Do not proceed to Stage 2 until Stage 1 is completely evaluated.

### Stage 1: Spec Compliance (Does it do what was asked?)
1. Start with the claimed task, touched files, and immediately relevant plan sections. Do not reread broad durable context unless the review reveals uncertainty or contradiction.
2. Check the relevant parts of `plan/tasks.md` and `plan/spec.md`. Does the code fulfill the exact requirements?
3. Did it miss any scoped requirements, edge cases, or constraints defined in the relevant plan sections?
4. Does it violate any relevant constraints from `plan/decisions.md`, `plan/architecture.md` if present, or `AGENTS.md`?

### Stage 2: Code Quality (Is it robust?)
1. **Proportional Depth:** Match the depth of review to the tier, work type, and consequence. Stay strict on real defects, but do not invent production-grade concerns for a small low-risk change.
2. **Error Handling:** Are there silent failures, swallowed errors, or misleading success paths? Fail if found.
3. **YAGNI Check:** Is it overly complex for the scoped requirement? Could a simpler boring solution replace the current approach? Fail if over-engineered.
4. **Readability:** Are variables/functions named using plain, obvious language that matches the domain?

## Output
- This skill is for implementation work only. Do not use it as the default review path for planning or documentation changes.
- If reviewing your own code: Fix the issues immediately before marking the task `[x]`.
- If reviewing a subagent or user's code: Return a verdict of **PASS** or **FAIL**. If FAIL, provide a terse bulleted list of strictly required fixes. No stylistic nitpicks.
- A PASS means the implementation is review-clean for the scoped work. Run `reconcile-work` at the appropriate boundary before declaring the broader work complete.
