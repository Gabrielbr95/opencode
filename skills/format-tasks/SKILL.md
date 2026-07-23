---
name: format-tasks
description: Model-invoked. The canonical schema for plan/tasks.md. Loads when writing or updating tasks.
---

# Format: tasks.md
**Purpose:** The execution plan: visible full-path outline plus actionable next steps.

## Rules
1. The file has two levels: outcome-level slices, then sequential tasks inside each slice.
2. Slices must describe meaningful user-visible or system-visible progress, not internal technical layers.
3. Tasks must be strictly sequential (top-to-bottom).
4. The file should show the outline of the full plan, but only the next slice or user-requested slices need fine detail.
5. Task granularity must match the work:
   - implementation-heavy work may use finer-grained tasks
   - planning/docs work may use coarser outcome-oriented tasks
   - avoid forced micro-tasking when it adds ceremony without reducing risk
6. Every task must include verification criteria, but verification should be proportional to the work.
   - implementation tasks may use tests, runs, or concrete behavior checks
   - planning/docs tasks may use lightweight consistency, scope, or stale-reference checks
7. Leave room for refinement: later slices may stay broader until they become the active work, unless the user explicitly asks for a fully detailed plan up front.
8. Strict state symbols: `[ ]` (Pending), `[>]` (In Progress), `[x]` (Done), `[!]` (Failed/Blocked).

## Schema
Use this canonical Markdown structure when creating or substantially rewriting `plan/tasks.md`:

```markdown
# Implementation Plan

## Slice 1: [Meaningful Outcome]
- [ ] 1. [Verb] [Target] (Verification: [What to check])
- [ ] 2. [Verb] [Target] (Verification: [What to check])

## Slice 2: [Meaningful Outcome]
- [ ] 3. [Broader next step or placeholder for later refinement] (Verification: [What to confirm when this slice becomes active])
```
