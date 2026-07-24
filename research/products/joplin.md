# Joplin

## Freshness
- Last verified: 2026-07-24
- Verified against: Joplin docs and help pages
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium
- Recheck triggers:
  - Data API or MCP support changes
  - semantic search feature changes
  - Windows portable distribution changes

## Scope
- Joplin as an existing local-first note and knowledge product
- relevance to a topic-scoped second-brain system that opencode can later retrieve from

## Canonical Boundary
This note covers Joplin as a concrete product.

For the cross-product decision context, see:
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Why This Matters Here
- Joplin is one of the strongest candidates when the goal is an existing second-brain product rather than a custom retrieval system.
- It has better documented automation and retrieval surfaces than most note-centric alternatives reviewed so far.

## Current Findings
- Joplin is a desktop note product with local storage and optional filesystem sync.
- It offers a Windows **portable** build, which matters on restricted corporate laptops.
- Topic organization appears strong through:
  - notebooks
  - sub-notebooks
  - tags
  - search filters
- Search is built on SQLite FTS and also has optional local semantic search support.
- Joplin exposes multiple integration surfaces relevant to opencode:
  - Data API / REST API
  - Web Clipper local service
  - MCP server

## Product-Specific Details

### Local-first posture
- data and profile live locally
- sync can remain local or be omitted
- the product does not require cloud-first use

### Topic scoping
The most natural topic boundaries appear to be:
- notebooks / sub-notebooks
- tags
- filtered search views

This makes it plausible to expose only selected notebook/tag scopes to an agent.

### Retrieval surfaces
- keyword/full-text search
- local semantic search feature
- structured API access to notes and metadata
- MCP surface for agent/tool integration

### Corpus fit
Strong fit for:
- research notes
- curated knowledge
- operational notes
- attachments/resources

Less naturally file-native than plain-folder markdown tools.

### Risk notes
The privacy posture is good enough to consider, but some optional/default network touches need review, such as update checks, plugin browsing, or other convenience surfaces.

## Relationships to Other Notes
- `research/products/obsidian.md`
- `research/products/anythingllm.md`
- `research/products/open-webui.md`
- `research/products/khoj.md`
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Relevance to This Repository
- Joplin currently looks like the strongest note-centric product candidate for a second brain that later exposes scoped retrieval to opencode.
- It fits the existing desire for an off-the-shelf product better than raw retrieval engines alone.
- It also supports a likely split architecture where curated knowledge lives in Joplin even if heavier manual/PDF retrieval later uses a second product.

## Open Questions
- How practical is notebook/tag-scoped retrieval through the MCP/API surface in daily use?
- How much of the product can stay fully local in this environment after optional network touches are disabled?
- How well does Joplin handle a growing procedures/manuals corpus compared with a retrieval-first product?

## References
- Joplin install / portable docs
- Joplin home directory docs
- Joplin search docs
- Joplin MCP docs
- Joplin semantic search docs
- Joplin REST API docs
- Joplin privacy docs
