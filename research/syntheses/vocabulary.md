# Repository Vocabulary

This document defines the working vocabulary for the AI workflow research repository.

Its purpose is to reduce terminology drift, prevent false equivalences, and make later notes easier to compare.

## How to Use This Document
- Prefer these definitions when writing new research notes or workflow docs.
- If a source uses a term differently, note the source-specific meaning instead of silently changing the repository meaning.
- When two terms are easy to confuse, check the **Not the same as** line.

---

## Agent
An AI-driven worker that can decide among multiple next actions during execution rather than only following a fixed predefined sequence.

**Core idea:** dynamic control of process.

**Not the same as:** workflow, tool, skill, model.

**Boundary:** a tool-using script is not automatically an agent if the control flow is still fully predefined by code.

---

## Agent Architecture
The overall coordination structure of an AI system: who owns the task, who decides next steps, how work is delegated, how context is partitioned, and where stop conditions or reviews occur.

**Core idea:** system structure around agents, tools, memory, and control flow.

**Not the same as:** prompt wording, planning alone, model choice.

---

## Workflow
A predefined sequence or graph of steps whose main control logic is authored in code or configuration rather than decided dynamically by the model at runtime.

**Core idea:** fixed orchestration.

**Not the same as:** agent.

**Boundary:** workflows may still use models and tools, but the path is mostly known in advance.

---

## Orchestration
The runtime coordination of steps, workers, tools, or sub-processes in a workflow or agent system.

**Core idea:** who calls whom, in what order, with what handoffs.

**Not the same as:** planning.

**Boundary:** planning decides what should happen; orchestration is how the system coordinates it.

---

## Planning
Task decomposition and progress control: deciding subgoals, sequencing or parallelizing work, checking progress, and replanning when needed.

**Core idea:** how the task is broken down and revised.

**Not the same as:** chain-of-thought verbosity, orchestration, task tracking.

**Boundary:** a todo list can represent part of a plan, but is not the full planning system.

---

## Reasoning
The model’s internal or externalized process for drawing inferences, comparing options, or working through a problem.

**Core idea:** cognitive work, not necessarily visible.

**Not the same as:** planning.

**Boundary:** planning is one use of reasoning, but not all reasoning is planning.

---

## Tool
A callable capability that performs an action, query, or computation through a defined interface.

**Core idea:** action surface.

**Not the same as:** skill, memory, policy.

**Boundary:** a tool does something; it does not by itself explain when or why it should be used.

---

## Tool-Use Policy
The rules or guidance that shape when, why, and how the model should use tools.

**Core idea:** behavioral guidance for tool use.

**Not the same as:** permissions.

**Boundary:** policy influences decisions; runtime permission enforcement decides what actually executes.

---

## Permission / Authorization
The runtime control that allows or blocks an action, tool call, data access, or external effect.

**Core idea:** enforceable access boundary.

**Not the same as:** approval, policy.

**Boundary:** a tool call can be policy-compliant yet still blocked by permission rules, or schema-valid yet unauthorized.

---

## Approval
A workflow control point where a human or approval policy must explicitly allow execution to continue.

**Core idea:** gate before action.

**Not the same as:** authorization.

**Boundary:** approval is part of run control; authorization is part of security/access control.

---

## Guardrail
An automated check or constraint applied to inputs, outputs, tool calls, or intermediate states.

**Core idea:** automated safety/control layer.

**Not the same as:** HITL.

**Boundary:** a guardrail is automatic; HITL adds a human decision step.

---

## Human-in-the-Loop (HITL)
An explicit human intervention point in the workflow where a person can review, edit, approve, reject, override, or stop execution.

**Core idea:** human control at selected boundaries.

**Not the same as:** final-answer review only, guardrails, general monitoring.

---

## Handoff
Transfer of ownership of the active task or conversation from one agent/role to another.

**Core idea:** ownership change.

**Not the same as:** delegation.

**Boundary:** in delegation, the original manager still owns the final result.

---

## Delegation
Bounded assignment of sub-work to another worker, tool, or subagent while the original coordinator retains responsibility for the overall result.

**Core idea:** temporary bounded assistance.

**Not the same as:** handoff.

---

## Skill
A reusable capability bundle that packages procedural knowledge, instructions, resources, and sometimes scripts for on-demand use.

**Core idea:** reusable know-how loaded when relevant.

**Not the same as:** tool, subagent, memory.

**Boundary:** a skill teaches or supports how to do work; a tool performs an action.

---

## Subagent
A separate worker context with its own prompt, tool boundaries, and often a narrower responsibility.

**Core idea:** separate execution/context boundary.

**Not the same as:** skill.

**Boundary:** a skill augments one agent; a subagent creates a distinct worker.

---

## Prompt
The instruction and context text given to a model for a specific invocation or interaction.

**Core idea:** immediate model input.

**Not the same as:** skill, workflow, repository architecture.

**Boundary:** prompts are one layer of the system, not the whole system design.

---

## Prompt Engineering
The practice of designing prompts to improve model behavior for a specific task.

**Core idea:** better immediate model instructions.

**Not the same as:** context engineering.

**Boundary:** prompt engineering is a subset of context engineering, not the whole discipline.

