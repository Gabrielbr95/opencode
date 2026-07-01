---
name: wrap-session
description: User-invoked. Compacts the current session state into activeContext.md to survive 14-day offshore gaps.
disable-model-invocation: true
---

# Wrap Session
**Triggered by:** The user manually calling `/wrap-session`.

## Procedure
1. If the session changed code or planning artifacts, run `converge-work` and `sync-artifacts` first so durable files reflect reality.
2. Load `format-active-context`.
3. Read the current project state, `plan/tasks.md`, relevant `plan/*` files, and any recent discussions.
4. Write only the resume baton to `activeContext.md` using the canonical schema:
   - what was accomplished in this session,
   - the exact next step,
   - current blockers or open questions,
   - which files to read first on resume.
5. Do not store durable decisions, architecture, or vocabulary in `activeContext.md`; those belong in `plan/*`.
6. Overwrite `activeContext.md` with the new summary.
7. Inform the user that the session is wrapped and safe to close.
