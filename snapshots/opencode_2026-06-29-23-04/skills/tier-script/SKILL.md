---
name: tier-script
description: >-
  Coding guidelines for the script tier. Use when the builder agent is working
  on a task whose tier is "script" in plan/tasks.md. Recurring automation scripts
  with reliability, clear logging, and YAGNI simplicity.
---

# Tier: Script

Highly reliable recurring automation. Easy to run, maintain, and troubleshoot.

## Rules

1. **YAGNI**: Avoid unnecessary abstractions, class architectures, or custom frameworks. Prefer flat, procedural code in a single Python file unless a modular split is clearly justified.
2. **CLI vs. Direct Config**: `argparse` is optional and context-dependent. For simple scripts run in static directories, use clear global variables at the top of the file so they are easy to edit. For scripts with variable inputs, use `argparse`.
3. **Logging & Output**:
   - `print()` for immediate user-facing feedback and console progression.
   - `logging` for background trace logs, error output, and debugging diagnostics.
4. **File Safety**: Defensively guard file/folder operations — check existence, verify destinations, warn before overwriting. Prevent accidental data loss.
5. **`--dry-run`**: Strongly preferred for any script that writes or deletes files.
6. Ask for confirmation before implementing complex edge cases or custom features not requested by the user.
7. No plugin systems, no dependency injection, no factories, no base classes.

## What to produce

A script the user can run immediately, modify in 5 minutes, and trust to tell them when something went wrong.

## What to skip

- Abstract architecture
- Reusable library design
- Plugin hooks
- Comprehensive test suites
- Anything that won't be needed in the next 6 months

## Logging Example

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("script.log"),
        logging.StreamHandler(),
    ]
)
log = logging.getLogger(__name__)

log.info("Processing %s", filepath)
log.error("Failed to parse %s: %s", filepath, e)
```
