---
name: format-architecture
description: Model-invoked. The canonical schema for plan/architecture.md. Loads only when writing architecture.
---

# Format: architecture.md
**Purpose:** Defines *How* we are building it. (Used primarily for Application tier).

## Schema
Follow this exact Markdown structure:

```markdown
# Architecture

## System Context
[High-level overview of how the system fits together]

## Data Models / State
[Description of primary data structures, databases, or state management]

## Component Hierarchy
- `directory/`
  - `file.py`: [Purpose of file]

## Third-Party Dependencies
- `[Library Name]`: [1-line justification for why it was chosen over stdlib]
```
