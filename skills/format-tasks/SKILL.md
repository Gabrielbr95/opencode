---
name: format-tasks
description: Model-invoked. The canonical schema for plan/tasks.md. Loads when writing or updating tasks.
---

# Format: tasks.md
**Purpose:** The bite-sized execution checklist. 

## Rules
1. The file has two levels: outcome-level slices, then sequential micro-tasks inside each slice.
2. Slices must describe meaningful user-visible or system-visible progress, not internal technical layers.
3. Tasks must be strictly sequential (top-to-bottom).
4. Tasks must be micro-scoped (approx 2-5 minutes of work each).
5. Every task must include verification criteria (how do we know it's done?).
6. Strict state symbols: `[ ]` (Pending), `[>]` (In Progress - strictly one at a time), `[x]` (Done), `[!]` (Failed/Blocked).

## Schema
Follow this exact Markdown structure:

```markdown
# Implementation Plan

## Slice 1: [Meaningful Outcome]
- [ ] 1. [Verb] [Target] (Verification: [What to check])
- [ ] 2. [Verb] [Target] (Verification: [What to check])

## Slice 2: [Meaningful Outcome]
- [ ] 3. [Verb] [Target] (Verification: [What to check])
```
