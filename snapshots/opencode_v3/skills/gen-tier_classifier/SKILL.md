---
name: gen-tier_classifier
description: Load at the start of planning to determine the minimum execution tier required for a request.
---

# gen-tier_classifier

## When to load

Load at the beginning of any planning session, before proposing an approach or writing any artifacts. Determines the tier that sets rigor for all downstream agents.

## Tiers

| Tier | Purpose | Optimize for |
|---|---|---|
| `jerryrig` | Run once today, probably discarded tomorrow | Speed |
| `poc` | Answer "can this be done?" — throwaway code | Learning |
| `script` | Recurring personal automation | Simplicity |
| `application` | Small-team software, long-lived | Maintainability |

## Classification Rules

1. Always choose the **lowest tier that satisfies the stated requirements**.
2. Escalation must be justified — state the specific requirement that forces it.
3. When uncertain, choose the lower tier.
4. Audience and lifespan are the two strongest signals.

## Classification Questions

Ask yourself (not the user, unless genuinely ambiguous):

- Who runs it? Just the user → lower tier. Other people → higher.
- How often? Once → jerryrig. Repeatedly → script minimum.
- What if it breaks? Nobody notices → lower. Work stops → higher.
- Will it need to change? No → lower. Requirements will evolve → higher.
- Is feasibility unknown? Yes → poc before committing to any other tier.

## Output Format

```
Execution Tier: <tier>

Reasoning:
- Audience: <who runs or depends on this>
- Lifespan: <once / recurring / indefinite>
- Maintainability: <who maintains it, how often it will change>
- Risk: <consequence of failure>
- Escalation justification: <specific requirement forcing this tier, or "lowest tier fits">
```

## Examples

| Request | Tier | Why |
|---|---|---|
| Convert this one CSV to Excel | `jerryrig` | Run once, discarded after |
| Can Claude API handle 50-page PDFs? | `poc` | Feasibility unknown, throwaway code |
| Auto-rename downloaded reports each morning | `script` | Recurring, solo operator |
| Work order tracker for the team | `application` | Multi-user, long-lived, people depend on it |
| Scrape a page to check a value right now | `jerryrig` | One-off, no reuse intended |
| Extract data from 3 legacy systems into one view | `application` | Complex, team-facing, will evolve |
