# Second-Brain and Retrieval Product Comparison

This note compares existing products that could serve as a local-first second brain and later expose scoped retrieval to opencode.

Its focus is constrained by this repository's operating environment:
- corporate Windows laptop
- low/no admin preference
- local-first bias
- existing product preferred over custom system design
- corpus grows over time
- topic-gated access matters

It is a decision aid, not an implementation plan.

---

## Product Families Seen in Research

The products split into two broad families.

### A. Note-centric second-brain products
Examples:
- Joplin
- Obsidian
- Khoj (partly overlaps retrieval-first, but conceptually close to second-brain use)

These are strongest when the main value is:
- curated notes
- human knowledge capture
- organization and browsing

### B. Retrieval-centric knowledge workspace products
Examples:
- AnythingLLM
- Open WebUI

These are strongest when the main value is:
- querying larger corpora
- handling PDFs/manuals/procedures
- explicit retrieval APIs or knowledge-base scopes

---

## Comparison Matrix

| Product | Product family | Local-first fit | Windows / low-admin fit | Topic scoping | Corpus fit | opencode integration path | Main risk |
|---|---|---|---|---|---|---|---|
| Joplin | Note-centric | Strong | Strong | notebooks, tags, filters | notes + attachments, moderate manuals fit | REST API, local service, MCP | more app-managed than plain files; optional network touches need review |
| Obsidian | Note-centric | Strong | Good | vaults, folders, files | excellent markdown/research fit | direct filesystem access, URI | weaker official API surface |
| AnythingLLM Desktop | Retrieval-centric | Strong | Good | workspaces | strong mixed-doc/manual fit | API, MCP compatibility | strongest access-control story may require heavier deployment shape |
| Open WebUI | Retrieval-centric | Strong in principle | Mixed | knowledge bases, permissions, groups | strong mixed-corpus fit | REST APIs, tool ecosystem | more operationally heavy; desktop still early |
| Khoj | Hybrid / second-brain-leaning | Strong | Weaker | filters, source scoping, conversation scoping | strong mixed-note/doc fit | HTTP APIs | Windows setup friction |

---

## Best Fit by Priority

### If the priority is “existing second-brain product first”
Best current fit:
- **Joplin**

Why:
- strongest documented integration surface among the note-centric products reviewed
- good topic boundaries through notebooks/tags
- Windows portable build matters in this environment

### If the priority is “local retrieval over manuals/procedures first”
Best current fit:
- **AnythingLLM Desktop**

Why:
- retrieval-oriented product
- good mixed-document support
- easier Windows path than heavier server-style platforms

### If the priority is “topic-gated corpora and future API flexibility”
Best current fit:
- **Open WebUI**

Why:
- strongest explicit knowledge-base scope model
- best-scoped retrieval story on paper
- stronger permission/group model than simpler desktop note apps

### If the priority is “plain local files and low lock-in”
Best current fit:
- **Obsidian**

Why:
- markdown vaults are transparent and inspectable
- separate vaults create a clean trust boundary

---

## Likely Architecture Patterns

### Pattern 1: One product for everything
Examples:
- Joplin as both note system and retrieval source
- AnythingLLM as both knowledge workspace and retrieval layer

Strength:
- simpler mental model

Weakness:
- one product may not be equally strong for curated notes and heavy mixed-corpus retrieval

### Pattern 2: Curated notes product + retrieval product
Examples:
- Joplin or Obsidian for curated second-brain knowledge
- AnythingLLM or Open WebUI for procedures/manuals/PDF-heavy corpora

Strength:
- each product does the job it is better suited for

Weakness:
- two systems to maintain

This pattern currently looks realistic for this repository because:
- `research/` and similar curated notes fit note-centric products well
- corporate manuals/procedures fit retrieval-centric products better

---

## Topic-Gated Access View

Topic-gated access can mean at least three different things.

### 1. Organizational scoping
Examples:
- notebook
- vault
- workspace
- knowledge base

### 2. Retrieval scoping
Examples:
- only search selected notebook/tag/workspace/knowledge-base
- only use selected file filters or sources

### 3. Permission scoping
Examples:
- one agent may query topic A but not B
- one session may only access selected corpora

The products reviewed vary a lot across these three meanings.

Observed trend:
- note apps are usually stronger at organizational scoping
- retrieval workspaces are usually stronger at retrieval scoping
- heavier platforms are stronger at permission scoping

---

## Current Repository Conclusion

At the current research level, the strongest candidates are:

1. **Joplin** — best note-centric second-brain candidate with future opencode retrieval path
2. **AnythingLLM Desktop** — best retrieval-first existing product with realistic Windows fit
3. **Open WebUI** — strongest long-term scoped-corpus platform, but heavier

This suggests a practical shortlist rather than one final universal winner.

---

## Open Questions

- Is one product preferred even if it is not the best at both curated-note management and manual/PDF retrieval?
- How much explicit permission scoping is needed beyond simple notebook/workspace selection?
- Is local Windows ease more important than retrieval sophistication in the first adoption step?
- Should the first pilot focus on the `research/` corpus, the manuals/procedures corpus, or both?

## Relationships to Other Notes
- `../products/joplin.md`
- `../products/obsidian.md`
- `../products/anythingllm.md`
- `../products/open-webui.md`
- `../products/khoj.md`
- `../capabilities/retrieval-pipelines.md`
- `../capabilities/context-attachments.md`

## Relevance to This Repository
- This note is the main decision aid for choosing an off-the-shelf second-brain or retrieval product under the repository's real-world constraints.
- It sharpens the likely next decision from “what is retrieval?” to “which existing product family fits this environment best?”
