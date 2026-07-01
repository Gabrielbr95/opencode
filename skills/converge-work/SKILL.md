---
name: converge-work
description: Model-invoked. Reconcile code, tasks, and durable planning artifacts before declaring a task, slice, or feature done.
---

# Converge Work
**Triggered by:** A task, slice, or feature appearing complete, or before wrapping a session with meaningful changes.

## Procedure
1. **Skip Jerryrig:** If the tier is Jerryrig, skip this skill.
2. **Read the Durable Truth:** Read `plan/tasks.md`, `plan/spec.md`, `plan/decisions.md`, and `plan/architecture.md` if it exists.
3. **Compare Against Reality:** Check whether the implemented code, changed files, and verification results actually match the plan.
4. **Surface Drift:** If the implementation introduced scope changes, new dependencies, missing edge cases, or undocumented behavior, do not ignore it.
5. **Update the Backlog:** Append any newly discovered work to `plan/tasks.md` as new `[ ]` micro-tasks under the correct slice. Do not silently absorb extra work into a completed task.
6. **Sync Durable Artifacts:** If the code intentionally changed the design or workflow, update the durable artifacts so they match reality.
7. **Declare Status Honestly:** Only call the work complete when code, tasks, and durable artifacts all agree.
