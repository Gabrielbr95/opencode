---
name: gen-application
description: Apply application tier rules. Long-lived small-team software — structure, error handling, maintainability, tests.
---

# gen-application

## When to load

Load when tier is `application`. Other people may use or maintain this. It will live for months or years.

## Rules

**Structure**
- Follow the folder structure defined in `architecture.md` exactly.
- Separate configuration from code — use a config file or environment variables, not hardcoded values.
- Separate concerns into modules. No 500-line single files.

**Reliability**
- Handle and recover from user mistakes gracefully. Never show a raw Python traceback to an end user.
- Write clear, user-friendly error messages that explain what went wrong and what to do about it.
- Log at appropriate levels: DEBUG for internal state, INFO for operations, WARNING for recoverable issues, ERROR for failures.

**Testing**
- Test important behavior — the things that break silently or have non-obvious edge cases.
- Do not pursue coverage metrics. Prefer a few valuable tests over many brittle ones.
- Use `pytest`. Name tests clearly: `test_<what>_<condition>_<expected>`.

**Documentation**
- Module-level docstring explaining purpose.
- Function docstrings for public interfaces.
- `README.md` covering: purpose, setup, workflow, major decisions.

**Dependencies**
- Every dependency must justify its existence.
- Prefer stdlib over third-party where the tradeoff is reasonable.
- Pin versions in `requirements.txt`.

## Forbidden unless justified

- Microservices or multi-process architectures for single-user tools
- Plugin frameworks
- Dependency injection frameworks
- Abstract base classes for things that have only one implementation
- Excessive abstraction layers

State the justification explicitly if any of the above are proposed.

## What to produce

Working code that a new maintainer can understand, run, and modify without asking for help.
