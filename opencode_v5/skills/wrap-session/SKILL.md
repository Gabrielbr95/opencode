---
name: wrap-session
description: User-invoked. Compacts the current session state into activeContext.md to survive 14-day offshore gaps.
disable-model-invocation: true
---

# Wrap Session
**Triggered by:** The user manually calling `/wrap-session`.

## Procedure
1. Read the current project state, `plan/tasks.md`, and any recent discussions.
2. Generate a highly condensed summary of:
   - What was accomplished in this session.
   - What the exact next step is (be specific about file paths and functions).
   - Any current blockers or open questions.
   - Any new jargon or domain rules established.
3. Overwrite `activeContext.md` with this summary.
4. Inform the user that the session is wrapped and safe to close.
