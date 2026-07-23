---
name: workflow-execute
description: Model-invoked. The execution loop for bounded implementation work. Loads automatically when performing scoped execution.
---

# Workflow Execute
**Triggered by:** The Generalist beginning bounded implementation work from `plan/tasks.md`.

## Procedure
1. **Confirm Scope:** Start from the approved execution scope in `plan/tasks.md` and the immediately relevant plan context. Stay within that scope. If the work needs to expand materially, stop and return to planning instead of silently broadening execution.
2. **Claim Honestly:** Mark each task `[>]` before touching the implementation tied to that task.
3. **Implement (YAGNI):** Write the simplest, most boring change that fulfills the scoped requirement. Do not add future-proofing abstractions or unrelated cleanup outside the approved scope.
4. **Verify Proportionally:** Run the lightest check that gives real confidence for the scoped work: test, script, targeted command, or direct behavior check as appropriate.
5. **Troubleshoot Deliberately:** If verification fails, load `diagnose-bug` and run one evidence-based troubleshooting loop. Re-verify after each loop.
6. **Cap the Loop:** After 3 failed troubleshooting loops, stop. Mark the affected task `[!]`, record the blocker, and report the failure instead of guessing.
7. **Complete Honestly:** Only after verification passes, change the completed scoped task from `[>]` to `[x]`. If more approved tasks remain in scope, continue; otherwise stop.
8. **Escalate Scope Back to the Session Owner:** If the approved scope no longer fits this bounded execution skill, stop and return control to the primary session owner instead of widening execution or invoking broader orchestration from inside this skill.
9. **Report:** Provide a terse bulleted list of changed files, verification results, completed tasks, and any blocker if part of the scoped work ended as `[!]`.
