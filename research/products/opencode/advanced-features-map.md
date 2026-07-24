# opencode: Advanced Features Map

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, v2 spec excerpts
- Product version: current docs snapshot plus dev spec direction; exact installed local version not verified
- Stability: Low-Medium
- Recheck triggers:
  - config/schema changes
  - release notes mention feature changes
  - local behavior differs from docs

## Scope
- A practical map of which opencode features feel foundational versus genuinely advanced
- Which advanced areas are worth learning next for this repository
- Which advanced areas look powerful but volatile

## Why This Matters Here
- The foundation notes now cover the base product model.
- This note exists to prevent “advanced features” from becoming a grab bag.
- The goal is to rank advanced areas by practical value, not by novelty.

## Foundation vs Advanced

### Foundation already covered
- config and instruction loading
- agents, permissions, and skills basics
- references and external context basics
- local-first models and providers
- config-surface drift and safety posture

### More advanced from this point forward
- deeper agent specialization and role shaping
- MCP as a tool-extension layer
- plugins and hook-based customization
- session control, compaction, undo/redo, and recovery behavior
- system-prompt surgery / experimental hooks

## Ranked Advanced Areas

### 1. Deeper agent shaping
Examples:
- custom specialized agents
- different permission envelopes per role
- more deliberate primary vs subagent use

Why it matters:
- high practical value
- close to existing workflow needs
- builds directly on the foundation notes

Risk level:
- medium

### 2. Session control and recovery features
Examples:
- sessions
- compaction
- undo / redo
- snapshot behavior

Why it matters:
- strong fit for interrupted workflows and long gaps
- likely high practical leverage once basic behavior is trusted

Risk level:
- medium

### 3. MCP and external tool integration
Examples:
- local MCP servers
- remote MCP servers
- auth and timeout handling

Why it matters:
- expands the harness significantly
- can add real power

Risk level:
- medium-high
- especially high in a corporate local-first environment

### 4. Plugins and hook-based customization
Examples:
- tool execution hooks
- system/message transform hooks
- custom enforcement or logging behavior

Why it matters:
- maximum customization potential
- likely the strongest escape hatch when normal config is insufficient

Risk level:
- high
- more code-like, less config-like
- more maintenance burden

### 5. Legacy command surface and workflow entrypoints
Examples:
- custom commands
- command-like reusable workflows

Why it matters:
- can improve ergonomics

Risk level:
- high volatility
- spec direction suggests this area may be deemphasized in favor of skills

### 6. System-prompt surgery / experimental transforms
Examples:
- experimental system transform hooks
- trimming baked prompt layers

Why it matters:
- potentially useful for token and behavior control

Risk level:
- very high
- advanced, fragile, and version-sensitive

## Best Next Advanced Topics for This Repository

### Best next
1. `instruction-layering.md`
2. `mcp-and-tooling.md`
3. `session-control-and-recovery.md`

### Defer until needed
1. plugin deep dive
2. system-prompt transform experimentation
3. legacy command deep dive

## Practical Decision Rules

### Learn next if:
- the feature improves control, resumption, or local usefulness
- the feature is understandable after a long gap
- the feature can be adopted incrementally

### Defer if:
- it mainly adds cleverness
- it depends on unstable experimental hooks
- it increases supply-chain or network risk without a strong payoff

## Advanced-Feature Posture for This Repository
For this workflow, “advanced” should usually mean one of:
- more precise control
- safer extensibility
- better resume/recovery behavior

It should **not** mean:
- more hidden behavior
- more magic layers
- more hard-to-debug moving parts just because they exist

## Relationship to Other Notes
- `research/products/opencode/foundations.md`
- `research/products/opencode/config-surface-and-volatility-map.md`
- `research/products/opencode/permissions-and-agent-safety.md`

## Open Questions
- Which advanced surfaces are actually durable enough to incorporate into personal workflow?
- Is MCP worth adopting before session-control research is complete?
- Which advanced features are best treated as occasional tools rather than default workflow components?

## References
- Context7 `/anomalyco/opencode` — current docs/spec excerpts on agents, MCP, skills, permissions, and config direction.
