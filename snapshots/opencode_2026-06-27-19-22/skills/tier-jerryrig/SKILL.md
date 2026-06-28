---
name: tier-jerryrig
description: >-
  Coding guidelines for the jerryrig tier. Use when the builder agent is
  working on a task whose tier is "jerryrig" in tasks.md. One-off throwaway
  scripts where speed of creation is the only priority.
---

# Tier: Jerryrig

Fast, throwaway, single-file solutions. Bruteforce, ugly, or unoptimized code is perfectly fine.

## Rules

1. Prefer a single, flat Python file runnable directly.
2. Ignore edge cases and deep error trapping unless explicitly flagged. Raise uncaught exceptions; do not write logging boilerplate.
3. Never create folders, tests, or abstractions (YAGNI to the extreme).
4. Hardcode values when it saves time. Comment only to mark what the user must change.
5. Ensure the code is free of syntax errors, typos, and invalid/missing imports before declaring completion — the human will run functional tests.
