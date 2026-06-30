---
name: format-architecture-md
description: >-
  Canonical format for plan/architecture.md — the technical design document.
  Use when creating or reading plan/architecture.md. Produced by the planner
  for application-tier projects only. Read by the builder and antagonist.
---

# architecture.md Format

The architecture defines *how* the system is built. It translates the spec into concrete technical decisions. Only produced for **application-tier** projects.

## Structure

```markdown
# Architecture: <Project Name>

## Overview
[1-2 sentences: the high-level approach and primary technology choices.]

## Stack
| Layer | Choice | Why |
|-------|--------|-----|
| Language | Python 3.12 | [1-line justification] |
| Framework | Streamlit | [1-line justification] |
| Data | pandas + CSV | [1-line justification] |
| ... | ... | ... |

## Directory Layout
```
project/
├── main.py            # entrypoint
├── config.py          # constants and configuration
├── core/              # business logic
│   ├── parser.py
│   └── processor.py
├── ui/                # interface layer (if any)
└── tests/
    └── test_core.py
```

## Components
### <Component Name>
- **Responsibility**: [What it does, in one sentence.]
- **Interfaces**: [What it exposes — functions, classes, CLI commands, API endpoints.]
- **Dependencies**: [What it imports or calls.]

### <Component Name>
- ...

## Data Flow
[Describe the primary data path through the system: input → processing → output. Use a numbered list or simple diagram.]

## Key Decisions
- **<Decision>**: <Rationale and rejected alternative.>
- ...
```

## Rules

1. Keep the directory layout **flat**. Avoid nesting beyond 2 levels unless clearly justified.
2. Every stack choice needs a "why" and ideally a rejected alternative.
3. Components should map to files or small modules, not abstract layers.
4. Data flow describes the *runtime* path, not the build/deploy process.
5. Key decisions capture choices the builder needs to respect but might not guess — "why X instead of Y."
6. Do not duplicate plan/spec.md content (purpose, scope, constraints). Reference it.
