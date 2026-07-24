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
- what opencode currently appears to provide for session-backed continuity
- what opencode currently appears to provide for local document navigation and explicit external context
- what it does not currently appear to provide as a first-class retrieval stack

## Canonical Boundary
This note is the opencode-specific product snapshot for memory/retrieval boundaries.

For reusable cross-tool ideas, see:
- `research/concepts/memory-systems.md`
- `research/capabilities/context-attachments.md`
- `research/capabilities/retrieval-pipelines.md`

For product-specific subtopics, see:
- `research/products/opencode/references-and-external-context-basics.md`
- `research/products/opencode/session-control-and-recovery.md`

## Summary
- opencode appears to have meaningful session continuity and compaction.
- opencode appears to have strong bounded file/navigation tools and named references.
- current evidence does not suggest a first-class built-in semantic retrieval, embeddings, or managed knowledge-store stack.

## Current Product Boundary

### Memory-like surfaces present
- session continuity
- compaction / bounded history management
- revert / redo / snapshot-like recovery behavior

### Retrieval-adjacent surfaces present
- references as explicit external context roots
- bounded `read` / `glob` / `grep` / listing tools
- `@` file and reference inclusion surfaces

### Retrieval-stack surfaces not clearly present
- embeddings-backed retrieval
- vector-store management
- document chunking/index freshness pipeline
- semantic corpus search as a first-class built-in subsystem

## Strongest Evidence Shaping This Boundary
- package/design evidence points to embeddings as a future domain rather than a present built-in feature area
- the `read` tool appears line/byte-offset based rather than semantic or index-backed
- current external-context surfaces look closer to attachment plus deterministic navigation than to full retrieval infrastructure

## Relationships to Other Notes
- `research/concepts/memory-systems.md`
- `research/capabilities/context-attachments.md`
- `research/capabilities/retrieval-pipelines.md`
- `research/products/opencode/references-and-external-context-basics.md`
- `research/products/opencode/session-control-and-recovery.md`
- `research/syntheses/memory-policy.md`

## Relevance to This Repository
- This note is the product-level place to record what opencode concretely has today and what it does not.
- Repository-level decisions about memory policy or future retrieval architecture should defer upward to the concept, capability, and synthesis notes rather than living here.

## Open Questions
- Will opencode later add first-class semantic retrieval or embeddings support?
- If so, will it look more like hosted file search, local index management, or MCP-mediated retrieval?
- How much session continuity is enough before explicit external wrap-up still matters after long gaps?

## References
- Context7 `/anomalyco/opencode` — session compaction config and lifecycle excerpts.
- Context7 `/anomalyco/opencode` — references, `@` file inclusion, and location-scoped filesystem tool contracts.
- Context7 `/anomalyco/opencode` — package/source excerpts showing embeddings are not part of the present design and `read` is offset/limit based rather than semantic retrieval.