---

## Context Engineering
The design of what information is presented to the model, tools, or workflow at each step, in what format, with what timing, and with what persistence behavior.

**Core idea:** information shaping and delivery.

**Not the same as:** prompt engineering, memory.

**Boundary:** memory may supply context, but context is the actual information made available for the current step.

---

## Context
The actual information available to the model or step at execution time.

**Core idea:** what the system sees right now.

**Not the same as:** all stored knowledge, memory.

---

## Memory
Information deliberately retained for future reuse across steps, tasks, or sessions.

**Core idea:** persistence with possible later recall.

**Not the same as:** context, retrieval, chat history alone.

**Boundary:** memory is what may persist; context is what is currently loaded.

---

## Retrieval
The process of selecting and fetching relevant external information for the current task.

**Core idea:** fetch useful evidence when needed.

**Not the same as:** memory.

**Boundary:** retrieval may operate over memory stores, documents, or external systems, but it is the fetching mechanism, not the persistence strategy.

---

## RAG (Retrieval-Augmented Generation)
A pattern where generation is supported by externally retrieved information.

**Core idea:** external evidence informs output.

**Not the same as:** full memory architecture.

**Boundary:** RAG can be part of memory or context design, but by itself it does not guarantee durable memory across sessions.

---

## Working Memory / Short-Term Memory
Task-local or thread-local state used during an active run or session.

**Core idea:** immediate continuity.

**Not the same as:** long-term memory.

---

## Long-Term Memory
Persistent information kept beyond a single run or session for reuse later.

**Core idea:** durable continuity.

**Not the same as:** current context window.

---

## Semantic / Episodic / Procedural Memory
- **Semantic memory:** facts, concepts, stable knowledge.
- **Episodic memory:** events, experiences, prior runs.
- **Procedural memory:** how to do recurring tasks.

**Core idea:** different memory types serve different purposes.

**Not the same as:** semantic search.

---

## Observability
The ability to understand what happened inside a system by examining traces, spans, logs, metrics, and structured metadata.

**Core idea:** inspect internal behavior from outside.

**Not the same as:** evaluation.

---

## Trace
The end-to-end record of one workflow run, request, or task execution.

**Core idea:** one complete path through the system.

**Not the same as:** log line, span.

---

## Span
A timed sub-operation inside a trace, such as a model call, retrieval step, tool call, or approval event.

**Core idea:** one meaningful step in the trace.

**Not the same as:** whole workflow trace.

---

## Traceability
The ability to link outputs, decisions, memory writes, or actions back to their sources and execution path.

**Core idea:** provenance and causal linkage.

**Not the same as:** reproducibility.

**Boundary:** a trace can explain what happened without guaranteeing the run can be replayed deterministically.

---

## Evaluation
The process of judging whether a prompt, agent, workflow, or run performed well according to explicit criteria.

**Core idea:** quality judgment.

**Not the same as:** observability, testing.

**Boundary:** observability records what happened; evaluation judges whether it was good.

---

## Testing
The practice of checking whether behavior meets expected conditions, often through repeatable cases, assertions, or regressions.

**Core idea:** verification against expectations.

**Not the same as:** evaluation.

**Boundary:** testing is often narrower and more assertion-driven; evaluation may use broader qualitative or comparative criteria.

---

## Offline Evaluation
Evaluation on curated examples, datasets, fixtures, or historical traces outside live production flow.

**Core idea:** controlled pre-release or retrospective judgment.

**Not the same as:** online evaluation.

---

## Online Evaluation
Evaluation of real production or live workflow runs, often without gold-reference answers.

**Core idea:** judgment under real operating conditions.

**Not the same as:** offline evaluation.

---

## Prompt Repository Architecture
The structure and rules for organizing prompts, instructions, skills, examples, templates, policies, and evals in a repository.

**Core idea:** how the prompt/agent repo is laid out and maintained.

**Not the same as:** a single prompt, a skill, or a config file.

---

## Policy-as-Code
Machine-enforceable policy represented in structured logic or configuration rather than only in natural-language instructions.

**Core idea:** enforcement-ready policy.

**Not the same as:** prompt policy text.

**Boundary:** a prompt can describe a rule; policy-as-code can actually enforce it.

---

## Durable Truth
The repository artifacts that should remain authoritative across sessions and interruptions.

**Core idea:** persistent source of truth.

**Not the same as:** temporary working notes, live chat context.

---

## Resume Baton
A short current-state summary meant to restart work after interruption without becoming the durable design log.

**Core idea:** lightweight continuation aid.

**Not the same as:** durable truth.

---

## Practical Boundary Rules
- If it **acts**, it is probably a **tool**.
- If it **teaches reusable procedure**, it is probably a **skill**.
- If it **persists for later reuse**, it is probably **memory**.
- If it **is loaded for the current step**, it is **context**.
- If it **judges quality**, it is **evaluation**.
- If it **records what happened**, it is **observability**.
- If it **enforces access or execution limits**, it is **permission/policy-as-code**.
- If a **human must decide**, it is **HITL/approval**.

## Related Documents
- Concept notes under `research/concepts/`
- `research/index.md`
- `research/backlog.md`
