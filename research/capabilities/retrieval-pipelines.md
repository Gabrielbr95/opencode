# Retrieval Ingestion and Index Freshness Pipelines

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - vendor-specific indexing APIs and store abstractions
  - default chunking/ranking heuristics
  - built-in citation and filtering features

## Summary
- Many systems need more than explicit file attachment; they need retrieval over a larger corpus.
- The durable capability is the pipeline that turns source documents into retrievable units, keeps them fresh enough, and returns grounded results with acceptable quality and traceability.
- The reusable problem is not just “semantic search.” It is the full chain from source ingestion through index maintenance to retrieval-time evidence.

## Motivation
- A simple file or root attachment works well for bounded context, but it does not scale to large or changing corpora.
- Once a system depends on indexed stores, chunked documents, or retrieval-time ranking, the engineering problem changes.
- This note captures that capability boundary separately from context attachments and separately from long-term memory architecture.

## Problem Statement
- Systems need relevant context from large collections without pasting entire corpora into prompts.
- The design problem is how to:
  - ingest documents reliably
  - preserve identity and provenance
  - keep the index fresh enough
  - retrieve relevant evidence with acceptable recall and precision
  - make failures visible when retrieval goes stale or weak

## Core Function
- Convert source material into retrievable representations.
- Maintain enough document identity, provenance, and freshness information to trust the results.
- Return relevant evidence rather than forcing the model to search blindly through raw corpora.

## What This Note Is About
- Ingestion
- document identity
- chunking boundaries
- indexing
- freshness/update rules
- retrieval-time filtering, ranking, and evidence return

## What This Note Is Not About
- Not broad memory architecture
- Not simple one-off file attachment
- Not the full philosophy of context engineering
- Not vendor-specific SDK details except as examples

## Minimal Durable Model

### 1. Source identity
What source document or artifact does this indexed content come from?

Minimum useful fields:
- source ID
- source location or URI
- content type
- version or modified-at marker

### 2. Ingestion transform
How is the source turned into retrievable units?

Typical steps:
- parsing
- normalization
- segmentation/chunking
- metadata enrichment
- embedding and/or keyword indexing

### 3. Index record
What retrievable object gets stored?

Typical fields:
- chunk or document ID
- source ID
- chunk text or representation
- metadata
- embedding and/or lexical index terms

### 4. Freshness policy
When is re-ingestion required?

Typical options:
- never/immutable snapshot
- manual refresh
- scheduled refresh
- event-triggered refresh

### 5. Retrieval result
What evidence comes back at query time?

Typical fields:
- matched chunk/document
- score or rank
- source citation
- metadata filters used
- retrieval timestamp or run context

## Common Patterns
- upload documents into a hosted knowledge store
- maintain a vector store keyed by source documents
- combine semantic and keyword retrieval
- attach metadata filters to narrow the search space
- return citations or source references with retrieved text
- re-index on source changes or scheduled refresh
- preserve stable document identity across re-ingestion

## Typical Components
- document loader/parser
- chunker/segmenter
- metadata extractor
- embedding/index writer
- store or search backend
- freshness tracker
- retrieval/ranking layer
- citation/provenance formatter
- evaluation harness for retrieval quality

## Durable Distinctions

### Retrieval vs attachment
Attachment says what outside corpus, store, or resource is available.

Retrieval says how relevant pieces are selected from that larger available corpus.

### Retrieval vs memory
Retrieval can serve memory systems, but retrieval alone is not memory.

Memory also needs persistence policy, write policy, promotion rules, correction, and retirement.

### Document identity vs chunk identity
The source document and the retrievable chunk are related but different.

Stable source identity matters for provenance, deduplication, and freshness.

### Freshness vs relevance
A relevant result can still be stale.

A fresh result can still be irrelevant.

Both must be considered separately.

## Portability
- Portable across tools:
  - large corpora need indexing or structured search rather than raw prompt stuffing
  - provenance and source identity matter
  - freshness policy matters as much as ranking quality
  - retrieval should return inspectable evidence, not only invisible host magic
  - metadata filters are often necessary, not optional sugar
- Product-shaped:
  - exact upload/store API shape
  - chunking defaults
  - embedding and ranking implementation
  - hosted versus self-managed indexes
  - citation and filter syntax

## Advantages
- scales beyond direct file attachment
- reduces prompt size for large corpora
- enables reusable knowledge stores
- can improve grounding and citation quality
- supports selective retrieval over changing corpora

## Risks / Failure Modes
- stale index after source changes
- chunking that breaks important context
- poor metadata causing wrong filtering or no filtering
- weak provenance that makes results hard to audit
- hidden retrieval logic that is hard to debug
- over-retrieval that floods the model with noise
- under-retrieval that misses crucial evidence
- retrieval quality drifting silently over time

## Tradeoffs
- **Big chunks vs small chunks**: more context continuity versus better pinpoint retrieval.
- **Semantic vs lexical retrieval**: conceptual recall versus exact-term precision.
- **Hosted store vs local/self-managed index**: convenience versus transparency and control.
- **Frequent refresh vs cheaper refresh**: freshness versus cost and operational complexity.
- **Aggressive recall vs tight precision**: completeness versus context noise.

## Relationships to Other Notes
- `../concepts/context-engineering.md`
- `../concepts/memory-systems.md`
- `../concepts/observability-traceability.md`
- `../concepts/evaluation-prompt-testing.md`
- `../capabilities/context-attachments.md`
- `../capabilities/eval-harnesses.md`
- `../syntheses/memory-policy.md`
- `../syntheses/observability-schema.md`

## Practical Applications for This Repository
- Prefer direct attachment for small, known context.
- Use retrieval only when the corpus is too large or too changeable for direct attachment.
- Preserve source identity and modified-at metadata if a local knowledge store is ever introduced.
- Evaluate retrieval quality with explicit cases before trusting it as durable workflow infrastructure.
- Treat freshness failures as first-class operational failures, not minor implementation detail.

## Open Questions
- If this repository ever uses a knowledge store, what source metadata is the minimum useful set?
- Which refresh policy would be maintainable in a long-gap, local-first workflow?
- When is exact search enough, and when is semantic retrieval justified?
- What retrieval evidence should be surfaced by default for audit and debugging?

## References
- OpenAI file search / retrieval docs — representative hosted example of store-backed retrieval, metadata filters, and citations.
- RAG paper (`Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks`) — foundational framing of retrievable external knowledge.
- `../concepts/memory-systems.md` — clarifies why retrieval is only one part of memory architecture.
- `../capabilities/context-attachments.md` — clarifies the boundary between making a corpus available and searching within it.
