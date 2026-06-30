---
name: sync-artifacts
description: Model-invoked. Updates markdown planning files to match reality after code changes.
---

# Sync Artifacts
**Triggered by:** A coding session ending, or significant divergence between the code and the plan.

## Procedure
1. Compare the current codebase state against `plan/spec.md`, `plan/architecture.md` (if Application tier), and `plan/decisions.md`.
2. Identify undocumented dependencies, changed file paths, or altered architectural decisions.
3. Update the markdown files to reflect the current reality of the codebase.
4. **Rule:** Planning artifacts must never lie. They are the source of truth for the next session.
