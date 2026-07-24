# Tool Calling

## Freshness
- Last reviewed: 2026-07-24
- Stability: Medium
- Likely drift areas:
  - vendor-specific schema strictness and convenience helpers
  - protocol details for remote tool exposure and result transport

## Summary
- Structured action contracts are the machine-readable boundary between model intent and real execution.
- The durable idea is not any one vendor's "function calling" or "tool use" feature. It is the need for explicit callable actions with stable names, structured inputs, clear result correlation, and runtime control around execution.
- Reliable tool invocation depends on separating three things clearly:
  - the **action contract**
  - the **tool call event**
  - the **tool result**

## Motivation
- Tool use is now a normal capability across agent systems, but the reusable engineering problem is still often hidden inside vendor API branding.
- This repository already has strong concept coverage for tool policy and permissions. What it lacked was the capability-layer note explaining how callable actions should be shaped before product-specific implementation details enter the picture.

## Problem Statement
- A model can want to act, but real execution only becomes dependable when the callable surface is explicit and machine-checkable.
- Without structured action contracts, systems become vulnerable to:
  - ambiguous tool choice
  - malformed arguments
  - hidden side effects
  - brittle orchestration loops
  - poor auditability
  - confusing retries and failure handling

## Core Function
- Declare callable actions in a way both the model and the runtime can use.
- Constrain tool invocation to explicit names, inputs, and result channels.
- Make runtime validation, authorization, execution, and tracing possible.

## Minimal Durable Model

### 1. Action contract
Defines what can be called.

Minimum useful fields:
- stable action/tool name
- short description of purpose
- structured input schema

Often also useful:
- output schema
- side-effect class
- idempotency expectations
- timeout or retry expectations
- auth or permission scope

### 2. Tool call event
Defines a specific attempted invocation.

Typical fields:
- action name
- arguments
- correlation/call ID
- calling context or task/run ID

### 3. Tool result
Defines what came back from execution.

Typical fields:
- correlation/call ID
- success/error status
- structured result payload or error payload
- provenance or execution metadata

This separation is one of the most durable distinctions in the whole space.

## Invocation Lifecycle
The portable invocation loop looks roughly like this:

1. declare callable actions
2. model emits one or more tool calls
3. runtime validates the proposed call
4. runtime authorizes the call
5. runtime executes the call
6. runtime returns correlated results
7. model continues, retries, or finishes

Convenience SDKs may hide parts of this loop, but the loop still exists.

## Common Patterns
- JSON-schema-style input contracts
- explicit tool name plus arguments object
- call ID / correlation token for associating outputs with calls
- strict validation before execution
- model-call / runtime-execute split
- local tool execution versus remote protocol-mediated execution
- read-only versus side-effecting action classes
- multi-turn invocation loops where tool results re-enter model context

## Typical Components
- action registry
- schema validator
- authorization or permission check
- execution adapter
- error envelope
- trace/event logging
- correlation IDs
- retry/timeout handling

## Durable Distinctions

### Action contract vs tool call event vs tool result
These are related, but not the same object.

### Input schema validity vs execution validity
A schema-valid call can still be unsafe, unauthorized, or semantically wrong.

### Model-selected call vs runtime-approved execution
The model may propose an action; the runtime still decides whether it runs.

### Structured output formatting vs tool invocation
Structured output is about formatting model output.
Tool invocation is about requesting external execution.

### Client-side/local tools vs server-managed tools vs protocol-exposed tools
The responsibility boundary changes who owns security, networking, reliability, and auditability.

### Read-only / idempotent vs destructive / non-idempotent
Side-effect semantics matter as much as argument shape.

## Contract Design Heuristics

### Keep action names narrow and unambiguous
If two tools sound interchangeable, the model will treat them that way.

### Put selection clues in the description
The description should answer:
- when to use this action
- when not to use it
- what inputs are required

### Treat output shape as a first-class contract when downstream automation depends on it
Many systems focus harder on input schemas than output schemas.
That is acceptable for loosely human-reviewed workflows, but weaker for automation.

