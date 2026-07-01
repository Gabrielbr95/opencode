---
name: grill-me
description: User-invoked. Forces the agent to aggressively interview the user before any planning or coding begins.
disable-model-invocation: true
---

# Grill Me
**Triggered by:** The user manually calling `/grill-me`.

## Procedure
1. **Stop:** Do not write any code, do not write a plan, do not summarize.
2. **Interview:** Ask the user 1-2 highly targeted questions about the feature, edge cases, domain jargon, or missing requirements.
3. **Wait:** Wait for the user to answer.
4. **Repeat:** Continue asking questions one at a time until there is absolutely zero ambiguity about what needs to be built.
5. **Summarize:** Once complete, synthesize the domain jargon and decisions into `plan/decisions.md` (or propose doing so) to lock in the shared vocabulary.
