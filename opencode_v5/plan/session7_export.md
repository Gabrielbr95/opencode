# Session Export: Agentic coding setup architecture

---
## USER  10:00:09

this is a green field repositoty.
i'm researching agentic coding and coding harnesses. 
this is a purposefully open ended request. help me figure out what i need.
read C:\Users\btny\.config\opencode\my-context.md to know me.
research the web. see what people are doing.
make questions. don't suggest right away.
what i mean is setups for claude code, codex, opencode and the like
stay platform agnostic.
setup should fit home and work, with minor or no changes.

---
## ASSISTANT  10:00:09

**[TOOL: read]**
Input: {
  "filePath": "C:\\Users\\btny\\.config\\opencode\\my-context.md"
}

---
## ASSISTANT  10:00:14

Good. Let me research what people are actually doing with these setups before asking anything.

**[TOOL: task]**
Input: {
  "description": "Research agentic coding harnesses",
  "subagent_type": "explore",
  "prompt": "Research what people are doing in 2025/2026 with agentic coding harnesses and setups. Focus on:\n\n1. Claude Code (Anthropic's CLI tool) - what does a typical setup look like? What files do people configure? CLAUDE.md, MCP servers, hooks, custom slash commands, permission scopes.\n2. OpenCode - similar questions. What config files, what conventions are emerging?\n3. Codex (OpenAI) - same.\n4. General concepts: what are \"coding harnesses\"? What do AGENTS.md, CLAUDE.md, and similar files do? How do people structure instructions for agents? What are MCP servers and how are they used in these setups?\n5. What patterns are emerging for \"portable\" setups that work across tools and environments?\n6. What do people put in system prompts / instruction files for these tools?\n7. What are the main categories of config: tool permissions, memory/context files, MCP integrations, hooks/callbacks, custom commands?\n\nSearch the web broadly. Look at:\n- https://docs.anthropic.com/en/docs/claude-code/overview\n- https://opencode.ai/docs\n- Any GitHub repos or blog posts about \"claude code setup\", \"agentic coding harness\", \"CLAUDE.md examples\", \"coding agent configuration\"\n- Reddit, HN discussions about people's actual setups\n\nReturn a structured summary of what you find, organized by tool and by concept. Include any surprising or non-obvious patterns people are using. Be thorough - this is research for planning purposes."
}

---
## USER  10:05:06

looks like the task halted. maybe a connection error. resume. try to use the same context in order not to research all over again.

---
## ASSISTANT  10:05:06

The task was cancelled before it returned any results ÔÇö there's no prior context to resume from. I'll need to re-run it.

**[TOOL: task]**
Input: {
  "description": "Research agentic coding harnesses",
  "prompt": "Research what people are doing in 2025/2026 with agentic coding harnesses and setups. Focus on:\n\n1. Claude Code (Anthropic's CLI tool) - what does a typical setup look like? What files do people configure? CLAUDE.md, MCP servers, hooks, custom slash commands, permission scopes.\n2. OpenCode - similar questions. What config files, what conventions are emerging?\n3. Codex (OpenAI) - same.\n4. General concepts: what are \"coding harnesses\"? What do AGENTS.md, CLAUDE.md, and similar files do? How do people structure instructions for agents? What are MCP servers and how are they used in these setups?\n5. What patterns are emerging for \"portable\" setups that work across tools and environments?\n6. What do people put in system prompts / instruction files for these tools?\n7. What are the main categories of config: tool permissions, memory/context files, MCP integrations, hooks/callbacks, custom commands?\n\nSearch the web broadly. Look at:\n- https://docs.anthropic.com/en/docs/claude-code/overview\n- https://opencode.ai/docs\n- Any GitHub repos or blog posts about \"claude code setup\", \"agentic coding harness\", \"CLAUDE.md examples\", \"coding agent configuration\"\n- Reddit, HN discussions about people's actual setups\n\nReturn a structured summary of what you find, organized by tool and by concept. Include any surprising or non-obvious patterns people are using. Be thorough - this is research for planning purposes.",
  "subagent_type": "explore"
}

---
## USER  10:12:45

you invoked the explorer twice and it halted at the end twide. do the research yourself. do not invoke a subagent.
don't get stuck in claude code, opencode, codex. i want general concepts and workings. there are other good harneces i did not mention.

---
## ASSISTANT  10:12:45

Got it. Doing this myself.

**[TOOL: webfetch]**
Input: {
  "url": "https://docs.anthropic.com/en/docs/claude-code/overview"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://opencode.ai/docs"
}

---
## ASSISTANT  10:12:52

**[TOOL: webfetch]**
Input: {
  "url": "https://opencode.ai/docs/configuration"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://docs.anthropic.com/en/docs/claude-code/memory"
}

---
## ASSISTANT  10:12:58

**[TOOL: webfetch]**
Input: {
  "url": "https://docs.anthropic.com/en/docs/claude-code/hooks"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://platform.openai.com/docs/codex/overview"
}

---
## ASSISTANT  10:13:05

**[TOOL: webfetch]**
Input: {
  "url": "https://codex.openai.com/docs/guides/agents-md"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://modelcontextprotocol.io/introduction"
}

---
## ASSISTANT  10:13:19

**[TOOL: webfetch]**
Input: {
  "url": "https://platform.openai.com/docs/codex/guides/agents-md"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://docs.cursor.com/context/rules-for-ai"
}

---
## ASSISTANT  10:13:27

**[TOOL: webfetch]**
Input: {
  "url": "https://docs.cursor.com/context/rules-for-ai",
  "format": "text"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://platform.openai.com/docs/codex/rules"
}

---
## ASSISTANT  10:13:34

**[TOOL: webfetch]**
Input: {
  "url": "https://docs.cursor.com/context/rules"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://platform.openai.com/codex/rules"
}

---
## ASSISTANT  10:13:41

**[TOOL: webfetch]**
Input: {
  "url": "https://github.com/eastlondoner/cursor-tools"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://continue.dev/docs/reference/config"
}

---
## ASSISTANT  10:13:48

I have enough. Good research. Let me now formulate questions.

---

Here's what I've learned. The landscape is bigger and more structured than it appears. Let me give you a quick map, then ask my questions.

---

## What I Found

**The core concept:** A *coding harness* is the scaffolding you build around an agentic coding tool to make it work reliably for *you* ÔÇö not just the tool itself. It's the difference between "I installed Claude Code" and "Claude Code reliably follows my standards, knows my environment, doesn't do dumb things, and picks up where it left off."

**The harness has 5 layers:**