### Encode side-effect semantics explicitly
At minimum, a contract should make it obvious whether the action is:
- read-only
- reversible internal mutation
- durable internal mutation
- external side effect

### Prefer fewer better actions over large vague catalogs
Too many tools degrade selection quality and enlarge prompt/context surface.

## Portability
- Portable across tools:
  - explicit callable actions beat implied behavior
  - structured arguments improve reliability
  - call/result correlation matters in multi-step loops
  - runtime validation and authorization remain necessary even with strict schemas
  - side-effect classes should shape control policy
- Vendor-shaped:
  - exact JSON schema dialect or strictness rules
  - automatic schema generation helpers
  - result transport shape
  - built-in versus client-executed tool boundaries
  - protocol details for remote tool exposure

## Advantages
- clearer model-to-runtime boundary
- fewer malformed calls
- easier validation and auditing
- more testable tool behavior
- cleaner permission and approval integration
- better traceability for multi-step workflows

## Risks / Failure Modes
- underspecified or overlapping tool descriptions
- schemas that are too loose to prevent ambiguity
- assuming schema-valid means safe or correct
- failing to correlate results to the original call
- returning free text where structured downstream handling is needed
- exposing too many tools at once
- hiding critical policy inside SDK automation
- not encoding side-effect semantics or idempotency assumptions
- collapsing refusal, validation, transport, and execution errors into one generic failure bucket

## Tradeoffs
- **Strict schemas vs flexibility**: stricter contracts reduce ambiguity but increase authoring effort.
- **Rich contracts vs small contracts**: more metadata improves control, but increases maintenance burden.
- **Automatic helpers vs explicit orchestration**: helpers reduce boilerplate, but can hide the real runtime boundary.
- **Few broad tools vs many narrow tools**: broad tools simplify catalogs; narrow tools simplify validation and policy.

## Relationships to Other Notes
- `../concepts/tool-use-policy-and-permission-systems.md`
- `../concepts/skill-systems.md`
- `../concepts/observability-traceability.md`
- `../capabilities/mcp.md`
- `../capabilities/context-attachments.md`
- `../syntheses/control-boundaries.md`

## Relevance to This Repository
- Define tool/action surfaces with explicit purpose, inputs, and side-effect class.
- Keep permission policy near the action surface instead of hiding it only in prompts.
- Treat tool invocation loops as observable runtime behavior, not as prompt magic.
- Prefer narrow, boring action contracts over highly general tools when safety or maintainability matters.
- Distinguish skill design from tool design:
  - skills package reusable procedure
  - action contracts expose callable execution surfaces

## Open Questions
- What is the smallest useful contract shape for low-risk local tools in this workflow?
- Which side-effect metadata is worth standardizing in this repository?
- When is strict output structure worth the extra authoring cost?
- How should permission and approval policies attach to action contracts in a portable way?

## References
- [Function calling guide](https://platform.openai.com/docs/guides/function-calling) — OpenAI docs. Useful evidence for explicit tool schemas and model-emitted calls.
- [Programmatic tool calling](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling) — OpenAI docs. Helpful for the explicit invocation loop and call/result handling.
- [Structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs) — OpenAI docs. Useful distinction between structured output formatting and action invocation.
- [Handling stop reasons](https://platform.claude.com/docs/en/api/handling-stop-reasons) — Anthropic docs. Useful for separating invocation flow states and response handling.
- [Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) — Anthropic docs. Evidence that schema strictness helps but is not the whole control model.
- [Function calling](https://ai.google.dev/gemini-api/docs/generate-content/function-calling) — Google Gemini API docs. Cross-vendor confirmation that structured invocation is now a general capability.
- [Model Context Protocol schema](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-06-18/schema.ts) — MCP schema source. Useful for protocol-level tool contract structure.
- [JSON Schema support proposal context](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/seps/2106-json-schema-2020-12.mdx) — MCP proposal text. Useful for drift and limitation awareness around schema support.
