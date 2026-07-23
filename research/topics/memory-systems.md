# Memory Systems

## Summary
- Memory in AI systems is a design problem, not just a storage problem.
- The durable pattern is tiered memory: working context for the current task, session/thread memory for continuity, and long-term memory for stable facts, preferences, lessons, and artifacts.
- Good memory systems retrieve selectively, store deliberately, and preserve provenance.

## Motivation
- This repository already distinguishes durable truth from temporary active context, so memory architecture matters directly.
- Better memory design helps with long gaps between sessions, prompt reuse, and not losing decisions or lessons.

## Problem Statement
- Without a memory system, agents forget preferences, lose continuity, repeat the same work, and overload prompts with replayed history.
- The design problem is how to preserve useful continuity without filling the system with stale, misleading, or low-value memory.

## Key Concepts
- Working / short-term memory
- Long-term memory
- Parametric vs non-parametric memory
- Episodic / semantic / procedural memory
- Retrieval policy
- Reflection / synthesis
- Hierarchical memory
- Provenance

## Principles vs Implementations
### Principles
- Separate memory by purpose.
- Retrieve instead of replaying full history.
- Promote information upward selectively.
- Store summaries, decisions, and lessons, not only raw logs.
- Treat memory as fallible and correctable.
- Preserve source traceability.
- Evaluate memory by task usefulness, not storage volume.

### Implementations / Examples
- RAG
- Generative Agents memory stream + reflection
- MemGPT hierarchical memory
- LangGraph checkpointers and stores
- Local repo summaries, ADRs, and session batons

## Design Patterns
- **Thread memory + global memory**: per-run state plus cross-session durable memory.
- **Event log + distilled summary**: raw traces plus compressed reusable summaries.
- **Memory write gate**: only store stable, reusable, trusted information.
- **Multi-signal retrieval**: relevance + recency + importance + source quality.
- **Hierarchical promotion**: events → summaries → durable facts/procedures.
- **Memory with provenance links**: every memory item points to its source.

## Advantages
- Better continuity across sessions.
- Lower prompt bloat.
- Better personalization and decision reuse.
- Better long-horizon workflow support.
- Easier adaptation without retraining.

## Disadvantages
- Stale memory can mislead future runs.
- Bad summaries can become durable corruption.
- More system complexity and governance burden.
- Persistent memory introduces privacy and audit concerns.

## Tradeoffs
- **Recall breadth vs precision**: more recall can mean more distraction.
- **Raw logs vs summaries**: fidelity versus efficiency.
- **Automatic writes vs curated writes**: scale versus safety.
- **Per-user personalization vs reproducibility**: performance versus portability.
- **Long context vs external memory**: bigger windows help but do not replace persistence or governance.

## Relationships to Other Topics
- Memory is a major part of [Context Engineering](./context-engineering.md).
- Memory policies affect [Human-in-the-loop control points](./human-in-the-loop-control-points.md), especially for durable writes.
- Procedural memory overlaps with [Skill Systems](./skill-systems.md).
- Memory quality should be verified through [Evaluation / Prompt Testing](./evaluation-prompt-testing.md).
- Memory operations benefit from [Observability / Traceability](./observability-traceability.md).

## Practical Applications for This Repository
- Keep at least three memory layers: current task state, durable repo knowledge, and reusable lessons from prior runs.
- Prefer structured durable memory for rules, terminology, and decisions.
- Use write gates before promoting model-generated claims into durable truth.
- Preserve provenance for summaries, decisions, and lessons.
- Avoid storing every conversation indiscriminately.

## Open Questions
- What is the right write policy for durable memory?
- How should stale or contradicted memories be retired?
- When should exact structured lookup beat semantic retrieval?
- How much summarization is useful before it starts hiding important detail?

## Clarifications and Common Misconceptions
- **Memory is not just chat history.** Thread/session state, durable semantic facts, episodic logs, and procedural know-how are different memory forms.
- **Memory is not just a vector database.** Some memory is better stored as structured records, profiles, decisions, or documents with provenance.
- **RAG is not automatically “memory.”** If nothing is persisted across sessions or updated as experience accumulates, it is retrieval, not full memory architecture.
- **Semantic memory is not the same as semantic search.** One is a category of stored knowledge; the other is a retrieval method.
- **Writing memory is itself risky.** Bad durable writes can be worse than forgetting, so write gates and correction paths matter.

## References
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — arXiv / NeurIPS noted, 2020. Foundational paper for combining model knowledge with external retrievable memory.
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — arXiv, 2023. Clear memory architecture using observation streams, retrieval, and reflection.
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — arXiv, 2023/2024 revision shown. Strong articulation of hierarchical memory and virtual context management.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — Lilian Weng, 2023. Practical synthesis of short-term vs long-term memory in agents.
- [LangGraph add memory](https://docs.langchain.com/oss/python/langgraph/add-memory) — LangGraph docs, year not clearly visible. Current engineering example of memory layering.
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) — LangGraph docs, year not clearly visible. Useful distinction between thread-scoped persistence and broader storage.
- [LangGraph stores](https://docs.langchain.com/oss/python/langgraph/stores) — LangGraph docs, year not clearly visible. Good example of cross-thread long-term memory store design.
- [LongNet: Scaling Transformers to 1,000,000,000 Tokens](https://arxiv.org/abs/2307.02486) — arXiv, 2023. Useful counterpoint: longer context windows do not replace proper memory architecture.
- [LangGraph memory](https://docs.langchain.com/oss/python/langgraph/memory) — LangGraph docs, year not clearly visible. Useful distinctions between semantic, episodic, and procedural memory, plus hot-path vs background writes.
