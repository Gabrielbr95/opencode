---
name: tier-script
description: Model-invoked. Coding guidelines for Script tier. Loads when working on recurring personal automation.
---

# Tier: Script
**Optimize for:** Simplicity and reliability for recurring personal use.

## Engineering Rules
1. **Keep It Simple:** Use the lightest boring structure that preserves reliability for recurring use. Prefer simple functions and straightforward flow over heavy architecture.
2. **Be Careful With Dependencies:** Prefer the Python standard library when it is good enough. Add dependencies only when they clearly reduce effort or improve reliability.
3. **Loud Failures:** Fail fast and surface clear, actionable error messages. No silent `except: pass`.
4. **Use Right-Sized Observability:** Add enough output, logging, or status reporting to make recurring runs debuggable. Do not force formal logging when simple output is sufficient.
5. **Parameterize When It Helps Reuse:** Avoid baking in paths or inputs that make the script fragile, but do not force a full configuration layer when a simple argument or constant is enough.
