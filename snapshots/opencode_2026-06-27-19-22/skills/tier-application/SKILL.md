---
name: tier-application
description: >-
  Coding guidelines for the application tier. Use when the builder agent is
  working on a task whose tier is "application" in tasks.md. Long-lived team
  software with clean design, docs, error handling, and tests.
---

# Tier: Application

Long-lived software intended for repeated team use. Clean design, usability, comprehensive docstrings, and robust error resilience.

## Rules

1. **Architecture**: Strictly align with `architecture.md` and `spec.md`. Organize code using modular but **flat** folder hierarchies. Avoid unnecessary nesting, complex design pattern boilerplate, or deep enterprise layer isolation.
2. **Configuration**: Separate configuration variables and constants from the core implementation logic.
3. **Error Resilience**: Anticipate and handle common user mistakes or input file corruptions gracefully. Write clear, descriptive, forgiving user-facing error messages instead of raw tracebacks.
4. **Tests**: Add lightweight unit/integration tests for primary functional blocks. Do not over-test — focus on critical paths and edge cases.
5. **Documentation**: Do not generate `README.md`, `requirements.txt`, `pyproject.toml` from scratch unless explicitly requested. Do update existing dependency files and documentation to reflect implementation changes.
