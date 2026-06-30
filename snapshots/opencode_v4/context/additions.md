- I'm a thinkerer. I like to build things and learn how they work. 
- interests involve programing, electronics, finances, engineering. This evolves to 3d printing and trading algorithms, but anything in-between also sparks my interest.
- i despise friction in my routine and am willing to automate most non critical, boring stuff I can. Either in personal life and at work. 
- main constraints are mostly time and money. This one is very important. This also means I frequently have to stop my projects in the middle and resume another time. I keep thinking during the mean time. Requirements evolve, and sometimes this leads to reactors before the V0 is ready. 
- I have some hard builder skills, but not necessarily the tools to solve problems. I know wood working, metal welding, machining, electrical work and such. I'm not afraid of tools. 
- I work in a offshore oil rig as a mechanic. I fix all sorts of stuff. This includes jet engine generators, diesel motors the size of a room, cranes, pumps, compressors, hydraulic units, hvac units, fans, all the way down to toilets. This is my main trade and bread earner.
- I sometimes am alocated to maintenance planning. This is the case now. This is previsible and happens from time to time. They need someone with hands down experience in the planning team and my team rotates technicians in this hole.
- I get frustrated when I have a idea or necessity and the specific tool to solve my problem either don't exist or is too expensive. This is the origin of most of my personal projects. This is a strength and a drawback, as I tend to want to reinvent the wheel when sometimes a slightly different wheel already exists and solves my problem. I have to take care not to fall too deep in this habit hole. Otherwise there is no progress.
- cost effectiveness is very important in my personal projects. The thing needs to be cheap, pay for itself (investment), or bring a lot of value to the table for me to pay a high price for it. Given it's a well spent money, I have no problem paying a high price for a high quality tool.
- I also despise substription services. These are real money sinks. Good for corporations. Bad for me. Some of them are unavoidable. Some others are worth their price, but these ones are rare.
- home setup: personal desktop PC, Manjaro Linux + windows (Linux main), 32gb ram, ryzen 5600, 1tb ssd, rtx 3060ti 8gb, 1tb hdd. Personal laptop: manjaro Linux + Windows (Linux main), 16gb ram, ryzen 5700x mobile, 1tb ssd, rtx 3060 mobile. Home server: intell n300, fedora server, podman, next cloud, wireguard. 





Context files to read first:
- /home/gabriel/.config/opencode/opencode_v4/my-context-v2.md — who I am, how I work, what I expect. Ignore the opencode_v4/context/ folder; this file summarises everything.
- /home/gabriel/.config/opencode/opencode_v3/ — my current opencode workflow (work setup). 
- /home/gabriel/.config/opencode - my current opencode home workflow (home setup)

backstory: 
i had 1 instance of opencode configuration at home.
i migrated it to work environment 
i iterated on it at home up to current state.
i did not migrate the current changes and iterated at work 3 times (v3)
one is not more current than the other. they are paralel. i tried to transfer the same concepts, but the final result is not 100% identical. some ideas appear in one, but not the other.
now i want to merge both and retain a single configuration on both environments.


What I want:
Iterate on my opencode setup. Restructure agents and skills, then implement to opencode_v4.
Agent restructure — 3 agents total:
1. Planner — absorbs the current orchestrator role as a skill (not a separate agent).
2. Builder — stays as-is or with minor adjustments.
3. Antagonist — absorbs the current reviewer and architect roles as skills (not separate agents).
Skill hygiene:
- Review all existing skills in current direcotry and v3.
- Ensure the new orchestrator, reviewer, and architect skills do not overlap with any other skill. No skill overlap allowed. If overlap exists, merge or reassign cleanly.
Implementation rules:
- Copy work directly wherever it applies. Edit only what needs to change.
- Apply any improvements you see fit based on my-context-v2.md (my constraints, preferences, tier system, session patterns, etc.).
- Output everything to /home/gabriel/.config/opencode/opencode_v4/.
Approach:
- Discuss the restructure plan before writing any files. No code until the design is agreed on.