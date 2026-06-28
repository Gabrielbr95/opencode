# My Situation — Context for AI Assistants

## Who I am

Mechanical engineer working in maintenance at a large, old-school oil and gas corporation. I have an intermediate technical background — I've studied machine learning and understand how AI works at a conceptual level (tokenization, transformer architecture, how inference works). I am not a professional developer. My coding skills are mediocre. My main language is Python. I have some exposure to C++ and Java. I haven't kept up with AI news much in the past year due to lack of time.

The tools I build range from simple personal scripts to small applications for my immediate team. I frequently have to reverse engineer connection points because the systems I work with were built for human input and don't expose APIs.

## My work environment

- Corporate Windows laptop, no admin privileges
- Personal home server running Fedora with Podman (for non-corporate workloads)
- Heavy legacy system environment — many systems that don't communicate with each other
- Workflows are manual, repetitive, error-prone, and bureaucratic
- The company has written procedures for almost everything, but they rarely reflect what actually happens
- The industry is heavily regulated

## My constraints

- No management support yet — I need to build working tools, show results, and climb at least 4 layers of corporate hierarchy before I can get authorization for any paid tooling
- I am funding everything out of my own pocket, probably for around a year
- Corporate data must stay local or pass through approved corporate APIs
- Some Azure services are available. I can request access to some more. I'm not sure what is available and what is not.
- I have a corporate-approved Claude API key — that channel is cleared
- External hosted services that receive corporate data are a problem and should be avoided
- MCP servers I run locally on my own machine are fine — they never send data externally

## What I am trying to do

Automate the bureaucratic, repetitive parts of my maintenance engineering job. My workflows involve:

- Reading from and writing to systems that were designed for human input only (no API, sometimes just a web UI or a desktop application)
- Dealing with a large volume of PDF documents, scanned records, and internal procedures
- Producing reports and documents that other people review and approve
- Following compliance and audit trail requirements because of industry regulation

My immediate goal is to build tools that save measurable time, are visible to people above me, and make a compelling case for budget and formal authorization. I am not building a platform. I am building individual tools that solve specific pain points.

## What a good answer looks like for me

- Practical and direct — skip abstract architecture theory unless it changes what I should actually build
- Acknowledge my constraints (no admin, no budget, data locality, no management support)
- Assume I can follow technical concepts but may need help with implementation details
- Use standard industry terms (MCP, RAG, RPA, etc.) but explain them briefly if they are central to a recommendation
- When suggesting tools or frameworks, tell me whether they run locally, require a subscription, or phone home
