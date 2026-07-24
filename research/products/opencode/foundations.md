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
- What opencode appears to be, at a practical level
- Which control surfaces matter before chasing advanced features
- Which areas seem stable enough to learn first

## Branch Boundary
This note is the short product mental model.

For reusable cross-tool explanations, prefer:
- `research/concepts/instruction-layering.md`
- `research/capabilities/context-attachments.md`
- `research/capabilities/model-routing.md`
- `research/capabilities/sessions.md`
- `research/capabilities/mcp.md`

## Why This Matters Here
- This repository already uses opencode as the active harness.
- Before researching advanced features, it helps to understand the basic control model: where instructions come from, how agents are shaped, and where permissions sit.

## Current Findings
- opencode is not just a chat UI. It is a configurable coding harness with:
  - instruction loading
  - agent roles
  - permission control
  - skill loading
  - references
  - provider routing
  - MCP support
  - plugin hooks
- The most important learning surfaces do **not** seem to be the flashy ones.
- For practical use, the foundation appears to be:
  1. config loading and precedence
  2. instruction layering
  3. agents and permissions
  4. skills
  5. references

## Core Product Model

### 1. Ambient instructions
Always-on guidance loaded from files such as `AGENTS.md` and configured instruction sources.

### 2. Agents
Named workers with their own prompt, model, mode, and permissions.

### 3. Permissions
The runtime control layer that decides what tools/actions are allowed, denied, or require asking.

### 4. Skills
On-demand procedural modules loaded when relevant, rather than injected all the time.

### 5. References
Named external context sources such as local directories or Git repositories.

### 6. Providers
The model backends opencode can call, including local or OpenAI-compatible endpoints.

### 7. Extensions
MCP servers, plugins, and commands extend the harness further, but they are not the first layer to master.

## Practical Reading Rule
Start with the short product notes that explain current opencode behavior.
When a note starts feeling cross-tool, jump up to the matching capability note instead of repeating the same explanation here.

## Likely Stable vs Volatile Areas

### More stable to learn first
- AGENTS/rules style instruction layering
- named agents
- permission boundaries
- skills as reusable procedural modules
- references as external context

### More volatile or advanced
- plugins
- experimental hooks
- deeper MCP integration shape
- exact config key naming during spec transitions
- command surface and legacy config forms

## Practical Recommendation
For now, treat opencode primarily as a harness with five main questions:

1. What context does it load automatically?
2. Which agent is active?
3. What is that agent allowed to do?
4. Which skills are available and when are they loaded?
5. Which external sources can it read from safely?

If those are clear, the advanced features become easier to evaluate.

## Relationship to General Concepts
- `research/concepts/agent-architectures.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`
- `research/concepts/prompt-modularity-repository-architecture.md`
- `research/concepts/skill-systems.md`

## Relationship to Capabilities
- `research/concepts/instruction-layering.md`
- `research/capabilities/context-attachments.md`
- `research/capabilities/model-routing.md`
- `research/capabilities/sessions.md`
- `research/capabilities/mcp.md`

## Open Questions
- Which parts of the current product surface are stable enough to rely on for long periods?
- Which defaults are too permissive for a corporate local-first setup?
- Which customization belongs in config versus AGENTS.md versus skills?

## References
- Context7 `/anomalyco/opencode` — current docs/source excerpts used for this note.
- `research/products/opencode/system-prompt-control.md` — later advanced/unverified branch.
