---
name: gen-script
description: Apply script tier rules. Recurring personal automation — single file, reliable, YAGNI.
---

# gen-script

## When to load

Load when tier is `script`. The user runs and maintains this themselves, probably repeatedly.

## Rules

- Single Python file unless a split is clearly justified — state the reason if splitting.
- `argparse` for all runtime parameters. No hardcoded paths or values the user might change.
- `logging` module, not `print`. Use `logging.basicConfig(level=logging.INFO)` as default.
- Raise exceptions rather than swallowing them silently. Let failures be visible.
- Defensive file and folder operations: check existence before writing, never overwrite silently without a flag.
- Handle realistic failures only — what will actually happen in this user's environment. Skip theoretical edge cases.
- No plugin systems, no dependency injection, no factories, no base classes for extensibility.
- No tests required, but a `--dry-run` flag is strongly preferred for any script that writes or deletes files.

## What to produce

A script the user can run immediately, modify in 5 minutes, and trust to tell them when something went wrong.

Conclude with:
- What file was created
- Exact command to run it (with example flags)
- How to verify it worked

## What to skip

- Abstract architecture
- Reusable library design
- Plugin hooks
- Comprehensive test suites
- Anything that won't be needed in the next 6 months

## Example of good logging

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
