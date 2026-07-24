# opencode: Config Surface and Volatility Map

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, current docs excerpts, v2 config spec excerpts
- Product version: current docs snapshot plus dev v2 spec direction; exact installed local version not verified
- Stability: Low
- Recheck triggers:
  - schema changes
  - config docs changes
  - local behavior differs from docs
  - v2 config migration becomes official

## Scope
- Where opencode's config surface appears stable versus in motion
- Which areas look risky to depend on too hard right now
- How to read current docs without confusing them with future shape

## Why This Matters Here
- This repository wants durable understanding without pretending the product is static.
- opencode appears to have a real gap between current documented behavior and newer v2 spec direction.
- Without a volatility map, it is easy to over-learn the wrong shape.

## Current Findings
- The current docs and the v2 spec appear related but not fully aligned.
- Some features appear stable in principle but unstable in exact config naming.
- The important distinction is:
  - **stable concept**
  - **moving config shape**

## Highest-Drift Areas Seen So Far

### 1. Singular vs plural config keys
Examples seen in current docs/spec direction:
- `agent` -> `agents`
- `provider` -> `providers`
- `permission` -> `permissions`

Practical takeaway:
- the concept is stable
- the exact key names may not be

### 2. Commands vs skills
The v2 spec direction appears to remove user-defined `command` config as a first-class reusable workflow surface and push that role toward skills.

Practical takeaway:
- reusable workflows seem conceptually stable
- their preferred home is shifting

### 3. MCP config shape
Current docs and spec direction suggest drift in how MCP servers are nested and configured.

Example of the kind of shift seen:
- flatter keyed object in current usage
- `mcp.servers` nested structure in v2 direction

Practical takeaway:
- MCP as a capability is stable enough to study
- exact config shape looks volatile

### 4. Permission representation
There appears to be drift between:
- current object-shaped config patterns
- newer normalized ruleset thinking in v2/core permission logic

Practical takeaway:
- allow / ask / deny remains stable
- exact authored representation may move

### 5. Provider config surface
The provider concept looks stable.
The naming and surrounding policy surface may still evolve.

## Lower-Drift Areas to Learn First
These seem safer to treat as conceptual foundation even if the config keys move:

- opencode uses ambient instruction files
- opencode supports named agents
- opencode has permission boundaries
- opencode supports skills as reusable procedures
- opencode supports references as external context
- opencode can route to local or custom providers

These are the areas worth learning deeply before memorizing exact schemas.

## Practical Reading Rule
When reading opencode docs, classify each finding as one of:

### A. Stable product idea
Example:
- "skills are on-demand reusable procedures"

### B. Current config snapshot
Example:
- exact field names or nesting in today's docs

### C. Forward-looking spec direction
Example:
- v2 rename or structural redesign

This keeps the notes honest.

## What To Trust Most Right Now

### Trust more
- current runtime behavior
- current official docs for day-to-day use
- source excerpts when docs are ambiguous

### Trust carefully
- v2 spec direction as a signal of where churn may happen

### Do not confuse
- future direction with current guaranteed behavior

## Relevance to This Repository

### Document stable ideas separately from moving syntax
If a note is about:
- what agents are
- what permissions do
- why references matter

then it can stay fairly durable.

If a note is about:
- exact config keys
- exact nesting
- deprecated versus replacement fields

then it should carry strong freshness warnings.

### Avoid overcommitting to legacy command config
Since commands appear to be one of the surfaces most likely to shift, do not build too much mental or process structure around them.

### Use product notes as snapshots
This branch should record what appears true now, not claim timeless stability.

## Working Heuristic for Future Research
For any opencode feature, ask:

1. Is the concept stable even if the key names change?
2. Is this a current documented surface or a spec-direction surface?
3. Would I design around this for six months without checking again?
4. Does this belong in a foundation note or a volatility note?

## Relationships to Other Notes
- `research/products/opencode/foundations.md`
- `research/products/opencode/config-and-instruction-loading.md`
- `research/products/opencode/agents-permissions-and-skills-basics.md`

## Open Questions
- When will the v2 config direction become the practical default?
- Which current surfaces are legacy but still worth using today?
- Which features are stable enough to build personal workflow conventions around?

## References
- Context7 `/anomalyco/opencode` — current docs and v2 spec excerpts on config drift.
