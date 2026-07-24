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

## Minimal Durable Model

### 1. Memory unit
What is the thing being remembered?

Examples:
- fact
- decision
- preference
- episodic event
- reusable procedure
- summary linked to richer source material

### 2. Time horizon
How long should it remain useful?

Typical layers:
- current-step working state
- session/thread continuity
- cross-session durable memory

### 3. Write path
How does information enter memory?

Typical options:
- explicit user write
- automatic event capture
- model-generated summary or reflection
- reviewed promotion from temporary notes into durable artifacts

### 4. Retrieval path
How is remembered information recalled later?

Typical options:
- direct structured lookup
- lexical search
- semantic retrieval
- hand-maintained indexes or links
- explicit user navigation to authoritative artifacts

### 5. Governance
Why should this memory be trusted and how can it be corrected?

Minimum concerns:
- provenance
- confidence / status
- review threshold
- supersession / retirement path

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

## Durable Distinctions

### Memory vs context
Context is what is visible to the model now.

Memory is what may persist and be recalled later.

Something can exist in memory without being in the active prompt, and something can be in the active prompt without being durable memory.

### Memory vs retrieval
Retrieval is one access path into memory or other external corpora.

It answers:
- how do we find relevant material now?

Memory also answers:
- what should persist?
- what gets promoted?
- what can be trusted?
- what should be retired or corrected?

Retrieval can operate over documents that are not really "memory" at all, such as a product manual or source tree.

### Memory vs retrieval pipeline
A retrieval pipeline is the subsystem that ingests, indexes, refreshes, and returns evidence from a corpus.

Memory architecture is broader. It also includes write policy, promotion rules, retention, correction, governance, and often multiple memory types.

### Episodic vs semantic vs procedural memory
- **Episodic memory** stores what happened.
- **Semantic memory** stores distilled facts and concepts.
- **Procedural memory** stores how to do recurring work.

Confusing these usually leads to bad write policies and poor retrieval behavior.

## Relationships to Other Topics
- Memory is a major part of [Context Engineering](./context-engineering.md).
- Memory policies affect [Human-in-the-loop control points](./human-in-the-loop-control-points.md), especially for durable writes.
- Procedural memory overlaps with [Skill Systems](./skill-systems.md).
- Memory quality should be verified through [Evaluation / Prompt Testing](./evaluation-prompt-testing.md).
- Memory operations benefit from [Observability / Traceability](./observability-traceability.md).
- Retrieval infrastructure details live in `../capabilities/retrieval-pipelines.md`.
- Repository write/retire/review rules live in `../syntheses/memory-policy.md`.

## Practical Applications for This Repository
- Keep at least three memory layers: current task state, durable repo knowledge, and reusable lessons from prior runs.
- Prefer structured durable memory for rules, terminology, and decisions.
- Use write gates before promoting model-generated claims into durable truth.
- Preserve provenance for summaries, decisions, and lessons.
- Avoid storing every conversation indiscriminately.
- Treat session continuity features as useful working memory, but not as a replacement for repo-backed durable truth.
- Prefer exact lookup into authoritative files when the repository already has a known home for a fact.
- Use retrieval-oriented stores only when the corpus is large or changing enough that direct navigation is no longer practical.

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
