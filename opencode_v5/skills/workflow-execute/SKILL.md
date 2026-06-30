---
name: workflow-execute
description: Model-invoked. The strict loop for implementing a single task. Loads automatically when writing code.
---

# Workflow Execute
**Triggered by:** The Generalist beginning implementation of a single task from `plan/tasks.md`.

## Procedure
1. **Claim:** Change the task status in `plan/tasks.md` from `[ ]` to `[>]` before touching any source code.
2. **Implement (YAGNI):** Write the simplest, most boring code that fulfills the requirement. Do not add future-proofing abstractions.
3. **Verify:** Run the appropriate test, linter, or script via the `bash` tool to ensure it works. 
4. **Complete:** Change the task status in `plan/tasks.md` from `[>]` to `[x]`. 
5. **Report:** Provide a terse bulleted list of changed files and verification results to the user.
