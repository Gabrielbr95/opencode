# Pi Sessions and Compaction

## Freshness
- Last verified: 2026-07-28
- Verified against: Pi usage docs, sessions docs, compaction docs, settings docs
- Product version: current docs snapshot
- Stability: Medium
- Recheck triggers:
  - session format or tree behavior changes
  - compaction hooks/settings change
  - branch-summary behavior changes

## Scope
- Pi session persistence and branching model
- compaction and branch summarization behavior
- the main user-facing controls around resume and tree navigation

## Canonical Boundary
This note owns Pi's session and compaction behavior.

It is not the main home for:
- RPC protocol details
- general durable-execution theory
- extension-package add-ons that build extra state on top of sessions

## Why This Matters Here
- Resume behavior, branch structure, and compaction shape whether a harness can survive long interruptions and iterative work.

## Current Findings
- Pi stores sessions as tree-structured JSONL files.
- Sessions auto-save by working directory under `~/.pi/agent/sessions/` unless disabled.
- Pi supports continue, resume, new session, fork, clone, and in-file tree navigation.
- Pi has both auto-compaction and branch summarization.

## Session Storage and Commands

Documented startup/session flags:
- `-c` / `--continue`
- `-r` / `--resume`
- `--no-session`
- `--name`
- `--session <path|id>`
- `--fork <path|id>`

Documented session commands:
- `/resume`
- `/new`
- `/name <name>`
- `/session`
- `/tree`
- `/fork`
- `/clone`
- `/compact [prompt]`
- `/export [file]`
- `/share`

## Tree Model

Pi documents sessions as trees where:
- every entry has an `id` and `parentId`
- the current position is the active leaf
- `/tree` lets the user jump to previous points and continue from there within the same file

Selecting a prior user message rehydrates the prompt into the editor for a new branch. Selecting a non-user entry moves the leaf to that entry and leaves the editor empty.

## Compaction

Pi documents auto-compaction when context tokens exceed `contextWindow - reserveTokens`.

Relevant settings:
- `compaction.enabled`
- `compaction.reserveTokens`
- `compaction.keepRecentTokens`

The documented default behavior:
- keep a recent token window unsummarized
- summarize older messages
- append a `CompactionEntry`
- rebuild future context from the summary plus kept messages

Pi also documents extension hooks for custom compaction.

## Branch Summarization

Pi documents branch summarization during `/tree` navigation when switching away from one branch to another.

The documented purpose is preserving context from the abandoned branch by attaching a summary at the new position.

Related settings include:
- `branchSummary.reserveTokens`
- `branchSummary.skipPrompt`

## Stored Summary Structure

Pi docs describe both compaction and branch-summary entries as storing:
- summary text
- usage data when available
- details payloads
- file-operation tracking information in the default implementation

## Export and Sharing

Pi documents:
- HTML export via `/export`
- private GitHub gist sharing via `/share`

## Relationships to Other Notes
- `research/products/pi/foundations.md`
- `research/products/pi/providers-and-programmatic-surfaces.md`
- `research/capabilities/sessions.md`
- `research/concepts/durable-execution.md`

## Repository Relevance
- This note identifies the core resume, branch, and summarization behavior available in Pi without requiring add-ons.

## Open Questions
- Which additional session artifacts, if any, are needed on top of Pi's tree/session model for long-gap resumption in this repository?

## References
- [Using Pi](https://pi.dev/docs/latest/usage) — session commands and top-level behavior.
- [Sessions](https://pi.dev/docs/latest/sessions) — tree model, branching, resume, and session storage.
- [Compaction](https://pi.dev/docs/latest/compaction) — compaction and branch-summary mechanics.
- [Settings](https://pi.dev/docs/latest/settings) — compaction and branch-summary settings.