| Layer | What it is | Examples |
|---|---|---|
| **Identity files** | Markdown read at session start ÔÇö tells the agent who you are, what the project is, what rules to follow | `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `.windsurfrules`, `codex.md` |
| **Tool integrations (MCP)** | Plugins that give the agent hands ÔÇö filesystem, search, git, APIs, databases | `mcp__filesystem`, `mcp__github`, `mcp__memory`, custom servers |
| **Hooks / lifecycle events** | Shell commands or scripts that fire before/after the agent acts | Auto-format after file edit, block destructive commands, log all tool calls |
| **Skills / slash commands** | Reusable workflows the agent can invoke on demand | `/review-pr`, `/deploy-staging`, `/run-tests` |
| **Memory / context management** | Persistence across sessions ÔÇö what survives compaction, what auto-saves | Auto-memory, project memory files |

**Key pattern emerging:** Tools are converging on `AGENTS.md` as a near-universal identity file. Claude Code reads `CLAUDE.md` but can import `@AGENTS.md`. Codex reads `AGENTS.md`. Cursor has `.cursorrules` but also reads `AGENTS.md`. Windsurf has `.windsurfrules`. The field isn't settled, but `AGENTS.md` at repo root is the closest thing to a portable standard right now.

**MCP** (Model Context Protocol) is a USB-style open standard ÔÇö you write an MCP server once and any compatible tool (Claude Code, Codex, Cursor, Windsurf, Continue, etc.) can use it. This is the main portability lever.

**Other harnesses worth knowing:** Cursor (IDE with deep agent mode), Windsurf, Cline/Roo (VS Code extensions, open-source, local-model-friendly), Continue.dev (open-source VS Code), Aider (CLI, git-native, very scriptable). `vibe-tools` is a meta-layer that installs itself into whichever harness you use.

**Your situation specifically:** You already have `AGENTS.md` at `~/.config/opencode/` and a skills system. That's the identity-file layer, partially built. You're running OpenCode on corporate Windows and personal Linux ÔÇö the portability question matters.

---

## Questions Before Suggesting Anything

**On goals:**

**[TOOL: question]**
Input: {
  "questions": [
    {
      "question": "What's the primary goal right now ÔÇö learning how these systems work internally, or building a setup that actually helps you ship work faster?",
      "header": "Goal",
      "options": [
        {
          "label": "Learning / research (Recommended)",
          "description": "Understand the concepts, experiment, build something from scratch to see how it works"
        },
        {
          "label": "Practical setup",
          "description": "Get a working harness I can use at work and home as fast as possible"
        },
        {
          "label": "Both equally",
          "description": "Want a working setup AND to understand what I built"
        }
      ]
    },
    {
      "question": "What's your current pain point ÔÇö the thing that made you research this?",
      "header": "Pain point",
      "options": [
        {
          "label": "Context loss between sessions",
          "description": "Agent forgets what was decided, I repeat myself constantly"
        },
        {
          "label": "Agent does unsafe things",
          "description": "No guardrails ÔÇö it deletes, overwrites, runs risky commands without asking"
        },
        {
          "label": "No reusable workflows",
          "description": "I keep re-explaining the same tasks from scratch"
        },
        {
          "label": "No idea what to set up first",
          "description": "Blank slate, want to understand the problem space before building"
        }
      ]
    },
    {
      "question": "Which harnesses are you actively using or seriously considering? (pick all that apply)",
      "header": "Harnesses",
      "multiple": true,
      "options": [
        {
          "label": "OpenCode (current)",
          "description": "Already using it ÔÇö you're in it now"
        },
        {
          "label": "Claude Code (CLI)",
          "description": "Anthropic's terminal tool, subscription or API key"
        },
        {
          "label": "Cursor",
          "description": "IDE fork ÔÇö paid subscription"
        },
        {
          "label": "Cline / Roo",
          "description": "VS Code extension, open-source, works with local models"
        },
        {
          "label": "Aider",
          "description": "CLI, git-native, very scriptable, OSS"
        },
        {
          "label": "Continue.dev",
          "description": "VS Code extension, open-source, self-hostable"
        }
      ]
    },
    {
      "question": "Your corporate constraint: the Claude API key is approved. What about the harness itself on the work laptop?",
      "header": "Work install",
      "options": [
        {
          "label": "No admin ÔÇö needs to run without install privileges",
          "description": "Must be portable/user-space install only"
        },
        {
          "label": "Can install user-level Node/Python packages",
          "description": "pip install --user or npm global to user dir works"
        },
        {
          "label": "Unclear, haven't tested yet",
          "description": "Don't know what's blocked"
        }
      ]
    },
    {
      "question": "MCP servers ÔÇö local tools you plug in to give the agent capabilities. Which categories matter most to you?",
      "header": "MCP priorities",
      "multiple": true,
      "options": [
        {
          "label": "Filesystem / file access",
          "description": "Read/write files, navigate directories"
        },
        {
          "label": "Git / version control",
          "description": "Commit, diff, branch operations"
        },
        {
          "label": "Web search / fetch",
          "description": "Agent can look things up in real time"
        },
        {
          "label": "Memory / knowledge base",
          "description": "Agent saves and retrieves notes across sessions"
        },
        {
          "label": "Corporate systems (SAP, PDF, web UI scraping)",
          "description": "The maintenance planning and document workflows"
        }
      ]
    }
  ]
}

---
## ASSISTANT  10:23:50

Good. That's a clear picture. A few more targeted questions before I can propose anything concrete:

**[TOOL: question]**
Input: {
  "questions": [
    {
      "header": "IDE situation",
      "options": [
        {
          "description": "VS Code at work, VS Code at home ÔÇö same editor both places",
          "label": "VS Code everywhere"
        },
        {
          "description": "VS Code at work, something else personal",
          "label": "VS Code work only"
        },
        {
          "description": "Terminal-first, minimal IDE dependency",
          "label": "Prefer terminal-first"
        }
      ],
      "question": "Your AGENTS.md file, skills, and settings are currently inside ~/.config/opencode/. Are you running VS Code-based workflows, terminal-first, or mixed?"
    },
    {
      "header": "Config portability",
      "options": [
        {
          "description": "A git repo I push/pull between machines ÔÇö home Linux and work Windows",
          "label": "Sync via git repo (Recommended)"
        },
        {
          "description": "Manually copy when needed",
          "label": "Manual copy, no sync needed"
        },
        {
          "description": "Haven't thought about it, let's decide now",
          "label": "No plan yet"
        }
      ],
      "question": "Your setup spans home Linux, home Windows dual-boot, and work Windows. How do you plan to keep your harness config in sync across machines?"
    },
    {
      "header": "Automation depth",
      "options": [
        {
          "description": "Agent reads context, follows instructions, I drive it manually",
          "label": "Assisted ÔÇö I prompt, agent acts"
        },
        {
          "description": "Agent runs repeatable tasks autonomously with minimal prompting",
          "label": "Semi-autonomous ÔÇö trigger and review"
        },
        {
          "description": "Scheduled, unattended runs e.g. overnight analysis",
          "label": "Fully autonomous ÔÇö fire and forget"
        }
      ],
      "question": "How autonomous do you want the agent to be? This affects what layers you need to build."
    },
    {
      "header": "Work constraint",
      "options": [
        {
          "description": "Corporate data never leaves my machine. Harness + agent must run entirely local.",
          "label": "Fully local processing required"
        },
        {
          "description": "API calls to Claude are approved. Data in my prompts must be sanitized.",
          "label": "Claude API ok, but I control what goes in"
        },
        {
          "description": "Haven't mapped this out yet for the harness itself",
          "label": "Need to think through this"
        }
      ],
      "question": "For work use: your Claude API key is approved. Can the harness itself make any outbound calls (e.g. MCP server phoning home for updates, telemetry)?"
    }
  ]
}

---
## ASSISTANT  10:29:52

That's everything I need. One last round ÔÇö these are about scope and priorities so I don't overbuild a plan:

**[TOOL: question]**
Input: {
  "questions": [
    {
      "header": "Build vs adopt",
      "options": [
        {
          "description": "Map what exists, adopt what fits, build only the gaps",
          "label": "Adopt-first (Recommended)"
        },
        {
          "description": "Design my own system from scratch with full control",
          "label": "Build-first"
        },
        {
          "description": "Start from an existing community template/starter kit",
          "label": "Template-first"
        }
      ],
      "question": "Strategy: you already have a partial harness in OpenCode (AGENTS.md, skills, config). Do you want to extend what you have, or design a new system from scratch?"
    },
    {
      "header": "Scope",
      "options": [
        {
          "description": "Get a minimal working cross-machine harness first, iterate from there",
          "label": "Minimal viable harness (Recommended)"
        },
        {
          "description": "Design the full system end-to-end, then build it in phases",
          "label": "Full design upfront"
        },
        {
          "description": "Just the work-use-case first, personal can wait",
          "label": "Work use case only"
        }
      ],
      "question": "Given your time constraints (1-2h sessions, offshore gaps), what scope feels right for a first version?"
    }
  ]
}

---
## ASSISTANT  10:32:39

Good. I have a clear picture now. Here's my synthesis before proposing anything:

---

## What I'm Seeing

**Your non-negotiables:**
- No phone-home MCP servers (per-case exceptions OK)
- Corporate data stays local or through approved Claude API only
- Works on corporate Windows without admin (npm/pip user-level OK)
- Platform-agnostic ÔÇö harness shouldn't be locked to OpenCode specifically
- Portable ÔÇö syncs via git home-side, manual copy work-side

**What you already have (partial harness):**
- `AGENTS.md` at `~/.config/opencode/` ÔÇö global identity/context file
- Skills system (OpenCode's custom skill mechanism)
- Some config files and context docs

**What's missing / undesigned:**
- A clear layer separation ÔÇö what lives globally vs per-project
- MCP server stack (local only)
- Hook definitions (safety rails, auto-format triggers)
- A sync/portability strategy for the config repo
- A working-mode model (assisted / human-in-loop / autonomous)

**Key decision the plan needs to resolve:**
Whether to stay OpenCode-native (and accept its config conventions) or build the harness in a tool-agnostic layer first (AGENTS.md + MCP servers + project-level rules) that OpenCode happens to consume. The second approach means if you switch tools in 6 months, 80% of your work survives.

That last point is worth your confirmation before I propose a structure.

**[TOOL: question]**
Input: {
  "questions": [
    {
      "header": "Portability tradeoff",
      "options": [
        {
          "description": "Design the core as tool-agnostic. Each tool reads from the same sources. OpenCode is just one consumer. (Recommended)",
          "label": "Tool-agnostic core, OpenCode as a consumer"
        },
        {
          "description": "Build for OpenCode now. If I switch, I'll adapt it then.",
          "label": "OpenCode-native, optimize later"
        },
        {
          "description": "I want to run multiple harnesses in parallel and compare them",
          "label": "Multi-harness side-by-side"
        }
      ],
      "question": "The most important architectural choice: should the harness be designed to survive a tool switch (Cursor, Cline, future tool), or is OpenCode-native acceptable for now?"
    }
  ]
}

---
## ASSISTANT  10:34:31

That's the key decision. I have everything I need to propose a plan now.

---

## Proposed Approach ÔÇö Tool-Agnostic Coding Harness

**Structure in one sentence:** A git repo at `~/.config/opencode/` that acts as your *harness repository* ÔÇö tool-agnostic at its core, with thin adapter layers per tool. OpenCode reads from it now; any future tool can be wired in by adding a small adapter.

**Layers, from core outward:**

### 1. Core Identity Layer (tool-agnostic)
- **`AGENTS.md`** ÔÇö the universal identity file. Already recognized by Codex, importable by Claude Code, readable by Cline/Roo. This is your persistent "who I am, how I work, what I care about." One file, all tools.
- **`my-context.md`** ÔÇö already exists. Stays separate; gets imported by `AGENTS.md` via `@path` or equivalent.
- **Project-level `AGENTS.md`** ÔÇö per-project rules that live in the repo root. Inherits from global.

### 2. MCP Server Stack (local, no phone-home)
A small curated set:
- `@modelcontextprotocol/server-filesystem` ÔÇö file read/write (already widely used, Node, local-only)
- `@modelcontextprotocol/server-git` ÔÇö git operations
- `mcp-server-fetch` ÔÇö web fetch/search (reads URLs, no telemetry)
- A custom Python MCP for your corporate PDF/form workflows ÔÇö you build this yourself when needed

These are configured once in a shared `mcp.json` (or equivalent) that each tool adapter points at.

### 3. Rules / Conventions Layer
Scoped markdown files for different contexts:
- `rules/global.md` ÔÇö universal coding standards
- `rules/work.md` ÔÇö compliance, audit-trail, data-locality reminders
- `rules/python.md` ÔÇö your Python conventions

### 4. Skills / Workflows Layer (OpenCode-native for now)
Your existing skills stay. The abstraction is: skills are just markdown files with frontmatter ÔÇö other tools have equivalents (Cursor `/commands`, Claude Code `/skills`). These can be migrated if needed.

### 5. Hooks (safety rails)
Minimal set to start:
- Block `rm -rf` variants
- Require confirmation before git push to main
- Log all tool calls to a session file (audit trail for work)

### 6. Sync Strategy
- Home: git repo at `~/.config/opencode/`, push/pull freely
- Work: keep a `harness-work/` export folder ÔÇö a flattened copy of the files that work laptop needs (AGENTS.md, mcp.json, rules/), updated manually when you need to sync

---

**What I'd NOT build yet:**
- Scheduled/autonomous runs ÔÇö too much infrastructure for V1
- Custom MCP for corporate systems ÔÇö build when you have a specific target
- Anything that requires admin on work laptop

---

**The question for you before I write this up as a proper plan:**

Does this structure make sense? Specifically ÔÇö do you want me to treat your current `~/.config/opencode/` repo as the harness repo itself (reorganize what's already there), or design this as a *new* repo with a clean structure?

---
## USER  10:45:57

1. my-context.md is too big to be referenced every time. keep it separate. i will invoke manually when more context is needed. agents.md will reflect a smaller, core version of it. i rarely use per project agents.md, but keep as possibility. used as exceptiom, not rule.
2. agree. maybe we can expant on the list later
3. agree
4. my skills are kind of messy. the ideas are interesting. the actual files are disposable. i'd actually like to reorganize it.
5. agree
6. agree

do not design the play yet. i want to talk more. disregard current ~/.config/opencode/ setup. i want a clean slate. work in opencode_v5/ folder. i will inspect and decide to merge or not. 
there are some specifics not discussed yet.

---
## ASSISTANT  10:45:57

Good. Clean slate in `opencode_v5/`. Let me hear the specifics before touching anything.

What haven't we covered yet?

---
## USER  10:48:46

what are people in my situation doing? what are the more advanced people/actual devs doing? should i conform to someone else's workflow or do my own thing? is there a well developed tool/mcp that is so good i should use and plan around it? multiple agents or single agent? what goes in agents prompts and what goes in skill prompts?

---
## ASSISTANT  10:48:46

Good questions. Let me go look at what people are actually doing before I answer.

**[TOOL: webfetch]**
Input: {
  "url": "https://www.reddit.com/r/ClaudeAI/comments/1l6y8kx/what_does_your_claude_code_setup_look_like/"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://www.reddit.com/r/cursor/comments/1l0vqjj/share_your_cursorrules_setup/"
}

---
## ASSISTANT  10:48:56

**[TOOL: webfetch]**
Input: {
  "url": "https://news.ycombinator.com/item?id=43952698"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://www.anthropic.com/research/claude-code-best-practices"
}

---
## ASSISTANT  10:49:08

**[TOOL: webfetch]**
Input: {
  "url": "https://docs.anthropic.com/en/docs/claude-code/best-practices"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://github.com/hesreallyhim/awesome-claude-code"
}

---
## ASSISTANT  10:49:16

Good. I have enough to answer your questions directly. Let me also quickly scan the awesome-claude-code templates since that repo is a goldmine.

**[TOOL: webfetch]**
Input: {
  "url": "https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/main/README.md"
}

---
## ASSISTANT  10:49:23

**[TOOL: webfetch]**
Input: {
  "url": "https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/main/THE_RESOURCES_TABLE.csv"
}

---
## ASSISTANT  10:49:30

Good. I have enough to answer well. Here's my honest take:

---

## What People Are Actually Doing

### Casuals / non-devs in your situation
Mostly just using the tools out of the box with a basic `CLAUDE.md` or `AGENTS.md`. Maybe a few personal rules. No hooks, no MCP stack, no multi-agent setup. Results are inconsistent ÔÇö they complain the agent forgets things and goes off-rails. They're not wrong, just under-equipped.

### Intermediate practitioners
This is the interesting tier. They've built a **persistent context layer** (AGENTS.md + project-level rules), added **2-4 MCP servers** (filesystem, git, fetch), and use **skills/commands for repeatable workflows** (review PR, write tests, plan task). They also have a handful of **hooks** as safety rails. They drive the agent manually but with a structured protocol: explore ÔåÆ plan ÔåÆ implement ÔåÆ verify. Results are significantly better. This is realistic for you in V1.

### Advanced / professional devs
They run **multi-agent orchestration** ÔÇö lead agent breaks work into tasks, subagents execute in parallel, reviewer agent checks output in a fresh context window. They've invested heavily in **spec-driven workflows**: agent writes a spec first, human approves, then execution proceeds against that spec. They use **"Ralph Wiggum" loops** ÔÇö the agent runs autonomously against a task file, retrying until it passes verification criteria. They have automated hooks, usage monitors, and in some cases full CI integration. High ROI, but also high investment and high API spend.

---

## Should You Conform to Someone Else's Workflow?

**Partially.** Here's the honest split:

- **Conform** on the structural patterns: exploreÔåÆplanÔåÆexecuteÔåÆverify, short AGENTS.md with only what changes behavior, skills for repeatable tasks, hooks for hard constraints, subagents for isolated investigation. These patterns are validated and tooling is built around them.
- **Build your own** on the content: what goes in your AGENTS.md, what skills you create, which MCP servers matter to you. Nobody else has your work context (SAP, PDF workflows, maintenance planning) or your constraints (no admin, corporate data).

---

## Is There a Tool So Good You Should Plan Around It?

**Two worth knowing about:**

1. **Task Master** (`claude-task-master`) ÔÇö task management layer on top of any coding agent. Breaks specs into tasks, tracks state, coordinates multi-agent execution. Has ~50k stars. It's become a de-facto standard for people doing structured autonomous work. **Worth knowing about, probably V2 for you** ÔÇö overkill until you have a working V1 harness.

2. **Serena** (MCP server) ÔÇö code intelligence layer. Gives the agent semantic understanding of code: go-to-definition, find references, symbol navigation. What LSP gives you as a developer, Serena gives the agent. **Worth evaluating for your personal coding.** Requires local setup.

For your work context specifically: nothing dominant yet. The PDF/SAP/web-scraping space is still largely DIY. That's actually good ÔÇö it means the custom MCP you'd write for your specific pain points has no real competition.

---

## Single vs Multiple Agents

**Single agent for most things you'll do.** Multi-agent pays off when:
- Tasks are large enough to fragment into independent chunks
- You want a fresh-context reviewer that wasn't biased by doing the work
- You're running long autonomous sessions where context degradation is a real problem

**The practical pattern that's worth adopting now:** use subagents for investigation/research, keep your main session clean for implementation. This is single-agent *orchestrating* sub-agents on demand ÔÇö not a full multi-agent architecture. Low overhead, high payoff.

---

## What Goes Where: Agent Prompts vs Skill Prompts

This is the most practically useful question. Here's the clean answer:

| Belongs in AGENTS.md | Belongs in a skill |
|---|---|
| Who you are and how you work | How to do a specific task |
| Universal constraints (data locality, language, code style) | Task-specific protocols (how to review a PR, how to write a report) |
| Things true in every session | Things only relevant when invoked |
| Short, stable, rarely changes | Longer, can change per project, loaded on demand |
| "Never commit directly to main" | "When asked to review a PR: do X, then Y, then Z" |
| Behavior rules | Workflow recipes |

**The failure mode to avoid:** putting workflow instructions in AGENTS.md. It gets bloated, the agent starts ignoring parts of it, and you've consumed context on things that only matter 10% of the time. Rule of thumb: if you wouldn't want it loaded for a 30-second one-off question, it belongs in a skill, not AGENTS.md.

---

Ready to talk specifics now, or still more questions?

---
## USER  10:56:51

i'd prefer if i could range from small user directed edits to full autonomous implementation after the planning phase, with planning and human in the loop depelopment as the standard

---
## ASSISTANT  10:56:51

That's a well-defined working model. Let me make sure I understand it correctly before we design around it.

You're describing three modes on a spectrum:

1. **Direct edit** ÔÇö "change this line", "rename this variable". No planning, no ceremony. Agent acts immediately.
2. **Human-in-the-loop** (your default) ÔÇö agent explores, produces a plan, you review and approve, then it executes step by step with checkpoints. You stay aware of what's happening.
3. **Autonomous execution** ÔÇö after a plan is approved, agent runs to completion without hand-holding. You come back and review the result.

A few things I want to confirm before this shapes the harness design:

**[TOOL: question]**
Input: {
  "questions": [
    {
      "header": "Mode switching",
      "options": [
        {
          "description": "I decide upfront which mode I want and tell the agent at the start of the session",
          "label": "Explicit at session start"
        },
        {
          "description": "I want to be able to escalate or de-escalate mid-task ÔÇö e.g. start human-in-the-loop, then hand off to autonomous",
          "label": "Fluid, switchable mid-task (Recommended)"
        },
        {
          "description": "Different slash commands or skills trigger each mode",
          "label": "Invoked via command"
        }
      ],
      "question": "How do you want to switch between modes? Upfront declaration, fluid mid-session, or command-triggered?"
    },
    {
      "header": "Plan format",
      "options": [
        {
          "description": "A markdown file on disk that I can read, edit, and hand back to the agent",
          "label": "Written plan file (Recommended)"
        },
        {
          "description": "Plan shown in chat, I approve verbally, agent proceeds",
          "label": "In-chat plan approval"
        },
        {
          "description": "Either is fine depending on task size"
        }
      ],
      "question": "In human-in-the-loop mode, what form should the plan take before you approve it?"
    },
    {
      "header": "Autonomous guardrails",
      "options": [
        {
          "description": "Only file edits within the project. No git push, no external calls, no deletes without listing them first.",
          "label": "Restricted scope (Recommended)"
        },
        {
          "description": "Full autonomy within the project ÔÇö commits included, but no push to remote"
        },
        {
          "description": "I define the guardrails per-task when I hand off"
        }
      ],
      "question": "When you hand off to autonomous mode after plan approval ÔÇö what hard limits should always apply?"
    },
    {
      "header": "Checkpoint behavior",
      "options": [
        {
          "description": "Agent stops at each major task in the plan and waits for a go/no-go before continuing",
          "label": "Stop at each plan step"
        },
        {
          "description": "Agent runs the full plan, then presents a summary of what it did for review",
          "label": "Run to completion, then report"
        },
        {
          "description": "Agent pauses only when it hits ambiguity or a decision it can't resolve alone",
          "label": "Pause only on uncertainty (Recommended)"
        }
      ],
      "question": "In autonomous mode: how should the agent handle checkpoints?"
    }
  ]
}

---
## ASSISTANT  10:57:12

**[TOOL: question]**
Input: {
  "questions": [
    {
      "header": "Mode switching",
      "options": [
        {
          "description": "I decide upfront which mode I want and tell the agent at the start of the session",
          "label": "Explicit at session start"
        },
        {
          "description": "I want to be able to escalate or de-escalate mid-task",
          "label": "Fluid, switchable mid-task (Recommended)"
        },
        {
          "description": "Different slash commands or skills trigger each mode",
          "label": "Invoked via command"
        }
      ],
      "question": "How do you want to switch between modes? Upfront declaration, fluid mid-session, or command-triggered?"
    },
    {
      "header": "Plan format",
      "options": [
        {
          "description": "A markdown file on disk that I can read, edit, and hand back to the agent",
          "label": "Written plan file (Recommended)"
        },
        {
          "description": "Plan shown in chat, I approve verbally, agent proceeds",
          "label": "In-chat plan approval"
        },
        {
          "description": "Either is fine depending on task size",
          "label": "Flexible by task size"
        }
      ],
      "question": "In human-in-the-loop mode, what form should the plan take before you approve it?"
    },
    {
      "header": "Autonomous guardrails",
      "options": [
        {
          "description": "Only file edits within the project. No git push, no external calls, no deletes without listing them first.",
          "label": "Restricted scope (Recommended)"
        },
        {
          "description": "Full autonomy within the project, commits included, but no push to remote",
          "label": "Commits ok, no remote push"
        },
        {
          "description": "I define the guardrails per-task when I hand off",
          "label": "Per-task defined guardrails"
        }
      ],
      "question": "When autonomous after plan approval: what hard limits should always apply?"
    },
    {
      "header": "Checkpoint behavior",
      "options": [
        {
          "description": "Agent stops at each major task in the plan and waits for a go/no-go before continuing",
          "label": "Stop at each plan step"
        },
        {
          "description": "Agent runs the full plan, then presents a summary of what it did",
          "label": "Run to completion, then report"
        },
        {
          "description": "Agent pauses only when it hits ambiguity or a decision it can't resolve alone",
          "label": "Pause on uncertainty only (Recommended)"
        }
      ],
      "question": "In autonomous mode: how should the agent handle checkpoints?"
    }
  ]
}

---
## ASSISTANT  11:02:28

Good ÔÇö and your tier answer is the key insight here. The plan format should be calibrated to the tier:

- **Jerryrig**: no plan file needed. Maybe a one-liner in chat. Agent acts.
- **POC**: brief in-chat plan or a short note. Quick approval.
- **Script/Application**: written plan file on disk, you review and edit before execution begins.

This maps cleanly to the working model:

| Tier | Default mode | Plan format | Autonomous? |
|---|---|---|---|
| Jerryrig | Direct edit | None | Yes, trivially |
| POC | Human-in-loop light | In-chat, quick approval | After approval |
| Script | Human-in-loop | Written file, you edit | After approval |
| Application | Human-in-loop strict | Written file + architecture notes | After approval, pause on uncertainty |

One more thing I want to nail down before this can shape the harness:

The "fluid, switchable" answer means the agent needs to *know* which mode it's in at any given moment, and you need a low-friction way to signal a shift. The options are:

- **Implicit** ÔÇö agent infers from prompt tone ("just do it" vs "let's plan this")
- **Explicit signal** ÔÇö a short keyword or prefix you type ("plan:", "go", "just:", or similar)
- **Tier declaration** ÔÇö you state the tier at the start, mode follows automatically from tier defaults above

Which of these feels natural to you, or do you want a combination?

---
## USER  11:04:14

i state the tier. infer and confirm if not stated

---
## ASSISTANT  11:04:14

Perfect. That's a clean, low-friction contract:

- You state the tier ÔåÆ agent knows what mode, what rigor, what plan format
- You don't state it ÔåÆ agent infers from context, proposes a tier, you confirm or correct before anything happens

This becomes a core behavior rule in AGENTS.md ÔÇö not a skill, because it applies to every single session regardless of task.

The inference signal the agent uses would be things like: scope of change, whether it touches existing code or creates new, whether it's throwaway or recurring, whether others will use it. Standard stuff it can read from your prompt.

---

I think we now have enough to design the harness. Before I propose the structure, let me summarize what I've captured so you can correct anything:

**Core behavior (AGENTS.md):**
- Tier system: jerryrig / POC / script / application ÔÇö stated or inferred+confirmed
- Tier drives: plan rigor, mode, autonomy level, definition of done
- Default working mode: human-in-the-loop with plan approval before execution
- Direct edits for jerryrig, written plan file for script/application
- Autonomous execution after plan approval; pause only on genuine uncertainty
- Restricted scope always: no git push to remote, no silent deletes

**Identity (AGENTS.md, compact):**
- Python-first, plain language, terse
- Corporate data stays local
- Failures loud, non-obvious decisions commented

**Skills (on-demand, not in AGENTS.md):**
- Reusable workflows ÔÇö to be designed, your current ones are disposable
- Tier-specific protocols (how to run a script-tier vs application-tier task)

**MCP stack (local only):**
- Filesystem, git, fetch ÔÇö baseline
- Corporate PDF/SAP workflows ÔÇö custom, built when needed

**Hooks:**
- Safety rails: block destructive commands, no silent remote push
- Audit log for work sessions

**Portability:**
- Tool-agnostic core (AGENTS.md + MCP config + rules)
- OpenCode-specific adapter layer on top
- Git-synced home, manual-copy work

**Repo:** clean slate in `opencode_v5/`

---

Anything wrong, missing, or that you want to argue about before I propose the folder structure and file breakdown?

---
## USER  11:06:43

i want to talk memory and planning artifacts.
what is the common approach?

---
## ASSISTANT  11:06:43

Good topic. Let me think through this carefully rather than just describing what tools offer.

---

## Two Separate Problems

**Memory** ÔÇö what the agent knows about *you and your environment* across sessions.
**Planning artifacts** ÔÇö what the agent and you know about *this specific task* during and after execution.

People conflate them. They're different problems with different solutions.

---

## Memory: What People Do

**Three layers in practice:**

**1. Static context (AGENTS.md / CLAUDE.md)**
What you've already decided to build. Hard-coded facts that are always true: your name, your constraints, your coding style, your tier system. Changes rarely, manually maintained. This is not really "memory" ÔÇö it's configuration.

**2. Auto-memory / learned context**
Tools like Claude Code have auto-memory ÔÇö the agent writes notes to itself after sessions. Things like "this project uses X pattern", "user prefers Y approach", "build command is Z". Stored in `~/.claude/projects/<project>/MEMORY.md`. Useful but messy ÔÇö you don't control what gets saved, quality degrades over time, it's tool-specific.

Most serious practitioners **disable auto-memory** and manage it manually instead. They write a `MEMORY.md` or equivalent themselves, keep it pruned, and treat it like a living document. Higher quality, lower noise.

**3. Project-level context files**
A `CONTEXT.md` or `project.md` in the repo root that describes the current state of the project: what's built, what's pending, key decisions made, gotchas discovered. The agent reads this at session start for that project. You maintain it ÔÇö or the agent updates it after sessions and you review.

---

## Planning Artifacts: What People Do

**The common pattern that works:**

A `plan/` or `tasks/` folder in the project. Contents depend on tier:

- Small tasks: a single `tasks.md` ÔÇö a checklist the agent works through and marks done
- Larger work: `spec.md` (what we're building and why) + `tasks.md` (how, step by step)
- Complex projects: add `architecture.md` (key design decisions, rejected alternatives)

**The key insight from practitioners:** the plan file is the handoff artifact. It's how you go from human-in-the-loop to autonomous ÔÇö you approve the plan file, the agent executes against it. It also survives session breaks. You come back after 2 weeks offshore, read the plan, know exactly where things stand.

**What most people get wrong:** they treat planning artifacts as throwaway. Agent writes a plan in chat, executes, session ends, plan is gone. Next session starts cold. This is the biggest source of "agent forgot everything" complaints.

---

## The Tension You'll Hit

Your situation has a specific wrinkle: **frequent interruptions**. 14 days offshore, 1-2 hour sessions, context switching between work and personal projects. Memory and planning artifacts are your primary tool against this ÔÇö but only if they're maintained.

The failure mode: you build a nice system, use it for 2 sessions, then stop maintaining it because it's friction. Then it's just dead files.

The practitioners who actually sustain this do one thing: **the agent maintains the artifacts, not the human**. You review and correct, but the agent does the writing. This only works if the agent knows it's supposed to do this ÔÇö which means it's a behavior rule, not something you remember to ask for.

---

## My Read for Your Situation

You need three things, no more:

1. **AGENTS.md** ÔÇö global, compact, always loaded. Who you are, how you work, the tier system. Never project-specific.

2. **Project memory file** ÔÇö per project, lives in the repo, agent maintains it, you review. Current state, key decisions, gotchas. Read at session start for that project. One file, stays small.

3. **Plan artifacts** ÔÇö tier-calibrated. Jerryrig: nothing. POC: maybe a one-pager. Script/Application: `plan/spec.md` + `plan/tasks.md`, written before execution, agent marks tasks done as it works.

What I'd skip: auto-memory (noisy, tool-specific), complex decision logs as a separate system (fold key decisions into the project memory file), architecture docs as a separate permanent artifact (fold into spec for your scale of work).

---

Does this match your instinct, or do you see it differently? Specifically: are you comfortable with the agent maintaining the project memory file, or do you want that to be manual?

---
## USER  11:10:12

research the topic online, then put in concrete terms.

---
## ASSISTANT  11:10:12

**[TOOL: webfetch]**
Input: {
  "url": "https://docs.anthropic.com/en/docs/claude-code/memory"
}

**[TOOL: webfetch]**
Input: {
  "url": "https://github.com/eyaltoledano/claude-task-master"
}

---
## ASSISTANT  11:10:21

Good. Concrete answer now.

---

## Memory: What Actually Exists and How People Use It

### Layer 1 ÔÇö Global identity (always loaded)
**File:** `AGENTS.md` or `CLAUDE.md` in your home config  
**Who writes it:** You  
**What's in it:** Who you are, how you work, universal rules. Short. Stable. Changes maybe once a month.  
**Failure mode:** People stuff everything in here. It bloats, agent starts ignoring parts of it. Rule: if removing it wouldn't cause a mistake on a typical session, cut it.

---

### Layer 2 ÔÇö Project context (loaded per project)
**File:** `AGENTS.md` or `CLAUDE.md` at project root  
**Who writes it:** You initially, agent updates it over time  
**What's in it:** Build commands, project layout, key architectural decisions, gotchas discovered during development, "always do X in this project" rules  
**Concrete example:**
```
# Build
- Run: `python -m pytest tests/` to verify
- Entry point: src/main.py

