---
name: format-decisions
description: Model-invoked. The canonical schema for plan/decisions.md. Loads when logging engineering choices.
---

# Format: decisions.md
**Purpose:** To prevent the agent from forgetting *why* something was done after a 14-day gap. 

## Rules
1. Log decisions that materially affect the architecture, dependencies, or user workflow.
2. If a decision is changed later, do not delete the old one. Mark it as `Superseded by [New ID]`.

## Schema
Follow this exact Markdown structure for each entry:

```markdown
# Decision Log

## [001] [Short Title]
- **Date:** YYYY-MM-DD
- **Context:** [What is the problem we are solving?]
- **Options Considered:** [Option A vs Option B]
- **Decision:** [What we chose]
- **Rationale:** [Why we chose it over the alternatives]
```
