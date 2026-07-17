# Future Improvements From Matt Pocock Skills Research

## Purpose
This note captures useful findings from reviewing Matt Pocock's `skills` repository, especially recent changes relevant to skill design, prompt structure, planning, review, and grilling workflows.

It is a **future improvement note**, not an immediate implementation checklist.

---

## Main Takeaways

### 1. Separate wrappers from reusable discipline
Recent repo direction strongly favors:
- **user-invoked wrappers** for orchestration entry points
- **model-invoked skills** for reusable process/rubric/reference

This supports a structure where thin front-door skills call shared internal discipline instead of duplicating large procedures.

### 2. Different review jobs should use different rubrics
The repo direction supports distinct review rubrics for distinct targets.

That validates this harness decision:
- `review-code` for implementation review
- `review-plan` for planning artifact review

This is not unnecessary duplication. It is separation of genuinely different jobs.

### 3. Execution skills should stay thin
Execution/orchestration skills should not absorb too much reusable discipline.

That supports keeping:
- planning in planning skills
- execution in execution skills
- review in review skills
- reconciliation in reconciliation skills

This also confirms the boundary that there should not be a “plan to make a plan” execution loop.

### 4. Trigger descriptions should be treated as scarce invocation surface
Recent guidance emphasizes:
- lead with the trigger
- keep one trigger branch per description
- avoid bloated summary-style descriptions

This suggests a future cleanup pass on skill descriptions in this harness.

### 5. Positive framing is preferred over excessive negation
The repo increasingly prefers instructions that say what to do instead of long chains of “do not do X”.

This is a likely future prompt-quality improvement for this harness, but not urgent.

---

## Grilling / Grill-With-Docs Findings

## Key point
`grill-with-docs` is **not** a rename of `grill-me`.

Matt’s repo kept both:
- `grill-me` = stateless front door for grilling
- `grill-with-docs` = engineering/stateful sibling that runs grilling plus durable documentation updates

The deeper evolution was:
1. keep `grill-me`
2. extract shared `grilling` behavior
3. add `grill-with-docs`

### What `grill-with-docs` adds
- one-question-at-a-time interviewing
- shared-understanding focus
- durable glossary/context updates
- selective ADR creation
- lazy document creation

### Important behavioral rules from newer grilling guidance
- **Facts vs decisions**:
  - facts should be looked up when discoverable
  - decisions should be asked from the human
- **Confirmation gate**:
  - do not act until the user confirms shared understanding is reached
- **One question at a time**
- **Recommended answer with each question** to speed convergence

### Recommendation for this harness
Do **not** simply rename `grill-me` to `grill-with-docs`.

Better future direction:
- keep `grill-me` as the simpler grilling front door
- consider adding `grill-with-docs` later if durable planning/doc updates during grilling become desirable
- if needed later, extract a shared `grilling` primitive to avoid duplicated interview logic

---

## Planning / Mapping / Oversized Work

The repo now distinguishes between:
- normal planning
- oversized or foggy work

The large-work path uses `wayfinder`, which is positioned as:
- a map of unresolved decisions
- not the default planning mode
- not a place to dump all project detail

### Relevance here
This harness may eventually benefit from a separate mode for:
- multi-session, high-fog, still-unclear work

But that should be considered only if the current planning skill still feels overloaded after the present refactor.

Not a priority right now.

---

## Concrete Improvements Worth Considering Later

### High-value later improvements
1. **Tighten skill descriptions** to be more trigger-oriented and less summary-oriented.
2. **Improve positive framing** in prompts where it increases predictability.
3. **Consider a `grill-with-docs` companion skill** rather than overloading `grill-me`.
4. **Possibly extract a shared grilling primitive** if grilling behavior becomes more central.
5. **Consider a separate oversized-work mapping skill** only if the current planning model still feels too broad.

### Already validated by the research
The current refactor direction appears sound:
- keep execution and planning separate
- keep `workflow-execute` implementation-only
- split `review-code` and `review-plan`
- keep orchestration skills thin
- avoid forcing unnecessary full-detail planning by default

---

## Most Relevant Repo References

- Repo root:
  - https://github.com/mattpocock/skills
- CHANGELOG:
  - https://raw.githubusercontent.com/mattpocock/skills/main/CHANGELOG.md
- Writing Great Skills:
  - https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/writing-great-skills/SKILL.md
- Grilling:
  - https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md
- Grill Me:
  - https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md
- Grill With Docs:
  - https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/grill-with-docs/SKILL.md
- Domain Modeling:
  - https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/domain-modeling/SKILL.md
- Wayfinder:
  - https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/wayfinder/SKILL.md

---

## Final Summary
The main lesson from the repo is not “copy Matt’s exact structure.”

It is:
- separate orchestration from reusable discipline
- separate different kinds of review
- keep execution thin
- ask humans for decisions, look up facts separately
- stop at shared understanding before acting
- keep durable documentation narrow and purposeful

That direction is compatible with the current harness refactor and suggests a few good future upgrades, especially around grilling and skill-description quality.