# Architecture
- Data flows: scraper ÔåÆ parser ÔåÆ DB ÔåÆ report
- Never use ORM, raw SQL only (performance reasons, decided 2025-06)

# Gotchas
- SAP session times out after 15min idle, reconnect logic in src/sap_client.py
- PDFs from vendor X have malformed headers, use pdfplumber not pypdf
```
**This is the most valuable layer.** The gotchas section alone pays for the whole system.

---

### Layer 3 ÔÇö Auto-memory (tool-specific, optional)
**Claude Code specific:** `~/.claude/projects/<project>/MEMORY.md`  
**Who writes it:** The agent automatically  
**What's in it:** Things the agent noticed ÔÇö build commands, patterns, your preferences  
**Honest assessment:** Noisy. Quality degrades. Most serious practitioners either disable it or prune it regularly. It's a convenience, not a foundation. **Don't rely on it. Treat it as a draft that needs review.**  
**OpenCode equivalent:** Doesn't have auto-memory in the same way. Your skills and AGENTS.md do that job manually.

---

## Planning Artifacts: The Concrete Patterns

### Pattern 1 ÔÇö The PRD ÔåÆ Tasks flow (Task Master style, most popular)

This is the dominant pattern among people doing structured work:

```
project/
ÔööÔöÇÔöÇ .taskmaster/
    Ôö£ÔöÇÔöÇ docs/
    Ôöé   ÔööÔöÇÔöÇ prd.txt          # What we're building and why
    ÔööÔöÇÔöÇ tasks/
        ÔööÔöÇÔöÇ tasks.json       # Structured task list with status, deps, subtasks
