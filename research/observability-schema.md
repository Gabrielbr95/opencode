# Observability Schema

This document defines the minimum useful observability schema for this repository.

Its goal is not to recreate a full tracing standard. Its goal is to define the practical fields and event shapes that make this workflow easier to:

- debug
- audit
- evaluate
- resume after interruption
- connect actions back to their evidence

The design target is a local-first workflow with multi-step research and implementation work, bounded autonomy, and meaningful human checkpoints.

---

## Summary

The core rule is:

> **Trace the meaningful boundaries, not just the final answer.**

For this repository, useful observability must capture:

- one root record for a task or run
- meaningful sub-steps as structured events or spans
- links between actions, approvals, durable writes, and source artifacts
- enough provenance to explain what happened later

Flat logs of “prompt in, answer out” are not enough.

The schema should make it easy to answer:

1. what was the task?
2. who or what acted?
3. what tools or artifacts were touched?
4. what decisions, approvals, or blocks occurred?
5. what became durable?
6. what failed, and where?

---

## 1. Design Goals

This schema should optimize for:

- **inspectability** over maximal detail
- **structured linkage** over free-text storytelling
- **local usefulness** over platform-specific features
- **provenance** for decisions, memory writes, and file changes
- **resume support** after interruptions

It should avoid:

- storing large raw payloads by default
- tracing every trivial internal thought
- collecting sensitive content when identifiers or summaries are enough
- inventing a schema so rich that nobody keeps it consistent

---

## 2. Core Model

The minimum practical model has three layers:

### A. Session
A user-facing stretch of work, possibly covering several tasks.

Examples:
- a research session
- a debugging session
- a planning session

### B. Task Run
One bounded unit of work inside a session.

Examples:
- write `research/memory-policy.md`
- update `plan/tasks.md`
- run a review pass

### C. Event or Span
One meaningful step inside the task run.

Examples:
- read source docs
- draft a file
- ask for clarification
- run a tool
- record a decision
- request approval
- write durable memory

For this repository, the important thing is consistent boundaries, not whether the storage backend calls them spans, events, traces, or records.

---

## 3. Required Root Fields

Every task run should have a root record with at least these fields.

| Field | Purpose |
|---|---|
| `session_id` | Links related work done in the same user session. |
| `task_run_id` | Unique identifier for this bounded unit of work. |
| `task_label` | Human-readable task name, such as “Task 23 observability schema”. |
| `task_type` | Planning, research, implementation, review, debugging, wrap-up, etc. |
| `tier` | Jerryrig, POC, Script, or Application. |
| `owner` | Primary actor responsible for the run. |
| `status` | Started, in_progress, completed, blocked, failed, cancelled. |
| `start_time` | When the run began. |
| `end_time` | When the run ended, if complete. |
| `repo_scope` | The files, folders, or subsystem claimed as in scope. |
| `goal` | Short statement of intended outcome. |
| `result_summary` | Short statement of what actually happened. |

These root fields are enough to anchor all subordinate events.

---

## 4. Required Event Fields

Each meaningful event inside a task run should include at least:

| Field | Purpose |
|---|---|
| `event_id` | Unique event identifier. |
| `task_run_id` | Parent task run. |
| `event_type` | Read, write, tool_call, decision, approval, memory_write, failure, etc. |
| `actor` | Who performed or initiated the event. |
| `timestamp` | When the event occurred. |
| `status` | Proposed, started, succeeded, failed, blocked, skipped. |
| `summary` | Short plain-language description. |
| `artifacts` | Files, docs, tools, or resources touched. |
| `source_refs` | What evidence or source material informed this step. |

Optional but often useful:

- `duration_ms`
- `parent_event_id`
- `linked_event_ids`
- `risk_class`
- `approval_state`
- `error_code`
- `redaction_level`

---

## 5. Canonical Event Types

These are the main event types worth standardizing.

### A. `context_read`
Reading files, notes, plans, research docs, or other local artifacts.

