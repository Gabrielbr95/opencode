tier: script

## High-Level Plan
We will refactor and improve all 7 custom agent prompts (`agents/*.md`) by introducing clean, standard frontmatter configuration for permissions and tools, eliminating redundant constraint-checking text, enforcing state tracking via `tasks.md` across all tiers, and tailoring the behavioral prompts for robust engineering workflows.

## Blockers / Open Questions
- None

## Tasks Checklist
- [x] Task 1: Refactor planner.md (Add todowrite tool support, user-disambiguation, scientific/engineering Python stack priorities, and clean redundancy)
- [x] Task 2: Refactor architect.md (Soften tone to prevent critic's trap, allow constructive architectural suggestions in text, and clean redundancy)
- [x] Task 3: Refactor reviewer.md (Set permissions to ask, allow bash execution for verification, and clean redundancy)
- [x] Task 4: Refactor jerryrig.md (Add execution frontmatter, require reading tasks.md, clarify "zero polish" safety checks, and add completion update)
- [x] Task 5: Refactor poc.md (Add execution frontmatter, require reading tasks.md, add assumption tracking/stub commenting, and add completion update)
- [x] Task 6: Refactor script.md (Add execution frontmatter, allow print for CLI feedback, make argparse optional, and ensure tasks.md read/write)
- [x] Task 7: Refactor application.md (Add execution frontmatter, enforce flat modular structure guidelines, define asset update behaviors, and ensure tasks.md read/write)
