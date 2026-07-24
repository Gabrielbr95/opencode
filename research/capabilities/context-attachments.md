# Context Attachments

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - exact alias syntax and UX
  - whitelisting behavior tied to permissions

## Summary
- Many harnesses need a middle ground between “current repo only” and “fully dynamic external tool integration.”
- External context attachments and references provide named, bounded access to outside context without making the whole environment ambient.
- The durable idea is selective attachment with explicit boundaries, provenance, and intended use.

## Motivation
- Product notes often repeat the same reasoning: local references are simpler than remote integrations, and outside context should be attached deliberately rather than copied blindly.
- This note captures that reusable pattern once.

## Problem Statement
- Systems need outside context, but unrestricted external access increases drift, trust, and governance problems.
- The design question is how to expose external context roots in a way that stays inspectable after long interruptions.

## Core Function
- Provide named access to external context roots or source collections.
- Make outside context attachable on purpose rather than implicitly ambient.

## Common Patterns
- local path aliases
- repository aliases
- explicit file attachment from a named root
- descriptions that explain intended use
- permission-aware treatment of outside-repo paths
- references over copies when the source may evolve

## Typical Components
- reference registry
- alias or selector syntax
- optional description/intent field
- boundary with permission or authorization rules
- provenance back to the external source root

## Portability
- Portable across tools:
  - named external context roots are a common design pattern
  - references are safer than ambient full-filesystem access
  - provenance and narrow scope matter more than syntax
- Product-shaped:
  - alias syntax
  - whether references are treated as trusted, whitelisted, or merely convenient
  - how Git or remote sources are materialized and refreshed

## Advantages
- lower-risk external context than broad integrations
- easier to inspect than dynamic retrieval magic
- easier to reason about after long gaps
- reduces unnecessary duplication of source material

## Risks / Failure Modes
- over-broad reference roots
- vague descriptions that encourage overreach
- implicit trust in external sources that still need policy boundaries
- stale attached context if the source changes and freshness is unclear

## Tradeoffs
- References are simpler than tool integration, but less powerful.
- Local references are easier to audit, but less dynamic than remote systems.
- Storing copies improves durability, but increases duplication and cleanup burden.

## Relationships to Other Notes
- `../concepts/context-engineering.md`
- `../concepts/tool-use-policy-and-permission-systems.md`
- `../syntheses/memory-policy.md`
- `../products/opencode/references-and-external-context-basics.md`
- `../products/opencode/mcp-and-tooling.md`

## Practical Applications for This Repository
- Prefer named local references before adopting heavier external integration.
- Use descriptions to say when a reference should be used, not just what path it points to.
- Treat reference roots as part of the trust boundary, not just autocomplete convenience.
- Prefer source-linked summaries over copied content when external material may drift.

## Open Questions
- Which external sources in this workflow deserve stable named references?
- When does a reference stop being enough and justify a tool or MCP integration?

## References
- `../concepts/context-engineering.md` — general principles for minimal sufficient context and explicit grounding.
- `../syntheses/memory-policy.md` — repository policy for references over copies and durable-write caution.
- `../products/opencode/references-and-external-context-basics.md` — concrete product example of aliases, external boundaries, and reference roots.
