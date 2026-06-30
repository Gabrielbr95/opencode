---
name: review-code
description: Model-invoked. The strict 2-stage code review procedure. Loads when verifying completed work.
---

# Review Code
**Triggered by:** A task being completed, a subagent returning work, or the user requesting a review.

## Procedure
Do not proceed to Stage 2 until Stage 1 is completely evaluated.

### Stage 1: Spec Compliance (Does it do what was asked?)
1. Check `plan/tasks.md` and `plan/spec.md`. Does the code fulfill the exact requirements?
2. Did it miss any edge cases defined in the plan?
3. Does it violate any constraints from `plan/decisions.md` or `AGENTS.md`?

### Stage 2: Code Quality (Is it robust?)
1. **Error Handling:** Are there silent failures? (e.g., empty `except` blocks, swallowed errors). Fail if found.
2. **YAGNI Check:** Is it overly complex? Could a standard library function replace custom logic? Fail if over-engineered.
3. **Readability:** Are variables/functions named using plain, obvious language that matches the domain?

## Output
- If reviewing your own code: Fix the issues immediately before marking the task `[x]`.
- If reviewing a subagent or user's code: Return a verdict of **PASS** or **FAIL**. If FAIL, provide a terse bulleted list of strictly required fixes. No stylistic nitpicks.
