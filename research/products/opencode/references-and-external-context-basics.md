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
- What references appear to be in opencode
- How references relate to external context and permissions
- Why references should be understood before deeper MCP or plugin work

## Why This Matters Here
- This repository values local-first, inspectable context.
- References appear to be one of the simplest ways to extend context safely without jumping straight into remote MCP or more complex integrations.

## Current Findings
- opencode appears to support named external context sources called **references**.
- References can point to:
  - local directories
  - Git repositories
- References are addressed by alias, such as `@alias` or `@alias/path`.
- References also seem to affect external-directory permission behavior by whitelisting reference roots.

## What a Reference Appears To Be
A reference is a named context root outside the current working directory.

Practical examples:
- local docs folder
- sibling repository
- shared standards repository

This is useful because it gives opencode a structured way to see approved outside context without making the whole filesystem feel ambiently available.

## Reference Shapes
Current docs/source excerpts suggest references can be configured as:

### Local path reference
- points at a local directory
- can include description
- can be hidden from autocomplete

### Git repository reference
- points at a repository and optional branch
- can include description
- can be hidden from autocomplete

There also appears to be a compact string form in newer config shapes.

## Practical Role of Descriptions
Descriptions matter because they help the agent know when a reference is relevant.

Practical takeaway:
- a reference is not just a path alias
- it is also a hint about intended use

That means sloppy descriptions will make retrieval worse.

## Relationship to `@` Referencing
The TUI supports `@` references for files and configured reference roots.

Practical effect:
- `@` can pull in local files from the current repo
- configured references also appear in autocomplete
- files within reference roots can then be added to context more deliberately

This makes references feel closer to **structured context attachment** than to full-blown retrieval automation.

## Relationship to `external_directory` Permissions
This is the most important operational point.

Current source excerpts suggest:
- when a path is outside the working directory, opencode treats it as `external_directory`
- `external_directory` rules are evaluated separately from normal in-repo paths
- default behavior appears to be `ask` for arbitrary external directories
- reference directories may be whitelisted into allow rules by default

Practical takeaway:
- references are not just convenience aliases
- they also participate in the trust boundary for outside-repo access

That is exactly why they should be learned before advanced external integrations.

## Why References Should Come Before MCP
For this repository, references seem like the lower-risk first step because they are:
- easier to inspect
- easier to explain
- more local-first
- less operationally magical than remote tool servers

Recommended learning and adoption order:

1. in-repo files
2. local references
3. Git references if really needed
4. local MCP only after the reference model is comfortable
5. remote MCP last

## Local-First / Corporate Notes
- Local path references fit this environment better than remote context sources.
- Git references may still imply network use, cloning, and update behavior.
- If a reference effectively whitelists outside access, it deserves the same care as any other permission boundary.
- Descriptions should stay specific so the agent does not overreach into side repositories casually.

## Working Heuristic for This Repository
When deciding whether to use a reference, ask:

1. Is this context stable enough to deserve a named alias?
2. Does it need to live outside the current repo?
3. Is a local directory enough, or is a Git reference actually needed?
4. Does the description clearly say when to use it?
5. Would a reference be simpler than adding more MCP or ambient instructions?

## Relationship to General Concepts
- `research/concepts/context-engineering.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`

## Open Questions
- How exactly does opencode materialize and refresh Git references in day-to-day use?
- Which reference patterns stay maintainable after long gaps?
- Which local directories are worth elevating to named references in this workflow?

## References
- Context7 `/anomalyco/opencode` — docs/source excerpts on references, `@` usage, and external-directory permission behavior.
