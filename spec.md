# Specification: Custom Agent Prompt Improvements

## Goal
Improve the set of Opencode custom agents to establish rigorous file-specific frontmatter permissions, robust state continuity, context-aware instructions, and optimal alignment with engineering workflows.

## Precise Scope

### 1. Frontmatter Configuration
Add or standardize YAML frontmatter for all agent markdown files under `agents/` to control tools and permissions in Opencode.
* **Execution Agents (`jerryrig.md`, `poc.md`, `script.md`, `application.md`)**:
  * Set `tools`: `write: true`, `edit: true`, `bash: true`.
  * Set `permission`: allow read, edit, write, and bash execution (`**/*: allow` or `ask` as appropriate).
* **Reviewer Agent (`reviewer.md`)**:
  * Set `tools`: `write: true`, `edit: true`, `bash: true`.
  * Set `permission`: deny edit/write of code files (or set to `ask`), allow bash execution to run/test code, and ask for editing markdown files.

### 2. State Continuity & Tasks Checklist
* Mandate that **all** agents (including `jerryrig` and `poc`) check and read `tasks.md` upon initialization.
* Instruct all execution agents to update `tasks.md` upon completion of a task.

### 3. Human-In-The-Loop Pipeling
* Restrict agents from executing transition actions automatically.
* Instead, instruct them to explicitly output recommendations to the human on which agent to invoke next (e.g., *"Next recommended step: run the Code Reviewer agent via [command]..."*).

### 4. Agent-Specific Optimizations
* **`planner.md`**: Enable the `todowrite` tool for maintaining system task state. If no tier is specified by the user, explicitly ask before selecting one. Emphasize native engineering/scientific Python stacks (e.g., scipy, numpy, pandas, matplotlib, streamlit).
* **`architect.md`**: Adjust tone to prevent over-negativity ("Critic's Trap") and hallucinating non-existent risks. Guide the agent to provide constructive design suggestions/alternatives in text without writing code files.
* **`reviewer.md`**: Permit executing verification commands via bash, while restricting code modifications.
* **`jerryrig.md`**: Clarify that "zero polish" does not mean buggy/broken code; require basic syntax and import checks before completing.
* **`poc.md`**: Require explicit tracking of technical assumptions, and adding `# POC ONLY` comments on stubbed components.
* **`script.md`**: Permit `print` for primary console/CLI feedback. Make `argparse` optional and context-dependent (prefer variables at the top of the file for simple workflows).
* **`application.md`**: Focus on flat, modular folder architectures. Require updating `pyproject.toml`, `requirements.txt`, and `README.md` only when they already exist or are specifically needed, rather than creating them from scratch.

## Success Criteria
1. Every markdown file in `agents/` conforms to a clean, non-redundant, structured system of frontmatter configuration and instruction body.
2. The custom agents correctly understand their tool permissions, run environments, and role expectations.
3. State files (`tasks.md`) are consistently read and updated.