```

Flow: you write a PRD (plain English description of what you want) ÔåÆ agent parses it ÔåÆ generates numbered tasks with dependencies ÔåÆ agent works through them one by one, marking status. You can interrupt, reprioritize, add tasks.

**Task Master** (27k stars) is the dominant tool implementing this. It's an MCP server ÔÇö works with Cursor, Claude Code, VS Code, OpenCode. Runs locally via `npx`. Phones home? No core function requires it, but it does use API keys for AI features. Worth knowing about.

---

### Pattern 2 ÔÇö Simple flat files (most portable, what you'd build yourself)

What the majority of practitioners not using Task Master do:

```
project/
ÔööÔöÇÔöÇ plan/
    Ôö£ÔöÇÔöÇ spec.md       # What we're building, why, what's out of scope
    Ôö£ÔöÇÔöÇ tasks.md      # Numbered checklist, agent marks [x] as it works
    ÔööÔöÇÔöÇ decisions.md  # Key choices made, alternatives rejected, why
```

**`spec.md`** ÔÇö written before any code. Contains: goal, constraints, what success looks like, what's explicitly out of scope. Agent reads this to stay on track. You edit it before handing off.

**`tasks.md`** ÔÇö the execution checklist. Each task is atomic, verifiable, and has a clear done state. Agent marks tasks complete as it works. Survives session breaks ÔÇö you come back, read it, know exactly where things are.

**`decisions.md`** ÔÇö log of non-obvious choices. "Used X instead of Y because Z." Prevents the agent from re-litigating settled decisions in future sessions.

Concrete `tasks.md` example:
```markdown
# Tasks ÔÇö PDF Parser v1 (script tier)

