---
name: gen-debug-mode
description: Apply structured root cause analysis. Gather evidence first, identify cause, then propose fixes.
---

# gen-debug_mode

## When to load

Load when diagnosing a bug, unexpected behavior, or system failure. Do not load when the cause is already known — this skill is for investigation, not implementation.

## Core Rule

**Never apply speculative fixes.** Every proposed fix must be backed by evidence gathered during investigation.

## Process

1. **Identify the symptom**
   - What exactly is happening? (error message, wrong output, no output, crash)
   - When does it happen? (always, intermittently, under specific conditions)
   - When did it start? (first occurrence, after a change, always been there)

2. **Gather evidence**
   - Read the full error message and traceback — do not skim
   - Identify the exact line where failure occurs
   - Read the function and the calling code
   - Check what inputs reached the failing code
   - Check what state the system was in (files present, environment variables, previous operations)

3. **Identify contributing factors**
   - What conditions must be true for the bug to occur?
   - What changed recently (code, data, environment) that could have caused this?
   - Is the bug in this code, a dependency, or the environment?

4. **Identify root cause**
   - The root cause is the earliest point in the chain where behavior deviated from expected.
   - State the root cause as a falsifiable claim: "The bug occurs because X, which causes Y."

5. **Propose fix**
   - Only after root cause is identified
   - State what the fix changes and why it addresses the root cause
   - Note any side effects or related areas to retest

## Output Format

```
Symptom: <what is happening>
Evidence:
- <observation 1>
- <observation 2>
Contributing factors: <conditions required for bug to occur>
Root cause: <earliest deviation from expected behavior>
Proposed fix: <what to change and why>
Retest: <how to confirm the fix worked>
```

## Anti-patterns

- Changing multiple things at once and hoping one works
- Fixing the symptom without identifying the root cause
- Assuming the bug is in the most recently changed code
- Applying a fix before reproducing the bug
