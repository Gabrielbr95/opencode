---
name: grill-me
description: User-invoked. Interview the user one question at a time to stress-test a plan, decision, or idea before planning or coding begins.
disable-model-invocation: true
---

# Grill Me
**Triggered by:** The user manually calling `/grill-me`.

## Procedure
1. **Stop:** Do not write any code, do not write a plan, do not summarize.
2. **Look Up Facts First:** If a fact can be found by exploring the environment, project files, or available tools, look it up instead of asking the user.
3. **Ask for Decisions:** Ask one highly targeted question at a time about the plan, edge cases, domain jargon, tradeoffs, or missing decisions. For each question, provide your recommended answer to speed convergence.
4. **Wait:** Wait for the user to answer before asking the next question. Do not ask multiple questions at once.
5. **Stop at Sufficient Clarity:** Continue until there is shared understanding that is good enough for the current objective and Tier. Do not force exhaustive questioning when the remaining uncertainty can be handled cheaply during planning or execution.
6. **Confirmation Gate:** Do not act on the idea until the user confirms that shared understanding has been reached.
7. **Summarize:** Once complete, summarize the resolved terms and decisions, and propose documenting them only if they are durable enough to matter later.
