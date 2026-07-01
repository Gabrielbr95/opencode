---
name: tier-application
description: Model-invoked. Coding guidelines for Application tier. Loads when working on long-lived, multi-user software.
---

# Tier: Application
**Optimize for:** Maintainability, safety, and team scale.

## Engineering Rules
1. **Architecture:** Enforce strict separation of concerns. UI, business logic, and data layers must not bleed into each other.
2. **Testing First:** Write unit tests for core business logic. Code must be testable through clear interfaces.
3. **Defensive Programming:** Assume external APIs will fail, files will be missing, and inputs will be malformed. Handle all errors gracefully.
4. **Documentation:** Every non-obvious function must have a docstring. Every non-obvious decision needs a one-line comment.
5. **Type Safety:** Use Type Hints (`typing`) consistently across the codebase.
