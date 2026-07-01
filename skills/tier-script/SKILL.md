---
name: tier-script
description: Model-invoked. Coding guidelines for Script tier. Loads when working on recurring personal automation.
---

# Tier: Script
**Optimize for:** Simplicity and reliability for recurring personal use.

## Engineering Rules
1. **YAGNI (You Aren't Gonna Need It):** Keep it simple. Avoid complex OOP; prefer pure functions.
2. **Dependency Police:** Rely on the Python standard library as much as possible. Only add external dependencies if absolutely necessary.
3. **Loud Failures:** Fail fast and print clear, actionable error messages. No silent `except: pass`.
4. **Basic Logging:** Use the `logging` module instead of `print()` for critical path events.
5. **Configuration:** Parameterize inputs via CLI arguments (`argparse`) or simple `.env` files. Avoid hardcoding paths.
