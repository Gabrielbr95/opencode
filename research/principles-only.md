# Principles Only

This document extracts the most durable design principles from the research repository.

The goal is to preserve rules that remain useful even when tools, vendors, frameworks, and fashionable terminology change.

These are not product instructions. They are the portable ideas underneath the implementations.

---

## 1. Prefer the simplest structure that solves the real task

Do not start with the most agentic or modular design by default.

Use the least complex structure that reliably accomplishes the job:
- plain prompt before workflow
- workflow before agent
- single agent before multi-agent
- narrow skill before giant capability bundle

Complexity is justified only when it improves outcomes enough to pay for its maintenance, debugging, and control cost.

---

## 2. Separate fixed orchestration from model-directed control

Treat workflows and agents as different things.

- A **workflow** is mostly predefined.
- An **agent** dynamically decides among next actions.

This distinction matters because predictability, testing difficulty, cost, and safety all change when control shifts from code to the model.

---

## 3. Architecture is mainly about boundaries

Good architecture is less about naming patterns and more about defining:
- who owns the task
- who may delegate
- who may take over
- who sees which context
- where review or stopping can occur

When boundaries are unclear, systems become expensive to debug and hard to trust.

---

## 4. Context is a scarce resource

More context is not automatically better.

Select, shape, and stage context deliberately:
- include what is relevant now
- avoid burying critical facts
- separate stable instructions from volatile data
- prefer retrieval over blind prompt growth

Treat attention, token cost, and salience as design constraints.

---

## 5. Memory and context are different layers

Do not confuse persistence with active visibility.

- **Memory** is what may persist for later reuse.
- **Context** is what is actually shown to the model now.

This distinction is essential for designing session continuity, resumability, and durable project truth.

---

## 6. Durable writes deserve stronger control than transient drafts

Draft generation is usually low risk.
Persistent changes are not.

Protect:
- long-lived docs
- rules
- skills
- prompts
- config
- durable memory
- learned defaults

Bad durable state silently poisons future behavior.

---

## 7. Treat memory as a governed system, not a dump

Useful memory is selective, attributable, and correctable.

Do not store everything.
Prefer memory that is:
- source-linked
- stable enough to matter later
- reusable beyond one transient turn
- reviewable and removable

Bad memory can be worse than forgetting.

---

## 8. Retrieve instead of replaying everything

Large histories and giant prompts are not the same as good recall.

Prefer:
- retrieving relevant evidence
- summarizing old state
- promoting only useful facts or lessons into durable memory

This keeps systems cheaper, clearer, and more robust.

---

## 9. Tools are action surfaces, not just helper metadata

Tool design is part of system behavior.

Tool names, descriptions, schemas, examples, and execution boundaries shape what the model does.

Treat tool interfaces as first-class design artifacts, not implementation leftovers.

---

## 10. Policy and enforcement are separate layers

Natural-language guidance is not the same as runtime control.

- **Policy** shapes what the model should do.
- **Permissions / authorization** decide what the system will allow.

Do not mistake prompt guidance for hard safety.

---

## 11. Schema-valid is not safe or correct

A well-formed action can still be:
- wrong
- premature
- unauthorized
- harmful
- business-invalid

Validation must exist at more than one layer: schema, policy, permission, and sometimes human review.

---

## 12. Use humans at consequential boundaries, not everywhere

Human review is most valuable at:
- destructive actions
- external side effects
- ambiguous scope changes
- durable memory promotion
- policy changes
- persistent repository changes

Too many approval steps turn oversight into empty clicking.

---

## 13. Guardrails, approvals, and HITL are different controls

Do not collapse them into one category.

- **Guardrails** are automatic.
- **Approvals** gate a specific run or action.
- **HITL** lets a human review, edit, override, or stop.

They complement each other; they do not replace each other.

---

## 14. Side effects should drive control intensity

Low-risk reasoning and drafting should be smooth.
High-risk side effects should be high-friction.

As consequence rises, strengthen:
- permissions
- guardrails
- approvals
- auditability
- human visibility

---

## 15. Planning is useful only when tied to feedback and evaluation

Planning is not performance theater.

Good planning:
- decomposes work
- checks progress
- revises based on evidence
- stops when the task is complete or blocked

If there is no real feedback loop, elaborate planning often becomes ceremony.

---

## 16. Visible reasoning is not the same as capability