Useful fields:
- `artifacts`
- `read_scope`
- `selection_reason`

### B. `plan_update`
Changing task tracking, task state, or declared slice status.

Useful fields:
- `artifacts`
- `old_state`
- `new_state`
- `task_number`

### C. `tool_call`
Calling a tool or externalized capability.

Useful fields:
- `tool_name`
- `tool_mode`
- `arguments_summary`
- `result_summary`
- `exit_status`

### D. `decision_recorded`
Capturing a durable or semi-durable decision.

Useful fields:
- `decision_summary`
- `decision_scope`
- `decision_basis`
- `source_refs`

### E. `approval_checkpoint`
A run crossed a boundary requiring user or policy approval.

Useful fields:
- `approval_reason`
- `approval_type`
- `approval_state`
- `resume_condition`

### F. `human_intervention`
The human reviewed, edited, clarified, rejected, or redirected work.

Useful fields:
- `intervention_type`
- `human_action_summary`
- `affected_scope`

### G. `memory_write`
Something was promoted into durable or semi-durable memory.

Useful fields:
- `memory_type`
- `target_artifact`
- `write_basis`
- `provenance_status`
- `review_state`

### H. `artifact_write`
A file or durable artifact was created or changed.

Useful fields:
- `artifacts`
- `change_kind`
- `authoritative_or_draft`
- `verification_method`

### I. `failure`
Something failed or produced blocking uncertainty.

Useful fields:
- `failure_stage`
- `failure_reason`
- `error_summary`
- `next_action`

### J. `evaluation_result`
A judgment about quality or correctness.

Useful fields:
- `evaluation_method`
- `criteria`
- `outcome`
- `linked_artifact`

Not every task needs every event type, but these give a stable vocabulary for meaningful boundaries.

---

## 6. Actor Schema

Every root record and event should identify the actor clearly enough to support audit and debugging.

Minimum useful actor fields:

- `actor_type` — user, primary_agent, subagent, tool, external_system
- `actor_name` — generalist, reviewer, bash, read, user, etc.
- `actor_role` — planner, implementer, reviewer, approver, observer

Why this matters:
- ownership and delegation are part of architecture
- debugging depends on knowing who decided versus who executed
- approvals and durable writes need stronger attribution than ordinary drafting

---

## 7. Artifact Reference Schema

Observability should point to artifacts without requiring full content capture.

Minimum useful artifact fields:

- `path`
- `artifact_kind` — plan, research_note, config, source_code, task_list, resume_baton
- `operation` — read, create, update, delete, inspect
- `authoritative` — yes/no

Optional useful fields:

- `line_range`
- `version_hint`
- `change_summary`

Prefer references to artifacts over copying large raw content into traces.

---

## 8. Provenance and Linkage Fields

Observability should preserve causal links, especially for consequential actions.

Important linkage fields:

- `source_refs` — what evidence informed the action
- `decision_refs` — which prior decision justified it
- `approval_refs` — which approval gate allowed it
- `memory_refs` — which durable memory item it used or created
- `evaluation_refs` — which review or eval judged it
- `followup_refs` — what later step continues from this one

This is what turns a pile of events into a traceable workflow record.

---

## 9. Required Coverage Boundaries

For this repository, observability is most useful when it covers these boundaries by default:

### Always worth tracing
- task start and completion
- task status transitions
- source reads that materially shaped the work
- artifact writes
- decisions that affect future work
- failures and block reasons

### Strongly recommended
- tool calls
- approval checkpoints
- human interventions
- durable memory writes
- review outcomes

### Optional or sampled
- repetitive low-risk reads
- very small intermediate draft steps
- verbose internal notes that add no diagnostic value

The rule is to trace what changes understanding, control, or durable state.

---

## 10. Redaction and Content Capture Rules

Because this is a local-first corporate workflow, observability must not assume that full raw content should always be stored.

### Default capture preference
Prefer:
- IDs
- file paths
- summaries
- argument summaries
- decision labels

