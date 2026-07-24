# opencode: Memory and Retrieval Boundaries

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, selected source excerpts
- Product version: current docs/source snapshot; exact installed local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - session model changes
  - compaction/revert changes
  - references or built-in search/read tool changes
  - any future first-class embeddings, file-search, or knowledge-store features

## Scope
- What opencode currently appears to provide for memory-like continuity
- What opencode currently appears to provide for retrieval-like access to external or local material
- What it does **not** currently appear to provide as a first-class retrieval/RAG stack

## Canonical Boundary
This note is the opencode-specific product snapshot for memory and retrieval boundaries.

For reusable cross-tool ideas, see:
- `research/concepts/memory-systems.md`
- `research/capabilities/retrieval-pipelines.md`
- `research/capabilities/context-attachments.md`

## Summary
- opencode appears to have meaningful **session continuity and compaction**, which makes it memory-relevant.
- opencode appears to have strong **bounded file/navigation tools and named references**, which makes it retrieval-adjacent.
- opencode does **not** currently appear to expose a first-class semantic retrieval / embeddings / vector-store capability in the way many RAG systems do.
- The practical product boundary today is closer to:
  - session-backed working memory
  - explicit context attachment
  - deterministic document navigation and search

than to:
  - built-in long-term semantic memory
  - hosted knowledge-store retrieval
  - automatic RAG pipeline infrastructure

## Current Memory-Like Surfaces

### Sessions as durable work objects
Current docs/source excerpts suggest opencode treats sessions as first-class runtime objects rather than as throwaway chat buffers.

Practical effect:
- work can continue across interruptions
- session state can outlive one terminal turn
- session identity matters operationally

### Compaction as working-memory management
Current docs/spec excerpts suggest:
- compaction is configurable
- automatic compaction can run before provider turns
- the system keeps a bounded recent-history budget and summary contract

Practical effect:
- opencode actively manages what remains visible in active context
- this is memory-relevant, but mostly in the sense of **working/session memory management**

### Revert / redo / snapshots
Current source excerpts suggest:
- revert is blocked while the session is busy
- snapshots can be captured for redo
- file patches and message history can be rolled back around a revert boundary

Practical effect:
- the product carries meaningful runtime history and recovery state
- this is stronger than a plain transcript, but still not the same as durable semantic memory

## Current Retrieval-Like Surfaces

### References
Configured references provide named external roots such as local directories or Git repositories.

Practical effect:
- opencode can expose bounded outside context deliberately
- this is best understood as **context attachment**, not a retrieval pipeline by itself

### Built-in read/glob/grep/list tools
Current docs/spec excerpts suggest opencode exposes:
- bounded file reads
- paged directory listings
- bounded glob results
- bounded grep results with previews

Practical effect:
- the product supports inspectable, deterministic document navigation and search
- this is often enough for code and document work inside known local corpora

### `@` references and fuzzy file inclusion
The TUI appears to support:
- `@path` style file references
- autocomplete over local files and configured references

Practical effect:
- useful material can be attached directly into the conversation
- again, this is closer to **attachment plus navigation** than to true RAG-like retrieval

## What opencode Does Not Currently Look Like

Current evidence does **not** suggest a first-class built-in stack for:
- embeddings-backed retrieval
- vector-store management
- document chunking/index freshness pipelines
- semantic file search over an indexed corpus
- hosted knowledge-base/file-search style retrieval

One especially strong signal is that current package design docs explicitly describe embeddings as a future domain outside the present LLM run/turn design.

Another strong signal is that the `read` tool appears to be line/byte-offset based rather than semantic or index-backed.

## Product Boundary: Best Current Mental Model

### Memory in opencode today
Best current interpretation:
- **working/session memory:** yes
- **durable semantic memory store:** not clearly exposed as a first-class product feature
- **repository-backed durable truth external to sessions:** still the user/workflow's responsibility

### Retrieval in opencode today
Best current interpretation:
- **bounded navigation/search over files:** yes
- **explicit attachment via references and `@` surfaces:** yes
- **full retrieval pipeline with ingestion/index/freshness semantics:** not clearly present as a first-class product feature

## Why This Matters for This Repository
- This workflow already prefers local-first, inspectable context.
- That means opencode's current strengths align well with:
  - file-level attachment
  - reference roots
  - path-scoped navigation
  - session continuity
- But it also means this repository should not pretend opencode already has a built-in long-term memory or RAG subsystem when the evidence says otherwise.

## Practical Guidance

### 1. Treat sessions as useful working memory, not durable truth
Session recovery and compaction help, but they should not replace repo-backed notes, decisions, and syntheses.

### 2. Treat references as attachment, not magic retrieval
References are valuable, but they mainly define approved context surfaces.

### 3. Treat read/glob/grep as deterministic search tools
These are excellent for inspectable local work.
They are not the same thing as a maintained semantic retrieval pipeline.

### 4. Do not over-design around missing product features
If a future workflow requires indexed semantic retrieval or long-term memory stores, that should be documented as an added subsystem, not assumed to already exist in opencode.

## Relationship to Other Notes
- `research/concepts/memory-systems.md`
- `research/capabilities/context-attachments.md`
- `research/capabilities/retrieval-pipelines.md`
- `research/products/opencode/references-and-external-context-basics.md`
- `research/products/opencode/session-control-and-recovery.md`
- `research/products/opencode/mcp-and-tooling.md`
- `research/syntheses/memory-policy.md`

## Open Questions
- Will opencode later add first-class semantic retrieval or embeddings support?
- If so, will it look more like hosted file search, local index management, or MCP-mediated retrieval?
- How much session continuity is enough before explicit external wrap-up still becomes necessary after long gaps?

## References
- Context7 `/anomalyco/opencode` — session compaction config and lifecycle excerpts.
- Context7 `/anomalyco/opencode` — references, `@` file inclusion, and location-scoped filesystem tool contracts.
- Context7 `/anomalyco/opencode` — package/source excerpts showing embeddings are not part of the present design and `read` is offset/limit based rather than semantic retrieval.