Do not judge quality by verbosity.

A system can:
- reason well with compact traces
- reason poorly with long chain-of-thought style text

Use outcomes, traceability, and evaluation rather than rhetorical confidence or length.

---

## 17. Skills should package reusable procedure, not become junk drawers

Use skills for:
- repeatable know-how
- structured workflows
- reusable resources
- helper scripts where determinism matters

Avoid giant omnibus skills with blurred scope.

Narrow, composable capabilities are easier to trigger, maintain, and review.

---

## 18. Separate ambient guidance from on-demand capability

Always-on repository instructions should stay broad.
Specific procedures should load on demand.

This reduces context waste and keeps high-level policy distinct from task-specific execution patterns.

---

## 19. Prompt repositories should behave like software projects

Treat prompts, skills, and orchestration rules as maintained artifacts.

That means:
- explicit structure
- known precedence rules
- reviewable changes
- test coverage where practical
- ownership and provenance

Do not let prompt behavior live only in scattered chat history or undocumented habits.

---

## 20. Co-locate behavior with evidence

When possible, keep prompts, examples, tests, and review criteria close enough to compare together.

This reduces drift between:
- what the system says it does
- what it actually does
- how it is judged

---

## 21. Observability records behavior; evaluation judges it

These are separate but connected.

- **Observability** tells you what happened.
- **Evaluation** tells you whether that behavior was good.

You need both.

Without observability, failures are hard to diagnose.
Without evaluation, traces are just forensic exhaust.

---

## 22. Trace the meaningful boundaries, not just the final answer

Useful traces include:
- prompt rendering
- retrieval
- tool calls
- approvals
- handoffs
- guardrail events
- evaluator outputs

Flat final-output logging is too weak for agent systems.

---

## 23. Preserve provenance for important decisions and memories

If a rule, memory, summary, or decision matters later, it should be traceable to:
- a source artifact
- a run
- a human decision
- a document
- a test or evaluation outcome

Provenance makes correction and trust possible.

---

## 24. Test the system the way it actually fails

Do not test only ideal outputs.

Also test:
- wrong tool choice
- missing context
- conflicting context
- bad retrieval
- bad handoff
- malformed output
- risky side effects
- prompt injection attempts
- regressions after edits

Failure-oriented tests are often more useful than polished demos.

---

## 25. Use multiple evaluation methods

No single evaluator is enough.

Combine as needed:
- exact or rule-based checks
- schema validation
- pairwise comparison
- LLM judges
- human review
- production feedback

Different qualities need different measurement methods.

---

## 26. Keep offline and online evaluation separate in your head

Offline evaluation answers:
- does this change look better on controlled cases?

Online evaluation answers:
- how is the system behaving in real conditions?

Blurring them creates false confidence.

---

## 27. Optimize for inspectability, not just capability

A system that is slightly less powerful but much easier to understand, test, pause, and repair is often the better engineering choice.

This matters more in:
- local-first setups
- corporate environments
- interrupted projects
- long-lived repositories

---

## 28. Favor reversible decisions early

When uncertainty is high, prefer decisions that are:
- easy to undo
- easy to inspect
- easy to migrate away from
- low-coupling

This keeps exploration cheap and reduces future cleanup cost.

---

## 29. Distinguish principles from implementations

When a framework or product suggests a useful pattern, preserve the underlying idea separately from the vendor-specific mechanism.

Examples:
- progressive disclosure
- context partitioning
- trace propagation
- evaluator-optimizer loop
- tiered memory
- human approval before side effects

This keeps the repository portable and durable.

---

## 30. Make the repository easier to resume than to remember

Interrupted work is normal.

Design for restartability:
- durable truth in stable files
- short resume baton for current state
- explicit terminology
- traceable decisions
- small enough artifacts to reread selectively

A good repository should survive loss of mental context.

---

## Practical Use

Before adding a new agent, skill, prompt layer, memory mechanism, or control rule, ask:

1. What real problem does this solve?
2. Is there a simpler structure that already works?
3. Which boundary does this belong to: architecture, context, memory, control, evaluation, or observability?
4. Is it guidance, enforcement, or evidence?
5. Is it durable truth or only current-state context?
6. How will it be tested, traced, and corrected later?
7. What future maintenance burden does it create?

## Related Documents
- `research/vocabulary.md`
- `research/control-boundaries.md`
- `research/topics/`
