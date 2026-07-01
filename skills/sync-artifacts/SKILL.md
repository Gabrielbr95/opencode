---
name: sync-artifacts
description: Model-invoked. Updates markdown planning files to match reality after code changes.
---

# Sync Artifacts
**Triggered by:** A coding session ending, or significant divergence between the code and the plan.

## Procedure
1. Compare the current codebase state against the durable planning artifacts: `plan/spec.md`, `plan/architecture.md` (if present), and `plan/decisions.md`.
2. Identify undocumented dependencies, changed file paths, changed task outcomes, or altered architectural decisions.
3. Update the durable markdown files to reflect the current reality of the codebase.
4. Keep `activeContext.md` separate; it is a resume baton, not a durable design artifact.
5. **Rule:** Planning artifacts must never lie. They are the source of truth for the next session.
