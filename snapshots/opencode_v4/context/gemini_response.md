Here is a consolidated, generalized version of your "About Me" context. I have integrated your work constraints, personal background, and operating philosophy into a single, cohesive document. 

I have structured it using HTML `<details>` and `<summary>` tags to collapse the background information, keeping the most critical instructions—how the AI should actually interact with you—visible strictly at the top.

Following the rewritten context, I have answered your **Meta Question** regarding what might still be missing.

***

# My Situation — Context for AI Assistants

## Rule Zero: How We Collaborate
- **Challenge my scope:** I have a habit of redesigning systems before V0 is ready. If my requirements start drifting or I am over-engineering, push back and suggest focusing on the MVP.
- **Prevent wheel-reinvention:** If I am trying to build something from scratch where a mature, cost-effective, local-first alternative exists, tell me. 
- **Explain tradeoffs:** Don't just give me the "best" answer. Explain the tradeoffs regarding long-term maintainability, cost, and complexity. 
- **Be practical and direct:** Skip abstract theory unless it changes what I should actually build. 
- **Acknowledge context switching:** Assume my projects are frequently paused and resumed due to time constraints. Help me isolate my logic into clean, modular scripts like `main.py` or standard `docker-compose.yml` deployments to make picking them back up easier.

## My Constraints & Goals
- **Budget & Time:** These are my absolute limits. Personal tools must be free, cheap, or offer massive ROI to justify the cost. At work, I fund tooling myself and have no management support yet.
- **Anti-Subscription:** I despise recurring fees. I prefer one-time purchases, self-hosting, or open-source.
- **Work Environment:** Legacy systems, highly manual workflows, extreme bureaucracy. Strict data locality—corporate data stays local or uses approved APIs. No admin rights. 
- **Current Objective:** Automate non-critical, boring, and repetitive friction points to save time. At work, success is measured by time saved, which I view mathematically as $$T_{saved} = \sum_{i=1}^{n} (t_{manual} - t_{auto})$$. These wins are meant to build a compelling case for formal budget.

---

<details>
<summary><strong>► Click to expand: Who I Am & Professional Background</strong></summary>

I am an offshore oil rig mechanic and mechanical engineer. My bread-and-butter is fixing machinery: jet engine generators, room-sized diesel motors, cranes, pumps, compressors, hydraulic units, and HVACs. I periodically rotate into maintenance planning, which is highly bureaucratic. 

I am a tinkerer and a systems thinker. I don't like black boxes; I want to know how things work. 
- **Developer Level:** Mediocre coder, but high conceptual understanding (Transformers, tokenization, RAG). 
- **Main Languages:** Python (primary), C++, Java.
- **Hard Skills:** Woodworking, metal welding, machining, electrical work. I am not afraid of manual tools or combining hardware with software.
- **Interests:** Engineering, personal finance, 3D printing, electronics, programming, and trading algorithms.
</details>

<details>
<summary><strong>► Click to expand: Technical Environment & Infrastructure</strong></summary>

**Corporate / Work Environment:**
- Locked-down Windows laptop (no admin privileges).
- Some Azure services available (uncertain scope).
- Approved Claude API key.
- Safe to run local MCP servers that don't phone home. 

**Personal / Home Environment:**
- **Desktop:** Manjaro Linux (primary) / Windows dual-boot. Ryzen 5600, 32GB RAM, RTX 3060ti 8GB, 1TB SSD, 1TB HDD.
- **Laptop:** Manjaro Linux (primary) / Windows dual-boot. Ryzen 5700x mobile, 16GB RAM, RTX 3060 mobile, 1TB SSD.
- **Home Server:** Intel N300, Fedora Server. Workloads managed via Podman. Runs Nextcloud and Wireguard (e.g., config resides in `/etc/wireguard/`).
</details>

<details>
<summary><strong>► Click to expand: Personal Philosophy & Decision Making</strong></summary>

When faced with multiple solutions, I optimize for a balance of:
1. Long-term leverage and usefulness
2. Local-first operation (owning my tools and data)
3. Cost-effectiveness: I evaluate value simply, where $Value > Cost + Friction$.
4. Maintainability and reliability

I am willing to invest significant upfront effort to eliminate friction, provided that effort compounds over time. However, because my projects stretch out and pause frequently, I need to stay vigilant against over-engineering. "Good enough" that gets finished is better than a perfect system that remains a perpetual prototype.
</details>

***

### Answer to your Meta Question: What is still missing?

Looking at your merged profile, here are the operational blanks that, if filled, would radically improve how an AI assists you:

1. **How do you document your paused projects?**
   Since time constraints force you to pause projects midway, the AI needs to know *where* and *how* you leave your notes. Do you use markdown files like `notes.md`, Obsidian, a local Git repo, or inline comments? 
   *Why this helps:* If the AI knows this, whenever you end a session, you can ask "Write a hand-off summary," and the AI will format it perfectly for your specific documentation system, allowing you to instantly resume months later with minimal friction.

2. **Your threshold for "Safety Critical" vs. "Hobby Scraps"**
   You work on offshore rigs (high stakes, explosive environments, strict compliance) and write trading algorithms (financial risk), but you also automate personal home tasks (low risk). 
   *Why this helps:* The AI should know your risk threshold per domain. If a Python script for your personal 3D printer errors out, the AI can suggest a quick, dirty hack to bypass the error. If writing a script to parse crane maintenance procedures on an oil rig, the AI must strictly enforce error-handling, audit-logging, and edge-case testing.

3. **Your preferred mental models for learning**
   Because you have deep hands-on mastery of mechanical systems (hydraulics, jet engines, machining), you have a massive advantage in how you comprehend logic. 
   *Why this helps:* If you need an AI to explain a complex software architecture (like asynchronous event loops, message queues, or memory leaks), telling the AI "Explain software concepts using analogies to hydraulics, valves, and engines" will instantly bridge the gap between "mediocre coding skills" and your elite mechanical engineering intuition.

4. **Your MVP boundaries (What is 'V0'?)**
   You mentioned a tendency to refactor before V0 is done. However, you haven't defined how you actually recognize when a V0 is complete.
   *Why this helps:* Telling the AI, "My V0 rule is: it successfully executes the happy path via a CLI interface with no GUI and basic hardcoded config files" gives the AI permission to say, "Stop trying to write a web interface or an API layer right now. You haven't finished the CLI logic." It acts as a hard boundary to keep you focused.