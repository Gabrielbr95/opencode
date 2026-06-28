---
name: format-spec-md
description: >-
  Canonical format for spec.md — the project specification. Use when creating
  or reading spec.md. Produced by the planner for poc, script, and application
  tiers. Read by the builder, architect, and reviewer for context.
---

# spec.md Format

The spec defines *what* the project does and *why*, without prescribing *how*. It is the contract between the planner and the builder.

## Structure

```markdown
# <Project Name>

## Purpose
[1-2 sentences: what problem this solves and for whom.]

## Scope
### In Scope
- [Concrete deliverable or behavior]
- [...]

### Out of Scope
- [Explicitly excluded feature or behavior]
- [...]

## Inputs & Outputs
- **Input**: [What the system receives — files, user input, API data, sensor readings, etc.]
- **Output**: [What the system produces — files, reports, UI, transformed data, etc.]

## Constraints
- [Technical, environmental, or domain constraints: OS, hardware, file formats, performance targets, etc.]

## Success Criteria
- [Measurable, verifiable conditions that define "done" for the whole project.]

## Assumptions
- [Things assumed true that, if false, would change the design.]
```

## Rules

1. Every section is required. Use "None" if a section genuinely has no content.
2. Scope boundaries must be explicit. If something is ambiguous, put it in Out of Scope and note it as a question in `tasks.md` blockers.
3. Success criteria must be **falsifiable** — same standard as task acceptance criteria.
4. Assumptions are first-class. The architect audits these; the builder should flag when an assumption breaks during implementation.
5. Do not include implementation details (library choices, folder structures, class designs). Those belong in `architecture.md`.
