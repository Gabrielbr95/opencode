Here's my take. I've merged your current doc, your handwritten additions, and the other AI's diff into a single, deduplicated, life-spanning context document — then below it I answer your meta question about what's *still* missing (including a couple of things I think matter a lot more than what either draft captured).

One thing I reconciled and want to flag up front: your current doc opens with *"Mechanical engineer working in maintenance,"* but your additions say you're an **offshore rig mechanic** (your main trade/income) who gets **rotated into maintenance planning periodically** (the current situation). Those tell different stories about your day-to-day. I rewrote it as "mechanic by trade with engineering-level knowledge, currently rotated into planning." Adjust if I got the emphasis wrong.

---

```markdown
# My Situation — Context for AI Assistants

## Who I am

Offshore oil rig mechanic by trade — this is my main role and primary income.
I fix everything on the rig: jet-engine generators, room-sized diesel engines,
cranes, pumps, compressors, hydraulic units, HVAC, fans, all the way down to
toilets. I work a rotation (weeks offshore, then time off at home).

I am periodically rotated into the maintenance **planning** team because they
need people with hands-on experience in that role. This is predictable and
happens from time to time. It is the case right now.

I have mechanical-engineering-level knowledge and an intermediate technical
background. I've studied machine learning and understand AI conceptually
(tokenization, transformer architecture, how inference works). I am NOT a
professional developer — my coding is mediocre. Python is my main language,
with some C++ and Java exposure. I haven't kept up with AI news much in the
past year due to lack of time.

I am a tinkerer. I build things to learn how they work. I learn by building,
not by reading.

## My skills and reach

- **Hands-on trades (expert):** mechanical work, welding, machining,
  woodworking, electrical work, hydraulics, pneumatics, general troubleshooting.
  I am not afraid of tools and I'm comfortable combining hardware + software.
- **Software (intermediate/hobbyist):** Python mainly; mediocre but functional.
- **AI/ML (conceptual):** I understand the theory; I need help with
  implementation details.
- I often have the *builder skills* but not the *specific tools* to solve a
  problem — which is frequently where my projects start.

## How I think

- I think in **systems**, not isolated problems.
- I want to understand how things work internally, not treat them as black boxes.
- When I hit friction, repetitive work, or unnecessary complexity, my instinct
  is to ask why it exists and whether it can be eliminated.
- I value long-term leverage over short-term convenience, and solutions that
  compound over years.
- Known failure mode: I tend to want to reinvent the wheel even when a slightly
  different wheel already exists. I also redesign systems before V1 is finished
  as requirements evolve in my head. I need help catching this.

## My interests

Programming, electronics, finances, engineering — extending out to 3D printing
and trading algorithms, with everything in between also fair game.

## My environments

**Work (corporate):**
- Corporate Windows laptop, no admin privileges.
- Heavy legacy environment: many systems that don't talk to each other.
- Workflows are manual, repetitive, error-prone, and bureaucratic.
- Written procedures exist for almost everything but rarely match reality.
- Heavily regulated industry; compliance and audit trails matter.

**Personal hardware:**
- Desktop: Manjaro Linux (main) + Windows, Ryzen 5600, 32 GB RAM, RTX 3060 Ti
  8 GB, 1 TB SSD + 1 TB HDD.
- Laptop: Manjaro Linux (main) + Windows, Ryzen 5700X mobile, 16 GB RAM,
  RTX 3060 mobile, 1 TB SSD.
- Home server: Intel N300, Fedora Server, Podman, Nextcloud, WireGuard.
- (Note: 8 GB VRAM is my ceiling for local models — factor this into any
  local-AI recommendation.)

**Personal tech preferences:** Linux-first, self-hosted, open-source,
local-first, automation over manual work, owning my own infrastructure when
practical.

## My constraints

**Universal (work AND personal): time and money.** This is the most important
constraint. Consequences:
- Projects get paused mid-way and resumed later; I keep thinking about them
  in between, so requirements drift.
- I sometimes refactor/redesign before V0 is even done.

**Work-specific:**
- No management support yet. I must build working tools, show results, and climb
  ~4 layers of hierarchy before any paid tooling gets authorized.
- I'm funding everything out of pocket, likely for ~a year.
- Corporate data must stay local or pass through approved corporate APIs.
- Some Azure services available; I can request more but don't know the full menu.
- I have a corporate-approved Claude API key — that channel is cleared.
- External hosted services that receive corporate data are a problem; avoid them.
- Local MCP servers on my own machine are fine — they never send data externally.

## What I'm trying to do

**At work:** automate the bureaucratic, repetitive parts of maintenance
engineering / planning. This involves:
- Reading from and writing to systems built for human input only (no API —
  sometimes just a web UI or a desktop app); I frequently reverse-engineer
  connection points.
- Large volumes of PDFs, scanned records, and internal procedures.
- Producing reports/documents that others review and approve.
- Meeting compliance and audit-trail requirements.
Immediate goal: build individual tools that save **measurable** time, are
**visible** to people above me, and make a compelling case for budget and formal
authorization. I'm building specific tools, not a platform.

**In personal life:** eliminate friction. I'll automate most non-critical,
boring tasks I can, at home or at work. Many personal projects exist because a
needed tool doesn't exist, is too expensive, or doesn't fit my workflow.

## Cost philosophy

- Cost effectiveness is extremely important. I prefer free/cheap tools, tools
  that pay for themselves, or tools with exceptional long-term value.
- I strongly dislike subscriptions — recurring money sinks, good for
  corporations, bad for me. Some are unavoidable; few are worth it.
- I will happily pay a premium for a genuinely high-quality tool that saves
  meaningful time or significantly improves my capabilities. Well-spent money
  is not a problem.

## Decision-making preferences

When several reasonable solutions exist, I optimize for some mix of: long-term
usefulness, maintainability, cost effectiveness, automation potential,
reliability, local-first operation, and simplicity. I prefer mature,
well-supported tech unless a newer option offers a compelling advantage.

## How AI should collaborate with me

- Be practical and direct — skip abstract architecture theory unless it changes
  what I should actually build.
- Acknowledge my constraints (time, money, no admin, no budget, data locality,
  no management support).
- Assume I follow technical concepts but may need implementation help.
- Use standard terms (MCP, RAG, RPA, etc.) but briefly explain ones central to
  a recommendation.
- When suggesting tools/frameworks, state clearly whether they run locally,
  require a subscription, or phone home.
- Challenge my assumptions; point out existing tools BEFORE I reinvent them.
- Explain key tradeoffs instead of giving one answer.
- Flag when I'm optimizing prematurely or when "good enough" beats redesigning.
- Help me distinguish worthwhile architectural improvements from unnecessary
  redesign.

## My values

Reduce friction. Build reusable systems. Prefer solutions that compound. Own my
tools long-term over short-term convenience. Keep complexity proportional to the
problem. Automate repetitive work when the investment makes sense.
```

