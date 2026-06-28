---
name: tier-script
description: >-
  Coding guidelines for the script tier. Use when the builder agent is working
  on a task whose tier is "script" in tasks.md. Recurring automation scripts
  with reliability, clear logging, and YAGNI simplicity.
---

# Tier: Script

Highly reliable recurring automation. Easy to run, maintain, and troubleshoot.

## Rules

1. **YAGNI**: Avoid unnecessary abstractions, class architectures, or custom frameworks. Prefer flat, procedural code in a single Python file unless a modular split is clearly justified.
2. **CLI vs. Direct Config**: `argparse` is optional and context-dependent. For simple scripts run in static directories, use clear global variables at the top of the file so they are easy to edit.
3. **Logging & Output**:
   - `print()` for immediate user-facing feedback and console progression.
   - `logging` for background trace logs, error output, and debugging diagnostics.
4. **File Safety**: Defensively guard file/folder operations — check existence, verify destinations, warn before overwriting. Prevent accidental data loss.
5. Ask for confirmation before implementing complex edge cases or custom features not requested by the user.