## Status: in progress

- [x] 1. Set up project structure and venv
- [x] 2. Implement pdfplumber-based text extractor
- [ ] 3. Parse table data from maintenance records (IN PROGRESS)
- [ ] 4. Write output to CSV with audit columns
- [ ] 5. Add error logging to file
- [ ] 6. Test with 5 real PDFs from work samples
```

---

### Pattern 3 ÔÇö Memory bank (Cursor/Roo community pattern)

Some people keep a `memory-bank/` folder in the project:

```
project/
ÔööÔöÇÔöÇ memory-bank/
    Ôö£ÔöÇÔöÇ projectbrief.md      # What this project is
    Ôö£ÔöÇÔöÇ activeContext.md     # Current focus, recent changes, next steps
    Ôö£ÔöÇÔöÇ progress.md          # What works, what doesn't, known issues
    ÔööÔöÇÔöÇ techContext.md       # Stack, dependencies, setup
```

The agent is instructed to read `activeContext.md` at the start of every session and update it at the end. This is the "continuity file" ÔÇö its entire purpose is surviving session breaks.

**Honest assessment:** works well but requires discipline. The agent needs an explicit instruction to update it, otherwise it won't. And if *you* forget to tell it, the file goes stale. But for a solo developer with long gaps between sessions, `activeContext.md` is the single highest-value file you can have.

---

## What Maps to Your Situation

Given your tier system and interruption pattern, here's the concrete mapping:

| Tier | Memory needed | Planning artifacts |
|---|---|---|
| **Jerryrig** | None | None |
| **POC** | None | Optional: one-line status comment in the file itself |
| **Script** | Project `AGENTS.md` with gotchas | `plan/tasks.md` (agent marks progress) |
| **Application** | Project `AGENTS.md` + `activeContext.md` | `plan/spec.md` + `plan/tasks.md` + `plan/decisions.md` |

The `activeContext.md` is your solution to the offshore gap problem. Before you go offshore, the agent writes a handoff note. When you come back, you read it, session resumes. No re-explaining.

**The key behavior rule** that makes this work: agent is instructed to update `activeContext.md` at the end of any script or application-tier session. Not optional, not on request ÔÇö automatic. Goes in AGENTS.md as a hard rule.

---

Does this give you enough to decide what you want? Specifically: do you want to adopt the flat-file pattern yourself (simple, portable, you control it), or is Task Master worth evaluating as a V1 component?

---
## USER  11:29:49

given this newly discussed context (different project tiers, variable workflow from firected edit to human in the loop to autonomous implementation), shoud i stick to single agent or multiple agents setup?

---
## ASSISTANT  11:29:49

Good question to resolve before designing anything. Let me think through it against your actual situation rather than the general case.

---

## The Honest Answer First

**Single agent with on-demand subagents. Not a multi-agent architecture.**

Here's why.

---

## What Multi-Agent Actually Means in Practice

There are two very different things people call "multi-agent":

**A) Orchestrated parallel agents** ÔÇö a lead agent spawns multiple workers running simultaneously on different parts of a task. Like a foreman dispatching crew members. High setup cost, high API cost, pays off on large codebases with parallelizable work. This is what Task Master and Claude Squad do. **Not for you. Not yet.**

**B) On-demand subagents** ÔÇö your main session stays clean, and you dispatch isolated agents for specific bounded tasks: "go investigate this file structure and report back", "review this diff for problems", "research how this library works". They run, return a summary, context stays clean. **This is available today with zero setup and directly solves your problems.**

The difference matters. A is an architecture decision that shapes everything. B is just a tool you use mid-session when it makes sense.

---

## Applied to Your Tier System

**Jerryrig / POC:** Single agent, no subagents. Overhead not justified. You're in and out fast.

**Script:** Single agent. Occasionally dispatch a subagent to investigate before implementing ÔÇö keeps your main context clean for execution. Not mandatory.

**Application:** Single agent as default. Subagents on demand for:
- Exploring the codebase before planning (so exploration tokens don't pollute your implementation context)
- Independent code review after implementation (fresh context, not biased by having written the code)
- Research tasks (look up how X works, come back with findings)

---

## The Specific Problem Multi-Agent Solves That You Actually Have

Your real constraint is **context window degradation during long sessions**. You described: human-in-the-loop as default, sometimes hand off to autonomous execution after plan approval. That means sessions can get long.

The subagent pattern solves this without a full multi-agent architecture:

1. **Explore phase** ÔåÆ dispatch subagent to read files and summarize. Main context only gets the summary, not the raw file reads.
2. **Implement phase** ÔåÆ main agent executes against the plan.
3. **Review phase** ÔåÆ dispatch fresh subagent to review the diff. It hasn't seen the implementation process, so it evaluates the result objectively.

This is three uses of a single pattern, not three coordinated agents. You don't manage them ÔÇö you just say "use a subagent to investigate X" and the tool handles it.

---

## What Would Push You Toward True Multi-Agent

- You're running the same type of task on many files in parallel (e.g. migrate 50 scripts to a new format)
- You need a dedicated reviewer running on every task automatically without you asking
- Sessions routinely hit context limits before finishing

None of these are your situation today. They might be eventually, but that's V2.

---

## Concrete Recommendation

**Design the harness for single agent.** Build in the habit of using subagents for the three cases above (exploration, review, research). Don't architect for multi-agent coordination ÔÇö the overhead isn't justified and it would complicate your setup for work you can't even do yet on your tier system.

If you reach the point where you're running application-tier projects that regularly hit context limits, revisit. The harness doesn't need to change ÔÇö you'd just add an orchestration layer on top of what's already there.

Ready to start designing the structure now?

---
## USER  11:34:26

so your proposal is generalist agent with especialist subagents?

---
## ASSISTANT  11:34:26

Yes. Exactly that.

One generalist agent that knows you, your standards, your tier system, and your workflow. It handles everything from jerryrig edits to application planning.

When it needs depth without polluting its own context, it dispatches a specialist subagent: an explorer that reads and summarizes, a reviewer that audits output, a researcher that fetches and distills. Each specialist is narrow, stateless, and disposable. The generalist stays clean.

The analogy from your world: you're the lead mechanic. You know the whole rig. When you need a specific reading from a confined space, you send someone in with a gauge. They come back with a number. You make the call.

---

Two things this implies for the harness design:

**1. The generalist's identity (AGENTS.md) should not contain specialist knowledge.** Reviewer behavior, research protocols, exploration patterns ÔÇö those belong in subagent definitions, not the main context. The generalist only needs to know *when* to dispatch, not *how* the specialist works.

**2. Specialists are skills or subagent files, not freeform prompts.** You define them once. "When asked to review code, use the reviewer subagent." The generalist calls it by name. Consistent behavior, no re-explaining.

---

This is also the pattern that scales gracefully. Today: one generalist, three specialists. Later, if you build work-specific tools (SAP navigator, PDF extractor, maintenance report writer), they slot in as additional specialists without touching the generalist.

Ready to design the structure?

---
## USER  11:36:35

where to draw the line between a agent and a skill?

---
## ASSISTANT  11:36:35

Good question to nail down before designing anything.

---

## The Concrete Distinction

**A skill is a recipe. An agent is an actor.**

A skill tells the generalist *how to do something* ÔÇö it's a set of instructions loaded into the existing context. The generalist reads it and follows it. No separate context window, no separate tool permissions, no independent judgment. It's just structured guidance.

A subagent *is* something ÔÇö it has its own context window, its own tool access, its own scope. It runs, does work, and reports back. The generalist doesn't follow its instructions, it receives its output.

---

## The Practical Test

Ask these questions in order:

**1. Does it need to read files, run commands, or take actions independently?**
Yes ÔåÆ subagent. No ÔåÆ skill.

**2. Do you want it isolated from the main context?**
Yes (exploration, review, research) ÔåÆ subagent. No ÔåÆ skill.

**3. Is it a workflow or a worker?**
Workflow (do these steps in this order) ÔåÆ skill. Worker (go figure this out and come back) ÔåÆ subagent.

**4. Does it need different tool permissions than the generalist?**
Yes ÔåÆ subagent. No ÔåÆ skill.

---

## Applied to Your Situation

| Thing | Type | Why |
|---|---|---|
| "How to run a script-tier task" | Skill | It's a protocol the generalist follows |
| "How to write a plan file" | Skill | It's a format/procedure |
| "How to handle tier inference" | Skill | It's decision logic for the generalist |
| "Review this diff for problems" | Subagent | Needs fresh context, independent judgment |
| "Explore the codebase before planning" | Subagent | Needs to read many files without polluting main context |
| "Research how library X works" | Subagent | Bounded task, returns a summary |
| "Write audit-trail compliant output" | Skill | It's a formatting rule, not an actor |
| "SAP/PDF workflow steps" | Skill | Procedural instructions the generalist follows |
| "Verify the implementation matches the plan" | Subagent | Fresh context, adversarial review |

---

## The Edge Case Worth Naming

Sometimes something *looks* like a skill but should be a subagent: anything where the generalist doing the work and then reviewing the work in the same context is a conflict of interest. Code review is the obvious one. The generalist wrote the code ÔÇö it's biased. A subagent with a fresh context is not.

The rule: if the value comes from *independence*, it's a subagent. If the value comes from *consistency*, it's a skill.

---

Ready to design now?

---
## USER  12:33:58

this is where i wanted to arrive with this discussion.
when should a agent execute the task directly? when to call a subagent? should the main agent be able to code, but still have dedicated coding subagent? should planning be a main task or a subagent task? my understanding is that review should be a subagent task. is this correct?
keep in mind i want to stay token efficient. sometimes the "clean", "book solution" is to call a subagent, but it might be worth it to execute in the main agent

---
## ASSISTANT  12:33:59

Good. This is the real design question. Let me be direct.

---

## Your Intuition on Review is Correct ÔÇö With a Caveat

Review should be a subagent **for application and script tier, not for jerryrig/POC**. The value is the fresh context and independence. For a 20-line throwaway script, the overhead isn't worth it. For a 300-line module someone else will maintain, it is.

---

## The Token Efficiency Reality

Calling a subagent costs tokens too. You pay for:
- Spawning the subagent's context
- Whatever it reads
- The summary it returns to the main context

So a subagent is only efficient if what it *prevents* (file reads, exploration tokens, bloated main context) is larger than what it *costs*. For small tasks it usually isn't.

**The break-even point is roughly: if the investigation or review would consume more context than the task itself, use a subagent. Otherwise don't.**

---

## Task by Task

**Direct edits / small changes**
Main agent executes directly. No subagents. Full stop. The overhead of dispatching is larger than the task.

**Planning**
Main agent, not a subagent. Planning requires your input, your approval, back-and-forth. You can't have that conversation with a subagent ÔÇö it runs and returns, it doesn't dialogue. Planning is the one thing that must stay in the main context because *you* are part of the loop.

The exception: the *exploration phase before planning* can be a subagent. "Go read the codebase and come back with what's relevant to this task." That's bounded, stateless, returns a summary. The planning itself then happens in main context with you.

**Coding / implementation**
Main agent executes directly for most cases. Here's why: coding against a plan is sequential and interactive. You watch it happen, redirect if it goes wrong, catch mistakes early. Putting that in a subagent removes your ability to intervene mid-execution.

The exception: if a task is truly isolated and you're confident in the plan ÔÇö "implement this one utility function that has no dependencies" ÔÇö you could dispatch a coding subagent. But in practice, implementation errors caught early are cheaper than implementation errors caught at review. Keep coding in main context.

**Should the main agent be able to code?** Yes. The generalist codes. A dedicated coding subagent adds complexity without clear payoff for your scale of work. You're not running 10 parallel coding workers. One agent, coding in main context, is the right call.

**Research / external information**
Subagent. Always. It reads URLs, docs, or files you point it at, returns a distilled summary. That's exactly the bounded stateless pattern. The main context gets the answer, not the 50 pages of documentation that produced it.

**Review**
Subagent for script and application tier. Main agent for jerryrig and POC. The value ÔÇö fresh context, no bias ÔÇö only matters when the code has meaningful longevity or complexity.

---

## The Practical Heuristic

```
Is the task interactive or requires your input mid-execution?
ÔåÆ Main agent.

