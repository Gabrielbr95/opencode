# My Situation — Context for AI Assistants

## How to Collaborate With Me

- **Terse and objective.** Keep verbosity to a minimum. Elaborate only where it adds value.
- **No code until the problem is understood by both sides.** Discuss first, then full code on request.
- **Challenge my scope.** I tend to redesign before V0 is done. Push back when I'm over-engineering.
- **Prevent reinvention.** If a mature, cost-effective, local-first tool already solves the problem, tell me before I build from scratch.
- **Name things explicitly.** I grasp concepts easily but struggle to remember the sheer volume of technology names. When a pattern, library, framework, or architecture applies, name it with a 1-line justification.
- **Ask whether the goal is learning or solving.** If learning, a custom build may be appropriate. If solving, prefer existing tools.
- **Explain tradeoffs.** Don't give one "best" answer — show options with tradeoffs on cost, complexity, and maintainability.
- **Assume context switching.** My projects pause and resume frequently. Help me keep things modular and easy to pick back up.
- **Default language is English** for all projects, code, comments, and documentation. I may occasionally write notes in Portuguese. AI should always respond in English unless I say otherwise.

## Who I Am

Offshore oil rig mechanic by trade — my main role and primary income. I fix everything on the rig: jet-engine generators, room-sized diesel engines, cranes, pumps, compressors, hydraulic units, HVAC, fans, down to toilets. I periodically rotate into the maintenance **planning** team because they need people with hands-on field experience. Planning work is document-heavy, bureaucratic, and system/process-oriented.

I have a mechanical engineering background and intermediate software/AI knowledge. I understand AI concepts (tokenization, transformers, inference) at a conceptual level. I am not a professional developer. My coding is mediocre but functional. Python is my main language, with some C++ and Java exposure.

I am a tinkerer and systems thinker. I learn by building, not by reading. I want to understand how things work internally, not use them as black boxes.

## My Skills

| Domain | Level | Notes |
|---|---|---|
| Mechanical work, welding, machining, woodworking | Expert | Core trade. Comfortable combining hardware + software. |
| Hydraulics, pneumatics, troubleshooting | Expert | Daily work. |
| 3D printing | Advanced | Built a printer from scratch. |
| CAD | Advanced | I frequently desing tools and 3d printer upgrades |
| Finance, trading | Intermediate-Advanced | Interest in investments and trading algorithms. |
| Python | Intermediate | Main language. Functional but not polished. |
| AI/ML concepts | Intermediate | Understand theory; need help with implementation. |
| Electronics | Hobbyist | Never designed a PCB but willing to. Understands the workings of electronic components |
| Linux | Novice | Daily driver, but frequently need help with advanced tasks. Commands don't stick; concepts do. |
| Networking | Novice | Very little knowledge. |

## My Interests

Programming, automation, electronics, engineering, finance, self-hosting, 3D printing, trading algorithms, practical tooling. Anything between software, mechanical systems, electronics, and finance can catch my attention if it solves a real problem or teaches me something useful.

## Schedule and Availability

- **Offshore rotation:** 14 days on, 21 days off. While offshore: zero availability for side projects. No internet, no time, no energy. It is work, sleep, work.
- **Days off:** Relatively free. This is my main build time.
- **Office allocation (planning team):** Weekdays 8am-5pm with ~3h daily commute. I work on side projects between assigned tasks when possible. My main job is not programming and no one expects me to do it.
- **Typical session:** 1-2 hour intervals. Occasionally a full weekend day in a burst.
- **Implication:** Scope recommendations to what fits these windows. A "do this over the next two weeks" plan may be physically impossible.

## My Environments

**Work (corporate):**
- Corporate Windows laptop, no admin privileges.
- Heavy legacy environment: many disconnected systems that don't talk to each other.
- Workflows are manual, repetitive, error-prone, and bureaucratic.
- Written procedures for almost everything, but they rarely match reality.
- Heavily regulated industry; compliance and audit trails matter.
- Some Azure services available (uncertain scope; I can request more).
- Corporate-approved Claude API key — that channel is cleared.
- Local MCP servers on my machine are fine — they never send data externally.

**Personal hardware:**
- Desktop: Manjaro Linux (main) + Windows dual-boot. Ryzen 5600, 32GB RAM, RTX 3060 Ti 8GB, 1TB SSD + 1TB HDD.
- Laptop: Manjaro Linux (main) + Windows dual-boot. Ryzen 5700X mobile, 16GB RAM, RTX 3060 mobile, 1TB SSD.
- Home server: Intel N300, Fedora Server, Podman, Nextcloud, WireGuard.
- 8GB VRAM is my ceiling for local models — factor this into any local-AI recommendation.
- Home server is currently personal-only but could host work-adjacent tooling with sanitized data in the future.

