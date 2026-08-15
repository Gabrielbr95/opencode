# Specification

## Objective
Create a POC migration plan for running OMP in a separate folder and configuring it to behave similarly to the current opencode harness, without replacing this repository or cutting over the active workflow.

## Core Requirements
- Treat this as a **parallel-run POC**, not a replacement project.
- Keep OMP in a separate folder and separate runtime/config area from this repository's active opencode harness.
- Optimize for answering: **can OMP be configured similarly enough to the current setup to be worth a practical side-by-side trial?**
- Use the current harness as the source reference for desired behavior, especially around:
  - ambient instructions and local context files
  - role separation
  - permission posture
  - MCP/tooling posture
  - workflow resumability and maintainability
- Prefer configuration and documented built-in OMP surfaces over custom OMP extension code for the first pass.
- Keep the initial target modest: OMP only needs to reach **similar-enough configuration behavior**, not full behavioral or feature parity.
- Preserve corporate-safety constraints:
  - no casual cloud/service sprawl
  - no unnecessary remote integrations
  - no hidden sharing/collaboration features enabled by default
  - explicit review of broad built-ins before trusting them
- Keep the current opencode repo and workflow untouched except for planning artifacts.
- Make the plan executable after a long interruption by recording the target folder split, config-mapping approach, and staged validation steps durably.

## Out of Scope (Crucial)
- No cutover from opencode to OMP inside this repository.
- No claim that OMP should become the default harness.
- No attempt to reproduce every opencode behavior or every repository-specific skill on the first pass.
- No custom OMP plugin/extension development unless the configuration-only path clearly fails and a later decision explicitly approves extension work.
- No broad multi-tool migration architecture covering Pi, OMP, and opencode together.
- No execution/setup work yet; this slice is planning only.

## User Interaction
The user will keep using this repository through opencode while a later session configures OMP in a separate folder. The plan should let the user build a side-by-side OMP setup that mirrors the current harness shape closely enough for comparison, without disturbing the active repo or requiring immediate cutover decisions.
