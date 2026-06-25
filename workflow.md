my workflow:

the user calls the planner. the planner interviews the user to understand the problem and designs a plan. the user can call the architect to help evaluate the plan. the user then calls the builder directly to act on tasks, or calls the orchestrator to coordinate autonomous execution. at the end, or if the builder fails a task, the user can call the reviewer to help understand what happened and adjust the plan.

planner > architect(optional) > builder / orchestrator(choose 1) > reviewer(optional)

## Agents

planner: i explain what i want. it asks questions (as much as necessary) to understand the demand. when it is well defined, write down a plan.
the plan can be composed of 3 files depending on the size and complexity of the project: tasks.md (always), spec.md (script onward), architecture.md (application tier).
tasks have a description, a "tier" that tells the builder which skill to load, and acceptance criteria.

architect: called optionally on demand to revise the plan designed by planner when the user deems it complex or dangerous.

builder: single coding agent for all tiers. reads the tier from tasks.md and loads the matching tier skill (jerryrig/poc/script/application). also loads the builder-workflow skill for shared procedure.

orchestrator: called optionally on demand by the user for autonomous coding. it reads the planning files and delegates to the builder, passing only the required context. this is an alternative workflow. the standard workflow is the user acts as orchestrator and calls the builder directly.

reviewer: revises the code after it was written. calibrates rigor via the tier-calibration skill. helps to troubleshoot and adjust the plan.

## Coding Tiers (loaded as skills)

jerryrig: small changes, fast scripts, "one offs", no tests. raise exceptions.
poc: proof of concept. goal is to answer "does this work? is it worth it?". minimal code that works. the code itself will probably be used as knowhow and rewritten later.
script: simple script or bundle that will run with a certain frequency. YAGNI principle. needs to track changes.
application: full blown application. documentation. tests (when applicable, not too much). coding best practices live here.

## Shared Skills

builder-workflow: state continuity, tasks.md schema, definition of done, conclusion format. loaded by every builder task.
tier-calibration: review/critique rigor tables per tier. loaded by architect and reviewer.
