# Task, Run, and Artifact Records

This note defines a shared record model for AI workflows.

Its purpose is to reduce drift between several nearby note families:
- sessions and durable execution
- observability and traces
- evaluation records
- durable artifacts and lineage

The main question is:

> What is the thing being done, what is the execution record of doing it, and what durable thing came out of it?

---

## Why This Note Exists

Different systems use different names for very similar objects:
- task
- flow
- run
- task run
- span
- artifact
- asset
- entity

Without a shared model, it becomes easy to blur:
- the definition of work
- the execution instance
- the observability trail
- the output or artifact record

This note is a synthesis layer because it bridges several existing concept, capability, and synthesis notes rather than replacing any one of them.

---

## Core Record Types

### 1. Work definition
The durable definition of a unit of work that can be executed.

Examples:
- a workflow definition
- a task type
- a repeatable procedure
- a named command or capability

Questions it answers:
- what kind of work is this?
- what inputs or preconditions does it expect?
- what should success look like?

### 2. Run record
One concrete execution instance of a work definition.

Questions it answers:
- when did this execution start?
- what state is it in now?
- what inputs, parent objects, or approvals shaped it?
- what happened during this run?

### 3. Artifact record
A durable thing produced, updated, or referenced by a run.

Examples:
- a generated document
- a changed file
- a summary
- an evaluation report
- a stored memory item

Questions it answers:
- what durable thing exists now?
- which run created or changed it?
- what version or location identifies it?

### 4. Event or observation record
A timestamped occurrence inside or around a run.

Examples:
- model call
- tool call
- approval event
- retry
- failure
- completion

Questions it answers:
- what happened during the run?
- in what order?
- with what status or metadata?

### 5. Lineage link
A relationship connecting work definitions, runs, artifacts, and events.

Examples:
- parent run -> child run
- run -> produced artifact
- artifact -> source artifact
- run -> evaluation result

Questions it answers:
- what came from what?
- what depends on what?
- what should be inspected when something looks wrong?

---

## Durable Distinctions

### Work definition vs run record
The work definition is the thing that can be executed.

The run record is one actual execution of it.

### Run record vs trace/span
A run record is an execution object.

A trace or span is an observability record of work that happened.

They are often correlated, but they are not the same object.

### Run record vs session
A session is a continuity container.

A run is a bounded execution instance that can often be paused, resumed, retried, completed, or failed.

### Artifact record vs run record
The artifact is the durable produced thing.

The run is the activity that produced, modified, or attempted to produce it.

### State snapshot vs event
State says where the run currently stands.

An event records something that happened on the way there.

### Hierarchy vs dependency vs lineage
- **Hierarchy** = parent/child execution structure
- **Dependency** = what must exist before work starts
- **Lineage** = what output was derived from what input

### Attempt vs run
A retry attempt may be modeled as:
- a new child run
- a run attempt inside one logical run

The important thing is to keep duplicate execution identity separate from fresh business intent.

### Control-plane record vs data-plane artifact
Control-plane records track scheduling, status, retries, approvals, and IDs.

Data-plane artifacts are the files, outputs, summaries, or stored records the run produces or mutates.

---

## Minimal Useful Schema

Not every workflow needs a heavy formal schema, but the minimum durable fields usually look like this.

### Work definition
- definition ID
- type or name
- declared purpose
- expected inputs
- expected outputs or success criteria

### Run record
- run ID
- work-definition ID
- parent run or triggering run if any
- created / started / ended timestamps
- current status
- actor / agent / workflow identity
- input references
- output references

### Artifact record
- artifact ID
- type
- location or storage reference
- version or revision marker
- producing run ID
- source references where relevant

### Event record
- event ID
- run ID
- time
- event type
- status or outcome
- metadata reference

### Lineage record
- source object ID
- target object ID
- relation type
- time or version boundary if relevant

---

## Why This Model Helps

### Debugging
It becomes easier to ask:
- which run created this bad output?
- which event showed the first failure?
- which artifact version did evaluation judge?

### Evaluation
Evaluation records can attach to:
- the work definition
- the run
- the produced artifact

This avoids mixing “what was supposed to happen” with “what happened in this specific instance.”

### Observability
Traces and spans become easier to interpret when they are clearly linked to run identity and artifact outcomes rather than treated as the whole data model.

### Durable execution
Pause/resume, retries, checkpoints, and approvals become easier to reason about when the run record is explicit.

### Provenance
Artifact lineage stays inspectable when outputs, source inputs, and producing runs are linked directly.

---

## Cross-Tool Correspondence Pattern

Different ecosystems name these objects differently, but the same shape keeps reappearing.

- workflow/task definition
- flow run/task run/activity
- trace/span/event
- artifact/asset/entity
- parent-child and input-output lineage links

The durable lesson is not the vendor vocabulary. The durable lesson is that execution identity, observability, and produced artifacts are separate but linked record families.

---

## Relationships to Other Notes
- `../syntheses/vocabulary.md`
- `../syntheses/observability-schema.md`
- `../concepts/durable-execution.md`
- `../concepts/observability-traceability.md`
- `../capabilities/eval-harnesses.md`
- `../capabilities/sessions.md`

## Relevance to This Repository
- This note gives the repository one place to normalize task, run, trace, and artifact language.
- It should reduce drift when future notes discuss task records, evaluation outputs, durable writes, or resumable workflows.
- It also sharpens a likely future gap area: task/artifact/run record models for local-first agent workflows.

## Open Questions
- What is the smallest record vocabulary this repository actually needs to standardize?
- When should retries become child runs versus attempts within one run?
- Which artifact types deserve durable lineage tracking versus lightweight reference links only?

## References
- W3C PROV overview — durable framing of entities, activities, and agents.
- OpenTelemetry traces docs — durable framing of trace/span/event relationships.
- MLflow tracking docs — useful example of run and artifact separation.
- Prefect flow/task docs — useful example of workflow definition, flow run, task run, and state.
- Dagster asset docs — useful example of durable produced artifacts and lineage.
