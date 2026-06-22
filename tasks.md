tier: jerryrig

## High-Level Plan
We will update the `opencode.jsonc` configuration file to individually disable the built-in native agents (`build`, `plan`, and `code-reviewer`) by setting `"disable": true` for each of them. This will prevent them from appearing in the tab completion or any other lists, leaving only your custom agents active.

## Blockers / Open Questions
- None

## Tasks Checklist
- [x] Task 1: Update opencode.jsonc (Configure native agents with disable: true and verify formatting)