---

## Answering your meta question: what's still missing

The two drafts cover *how you think* thoroughly. What they under-specify is **the practical envelope an AI needs to give you advice that actually fits your life**. The biggest gaps:

**1. Your rotation schedule and offshore connectivity — this is the single most important missing piece.** Your "projects pause and resume" pattern isn't random; it's structurally tied to a rotation cycle (X weeks offshore, X weeks home). An AI that knows this can scope tasks correctly: lightweight thinking/reading offshore, heavy build sprints at home. Add the specifics — e.g., "14 on / 14 off," whether you have reliable internet offshore, and whether you can even work on personal projects while on the rig. Right now an assistant might hand you a "do this over the next two weeks" plan that's impossible.

**2. How much time a "session" actually is.** "Time is a constraint" is vague. Are your build windows 30-minute evenings, full weekend days, or week-long stretches at home? This changes whether the right answer is "a 50-line script tonight" vs. "a phased project." Give a rough cadence.

**3. Response/communication format preferences.** You've defined *content* and *tone* but not *shape*: Do you want code-first or explanation-first? Long thorough answers or terse ones? Full working scripts or skeletons you complete? Step-by-step or just the final design? This is the cheapest thing to add and disproportionately improves every interaction.

**4. Language.** Your writing suggests English isn't your first language (and the offshore O&G context hints at where you're based). If you'd prefer answers in another language, want plain English, or don't care — say so. Also worth stating: should the *artifacts* (code comments, report templates) be in English or your local language, especially for work compliance docs?

**5. Per-domain skill calibration.** You're an *expert* mechanic, an *intermediate* coder, and *conceptual* on ML. A flat "intermediate technical background" makes an AI miscalibrate — over-explaining hydraulics, under-explaining a Python async pattern. The rewrite above splits these out; keep that granularity and extend it (e.g., where are you with Linux sysadmin, Docker/Podman, web scraping, electronics/PCB design, 3D-printing CAD?).

**6. Risk tolerance and reversibility.** Different at work vs. home. At work you're in a regulated, audit-trail, no-admin environment where a mistake has consequences. At home you can break things freely. State this explicitly so an AI knows when to be conservative (work, anything safety/compliance related) vs. when to suggest the bleeding-edge fun option (personal tinkering).

**7. A stated definition of "done" / anti-perfectionism guardrail.** You already admit to over-engineering. Make it actionable: give the AI permission and *criteria* to tell you to ship — e.g., "if it solves the immediate pain and is maintainable, tell me to stop." Otherwise the "challenge my assumptions" instruction has nothing concrete to push against.

**8. Existing tooling/stack you already use and like.** To stop you reinventing wheels, the AI needs to know what's already on your machines (editor, languages, frameworks, home-server apps, automation tools, any existing scripts). "Point out existing tools before I reinvent" works far better if it also knows what *you* already standardized on.

**9. Life obligations that compete for time/money.** Family, studying, other commitments — even one line ("I have a family / limited weekend time") materially changes what "realistic" looks like and is part of generalizing beyond work.

A couple of smaller ones worth a line each: your **physical/offline operating environment** (offshore = no cloud, harsh conditions — tools may need to run fully offline), and whether personal projects have any **"pay for itself" income angle** (the trading-algo and 3D-printing interests hint that some projects might be expected to generate value, not just save time).

If you add #1, #2, and #3, you'll get the biggest quality jump per word — those three are where assistants most often give you plans that don't physically fit your reality.

Want me to fold any of these into the document directly, or produce a shorter "lite" version for quick context-pasting alongside this full one?