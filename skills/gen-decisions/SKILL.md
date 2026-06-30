---
name: gen-decisions
description: Load when reading, writing, or reviewing plan/decisions.md. Defines the decision log format, when to create entries, and how to handle superseded decisions.
---

# gen-decisions

## When to load

Load when:
- About to record a new engineering decision
- Reviewing whether a decision has already been made
- Checking whether an implementation conflicts with a recorded decision
- Superseding an existing decision

## Purpose

`plan/decisions.md` is the project's persistent engineering memory. LLMs and agents are stateless — every session starts blank. This file ensures that reasoning about architecture, technology choices, and tradeoffs is never lost between sessions or model swaps.

**Rule**: If a design choice is important enough that it might be reconsidered in the future, it must exist in `plan/decisions.md`.

## File Rules

- One file per project: `plan/decisions.md`
- Append-only — never rewrite or delete past entries
- Chronological — oldest at top, newest at bottom
- New entries are always appended at the bottom

## Entry Format

```markdown
## Decision NNN: <Short Title>

**Date**: YYYY-MM-DD

**Context**
Why this decision was needed. What situation or constraint forced the choice.

**Decision**
What was decided. State it plainly.

**Reasoning**
Why this option over the alternatives. What evidence or logic supported it.

**Tradeoffs**
What was sacrificed or made harder by this choice.

**Consequences**
What this decision affects downstream — architecture, future choices, implementation constraints.

**Status**: Active
```

## When to Create a Decision

**Create an entry when:**
- Choosing between technologies or libraries
- Defining system architecture or folder structure
- Introducing or deliberately rejecting an abstraction
- Making a complexity tradeoff (e.g. "no ORM because...")
- Selecting a long-term pattern that other decisions will build on
- Rejecting an approach that will likely be reconsidered

**Do not create an entry for:**
- Trivial code changes
- Formatting or style choices
- Minor refactors with no structural impact
- Local implementation details that don't affect the rest of the system

## Superseding a Decision

When a previous decision becomes obsolete:

1. **Do not delete or edit the old entry.**
2. Change its status line to: `**Status**: Superseded by Decision NNN`
3. Append a new entry at the bottom referencing the old one.

New entry format when superseding:

```markdown
## Decision NNN: <Short Title> (Supersedes Decision MMM)

**Date**: YYYY-MM-DD

**Context**
Why the previous decision is no longer valid. What changed.

**Decision**
What is now decided instead.

**Reasoning**
Why the change is justified now.

**Tradeoffs**
What is sacrificed by changing course.

**Consequences**
What must change in the system as a result.

**Status**: Active
```

## Example

```markdown
## Decision 001: Use SQLite instead of PostgreSQL

**Date**: 2026-06-25

**Context**
The application needs persistent storage. The target machine is a corporate Windows laptop
with no admin privileges. Installing and managing a PostgreSQL server is not feasible.

**Decision**
Use SQLite via Python's stdlib sqlite3 module. Single .db file, no server process.

**Reasoning**
SQLite installs with Python — no additional setup. Sufficient for <10 concurrent users.
The .db file is easy to back up and move. No external service dependency.

**Tradeoffs**
Write concurrency is limited by SQLite's single-writer lock. Not suitable if usage grows
beyond the immediate team or if write frequency increases significantly.

**Consequences**
All queries use sqlite3 directly. No ORM. Connection management handled in database.py.
Migration path to PostgreSQL would require rewriting database.py and testing queries.

**Status**: Active
```
