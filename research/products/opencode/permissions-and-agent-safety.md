# opencode: Permissions and Agent Safety

## Freshness
- Last verified: 2026-07-24
- Verified against: Context7 `/anomalyco/opencode`, permission/core source excerpts, current docs excerpts
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Medium-Low
- Recheck triggers:
  - permission semantics change
  - default built-in agent behavior changes
  - external-directory handling changes

## Scope
- How permissions appear to shape agent safety in opencode
- Which defaults matter most for a cautious local-first workflow
- What to understand before granting more autonomy

## Canonical Boundary
This note is for **runtime safety posture**:
- permission semantics
- external boundary effects
- practical safe-baseline reasoning

It assumes the structural mental model from:
- `research/products/opencode/agents-permissions-and-skills-basics.md`

## Why This Matters Here
- This repository cares a lot about controllable, understandable behavior.
- The most useful question is not whether opencode supports powerful actions, but how narrowly those actions can be bounded.

## Current Findings
- Permissions appear to be the main runtime safety mechanism in opencode.
- Allow / ask / deny semantics seem stable even if config shape changes.
- Agent safety is not just about the agent prompt; it depends heavily on the permission envelope.

## Core Safety Model

### Agent
Defines the worker identity and role.

### Permission
Defines what that worker may do.

### Result
The real safety posture comes from the combination, not from role text alone.

## Default Safety Signals Found in Source
Current source excerpts suggest:
- default `external_directory` posture is `ask`
- general read access appears broad by default
- `.env` and similar sensitive files get more caution than ordinary files
- `doom_loop` is not simply left wide open
- built-in agents do not all inherit exactly the same envelope

Practical takeaway:
- opencode has meaningful safety structure
- but some defaults may still be broader than a cautious user wants

## Important Permission Behaviors

### `allow`, `ask`, `deny`
- `allow` = proceed
- `ask` = stop for approval
- `deny` = block

### Pattern-based matching
Permissions appear to match actions/resources by wildcard patterns.

### Later match / merged rule effects
Current permission logic suggests later matching rules can override earlier ones within the evaluated ruleset.

### Deny still matters strongly
The evaluation logic appears to preserve strong deny behavior when a denied resource is involved.

## External Directory Safety
This is one of the most important boundaries for this environment.

Current source excerpts suggest:
- outside-worktree paths become `external_directory` authorization events
- default arbitrary external access is `ask`
- some reference/skill/temp paths may be whitelisted automatically

Practical takeaway:
- outside-repo access deserves explicit attention
- references and permissions should be thought about together

## Built-In Agent Safety Difference
Current source excerpts suggest at least this distinction:

### Build-style agent
- inherits broader working defaults

### Plan-style agent
- edit is more restricted
- some planning-specific directories may still be allowed

Practical takeaway:
- opencode already embodies the idea that not all agents should have the same side-effect envelope

That is a useful product-level confirmation of a broader harness principle.

## Practical Safety Recommendations for This Repository

### 1. Start narrower than the product defaults
Even if defaults are usable, a corporate/local-first workflow should probably begin stricter.

### 2. Separate read-heavy roles from edit-heavy roles
If a role is mainly for exploration, review, or research, let its permissions reflect that.

### 3. Be explicit about external boundaries
Treat `external_directory` as a first-class decision, not a minor detail.

### 4. Be careful with saved approvals
If user approvals are persisted or appended into the effective ruleset, they can shape later behavior more than expected.

### 5. Treat prompt safety and permission safety as different layers
A careful prompt is useful, but it does not replace runtime permission control.

## Suggested Safe Baseline to Think About
Not a final config, just a direction for reasoning:

- broad destructive autonomy: no
- `bash`: usually ask
- `edit`: usually ask unless the task is tightly scoped
- `external_directory`: ask by default
- sensitive file patterns: tighter than ordinary files
- read-only or review agents: narrower than build agents

## Product Drift Warning
The exact config representation may change.
The safer durable understanding is:

- permission boundaries are central
- per-agent envelopes matter
- external access needs special treatment

## Relationship to Other Notes
- `research/products/opencode/agents-permissions-and-skills-basics.md`
- `research/products/opencode/references-and-external-context-basics.md`
- `research/syntheses/control-boundaries.md`
- `research/concepts/tool-use-policy-and-permission-systems.md`

## Open Questions
- What is the best practical safe baseline for this exact environment?
- Which built-in defaults are already sufficient, and which should be tightened?
- How visible are saved permission decisions during long-gap resumption?

## References
- Context7 `/anomalyco/opencode` — permission logic, external-directory handling, and built-in agent permission excerpts.