Is it a one-way bounded task that returns a result?
ÔåÆ Subagent candidate.

Is it a subagent candidate AND large enough that its token cost
  in main context exceeds the subagent overhead?
ÔåÆ Subagent.
ÔåÆ Otherwise: main agent.
```

---

## Mapped to Your Tiers

| Phase | Jerryrig | POC | Script | Application |
|---|---|---|---|---|
| Explore | Main | Main | Subagent if large | Subagent |
| Plan | Main | Main | Main | Main |
| Code | Main | Main | Main | Main |
| Review | Skip | Skip | Subagent | Subagent |
| Research | Main | Subagent | Subagent | Subagent |

---

The generalist codes, plans, and dialogues with you. Subagents handle the bounded, one-way, context-expensive tasks where independence or isolation has clear value. That's the line.

Ready to design now?

---
## USER  12:38:40

explore and research. what's the difference?

---
## ASSISTANT  12:38:40

Good catch. I used them loosely. They're different.

---

**Explore** ÔÇö looking inward. Reading *your* codebase, your files, your project structure. "What does this module do? What files are relevant to this task? What's the current state of the project?" The source is local, already on disk.

**Research** ÔÇö looking outward. Fetching external information. "How does this library work? What's the right pattern for this problem? What does the docs say?" The source is the web, documentation, external references.

---

## Why the Distinction Matters for Your Harness

They need different tools:
- Explore needs filesystem + grep + read. No network.
- Research needs fetch/web search. Minimal filesystem.

They have different trust profiles:
- Explore output is factual ÔÇö it read your files, it reports what's there.
- Research output requires skepticism ÔÇö web content can be wrong, outdated, or hallucinated. The agent should flag confidence and sources.

They have different when-to-dispatch rules:
- Explore: dispatch when the investigation would read enough files to significantly bloat main context. Small codebases or narrow investigations ÔåÆ main agent.
- Research: almost always dispatch. External fetching in main context is rarely worth the token cost, and you want the distilled answer, not the raw content.

---

## Updated Table

| Phase | Jerryrig | POC | Script | Application |
|---|---|---|---|---|
| Explore | Main | Main | Subagent if large | Subagent |
| Research | Skip | Main or subagent | Subagent | Subagent |
| Plan | Main | Main | Main | Main |
| Code | Main | Main | Main | Main |
| Review | Skip | Skip | Subagent | Subagent |

Research on jerryrig is skip because if you need to research to do a jerryrig task, it's probably not actually jerryrig tier.

---

Ready to design now?

---
## USER  13:34:27

say hello

---
## ASSISTANT  13:34:27

Hello! 

Ready to design the harness structure now, or do you have more questions to resolve first?

---
## USER  13:36:09

summarise current conversation to a md file in opencode_v5/ folder. intention is to continue with clean context. leave behind rejected ideas. keep "current state". intention is for me to prune/edit the file before resuming. retain details when they matter.

---
## ASSISTANT  13:36:09

**[TOOL: bash]**
Input: {
  "command": "Test-Path -LiteralPath \"C:\\Users\\btny\\.config\\opencode\\opencode_v5\"",
  "description": "Check if opencode_v5 directory exists"
}

---
## ASSISTANT  13:36:20
