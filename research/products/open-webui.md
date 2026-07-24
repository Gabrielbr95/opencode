# Open WebUI

## Freshness
- Last verified: 2026-07-24
- Verified against: Open WebUI README, desktop README, docs pages, and API docs
- Product version: current docs snapshot; exact local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - desktop maturity changes
  - knowledge-base API changes
  - permission/RBAC surface changes

## Scope
- Open WebUI as an existing retrieval-capable knowledge workspace platform
- relevance to topic-scoped corpora and later opencode retrieval

## Canonical Boundary
This note covers Open WebUI as a concrete product.

For cross-product comparison, see:
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Why This Matters Here
- Open WebUI is one of the strongest products reviewed for explicit corpus scoping, retrieval features, and future integration surfaces.
- It is more a platform than a simple note app, but that may be useful if topic-gated corpora become central.

## Current Findings
- Open WebUI is self-hosted/offline-capable in principle.
- Knowledge bases are first-class objects.
- The documented API supports knowledge-base identifiers, including explicit `knowledge_id` / `knowledge_ids` usage.
- Hybrid BM25 + vector search and reranking are documented.
- RBAC/groups/permissions are part of the broader product surface.
- Desktop exists, but is early/alpha and requires internet on first launch.

## Product-Specific Details

### Local-first posture
- local/self-hosted posture is strong in principle
- desktop app emphasizes offline use after first launch

### Topic scoping
Natural boundaries appear to be:
- knowledge bases
- workspaces
- permission/group structures

This is one of the strongest scoped-corpus stories in the researched set.

### Retrieval surfaces
- hybrid search
- reranking
- configurable loaders/parsers
- REST API
- broader ecosystem compatibility and tool-server integration

### Corpus fit
Strong fit for:
- PDFs
- spreadsheets
- code/text docs
- larger knowledge corpora
- multiple corpora requiring explicit selection

### Risk notes
- more operationally heavy than a simple note app
- desktop is still alpha
- local-first posture is strong, but deployment discipline still matters in a corporate environment

## Relationships to Other Notes
- `research/products/anythingllm.md`
- `research/products/khoj.md`
- `research/syntheses/second-brain-and-retrieval-product-comparison.md`

## Relevance to This Repository
- Open WebUI currently looks strongest when future topic-scoped retrieval and explicit corpus permissions matter more than note-taking simplicity.
- It may be a better long-term retrieval platform than a first personal second-brain tool on a locked-down laptop.

## Open Questions
- Is the desktop path mature enough for conservative daily use yet?
- How much setup friction would remain on this laptop compared with AnythingLLM Desktop?
- Would a knowledge-base-centric platform be overkill if Joplin already covers curated note needs?

## References
- Open WebUI main README
- Open WebUI desktop README
- Open WebUI knowledge docs
- Open WebUI env config docs
- Open WebUI API docs