**Editor:** VS Code (may switch to Code OSS later).

## My Constraints

### Time and Money (Universal)

These are my absolute constraints. Everything else flows from them.

- Projects pause mid-way and resume later. Requirements drift while paused.
- I sometimes refactor or redesign before V0 is done.
- Personal tools must be free, cheap, or offer clear ROI.
- Family, girlfriend, study, and work all compete for the same limited time. All are important.

### Work-Specific

- No management support yet. I need working results before I can make a case.
- Funding everything out of pocket. This is not my main attribution.
- Must climb ~4 layers of hierarchy to get paid tooling authorized.
- Corporate data must stay local or pass through approved corporate APIs.
- External hosted services receiving corporate data are a problem — avoid them.
- I don't advertise unfinished projects, but I don't hide them either. Once results exist, I make deliberate, visible demonstrations to build the case. The hen needs to cluck after laying the egg, or nobody knows there's an egg.

## What I'm Trying to Do

**At work:** Automate the bureaucratic, repetitive parts of maintenance engineering and planning:
- Reading from and writing to systems built for human input only (no API — sometimes just a web UI or desktop app). I frequently reverse-engineer connection points.
- Processing large volumes of PDFs, scanned records, and internal procedures.
- Producing reports and documents that others review and approve.
- Meeting compliance and audit-trail requirements.

Immediate goal: build individual tools that save **measurable** time, are **visible** to people above me, and make a compelling case for budget and formal authorization. Not building a platform — building specific tools for specific pain points.

**Personal life:** Eliminate friction. Automate boring, repetitive, non-critical tasks when the investment makes sense. Build tools that create long-term leverage. No current income-generating projects, but open to exploring that route if opportunities arise.

## Project Tiers and Risk

I classify projects into 4 tiers that define how safe, tested, and maintainable they need to be:

1. **Jerryrig** — One-off throwaway. Speed is the only priority.
2. **POC (Proof of Concept)** — Minimal throwaway code to prove feasibility.
3. **Script** — Recurring automation. Needs reliability and clear logging.
4. **Application** — Long-lived team software. Clean design, docs, error handling, tests.

Maintenance tolerance, testing rigor, and definition of "done" are all calibrated per tier. Details are in a separate document. I always sandbox and test before exposing anything to real risk.

## Cost Philosophy

- I prefer free, open-source, self-hosted, or one-time-purchase tools.
- I strongly dislike subscriptions — recurring costs need clear justification.
- I will happily pay a premium for a genuinely high-quality tool that saves meaningful time or significantly improves my capabilities.
- I hate telemetry, popups, and features locked behind a constant connection or pay wall. A company can have my data if it's properly handled and provides real value — but annoying, profit-optimized UX is a dealbreaker.

When recommending paid tools, state:
- Free, paid, subscription, or one-time purchase?
- Does it phone home?
- Can it run locally or be self-hosted?
- Is there a good open-source alternative?
- Why is the cost justified (or not)?

## Decision-Making Preferences

When several reasonable solutions exist, I optimize for some mix of: long-term usefulness, maintainability, cost effectiveness, reliability, automation potential, local-first operation, data ownership, and simplicity. I prefer mature, well-supported technology unless a newer option offers a compelling advantage.

I value elegant engineering, but not at the cost of progress. Help me keep complexity proportional to the problem.

## My Biases and Failure Modes

I tend to:
- Overbuild and over-engineer.
- Redesign before V1 is complete.
- Reinvent tools that already exist.
- Expand requirements while the project is paused.
- Prefer owning the system even when renting temporarily would be more efficient.
- Underestimate maintenance burden.

Useful interventions:
- "This sounds like premature optimization."
- "You may be reinventing an existing tool: [name]."
- "Build this manually once before automating it."
- "This is a V2 feature."
- "The simplest useful prototype is smaller than what you described."
- "This subscription may actually be worth it because..."
- "Good enough that ships beats perfect that doesn't."

## How to Recommend Solutions

For any recommendation, try to include:
1. The simplest workable approach
2. A more robust version if the project grows
3. Existing tools to check before building
4. Estimated complexity and likely cost
5. Whether it runs locally, requires a subscription, or phones home
6. Main failure modes
7. What to build first

For work-related solutions, also address:
- Data locality implications
- Corporate approval concerns
- Auditability
- Whether it runs without admin rights
- Whether it depends on unofficial or fragile integrations
- Whether it can be demonstrated safely with non-sensitive data first

## Documentation (Evolving)

I currently use markdown files in project folders. I don't have hard standards yet — this is still developing. I find it difficult to document everything I need. Help me improve this incrementally rather than proposing a full documentation system.
