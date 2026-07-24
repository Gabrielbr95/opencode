# Context Attachments

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - exact alias syntax and UX
  - whitelisting behavior tied to permissions

## Summary
- Many harnesses need a middle ground between “current repo only” and “fully dynamic external tool integration.”
- Context attachments are the mechanisms by which external context is explicitly bound to a request, session, or bounded tool surface.
- The durable idea is selective attachment with explicit boundaries, provenance, freshness expectations, and intended use.

## Motivation
- Product notes often repeat the same reasoning: local references are simpler than remote integrations, and outside context should be attached deliberately rather than copied blindly.
- This note captures that reusable pattern once.

## Problem Statement
- Systems need outside context, but unrestricted external access increases drift, trust, and governance problems.
- The design question is how to expose outside context in a way that stays inspectable after long interruptions.
- The answer is usually not “make everything ambient.” It is “bind the smallest relevant external context explicitly.”

## Core Function
- Bind external context to model work deliberately rather than implicitly.
- Expose outside context through explicit handles such as files, selections, workspace/project scopes, named roots, store IDs, and resource URIs.

## What This Note Is About
- This note is about attachment mechanisms.
- It focuses on how external context becomes available to the model or harness in an explicit, bounded way.

## What This Note Is Not About
- Not full memory architecture.
- Not broad context-engineering theory.
- Not the full retrieval/RAG pipeline.
- Not chunking, reranking, or embedding strategy except where they affect the attachment boundary itself.

## Minimal Durable Model

### 1. Attachment unit
What is being attached?

Examples:
- a selected snippet
- one file
- multiple files
- a workspace or project
- a named external root
- an indexed knowledge store
- a resource namespace

### 2. Addressing method
How is it identified?

Examples:
- local path
- alias
- file ID
- file URI
- store ID
- resource URI or URI template

### 3. Binding time
When does the attachment become available?

Typical options:
- per request
- per conversation/session
- persistent configured boundary

### 4. Resolution mode
How does the system turn the attachment into usable context?

Typical options:
- direct inclusion of the attached artifact
- host/IDE expansion of a reference like `#file` or `@workspace`
- lazy retrieval through an index or resource read

### 5. Boundary and freshness
What does the attachment authorize, and how fresh is it?

Typical concerns:
- exact file versus broad root
- snapshot versus live source
- indexed copy versus source-of-truth file
- whether the attachment is reproducible later

## Common Patterns
- direct file attachment by uploaded handle, URL, or file ID
- IDE/editor attachment via `#file`, `#selection`, or workspace/project scope
- local path aliases
- repository aliases
- explicit file attachment from a named root
- store-backed attachment via a knowledge-base or vector-store ID
- resource attachment through named URIs or roots
- descriptions that explain intended use
- permission-aware treatment of outside-repo paths
- references over copies when the source may evolve

## Typical Components
- reference registry or upload store
- alias or selector syntax
- optional description/intent field
- boundary with permission or authorization rules
- provenance back to the external source root or uploaded artifact
- freshness model
- optional citation or attachment trace surface

## Durable Distinctions

### Attachment vs retrieval
Attachment answers:
- what outside context is explicitly available?

Retrieval answers:
- how do we search/select relevant pieces from a larger corpus?

An attached vector store or resource namespace is still an attachment mechanism, but the ranking, chunking, and freshness pipeline behind it belongs in retrieval notes.

### Attachment vs memory
Attachment is about binding context for current work.

Memory is about preserving useful information across time:
- what gets stored
- what gets promoted to durable truth
- what gets retrieved later

### File attachment vs workspace scope
Attaching a file is a narrow artifact-level decision.

Attaching a workspace, root, or project is a broader namespace decision and usually a bigger trust boundary.

### Snapshot attachment vs live source attachment
Some systems attach a concrete uploaded snapshot.
Others reference a live local file or external resource that may change underneath the handle.

## Portability
- Portable across tools:
  - explicit attachment beats ambient context
  - narrower attachment scopes are easier to audit
  - provenance and freshness matter more than syntax
  - attachment handles can represent artifacts, stores, or namespaces
  - permission boundaries should align with attachment boundaries
- Product-shaped:
  - alias or handle syntax
  - whether attachments are file-like, workspace-like, or store-like
  - whether the host expands references eagerly or lazily
  - whether references are treated as trusted, whitelisted, or merely convenient
  - how Git or remote sources are materialized and refreshed

## Advantages
- lower-risk external context than broad integrations
- easier to inspect than dynamic retrieval magic
- easier to reason about after long gaps
- reduces unnecessary duplication of source material
- cleaner trust boundary than ambient filesystem or repo access
- often easier to reproduce than hidden host heuristics

## Risks / Failure Modes
- over-broad attachment scope
- vague descriptions that encourage overreach
- implicit trust in external sources that still need policy boundaries
- stale attached context if the source changes and freshness is unclear
- opaque host-side expansion where the exact attached material is hard to inspect later
- ambiguous filenames, aliases, or workspace scopes
- prompt injection or misleading instructions inside attached content

## Tradeoffs
- Direct file handles are precise, but less scalable than store-backed attachment.
- Workspace or root attachment is convenient, but broader and noisier than file-level attachment.
- Local references are easier to audit, but less dynamic than remote systems.
- Storing copies improves durability, but increases duplication and cleanup burden.
- Attached stores scale well, but push complexity into retrieval quality and freshness management.

## Relationships to Other Notes
- `../concepts/context-engineering.md`
- `../concepts/memory-systems.md`
- `../concepts/tool-use-policy-and-permission-systems.md`
- `../capabilities/retrieval-pipelines.md`
- `../syntheses/memory-policy.md`
- `../products/opencode/references-and-external-context-basics.md`
- `../products/opencode/mcp-and-tooling.md`

## Practical Applications for This Repository
- Prefer named local references before adopting heavier external integration.
- Prefer the narrowest useful attachment unit:
  - file before root
  - root before tool server
  - explicit store before ambient corpus search
- Use descriptions to say when a reference should be used, not just what path it points to.
- Treat reference roots as part of the trust boundary, not just autocomplete convenience.
- Prefer source-linked summaries over copied content when external material may drift.

## When Attachment Stops Being Enough
- If the corpus is too large to attach directly and needs searching, that becomes a retrieval problem.
- If information must persist, accumulate, or be promoted across sessions, that becomes a memory problem.
- If external context also exposes callable actions, that becomes a tool/MCP problem in addition to attachment.

## Open Questions
- Which external sources in this workflow deserve stable named references?
- When does a direct attachment stop being enough and justify indexed retrieval?
- Which attachment scopes remain understandable after long interruptions?

## References
- `../concepts/context-engineering.md` — general principles for minimal sufficient context and explicit grounding.
- `../concepts/memory-systems.md` — broader architecture of persistence, promotion, and recall across time.
- `../capabilities/retrieval-pipelines.md` — separate note for ingestion, indexing, freshness, and retrieval quality.
- `../syntheses/memory-policy.md` — repository policy for references over copies and durable-write caution.
- `../products/opencode/references-and-external-context-basics.md` — concrete product example of aliases, external boundaries, and reference roots.
- OpenAI file inputs and file search docs — representative examples of direct file handles and attached knowledge stores.
- GitHub Copilot IDE chat docs — representative examples of file, selection, and workspace-level attachment from host UI.
- MCP roots/resources docs — representative examples of boundary- and URI-based external context surfaces.
- Anthropic and Gemini file/document docs — representative examples of reusable uploaded artifact handles.
