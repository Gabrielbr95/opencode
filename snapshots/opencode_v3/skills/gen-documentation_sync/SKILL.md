---
name: gen-documentation_sync
description: Review and update planning artifacts whenever code changes. Keep spec, architecture, tasks, and decisions consistent with reality.
---

# gen-documentation_sync

## When to load

Load after any implementation change that may have deviated from or extended the original plan, or when a review reveals documentation is out of sync with code.

## Files to Check

After any significant code change, review each of these if present:

| File | Check for |
|---|---|
| `spec.md` | Requirements that were changed, added, or dropped during implementation |
| `architecture.md` | Structural decisions that shifted — new modules, changed interfaces, dropped components |
| `tasks.md` | Tasks completed, blocked, or deferred — ensure checklist reflects reality |
| `decisions.md` | New decisions made during implementation that were not captured at planning time |

## Process

1. Read the completed task description in `tasks.md`.
2. Read the files that changed.
3. Compare against each planning artifact.
4. Flag divergences — do not silently update without noting what changed and why.
5. Propose specific amendments. Wait for approval before editing.

## What Counts as a Divergence

- A function or module exists that is not described in `architecture.md`
- A requirement in `spec.md` was not implemented or was implemented differently
- A decision was made during implementation (library choice, data format, error strategy) that is not captured in `decisions.md`
- `tasks.md` shows a task as incomplete when the code shows it is done, or vice versa

## What Does Not Need Updating

- Minor implementation details (variable names, internal function structure)
- Things that are obvious from reading the code
- Tasks that are in progress — only update when complete or blocked

## Output Format

```
Sync Check — Task N: <name>

spec.md: <in sync / divergence: description>
architecture.md: <in sync / divergence: description>
tasks.md: <in sync / divergence: description>
decisions.md: <in sync / new decision to capture: description>

Proposed amendments: <list, or "None">
```
