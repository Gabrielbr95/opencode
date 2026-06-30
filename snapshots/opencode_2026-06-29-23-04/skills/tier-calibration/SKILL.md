---
name: tier-calibration
description: >-
  Tier-aware review and critique calibration tables. Use when reviewing,
  auditing, or critiquing code or plans against a tiered project in plan/tasks.md.
  Loaded by the antagonist to calibrate rigor per tier.
---

# Tier Calibration

Reference tables for calibrating review and critique rigor based on the active project tier.

## For Plan Review (Antagonist — review-plan mode)

| Tier | Calibration |
|------|-------------|
| **jerryrig** | Challenge only if the approach is completely unrunnable or takes >1 day. |
| **poc** | Focus on testing the core unknown. Flag over-design, unnecessary packages, or premature optimization immediately. |
| **script** | Enforce extreme simplicity (YAGNI). Challenge custom classes, deep nested structures, or external dependencies where stdlib suffices. |
| **application** | Rigorous architectural review. Check data flows, component boundaries, maintainability, CLI/UI layer isolation, and error diagnostics. |

## For Code Review (Antagonist — review-code mode)

| Tier | What to check | What to ignore |
|------|---------------|----------------|
| **jerryrig** | Runs and produces desired output. | Style, organization, logging, edge cases, tests. |
| **poc** | Core unknown is accurately isolated and resolved without high false-positive risk. | Code style, polish, structure. |
| **script** | Reliability, diagnostic logging, YAGNI compliance, defensive file/data guards. | Over-engineering, deep abstraction, comprehensive tests. |
| **application** | Folder architecture (flat + modular), user-facing error messages, edge-case handling, test coverage, documentation. | Nothing — full rigor applies. |

## Severity Categories

- **BLOCKER**: Actual bugs, syntax errors, run failures, plan violations.
- **MAJOR**: Logical gaps, missing logging/diagnostics (script+), missing key edge cases (application).
- **MINOR**: Suggestions, styling/polish, optional improvements.
