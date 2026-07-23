# Planning Systems

## Summary
- Planning systems for AI workflows decompose goals into steps, choose execution paths, coordinate workers or tools, and revise actions based on feedback.
- The durable insight is that some tasks need only predefined workflows, while others benefit from runtime planning and replanning.
- Useful planning is explicit, bounded, and connected to verification rather than being performative chain-of-thought for its own sake.

## Motivation
- This repository needs clearer boundaries between planning, execution, orchestration, and review.
- Planning patterns determine when to use a simple linear workflow versus a more dynamic agent or multi-agent setup.

## Problem Statement
- Complex tasks fail when the system cannot decompose work, choose the right next step, recover from bad intermediate results, or stop cleanly.
- The design problem is how to break work into executable steps and adapt when reality diverges from the original plan.

## Key Concepts
- Workflow vs agent
- Task decomposition
- Planning horizon
- Reasoning-action loop
- Evaluation / reflection
- Orchestration
- Specialization
- Termination conditions
- Grounding and verification

## Principles vs Implementations
### Principles
- Use the least agentic structure that works.
- Decompose hard tasks into easier subtasks.
- Interleave planning with environment feedback.
- Insert checks between steps to prevent compounding error.
- Use specialized workers only when subtasks actually differ.
- Keep success and stopping conditions explicit.
- Make plans inspectable.

### Implementations / Examples
- Prompt chaining
- Routing
- Parallelization / voting
- Orchestrator-workers
- Evaluator-optimizer
- ReAct
- Plan-and-Solve prompting
- Reflexion
- Group chat / mixture-of-agents patterns

## Design Patterns
- **Prompt chaining**: fixed sequence of subtasks.
- **Routing**: choose a branch or specialist first.
- **Parallel workers + aggregation**: independent work followed by synthesis.
- **Orchestrator-workers**: central planner delegates dynamic subproblems.
- **Evaluator-optimizer**: critique and revise loops.
- **Plan-first, execute-second**: outline before acting.
- **Reason-act-observe**: use environment feedback during execution.
- **Reflection loop**: learn from failure and retry.

## Advantages
- Better handling of multi-step or open-ended tasks.
- Easier specialization across tools, roles, or prompts.
- Better debugging when plans and checkpoints are explicit.
- Better recovery when the system can revise its path.

## Disadvantages
- Extra latency and cost.
- More failure points and coordination overhead.
- Planning can become fake ceremony instead of useful structure.
- Dynamic planners are harder to test than fixed workflows.

## Tradeoffs
- **Workflow vs autonomy**: workflows are predictable; dynamic planning is flexible.
- **Plan-first vs improvise**: planning improves structure; improvisation handles uncertainty.
- **Single-agent vs multi-agent**: simpler control versus specialized collaboration.
- **Reflection loops vs one-pass execution**: potential quality gains versus extra time/cost.
- **Explicit plans vs compact prompts**: inspectability versus token overhead.

## Relationships to Other Topics
- Planning is one dimension of [Agent Architectures](./agent-architectures.md).
- Planning decisions determine what context is needed next; see [Context Engineering](./context-engineering.md).
- Some planning procedures can be packaged as [Skill Systems](./skill-systems.md).
- Planning quality should be judged through [Evaluation / Prompt Testing](./evaluation-prompt-testing.md).

## Practical Applications for This Repository
- Maintain a small set of reusable planning/orchestration patterns.
- Document for each pattern: inputs, tools, stop conditions, failure handling, and evaluation criteria.
- Use fixed workflows first for repeatable work.
- Reserve dynamic planning for tasks with unknown branches or step counts.
- Keep human checkpoints for risky operations.
- Store reflection artifacts separately from stable instructions.

## Open Questions
- When does explicit planning help more than it hurts?
- What is the right planning depth before execution starts?
- When should the system replan versus continue?
- How should plan quality be evaluated separately from final answer quality?

## Clarifications and Common Misconceptions
- **Planning is not the same as chain-of-thought verbosity.** A system can plan well with compact or partially hidden reasoning, and can plan badly with very verbose text.
- **Planning is not automatically multi-agent.** Many planning patterns work inside a single workflow or single-agent loop.
- **A todo list is not the full planning system.** It is only one representation of current task state.
- **Up-front planning is not always best.** Some tasks benefit more from incremental replanning after tool results or tests.
- **Planning depends on evaluation.** If there is no way to judge intermediate progress, elaborate planning often degrades into ceremony.

## References
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic Engineering, 2024. Practical taxonomy of workflow patterns versus agents.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — arXiv, 2022. Foundational paper for interleaved reasoning and acting.
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/) — Google Research Blog, 2022. Engineering explanation of the pattern and why it works.
- [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091) — arXiv / ACL noted, 2023. Plan-first method for reducing missing-step errors.
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — arXiv, 2023. Reflection with episodic memory and verbal feedback.
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — arXiv, 2023. Framework paper for multi-agent conversation patterns.
- [Group Chat — AutoGen](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/group-chat.html) — Microsoft AutoGen docs, 2024 copyright shown. Example of manager-controlled role-based collaboration.
- [Mixture of Agents — AutoGen](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/mixture-of-agents.html) — Microsoft AutoGen docs, 2024 copyright shown. Example of layered worker/orchestrator aggregation.
- [Reasoning best practices](https://platform.openai.com/docs/guides/reasoning-best-practices) — OpenAI docs, year not clearly visible. Useful distinction between planning capability and visible step-by-step prompting.
