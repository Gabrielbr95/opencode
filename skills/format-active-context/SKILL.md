---
name: format-active-context
description: Model-invoked. The canonical schema for activeContext.md. Loads when writing or updating the resume baton.
---

# Format: activeContext.md
**Purpose:** A short resume baton for the next session. This file is ephemeral. Durable decisions and architecture belong in `plan/*`.

## Rules
1. Keep it short enough to read in under 2 minutes.
2. Write only the current resume state, not the full project history.
3. Reference durable files instead of duplicating their contents.
4. Be explicit about the next action, including file paths when possible.

## Schema
Follow this exact Markdown structure:

```markdown
# Active Context

## Resume Here
- **Tier:** [Jerryrig | POC | Script | Application]
- **Current Slice:** [Slice name or `N/A`]
- **Current Task:** [Task number/text or `N/A`]
- **Next Action:** [Exact next step]

## Completed This Session
- [Short bullet]

## Blockers / Open Questions
- [Short bullet or `None`]

## Read These First
- `path/to/file`: [Why it matters on resume]
```
