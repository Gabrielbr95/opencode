# Agent Architectures

## Summary
- Agent architecture is the structure around an LLM that lets it plan, use tools, observe results, manage state, and iterate over multiple steps.
- The durable pattern across sources is not “one giant smart prompt,” but a controlled loop that combines the model with tools, retrieval, memory, and explicit stopping conditions.
- A recurring recommendation is to start with the simplest workable structure and only add autonomy when the task actually needs it.

## Motivation
- This repository needs a clean way to distinguish simple workflows from genuinely agentic systems.
- Architecture choices affect cost, debuggability, safety, and how much of the workflow should live in prompts versus code or skills.

## Problem Statement
- Single-shot prompting breaks down when work requires multiple dependent steps, tool use, external information, retries, or verification.
- The architecture problem is deciding how much planning, tool access, memory, and control logic to add without turning the system into an opaque mess.

## Key Concepts
- Workflow vs agent
- Planning
- Tool use
- Memory
- Grounding through observations
- Reflection / evaluation loops
- Termination conditions
- Single-agent vs multi-agent coordination

## Principles vs Implementations
### Principles
- Prefer the simplest viable control structure.
- Separate planning, execution, retrieval, and evaluation when that improves clarity.
- Ground decisions in external observations instead of internal guesswork.
- Bound autonomy with stop conditions and checkpoints.
- Treat tool interfaces as part of the architecture, not as an afterthought.

### Implementations / Examples
- Prompt chaining
- Routing
- Parallelization / voting
- Orchestrator-workers
- Evaluator-optimizer loops
- ReAct
- Toolformer
- Multi-agent role-based systems

## Design Patterns
- **Prompt chaining**: fixed sequence of steps for predictable tasks.
- **Routing**: classify first, then send to the right specialist flow.
- **Parallel workers**: independent attempts or sections with later aggregation.
- **Orchestrator-workers**: a planner delegates dynamic subtasks to workers.
- **Evaluator-optimizer**: generate, critique, revise.
- **ReAct loop**: interleave reasoning, action, and observation.

## Advantages
- Better fit for multi-step work.
- Better grounding when tools or retrieval are used.
- More explicit failure points for debugging.
- More flexible than single-call prompting for open-ended tasks.

## Disadvantages
- Higher latency and token cost.
- More moving parts and more failure modes.
- Harder to test than a fixed workflow.
- Poorly bounded autonomy can create runaway loops or unsafe behavior.

## Tradeoffs
- **Workflow vs agent**: workflows are predictable; agents are flexible.
- **Transparency vs token cost**: explicit plans help debugging but consume context.
- **Single-agent vs multi-agent**: separation of concerns can help, but coordination overhead is real.
- **Tool-rich vs tool-light**: tools improve grounding but increase surface area.

## Relationships to Other Topics
- Strongly related to [Planning Systems](./planning-systems.md).
- Depends on [Context Engineering](./context-engineering.md) for memory, retrieval, and information flow.
- Should be validated through [Evaluation / Prompt Testing](./evaluation-prompt-testing.md).
- Skills can package reusable procedures used inside an agent architecture; see [Skill Systems](./skill-systems.md).

## Practical Applications for This Repository
- Maintain a small catalog of architecture patterns with “when to use / not use” guidance.
- Keep tool contracts and stop conditions explicit.
- Default to simple workflows first, then escalate to more agentic loops only when evidence justifies it.
- Separate architecture principles from framework-specific examples.

## Open Questions
- When does an autonomous agent actually beat a good workflow?
- How much explicit reasoning should be surfaced versus kept internal?
- Which multi-agent patterns deliver real value instead of ceremony?
- How should long-running agents balance memory, retrieval, and checkpointing?

## Clarifications and Common Misconceptions
- **Agent != any tool-using LLM app.** A fixed workflow that happens to call tools is still better described as a workflow unless the model is dynamically directing the process.
- **Multi-agent is not the default “advanced” design.** It adds coordination cost, state-sharing problems, and debugging overhead. A single agent plus good tools/skills often wins.
- **Handoff and delegation are different.** In a handoff, the specialist takes over the conversation/work ownership. In delegation, a manager keeps ownership and uses specialists as bounded workers.
- **Architecture choice is also a context-partitioning choice.** The question is not only “how many agents,” but “who sees what, and who owns the final answer.”
- **Visible reasoning is not the same as good architecture.** A verbose plan can still be structurally poor if tool boundaries, stop conditions, and ownership are unclear.

## References
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic Engineering, 2024. Practical taxonomy of workflows vs agents and common orchestration patterns.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — arXiv, 2022/2023. Foundational paper on interleaving reasoning with actions and observations.
- [ReAct project page](https://react-lm.github.io/) — project site by the authors, year not clearly shown. Clear implementation-oriented summary of the ReAct pattern.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — Lilian Weng, 2023. Strong overview of planning, memory, tool use, and limitations.
- [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) — arXiv, 2023/2025 version shown. Broad survey of agent construction, evaluation, and challenges.
- [The Landscape of Emerging AI Agent Architectures for Reasoning, Planning, and Tool Calling: A Survey](https://arxiv.org/abs/2404.11584) — arXiv, 2024. Focused survey of architecture choices and tradeoffs.
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — arXiv, 2023. Important reference for tool-using architectures.
- [LangChain multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent) — LangChain docs, year not clearly visible. Useful for context-partitioning and multi-agent fit criteria.
- [OpenAI orchestration](https://platform.openai.com/docs/guides/agents/orchestration) — OpenAI docs, year not clearly visible. Helpful distinction between handoffs and agents-as-tools.
