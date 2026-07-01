---
name: orchestrate-batch
description: User-invoked. Hands the agent a batch of tasks to grind through autonomously using subagents.
disable-model-invocation: true
---

# Orchestrate Batch
**Triggered by:** The user manually calling `/orchestrate-batch`.

## Procedure
1. **Read Tasks:** Read `plan/tasks.md` to identify pending `[ ]` tasks.
2. **Confirm:** Ask the user which tasks to execute (e.g., "Tasks 1 through 3?").
3. **Execution Loop:**
   - Mark task as `[>]` in `plan/tasks.md`.
   - Dispatch the **Coder** subagent via the `task` tool to implement the exact steps.
   - Dispatch the **Reviewer** subagent to verify the Coder's work.
   - If Reviewer FAILS, send the Coder back with the feedback.
   - If Reviewer PASSES, mark task as `[x]` in `plan/tasks.md`.
4. **Report:** Once the batch is complete or blocked `[!]`, present a summary to the user.
