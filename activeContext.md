# Active Context

## Resume Here
- **Tier:** POC
- **Current Slice:** Research capability-boundary cleanup + capability build-out
- **Current Task:** N/A
- **Next Action:** Re-read `research/capabilities/retrieval-pipelines.md`, `research/syntheses/local-first-retrieval-tool-comparison.md`, and the new tool notes under `research/products/`, then decide whether the next pass should design a repository-specific local retrieval architecture or move on to `research/capabilities/task-artifact-and-run-record-models.md`.

## Completed This Session
- Audited the whole `research/` tree and concluded the capabilities layer was the most behind.
- Added and integrated new capability notes for:
  - `research/capabilities/tool-calling.md`
  - `research/capabilities/eval-harnesses.md`
  - `research/capabilities/policy-engines.md`
- Added broader runtime/control notes, then corrected the boundary by moving concept-like material into:
  - `research/concepts/instruction-layering.md`
  - `research/concepts/durable-execution.md`
- Renamed capability files to short subsystem-style names and rewired indexes/maps/product links accordingly.
- Tightened the meaning of `research/capabilities/` so it now better matches cross-tool subsystems/facilities rather than broad architecture essays.
- Deepened the memory vs retrieval distinction across layers:
  - strengthened `research/concepts/memory-systems.md`
  - tightened `research/capabilities/retrieval-pipelines.md`
  - added `research/products/opencode/memory-and-retrieval.md`
  - updated indexes/maps/readme links to point at the new product boundary note
- Did a deeper pass on local-first corpus/database retrieval beyond `grep` / `glob`:
  - strengthened `research/concepts/context-engineering.md` around retrieval-oriented context shapes
  - significantly expanded `research/capabilities/retrieval-pipelines.md` for mixed corpora, local-first design goals, and practical local architectures
  - corrected the layer split by replacing the invalid comparison-style product note with:
    - product notes for `research/products/sqlite-fts5.md`, `research/products/docling.md`, `research/products/qdrant.md`, `research/products/lancedb.md`, and `research/products/chroma.md`
    - a synthesis note at `research/syntheses/local-first-retrieval-tool-comparison.md`

## Blockers / Open Questions
- No hard blocker.
- Main open question: should the next pass design a repository-specific local retrieval architecture/tool shape, or shift focus to task/artifact/run records?
- `research/capabilities/policy-engines.md` and `research/capabilities/sessions.md` are acceptable now, but are still the two most likely capability notes to tighten further later if they drift abstract again.

## Read These First
- `research/index.md`: Current top-level map of concepts, capabilities, products, and suggested next topics.
- `research/capabilities/README.md`: Current boundary rule for what does and does not belong in capabilities.
- `research/syntheses/concept-capability-product-map.md`: Best current map from concept -> capability -> product.
- `research/backlog.md`: Ranked next capability contenders and naming cleanup rules.
- `research/products/opencode/README.md`: Updated product branch bridge links after the capability cleanup.
