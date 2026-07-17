---
name: orchestrate-batch
description: User-invoked. Execute a batch of implementation tasks autonomously using subagents.
disable-model-invocation: true
---

# Orchestrate Batch
**Triggered by:** The user manually calling `/orchestrate-batch`.

## Procedure
1. **Read Tasks:** Read `plan/tasks.md` to identify pending `[ ]` tasks.
2. **Confirm:** Ask the user which tasks to execute (e.g., "Tasks 1 through 3?").
3. **Scope Boundary:** This skill is for implementation execution. Do not use it as the default workflow for planning or documentation maintenance.
4. **Execute Sequentially:**
   - Mark each task as `[>]` before execution.
   - Dispatch the **Coder** subagent via the `task` tool to implement the exact steps.
   - If the task verifies cleanly and does not introduce broader risk, mark it `[x]` without forcing an immediate reviewer pass.
   - If the task blocks, mark it `[!]`, record the blocker, and stop or continue based on user-approved batch scope.
5. **Review at Meaningful Boundaries:** Use the **Reviewer** subagent by default at slice boundaries, batch completion, or when risk justifies it: architecture-affecting changes, broad refactors, contradictory results, repeated failures, or explicit user request. Do not force a reviewer pass after every minor task by default.
6. **Repair If Needed:** If Reviewer FAILS at a review boundary, send the Coder back with the feedback, then re-review the affected scope.
7. **Report:** Once the batch is complete or blocked `[!]`, present a summary to the user.
