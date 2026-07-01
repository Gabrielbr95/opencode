---
name: diagnose-bug
description: Model-invoked. Strict root-cause analysis loop for fixing bugs.
---

# Diagnose Bug
**Triggered by:** The user reporting a bug, stack trace, or unexpected behavior.

## Procedure
Do not guess the fix. Follow this strict loop:
1. **Reproduce:** Ask the user for steps to reproduce, or write a quick test script to reproduce it locally.
2. **Minimize:** Isolate the failing component. Strip away unrelated code.
3. **Hypothesize:** State your assumption about *why* it fails.
4. **Instrument:** Add `print()` statements, logging, or use the `bash` tool to gather evidence proving or disproving the hypothesis.
5. **Fix & Verify:** Apply the fix only *after* evidence confirms the root cause. Run the reproduction script to verify it is fixed.
6. **Repeat with Discipline:** If the bug is not fixed, repeat steps 3-5. Stop after 3 total hypothesis/instrument/fix loops and return the task as blocked instead of continuing to guess.
