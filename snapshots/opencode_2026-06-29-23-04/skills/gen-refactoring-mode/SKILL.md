---
name: gen-refactoring-mode
description: Reduce complexity safely. Preserve behavior, prefer deletion, prefer functions over classes.
---

# gen-refactoring_mode

## When to load

Load when the goal is reducing complexity, not adding features. The refactoring is complete when the code is simpler and behavior is unchanged.

## Core Rule

**Preserve behavior.** A refactor that changes behavior is a bug, not a refactor.

## Process

1. **Establish a baseline** before touching anything
   - Identify how to verify the code still works after changes (tests, manual check, expected output)
   - If no verification method exists, create a minimal one first — even a quick manual test with known input/output
   - Note the current behavior explicitly: inputs, outputs, side effects

2. **Identify the target**
   - What specifically is complex? Name it.
   - What does "simpler" mean in this context? (fewer lines, fewer files, fewer dependencies, easier to read)

3. **Prefer these moves in order**:
   - **Delete** — unused code, dead branches, redundant comments, features no one uses
   - **Inline** — small functions that are only called once and add no clarity
   - **Flatten** — nested conditions that can be expressed as early returns
   - **Extract function** — only if a block is repeated or genuinely non-obvious
   - **Rename** — names that lie or mislead
   - **Move** — code that lives in the wrong module

4. **One move at a time** in isolated commits or checkpoints. Do not batch unrelated changes.

5. **Verify** after each move. Do not accumulate unverified changes.

## Prefer Functions Over Classes

Before creating or keeping a class, ask: does this have state that changes over its lifetime?
- No state: use a function or a module with functions.
- Shared state across calls: consider a simple dict or dataclass.
- Genuinely stateful lifecycle: a class may be warranted.

## Red Flags — Stop and Ask

- Refactoring that requires changing calling code outside the current scope
- Removing error handling "to simplify" — this usually makes failures silent
- Adding abstraction as part of the refactor (that's a redesign, not a refactor)
- Changes that make the code shorter but harder to understand

## Output Format

```
Refactoring target: <what is being simplified>
Baseline verification: <how behavior will be confirmed unchanged>
Moves planned:
1. <move type>: <what and why>
2. ...
Risk: <any behavior change risk to flag>
```
