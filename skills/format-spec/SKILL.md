---
name: format-spec
description: Model-invoked. The canonical schema for plan/spec.md. Loads only when writing the spec.
---

# Format: spec.md
**Purpose:** Defines *What* we are building and *Why*.

## Schema
Follow this exact Markdown structure:

```markdown
# Specification

## Objective
[1-2 sentences explaining the goal of the project]

## Core Requirements
- [Requirement 1]
- [Requirement 2]

## Out of Scope (Crucial)
- [Explicitly state what we are NOT building to enforce YAGNI]

## User Interaction
[How the user will run or interact with the system]
```
