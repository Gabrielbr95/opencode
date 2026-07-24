# opencode: Config and Instruction Loading

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, config loader and instruction loader excerpts
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - config schema changes
  - instruction precedence changes
  - local load order differs from docs/source

## Scope
- Where opencode appears to load config from
- How instruction files are discovered
- Which precedence rules matter first for practical customization

## Why This Matters Here
- This repository already depends heavily on ambient instructions and local customization.
- If config and instruction precedence are unclear, later changes to agents, permissions, or skills become confusing fast.

## Current Findings
- opencode appears to merge config from multiple sources, not just one file.
- Project config, `.opencode/` files, agent files, commands, plugins, and environment overrides all participate.
- Instruction loading is a separate layer from config loading.
- `AGENTS.md` appears to be first-class, with compatibility fallbacks like `CLAUDE.md`.

## Config Loading: Practical Model
The current source excerpt suggests this broad order:

1. some remote or well-known auth-linked config sources may load first
2. global config loads
3. explicit config flags can load more config
4. project config files load while walking up from the current directory
5. `.opencode/` directories contribute more config plus discovered agents/commands/plugins
6. env-based inline config can still override later
7. managed/org-level sources may also merge in

Practical takeaway:
- opencode is a **merged config system**, not a single-file config system.
- If behavior is surprising, precedence and multiple sources are a likely cause.

## Instruction Loading: Practical Model
Instruction loading appears to follow a distinct rule set.

### Global instruction layer
- global `AGENTS.md` appears to be checked first
- global `CLAUDE.md` can act as a fallback
- the first matching global file wins

### Project instruction layer
- project-level instruction files are searched upward from the current directory toward the worktree root
- the first matching file type wins
- this appears designed to avoid stacking `AGENTS.md` and `CLAUDE.md` from every ancestor

### Extra configured instructions
- configured `instructions` entries appear additive
- local files and globs can be pulled in
- remote URLs may also be allowed, but that is a higher-risk choice for a local-first setup

## Practical Boundary Rules

### Use `AGENTS.md` for:
- stable ambient behavior
- repo-wide working style
- safety defaults
- communication norms

### Use config for:
- providers
- agents
- permissions
- references
- tool availability and behavior

### Use skills for:
- reusable procedures that should not always be in context

## What Can Cause Confusion
- multiple config sources merging silently
- project config plus `.opencode/` entries both contributing behavior
- global and project instructions interacting
- remote or managed config sources existing without being top-of-mind

## Local-First / Corporate Notes
- Remote instruction URLs should be treated cautiously.
- Well-known remote config behavior means network-aware features deserve review.
- If behavior ever seems unexpected, inspect whether the source is:
  - global
  - project-local
  - `.opencode/`
  - environment override
  - managed/org source

## Working Heuristic for This Repository
When debugging opencode behavior, ask in this order:

1. Which config files are participating?
2. Which instruction file actually won?
3. Are extra `instructions` being injected?
4. Is the behavior from config, instructions, skills, or a plugin?

That sequence should prevent a lot of false guesses.

## Relationship to General Concepts
- `research/concepts/prompt-modularity-repository-architecture.md`
- `research/concepts/context-engineering.md`

## Open Questions
- Which parts of the source-order behavior are stable public surface versus implementation detail?
- How much of the merge behavior is documented clearly enough for routine maintenance?
- Which remote-loading behaviors should be explicitly avoided in this environment?

## References
- Context7 `/anomalyco/opencode` — config merge and instruction priority excerpts from current source/docs.
