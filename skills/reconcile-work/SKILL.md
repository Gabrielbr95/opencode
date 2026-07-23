---
name: reconcile-work
description: Model-invoked. Reconcile completed implementation work with tasks and durable planning artifacts before declaring a task, slice, feature, or session state complete.
---

# Reconcile Work
**Triggered by:** Completed implementation work, a slice or feature boundary, or before wrapping a session with meaningful implementation changes.

## Procedure
1. **Skip Jerryrig:** If the tier is Jerryrig, skip this skill.
2. **Start Delta-First:** Begin with the claimed task, touched files, verification results, and immediately relevant durable artifacts. Do not reread broad durable context unless the delta suggests broader drift.
3. **Compare Against Reality:** Check whether the implemented code, changed files, and verification results actually match the claimed scope and the relevant plan.
4. **Escalate Only If Needed:** Expand to broader rereads only when uncertainty, contradiction, missing context, or cross-artifact drift appears.
5. **Surface Drift:** If the implementation introduced scope changes, new dependencies, missing edge cases, undocumented behavior, or changed workflow assumptions, do not ignore it.
6. **Update the Backlog:** Add newly discovered work to `plan/tasks.md` under the correct slice. Do not silently absorb extra work into a completed task.
7. **Update Durable Artifacts:** Update only the durable artifacts affected by the change: `plan/spec.md`, `plan/decisions.md`, and `plan/architecture.md` if present. Keep `activeContext.md` separate; it is a resume baton, not a durable design artifact.
8. **Use Meaningful Boundaries:** Full reconciliation is expected mainly at task completion when durable truth changed materially, slice completion, feature completion, or session wrap. Do not treat every small change as a mandatory full-project reconciliation event.
9. **Declare Status Honestly:** Only call the work complete when the implementation, tasks, and affected durable artifacts agree at the relevant boundary.

## Rule
Planning artifacts must never lie, but they do not all need immediate full rereads after every micro-step.
