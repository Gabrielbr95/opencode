---
name: review-code
description: >-
  Post-implementation code review. Use when the antagonist is reviewing completed
  code against the plan. Runs verification commands, checks plan compliance and
  decisions compliance, evaluates maintainability. Load tier-calibration alongside
  this skill.
---

# Review Code

Challenge the implementation. Find bugs, plan violations, and risks. Do not modify code. Do not auto-fix.

## Process

1. **Read state**: `plan/tasks.md` (required). `plan/spec.md`, `plan/architecture.md`, and `plan/decisions.md` if present.
2. **Calibrate to tier**: Read the `tier:` field. Load **tier-calibration** and follow its code-review table.
3. **Verify**: Run verification commands as needed (bash). You may run `python`, `pytest`, linters, type checkers. You are **prohibited** from using bash to edit, write, or create files.
4. **Review**: Work through all review parameters below.
5. **Present findings**: Use the output format. Wait for approval before editing any file.

## Review Parameters

### Correctness
- Does the code run without errors?
- Does it produce the expected output?
- Are edge cases handled (per tier requirements)?

### Plan Alignment
- Verify the completed task exactly matches the active checkbox in `plan/tasks.md`.
- Check that implementation follows `plan/architecture.md` structure (if present).

### Decisions Compliance
- Check every active decision in `decisions.md`.
- Flag any implementation that silently contradicts or ignores one.

### Maintainability (assume the author is gone)
Apply these questions systematically:

**Understandability**
- Can a new maintainer understand what this code does within 10 minutes?
- Are the entry points obvious?
- Are non-obvious decisions explained in comments?
- Are there magic values with no explanation?

**Debuggability**
- If this fails at 11pm, can someone diagnose it without the original author?
- Are error messages specific enough to point to the cause?
- Is logging sufficient to reconstruct what happened?
- Can failures be reproduced with known inputs?

**Fragility**
- What assumptions does this code make that could break silently?
- What happens when input is slightly different from expected?
- Are there hardcoded paths, credentials, or environment assumptions?

**Abandonment Risk**
- If dependencies were not updated for two years, would this still run?
- Are there dependencies likely to be abandoned?

## Output Format

```
Summary
- Task reviewed: Task N — Name
- Tier applied: <tier>
- Verdict: PASS / PASS WITH NOTES / FAIL

Bugs & Risks
- BLOCKER: <immediate bug, unrunnable code, plan violation>
- MAJOR: <poor logging, unhandled logical edge case, missing test for key behavior>
- MINOR: <suggestion, small improvement>

Decisions Violations
- <decision number and title — how implementation contradicts it>

Maintainability
- <findings from understandability, debuggability, fragility, abandonment checks>

Conclusion
- <direct instruction: proceed, fix and re-review, or ask>
```

Report only. No speculative fixes. No academic refinements. No file edits without explicit approval.