over:
- full prompt text
- full file contents
- raw sensitive data
- copied corporate documents

### Content levels

Suggested `redaction_level` values:

- `none` — safe to store as-is
- `summary_only` — store summary, not raw payload
- `metadata_only` — store identifiers and status only
- `sensitive` — restricted handling or no retention

### Default heuristic
If the raw content is not needed to explain the decision, store metadata and provenance instead.

---

## 11. Retention Guidance

Not all observability data deserves the same lifetime.

### Keep longer
- task root records
- decisions
- approvals
- durable memory writes
- failures and blockers
- evaluation outcomes tied to durable changes

### Keep shorter or summarize
- repetitive read events
- verbose tool output summaries
- low-value intermediate drafting steps

### Safe default
Retain the records needed to explain durable changes and meaningful failures. Summarize or discard the rest.

---

## 12. Minimal Example Shape

### Root record

```json
{
  "session_id": "sess-2026-07-23-a",
  "task_run_id": "task-23-observability-schema",
  "task_label": "Write observability schema note",
  "task_type": "research",
  "tier": "POC",
  "owner": "generalist",
  "status": "completed",
  "start_time": "2026-07-23T10:00:00Z",
  "end_time": "2026-07-23T10:18:00Z",
  "repo_scope": [
    "plan/tasks.md",
    "research/topics/observability-traceability.md",
    "research/observability-schema.md"
  ],
  "goal": "Define the minimum useful observability schema for this repository.",
  "result_summary": "Created research/observability-schema.md and grounded it in existing synthesis notes."
}
```

### Event record

```json
{
  "event_id": "evt-003",
  "task_run_id": "task-23-observability-schema",
  "event_type": "artifact_write",
  "actor": {
    "actor_type": "primary_agent",
    "actor_name": "generalist",
    "actor_role": "researcher"
  },
  "timestamp": "2026-07-23T10:12:00Z",
  "status": "succeeded",
  "summary": "Created research/observability-schema.md.",
  "artifacts": [
    {
      "path": "research/observability-schema.md",
      "artifact_kind": "research_note",
      "operation": "create",
      "authoritative": true
    }
  ],
  "source_refs": [
    "research/topics/observability-traceability.md",
    "research/control-boundaries.md",
    "research/principles-only.md",
    "research/memory-policy.md"
  ]
}
```

---

## 13. Practical Default Event Set for This Repository

If this repository implements observability later, the minimum default event set should be:

1. `task_started`
2. `context_read`
3. `plan_update`
4. `tool_call`
5. `artifact_write`
6. `decision_recorded`
7. `approval_checkpoint`
8. `human_intervention`
9. `memory_write`
10. `failure`
11. `evaluation_result`
12. `task_completed`

That is enough to explain most consequential behavior without tracing everything.

---

## 14. Common Failure Modes

### 1. Capturing only final outputs
This hides the path that produced the result.

### 2. Logging raw content without structure
This creates search pain, privacy risk, and weak linkage.

### 3. Missing approval and HITL events
This makes it hard to audit consequential boundaries.

### 4. Missing durable-write events
This weakens memory provenance and correction.

### 5. Over-instrumenting low-value noise
This raises cost and makes real signals harder to find.

### 6. Using event names inconsistently
This ruins comparison across runs.

---

## 15. Schema Test Questions

Before adopting or expanding observability, ask:

1. Can this schema explain a failure end to end?
2. Can it show who approved or changed something consequential?
3. Can it connect durable writes back to source evidence?
4. Can it support session resumption after interruption?
5. Is it collecting more raw content than actually needed?
6. Will the event types stay stable enough for repeated use?

If the answer to the first four is no, the schema is too weak. If the answer to the fifth is yes, it is probably too heavy.

---

## Relationship to Other Documents

- `research/topics/observability-traceability.md`
- `research/control-boundaries.md`
- `research/principles-only.md`
- `research/memory-policy.md`
- `research/topics/evaluation-prompt-testing.md`
