# opencode: References and External Context Basics

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, source excerpts
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - reference config changes
  - external-directory permission changes
  - MCP or reference behavior changes in docs/source

## Scope
- what references appear to be in opencode
- how they are shaped and addressed
- how they interact with external-directory permissions

## Canonical Boundary
This note is the product-specific implementation note for opencode references.

For the reusable cross-tool attachment pattern, see:
- `research/capabilities/context-attachments.md`

For the broader memory/retrieval product boundary, see:
- `research/products/opencode/memory-and-retrieval.md`

## Why This Matters Here
- References appear to be one of opencode's clearest explicit external-context surfaces.
- Their practical importance is not only convenience; they also touch the trust boundary for outside-repo access.

## Current Findings
- opencode appears to support named external context sources called **references**.
- references can point to local directories or Git repositories.
- references are addressed by alias such as `@alias` or `@alias/path`.
- reference roots appear to interact with `external_directory` permission behavior.

## Observed Reference Shapes

### Local path reference
- points at a local directory
- can include description
- can be hidden from autocomplete

### Git repository reference
- points at a repository and optional branch
- can include description
- can be hidden from autocomplete

There also appears to be a compact string form in newer config shapes.

## Relationship to `@` Referencing
The TUI appears to support `@` references for both local files and configured reference roots.

Observed implication:
- references act as explicit external context roots that can then participate in bounded file inclusion

## Relationship to `external_directory` Permissions
Current source excerpts suggest:
- outside-worktree paths are treated as `external_directory`
- `external_directory` rules are evaluated separately from in-repo paths
- arbitrary external directories default toward `ask`
- configured reference roots may be whitelisted into allow behavior

Observed implication:
- references are part of the outside-context trust boundary, not just alias convenience

## Relationships to Other Notes
- `research/concepts/context-engineering.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`
- `research/capabilities/context-attachments.md`
- `research/capabilities/mcp.md`
- `research/products/opencode/memory-and-retrieval.md`

## Relevance to This Repository
- This note is the product-specific place to capture how opencode names and bounds external context roots.
- General adoption posture for references versus MCP belongs in capability or synthesis notes, not here.

## Open Questions
- How exactly does opencode materialize and refresh Git references in day-to-day use?
- Which reference patterns remain understandable after long interruptions?
- Which local directories are worth elevating to named references in this workflow?

## References
- Context7 `/anomalyco/opencode` — docs/source excerpts on references, `@` usage, and external-directory permission behavior.
