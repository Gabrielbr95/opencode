# opencode Foundations

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, dev source excerpts
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Low-Medium
- Recheck triggers:
  - major config schema changes
  - agent/permission doc changes
  - local behavior differs from docs

## Scope
- short product mental model for opencode
- the main control surfaces that shape day-to-day behavior
- the boundary between foundational understanding and more advanced branch notes

## Canonical Boundary
This note is the branch mental model.

It is not the main home for:
- durable instruction-layer theory
- general permission or memory concepts
- ranked product roadmap decisions already tracked elsewhere in the branch

## Why This Matters Here
- opencode is the active harness in this repository.
- A short mental model reduces re-learning cost before diving into narrower product notes.

## Current Findings
- opencode is not just a chat interface; it is a configurable harness with:
  - instruction loading
  - named agents
  - permission control
  - skills
  - references
  - provider routing
  - MCP support
  - plugins and hooks
- The most reusable understanding starts with the ordinary control surfaces rather than the most experimental ones.

## Core Product Model

### 1. Ambient instructions
Always-on guidance loaded from files such as `AGENTS.md` and configured instruction sources.

### 2. Agents
Named workers with their own prompt, model, mode, and permissions.

### 3. Permissions
Runtime control over what tools and actions are allowed, denied, or require asking.

### 4. Skills
On-demand procedural modules loaded when relevant rather than injected all the time.

### 5. References
Named external context roots such as local directories or Git repositories.

### 6. Providers
The model backends opencode can call, including local and OpenAI-compatible endpoints.

### 7. Extensions
MCP servers, plugins, and commands expand the harness further, but they sit on top of the earlier layers.

## More Stable vs More Volatile Learning Surfaces

### Relatively stable surfaces
- instruction loading as a category of behavior
- named agents
- permission envelopes
- skills as reusable procedural modules
- references as explicit external context roots

### More volatile surfaces
- plugins and experimental hooks
- deeper MCP integration details
- exact config key naming during spec transitions
- legacy command/config surface details

## Relationships to Other Notes
- `research/products/opencode/README.md`
- `research/products/opencode/config-and-instruction-loading.md`
- `research/products/opencode/advanced-features-map.md`
- `research/concepts/agent-architectures.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`
- `research/concepts/prompt-modularity-repository-architecture.md`
- `research/concepts/skill-systems.md`

## Repository Relevance
- This note is the shortest product-level re-entry point for the opencode branch.
- Notes that need to explain opencode-specific behavior should point here for the basic mental model, then narrow to their own topic.
- The branch roadmap lives in `advanced-features-map.md`, not here.

## Open Questions
- Which parts of the current product surface are stable enough to rely on for long periods?
- Which defaults are too permissive for a corporate local-first setup?
- Which customization belongs in config versus AGENTS.md versus skills?

## References
- Context7 `/anomalyco/opencode` — current docs/source excerpts used for this note.
- `research/products/opencode/system-prompt-control.md` — advanced branch note on system prompt transformation hooks.
