# Context Engineering

## Summary
- Context engineering is the design of what information an AI system sees, in what form, at what time, and with what controls.
- The term is newer than the underlying ideas, but the core problem is well established: LLMs operate on bounded working context, so real systems must manage retrieval, memory, prompt structure, and salience deliberately.
- The recurring principle is to provide the minimum sufficient context for the current task rather than dumping everything into the prompt.

## Motivation
- This repository depends on careful context boundaries: durable truth, session baton, active task context, and optional reference materials.
- Better context engineering reduces token waste, stale instructions, and prompt overload.

## Problem Statement
- Systems fail when critical information is absent, buried, stale, conflicting, or badly formatted.
- The design problem is how to provide relevant context reliably while controlling cost, latency, and attention failure.

## Key Concepts
- Context window
- Parametric vs non-parametric memory
- Retrieval augmentation
- Short-term vs long-term memory
- Context placement and salience
- Tool-mediated context
- Structured prompts
- Context compression / summarization
- Ground truth from environment or tools

## Principles vs Implementations
### Principles
- Treat context as a scarce resource.
- Prefer relevant context over maximal context.
- Ground freshness-sensitive tasks in external sources.
- Separate durable memory from active working context.
- Make important information easy to notice.
- Update context as the task evolves instead of using one giant static prompt.

### Implementations / Examples
- RAG
- Long-context prompting
- Hierarchical memory systems like MemGPT
- MCP-style resource and tool interfaces
- Session summaries and resume batons

## Design Patterns
- **Retrieve-then-read**: fetch a small evidence set before generation.
- **Pinned instructions + dynamic evidence**: stable policy plus task-specific context.
- **Two-tier memory**: short active state plus durable external memory.
- **Context distillation**: summarize history into compact state.
- **Tool over transcription**: provide a query interface instead of raw data dumps.
- **Salience-first ordering**: put critical facts where the model is more likely to use them.

## Retrieval-Oriented Context Shapes

### Direct navigation
The agent searches or reads files directly using deterministic tools such as path lookup, globbing, grep, or paged reads.

Best for:
- known repositories
- exact terms
- inspectable local work

### Corpus retrieval
The agent consults an indexed corpus that returns candidate evidence from a larger set of documents or records.

Best for:
- large or mixed corpora
- paraphrase-heavy queries
- cases where the answer may be buried in many sources

### Structured lookup
The agent queries explicit records, tables, IDs, or metadata-filtered datasets.

Best for:
- inventories
- plans
- tickets
- asset registers
- structured operational knowledge

### Hybrid consultation
The system combines structured lookup, lexical search, semantic search, and document reading.

Best for:
- mixed corpora where no single retrieval mode is sufficient
- real operational environments with documents, notes, and structured records together

## Advantages
- Better factuality and relevance.
- Better provenance when using retrieved or tool-sourced information.
- Better cross-session continuity.
- Lower hallucination risk when external grounding replaces unsupported inference.
- Easier updates when changing data rather than changing prompts.

## Disadvantages
- Retrieval and summarization can both fail.
- Memory systems can preserve wrong summaries.
- More moving parts increase debugging complexity.
- Bigger context is not automatically better.
- Hidden context layers can make failures harder to inspect.

## Tradeoffs
- **Long context vs retrieval**: long context is simpler; retrieval is more selective and scalable.
- **Raw history vs summaries**: raw history keeps detail; summaries reduce cost but can distort.
- **Embedded tools vs embedded text**: tools improve freshness and precision but add complexity.
- **Global memory vs task-local memory**: global memory improves continuity; local memory reduces contamination.
- **Direct navigation vs indexed retrieval**: navigation is simpler and easier to inspect; indexed retrieval scales better across larger or fuzzier corpora.
- **Lexical vs semantic retrieval**: lexical search is sharper and easier to debug; semantic search is better at paraphrase and latent similarity.

## Relationships to Other Topics
- Context delivery shapes how [Agent Architectures](./agent-architectures.md) behave.
- Skill loading is a targeted context-loading mechanism; see [Skill Systems](./skill-systems.md).
- Planning often determines what context is needed next; see [Planning Systems](./planning-systems.md).
- Context quality should be tested through [Evaluation / Prompt Testing](./evaluation-prompt-testing.md).
- Retrieval subsystem design lives in `../capabilities/retrieval-pipelines.md`.

## Practical Applications for This Repository
- Keep stable policies separate from task-specific context.
- Define context contracts for prompts, agents, and skills.
- Prefer small, coherent, retrieval-friendly documents.
- Maintain durable summaries for recurring workflows instead of replaying giant histories.
- Put critical constraints and acceptance criteria in consistent high-salience positions.
- Prefer tool/resource references for changing data rather than copied blobs of text.
- A common pattern once a corpus outgrows easy `grep`/`glob` use is to introduce a consultation tool that returns a small evidence set rather than exposing the whole corpus at once.
- Mixed-corpus retrieval is partly a context-engineering problem because source shape, evidence size, and salience all affect what the model actually sees.
- Retrieval interfaces with source identity, metadata, and inspectable evidence generally make context failures easier to debug.

## Open Questions
- How should the system decide between retrieval, summarization, and omission?
- How can stale memory or summary drift be detected?
- How should context sufficiency be evaluated beyond token count?
- When is long context enough, and when is structured retrieval better?

## Clarifications and Common Misconceptions
- **Context engineering is broader than prompt wording.** It includes tool context, retrieved evidence, state passing, summarization, and what persists between steps.
- **More context is not automatically better context.** Long prompts can bury critical facts, increase distraction, and worsen model performance.
- **Context and memory are not the same.** Memory is what may persist; context is what is actually presented for a specific step.
- **Tool interfaces are part of context engineering.** Parameter names, descriptions, examples, and tool availability shape model behavior as much as prompt text does.
- **Instruction persistence is easy to over-assume.** Some systems do not automatically carry prior instructions forward the way users expect.
- **Better retrieval is not just “faster grep.”** It may require ingestion, indexing, metadata, ranking, and evidence-return contracts that ordinary filesystem tools do not provide.

## References
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — arXiv / NeurIPS noted, 2020. Foundational paper for combining model knowledge with explicit retrieval.
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) — arXiv / TACL noted, 2023. Shows that long-context models often underuse information placed in the middle.
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — arXiv, 2023. Introduces hierarchical context and memory management.
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) — Anthropic Engineering, 2024. Practical framing of retrieval, tools, and memory in agent systems.
- [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro) — MCP documentation, year not clearly visible. Defines MCP as an open standard for connecting AI applications to tools and data.
- [Architecture overview (MCP)](https://modelcontextprotocol.io/docs/learn/architecture) — MCP documentation, year not clearly visible. Useful for tools, resources, prompts, and client/server roles.
- [LangChain context engineering](https://docs.langchain.com/oss/python/langchain/context-engineering) — LangChain docs, year not clearly visible. Useful distinctions between model, tool, and lifecycle context.
