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
- where opencode appears to load config from
- how instruction files are discovered
- which product-specific precedence facts matter first when behavior is surprising

## Canonical Boundary
This note is the main product note for **loader mechanics**:
- where config comes from
- where instruction sources come from
- which precedence rules appear to matter

For the cross-tool idea of layered ambient instructions, see:
- `research/concepts/instruction-layering.md`

For the narrower placement question of ambient files versus skills inside opencode, see:
- `research/products/opencode/instruction-layering.md`

## Why This Matters Here
- The repository depends heavily on local customization.
- When opencode behavior is surprising, the cause is often source merging or precedence rather than the visible text of one file.

## Current Findings
- opencode appears to merge config from multiple sources, not just one file.
- project config, `.opencode/` content, agent files, commands/plugins, and environment overrides all participate.
- instruction loading is a separate mechanism from config loading.
- `AGENTS.md` appears first-class, with compatibility fallbacks such as `CLAUDE.md`.

## Config Loading: Practical Model
The current source excerpt suggests this broad order:

1. some remote or well-known auth-linked config sources may load first
2. global config loads
3. explicit config flags can load more config
4. project config files load while walking up from the current directory
5. `.opencode/` directories contribute more config plus discovered agents/commands/plugins
6. env-based inline config can still override later
7. managed/org-level sources may also merge in

Observed implication:
- opencode behaves like a merged config system rather than a single-file config system

## Instruction Loading: Practical Model

### Global instruction layer
- global `AGENTS.md` appears checked first
- global `CLAUDE.md` can act as fallback
- the first matching global file wins

### Project instruction layer
- project-level instruction files are searched upward from the current directory toward the worktree root
- the first matching file type wins
- this appears to avoid stacking every `AGENTS.md` or `CLAUDE.md` from all ancestors

### Extra configured instructions
- configured `instructions` entries appear additive
- local files and globs can be pulled in
- remote URLs may also be allowed

## Main Debugging Questions This Note Owns
When behavior is surprising, this note suggests checking:

1. which config sources are participating
2. which instruction file actually won
3. whether extra configured `instructions` were added
4. whether the observed behavior comes from config, instructions, skills, or plugin logic

## Main Confusion Sources
- several config sources merging silently
- project config plus `.opencode/` entries both contributing behavior
- global and project instruction sources interacting
- remote or managed config sources existing outside the most visible local files

## Local-First / Corporate Notes
- remote instruction URLs and remote config sources are a distinct trust boundary
- network-aware config behavior deserves separate scrutiny from purely local customization

## Relationships to Other Notes
- `research/products/opencode/instruction-layering.md`
- `research/products/opencode/foundations.md`
- `research/concepts/instruction-layering.md`
- `research/concepts/prompt-modularity-repository-architecture.md`

## Relevance to This Repository
- This note is the product-specific home for config/source merge order and instruction discovery mechanics.
- It should stay factual and debugging-oriented rather than becoming a second home for general instruction strategy.

## Open Questions
- Which parts of the source-order behavior are stable public surface versus implementation detail?
- How clearly is the merge behavior documented for routine maintenance?
- Which remote-loading behaviors are operationally acceptable in this environment?

## References
- Context7 `/anomalyco/opencode` — config merge and instruction priority excerpts from current source/docs.
