---
name: tier-poc
description: Model-invoked. Coding guidelines for Proof-of-Concept tier. Loads when working on a POC project.
---

# Tier: Proof of Concept (POC)
**Optimize for:** Learning. Answer "Can this be done?" as fast as possible.

## Engineering Rules
1. **Throwaway Code:** Expect this code to be deleted.
2. **Speed over Safety:** Hardcode variables, skip automated tests, ignore edge cases unless they block the immediate happy path.
3. **No Abstractions:** Put everything in one or two files. Do not build classes or complex architectures.
4. **Console Output:** Use simple `print()` statements to verify behavior. Do not set up formal logging.
