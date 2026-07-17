---
name: review-code
description: Model-invoked. The strict 2-stage review procedure for implementation work. Loads when verifying completed code changes.
---

# Review Code
**Triggered by:** An implementation task being completed, a coding subagent returning work, or the user requesting review of code.

## Procedure
Do not proceed to Stage 2 until Stage 1 is completely evaluated.

### Stage 1: Spec Compliance (Does it do what was asked?)
1. Start with the claimed task, touched files, and immediately relevant plan sections. Do not reread broad durable context unless the review reveals uncertainty or contradiction.
2. Check the relevant parts of `plan/tasks.md` and `plan/spec.md`. Does the code fulfill the exact requirements?
3. Did it miss any edge cases defined in the relevant plan sections?
4. Does it violate any relevant constraints from `plan/decisions.md` or `AGENTS.md`?

### Stage 2: Code Quality (Is it robust?)
1. **Error Handling:** Are there silent failures? (e.g., empty `except` blocks, swallowed errors). Fail if found.
2. **YAGNI Check:** Is it overly complex? Could a standard library function replace custom logic? Fail if over-engineered.
3. **Readability:** Are variables/functions named using plain, obvious language that matches the domain?

## Output
- This skill is for implementation work only. Do not use it as the default review path for planning or documentation changes.
- If reviewing your own code: Fix the issues immediately before marking the task `[x]`.
- If reviewing a subagent or user's code: Return a verdict of **PASS** or **FAIL**. If FAIL, provide a terse bulleted list of strictly required fixes. No stylistic nitpicks.
- A PASS on a task, slice, or feature is not the final stop. Run `reconcile-work` before declaring the work complete.
