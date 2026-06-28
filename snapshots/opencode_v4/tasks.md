tier: script

## High-Level Plan
Restructure opencode configuration from 5 agents to 3 (planner, builder, antagonist). Merge best content from home and v3 setups. Absorb orchestrator into a shared skill, architect into review-plan skill, reviewer into review-code skill. Output 3 agent files, 21 skill files, AGENTS.md, and opencode.jsonc to opencode_v4/.

## Blockers / Open Questions
- None

## Tasks
- [x] **1. Write AGENTS.md**
  - **Description**: Merge home + v3 AGENTS.md. Absorb gen-pragmatic_engineer unique bits (boring solutions, loud failures, Windows compat anti-patterns). Add v3 communication style section.
  - **Tier**: script
  - **Files**: `opencode_v4/AGENTS.md`
  - **Acceptance**: File exists, contains all merged content, no duplication with my-context-v2.md.

- [x] **2. Write planner agent**
  - **Description**: Merge home + v3 planner. Absorb gen-tier_classifier into body. Add decisions.md responsibility. Use v3 permission schema. Add task delegation capability for orchestration.
  - **Tier**: script
  - **Files**: `opencode_v4/agents/planner.md`
  - **Acceptance**: Frontmatter has v3-style permissions with task.builder: allow. Body includes tier classification, decisions responsibility, artifact scaling.

- [x] **3. Write builder agent**
  - **Description**: Merge home + v3 builder. Add decisions.md awareness, decision conflict protocol, bash rules, in-progress marker.
  - **Tier**: script
  - **Files**: `opencode_v4/agents/builder.md`
  - **Acceptance**: Frontmatter has v3-style permissions. Body references builder-workflow and tier skills, includes decision conflict protocol and bash rules.

- [x] **4. Write antagonist agent**
  - **Description**: New agent combining architect + reviewer focus. Lean body — adversarial framing, two modes via skills. Same permissions as planner.
  - **Tier**: script
  - **Files**: `opencode_v4/agents/antagonist.md`
  - **Acceptance**: Frontmatter matches planner permissions. Body directs to review-plan or review-code skills. Can orchestrate via orchestrate skill.

- [x] **5. Write builder-workflow skill**
  - **Description**: Merge home builder-workflow with v3 gen-task_report. Add [-] in-progress marker, structured close-out format with "how to verify."
  - **Tier**: script
  - **Files**: `opencode_v4/skills/builder-workflow/SKILL.md`
  - **Acceptance**: Contains state continuity, [-] marker protocol, definition of done, structured task report with "what changed / how to run / how to verify / blockers."

- [x] **6. Write orchestrate skill**
  - **Description**: Extract from both orchestrator agents. Shared skill for planner and antagonist. Covers parsing tasks, handoff format, failure handling, final report.
  - **Tier**: script
  - **Files**: `opencode_v4/skills/orchestrate/SKILL.md`
  - **Acceptance**: Description mentions both planner and antagonist as users. Contains handoff format, failure protocol, final report template.

- [x] **7. Write review-plan skill**
  - **Description**: Merge architect agent body + gen-architecture_critique + gen-simplicity_enforcement. Pre-implementation design review. References tier-calibration.
  - **Tier**: script
  - **Files**: `opencode_v4/skills/review-plan/SKILL.md`
  - **Acceptance**: Contains audit parameters (assumptions, scope creep, gaps, YAGNI), complexity checklist from architecture_critique, simplicity checklist, output schema (PROCEED/AMEND/BLOCKED).

- [x] **8. Write review-code skill**
  - **Description**: Merge reviewer agent body + gen-senior_maintainer_review. Post-implementation code review. References tier-calibration.
  - **Tier**: script
  - **Files**: `opencode_v4/skills/review-code/SKILL.md`
  - **Acceptance**: Contains verification process, decisions compliance check, maintainability review (understandability, debuggability, fragility from senior_maintainer), output schema (PASS/REVISE with severity).

- [x] **9. Write format-tasks-md skill**
  - **Description**: Merge home format-tasks-md with v3 plan-task_write. Add depends_on, outcome fields, [-] state, agent field.
  - **Tier**: script
  - **Files**: `opencode_v4/skills/format-tasks-md/SKILL.md`
  - **Acceptance**: Schema includes all fields (number+title, description, tier, files, acceptance, agent, depends_on, outcome). Documents [-] state. Includes v3 example.

- [x] **10. Copy format-spec-md and format-architecture-md skills**
  - **Description**: Copy home versions as-is.
  - **Tier**: script
  - **Files**: `opencode_v4/skills/format-spec-md/SKILL.md`, `opencode_v4/skills/format-architecture-md/SKILL.md`
  - **Acceptance**: Files identical to home versions.

- [x] **11. Write merged tier skills**
  - **Description**: Merge home tier-jerryrig/poc/script/application with v3 gen-jerryrig/poc/script/application. Add v3 examples and unique guidance. Copy tier-calibration as-is.
  - **Tier**: script
  - **Files**: `opencode_v4/skills/tier-jerryrig/SKILL.md`, `opencode_v4/skills/tier-poc/SKILL.md`, `opencode_v4/skills/tier-script/SKILL.md`, `opencode_v4/skills/tier-application/SKILL.md`, `opencode_v4/skills/tier-calibration/SKILL.md`
  - **Acceptance**: Each tier skill contains home rules + v3 examples/unique content. No overlap with builder-workflow or tier-calibration.

- [x] **12. Copy standalone v3 skills with kebab-case rename**
  - **Description**: Copy gen-decisions, gen-debug-mode, gen-refactoring-mode, gen-dependency-police, gen-documentation-sync, gen-enterprise-auditability, gen-playwright-mode, gen-low-waste from v3. Rename to kebab-case. Update frontmatter name field.
  - **Tier**: script
  - **Files**: 8 SKILL.md files under `opencode_v4/skills/`
  - **Acceptance**: All 8 files exist with kebab-case names matching directory names. Frontmatter name fields updated.

- [x] **13. Copy gen-skill-creator**
  - **Description**: Copy home gen-skill-creator as-is.
  - **Tier**: script
  - **Files**: `opencode_v4/skills/gen-skill-creator/SKILL.md`
  - **Acceptance**: File identical to home version.

- [x] **14. Write opencode.jsonc**
  - **Description**: v3 as base. Update agent entries, skills path to v4, keep share/autoupdate/watcher/mcp config.
  - **Tier**: script
  - **Files**: `opencode_v4/opencode.jsonc`
  - **Acceptance**: Valid JSONC. Disables built-in build and plan agents. Skills path points to v4 skills. Contains share, autoupdate, watcher, mcp sections.
