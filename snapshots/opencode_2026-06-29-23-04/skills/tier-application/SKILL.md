---
name: tier-application
description: >-
  Coding guidelines for the application tier. Use when the builder agent is
  working on a task whose tier is "application" in plan/tasks.md. Long-lived team
  software with clean design, docs, error handling, and tests.
---

# Tier: Application

Long-lived software intended for repeated team use. Clean design, usability, comprehensive docstrings, and robust error resilience.

## Rules

1. **Architecture**: Strictly align with `plan/architecture.md` and `plan/spec.md`. Follow the folder structure exactly. Separate concerns into modules — no 500-line single files. Keep folder hierarchies **flat**; avoid unnecessary nesting or deep enterprise layer isolation.
2. **Configuration**: Separate configuration variables and constants from core implementation logic. Use a config file or environment variables, not hardcoded values.
3. **Error Resilience**: Handle and recover from common user mistakes or input corruptions gracefully. Write clear, user-friendly error messages that explain what went wrong and what to do about it. Never show a raw Python traceback to an end user.
4. **Logging**: Log at appropriate levels: DEBUG for internal state, INFO for operations, WARNING for recoverable issues, ERROR for failures.
5. **Tests**: Test important behavior — the things that break silently or have non-obvious edge cases. Do not pursue coverage metrics. Prefer a few valuable tests over many brittle ones. Use `pytest`. Name tests clearly: `test_<what>_<condition>_<expected>`.
6. **Documentation**: Module-level docstring explaining purpose. Function docstrings for public interfaces. Do not generate `README.md`, `requirements.txt`, `pyproject.toml` from scratch unless explicitly requested. Do update existing dependency files and documentation to reflect implementation changes.
7. **Dependencies**: Every dependency must justify its existence. Prefer stdlib over third-party where the tradeoff is reasonable. Pin versions in `requirements.txt`.

## Forbidden unless justified

- Microservices or multi-process architectures for single-user tools
- Plugin frameworks
- Dependency injection frameworks
- Abstract base classes for things with only one implementation
- Excessive abstraction layers

State the justification explicitly if any of the above are proposed.

## What to produce

Working code that a new maintainer can understand, run, and modify without asking for help.
