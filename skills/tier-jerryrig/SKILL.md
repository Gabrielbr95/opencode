---
name: tier-jerryrig
description: Model-invoked. Coding guidelines for Jerryrig tier. Loads when working on one-off throwaway changes.
---

# Tier: Jerryrig
**Optimize for:** Speed, obvious output, and minimal ceremony.

## Engineering Rules
1. **No Planning Files:** Do not create `plan/*` artifacts unless the user explicitly asks for them.
2. **Prefer Directness:** Use the smallest possible change, script, or command that solves today's problem.
3. **Verify Once, Clearly:** Run the thing or produce visible output so success or failure is obvious.
4. **Do Not Pretend It Is Durable:** No fake abstractions, architecture, or polish for hypothetical future reuse.
5. **Escalate When It Grows:** If the work stops being trivial, pause and reclassify it as POC or Script.
