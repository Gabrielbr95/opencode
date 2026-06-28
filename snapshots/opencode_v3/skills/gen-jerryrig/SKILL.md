---
name: gen-jerryrig
description: Apply jerryrig tier rules. Speed over everything. Run today, discard tomorrow.
---

# gen-jerryrig

## When to load

Load when tier is `jerryrig`. Overrides all quality defaults.

## Rules

- Single file. No packages, no modules, no imports beyond stdlib and one or two obvious deps.
- Hardcoded values are fine. No config files.
- No tests. No logging. No error handling beyond bare `raise` or letting Python crash.
- Duplicate code is fine. Abstraction is not needed.
- Manual steps in the instructions are fine.
- No docstrings required.

## What to produce

The minimum code that runs and gives the right answer today.

State at the end:
- What file was created
- Exact command to run it
- Expected output

## What to skip

Everything else. This code may be thrown away tomorrow.

## Example

Requirement: "I need to count how many rows in this CSV have status = OPEN"

```python
import csv
count = 0
with open("workorders.csv") as f:
    for row in csv.DictReader(f):
        if row["status"] == "OPEN":
            count += 1
print(count)
```

Run: `python count_open.py`
Expected: prints an integer.

That is the complete deliverable.
