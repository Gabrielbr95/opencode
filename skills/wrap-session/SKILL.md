---
name: wrap-session
description: User-invoked. Compacts the current session state into activeContext.md to survive 14-day offshore gaps.
disable-model-invocation: true
---

# Wrap Session
**Triggered by:** The user manually calling `/wrap-session`.

## Procedure
1. If the session materially changed implementation work or durable planning artifacts in a way that could mislead the next session, run `reconcile-work` first. Do not force a heavy reconciliation pass when the current state is already sufficiently clear.
2. Load `format-active-context`.
3. Re-read only the current project state, `plan/tasks.md`, the immediately relevant `plan/*` files, and recent discussion needed to write an honest baton. Do not reread broad durable context when the touched scope is already clear.
4. Write only the resume baton to `activeContext.md` using the canonical schema:
    - what was accomplished in this session,
    - the exact next step,
    - current blockers or open questions,
    - which files to read first on resume.
5. Do not store durable decisions, architecture, or vocabulary in `activeContext.md`; those belong in `plan/*`.
6. Keep the baton short, specific, and restart-oriented rather than a session transcript.
7. Overwrite `activeContext.md` with the new summary.
8. Inform the user that the session is wrapped and safe to close.
