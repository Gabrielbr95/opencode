---
name: format-tasks
description: Model-invoked. The canonical schema for plan/tasks.md. Loads when writing or updating tasks.
---

# Format: tasks.md
**Purpose:** The bite-sized execution checklist. 

## Rules
1. Tasks must be strictly sequential (top-to-bottom).
2. Tasks must be micro-scoped (approx 2-5 minutes of work each).
3. Every task must include verification criteria (how do we know it's done?).
4. Strict state symbols: `[ ]` (Pending), `[>]` (In Progress - strictly one at a time), `[x]` (Done), `[!]` (Failed/Blocked).

## Schema
Follow this exact Markdown structure:

```markdown
# Implementation Plan

## Phase 1: [Phase Name]
- [ ] 1. [Verb] [Target] (Verification: [What to check])
- [ ] 2. [Verb] [Target] (Verification: [What to check])
```
