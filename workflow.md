my workflow:

the user calls the planner. the planner interviews the user to understand the problem and designs a plan. the user can call the architect to help evaluate the plan. the user then can call coders directly to act on tasks or call the orchestrator to coordinate execution. at the end, or if a coder fails a task, the user can call the reviewer to help understand what happened and adjust the plan.

planner > architect(optional) > orchestrator(optional) > coders(choose 1 of 4) > reviewer(optional)

planner: a general purpose planner. i explain what i want. it asks questions (as much as necessary) to understand the demand. when it is well defined, write down a plan.
the plan can be composed of 3 files depending on the size and complexity of the project: tasks.md (always), spec.md(script onward), architecture.md (application tier)
tasks have a description, a "tier" according to the coding agent, a list of expected files to change, and a acceptance criteria
architect: called optionally on demand to revise the plan designed by planner when the user deems it complex or dangerous
orchestrator: called optionally on demand by the user for autonomous coding. it reads the planning files and calls the coding agents, passing only the required context.
this is an alternative workflow. the standard workflow is the user act as orchestrator and call the coding agents
reviewer: revises the code after it was writen. helps to troubleshoot and adjust the plan.
coding agents:
jerryrig: small changes, fast scripts, "one offs", no tests. raise exceptions.
poc: proof of concept. goal is to answer "does this work? is it worth it?". minimal code that works. the code itself will probably be used as knowhow and rewriten later
script: simple script or bundle that will run with a certain frequency. YAGNI principle. needs to track changes.
application: full blown application. doccumentation. tests (when applicable, not too much). coding best practices live here.