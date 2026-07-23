# Active Context

## Resume Here
- **Tier:** POC
- **Current Slice:** Slice 21: Workflow improvement cycle framing
- **Current Task:** 38 deferred; slices 20–21 complete
- **Next Action:** Start the next clean session by reading `plan/tasks.md`, `plan/permission-policy.md`, and `workflow-improvement-cycle.md`, then decide whether to (a) test/adjust the new permission model in real use, or (b) revisit deferred task `38` only if repeated workflow-improvement passes show a dedicated maintenance skill is now justified.

## Completed This Session
- Completed the deferred operational polish backlog (`46`–`51`) and committed it as `ee5dc31` — `refactor: polish deferred operational workflow`.
- Audited agent permissions against the research-backed control model.
- Added a durable permission map in `plan/permission-policy.md`.
- Tightened the enforcement baseline in `opencode.jsonc` and narrowed bash permissions for:
  - `agents/generalist.md`
  - `agents/coder.md`
  - `agents/reviewer.md`
- Committed the permission hardening slice as `671c394` — `refactor: harden agent permission model`.
- Added `workflow-improvement-cycle.md` as a top-level operational playbook that separates:
  - charter (`ai-workflow-improvement.md`)
  - recurring cycle (`workflow-improvement-cycle.md`)
  - still-deferred future automation (`38`)

## Blockers / Open Questions
- No hard blocker.
- Main open question: is the current permission model low-friction enough in real use, especially for Generalist git workflow and Coder test/implementation work?
- Deferred design question: should task `38` stay deferred permanently, become a user-invoked command first, or later graduate into a dedicated skill after more repeated real cycles?

## Read These First
- `plan/tasks.md`: Shows slices 20–21 completed and task `38` still deferred.
- `plan/permission-policy.md`: Current human-readable source of truth for the intended allow / ask / deny model and known enforcement limits.
- `workflow-improvement-cycle.md`: New operational playbook for recurring workflow-improvement passes.
- `opencode.jsonc`: Current global permission baseline (`external_directory: ask`).
- `agents/generalist.md`, `agents/coder.md`, `agents/reviewer.md`: Read together if the next session tests or refines the hardened permission model.
