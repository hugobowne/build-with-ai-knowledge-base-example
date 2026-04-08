---
type: guest_talk
title: "Building Tools for Thinking with AI: Canvas Chat and Spec-Driven Development"
date: 2026-04-01
speakers: [Eric Ma (Moderna), Hugo Bowne-Anderson]
topics: [thinking tools, canvas chat, branching conversations, LLM council, spec-driven development, vibe coding refactoring, plugin architecture, pixi, open router, SvelteKit, SQLite, feedback loops, testing harness]
source_file: raw/building_tools_for_thinking_with_ai_eric_ma.md
word_count: ~19400
---

## Overview

A live-coded workshop with Eric Ma, who leads research data science (and now also clinical development data science) at Moderna. Eric's Moderna audit finding that all production AI was workflows (not agents) is referenced in [[ws_6_building_ai_agents]] and [[ws_7_workflows_multiagent_and_context_engineering]]. Eric demonstrates Canvas Chat, a tool he built for nonlinear AI-assisted thinking, then rebuilds a v2 from scratch live on stream using Cursor, Open Code, and multiple LLM providers. The session is a masterclass in practical AI-assisted software development workflows.

Canvas Chat's core premise is that chat should be nonlinear: each message is a node on an infinite canvas, connected by edges, enabling branching conversations. Users can branch off any message, explore different ideas in parallel, then merge branches back. The "committee" feature implements Andrej Karpathy's LLM Council concept -- multiple LLM instances take different personas (e.g., quantum physics researcher, self-taught programmer, STEM educator), independently research a question with web search, review each other's outputs, and synthesize a final answer.

The live build demonstrates Eric's opinionated stack: PDS CLI for project scaffolding with cookie-cutter templates, Pixi for multilingual environment management, LiteLLM for provider-agnostic LLM routing, SvelteKit with SvelteFlow for the canvas UI, SQLite for data storage, and FastAPI for the backend. The session provides exceptional insight into spec-driven development: when to use it (not for first prototypes, but after the problem/solution space is understood), how to balance planning with execution, and the critical role of immediate feedback loops (Cypress end-to-end tests that feed errors back to the coding agent).

A candid discussion of "undoing vibecoded slop" reveals how Eric's first version of Canvas Chat was "opusmaxed" without architectural control, leading to 8,000+ line monolithic files. This connects to the vibe coding debate in [[builders_club_brad]]. He systematically refactored with AI assistance into a plugin architecture with small modules, making context gathering easier for coding agents.

## Key Topics

- Canvas Chat: nonlinear branching conversation tool for AI-assisted thinking
- LLM Council / Committee: multiple personas independently research, cross-review, and synthesize answers
- Spec-driven development: when to use formal specs vs. exploration, levels of formality
- Refactoring vibecoded slop: systematic decomposition from monolith to plugin architecture
- Cookie-cutter project templates: opinionated scaffolding as "step zero" for AI-assisted building
- Pixi for multilingual environment management (Python, R, TypeScript)
- LiteLLM for provider-agnostic routing
- Immediate feedback loops: Cypress tests feeding JS console errors back to coding agents
- The spectrum from exploration (low formality) to production (high formality)
- Model selection: smart models for planning, cheaper models for execution

## Key Insights

- "You can't know your problem deeply until you've built a wrong solution" -- first versions should never use strict spec-driven development; feel out the problem first
- After exploration, specs and tests become double constraints: documentation constrains intent, tests constrain behavior -- both prevent the coding agent from going off the rails
- Opusmaxing without architectural control leads to 8,000+ line monolithic files that are painful to extend; systematic refactoring into plugin architecture with small modules makes AI assistance much more effective
- Immediate feedback loops are the key to going hands-free with coding agents: Cypress end-to-end tests that catch dropped curly braces and feed JS console errors directly back to the agent -- relates to the testing and feedback loops discussed in [[ws_4_testing_and_observability]] and [[ws_3_evals_and_feedback_loops]]
- Having an opinionated project template (cookie-cutter) is "step zero" -- it constrains the design space for the coding agent from the start
- When a tech stack is well-established and likely in training data, let the LLM recommend; for genuinely new or internal tools, come in with a strong opinion
- Provider lock-in aversion is a practical stance: Eric cycles through whatever frontier models are available, hitting rate limits then switching, staying familiar with the full ecosystem. See [[ws_4_testing_and_observability]] where William Horton advocates OpenAI SDK + LiteLLM gateway for the same reason
- PDF ingestion for scientific papers with formulas remains unsolved; best approach is to go to LaTeX source when possible, or screenshot equations for multimodal processing

## People & Tools Mentioned

- Eric Ma -- Research Data Science lead and now Clinical Development Data Science lead at Moderna
- Canvas Chat -- Eric's nonlinear branching conversation tool
- Andrej Karpathy's LLM Council -- inspiration for the committee feature
- PDS CLI -- Eric's CLI for scaffolding Python projects from cookie-cutter templates
- Pixi -- multilingual environment manager (Python, R, TypeScript), used at Moderna
- LiteLLM -- provider-agnostic LLM routing library
- SvelteKit / SvelteFlow -- frontend framework and node-link diagram library
- Open Code -- terminal-based coding assistant Eric uses alongside Cursor
- Minimax m2.7, Opus 4.6, GPT-4o, GLM5 -- models used during the session
- Carol Willing -- CPython core developer, commented on branching Jupyter notebooks and obsidian integration
- Christy de Gova -- Eric's former Moderna colleague, coined "level of formality" concept
- Eleanor and Isaac -- referenced for effective AI-assisted coding course and top-10 questions blog post

## Quotable Moments

- "You can't know your problem deeply until you've built a wrong solution. So just build and if it's wrong you'll feel it." -- Eric Ma [~30:58]
- "I opusmaxed a lot of Canvas Chat and I didn't check the architecture. I didn't look at how code was organized. I was just like build build build until it became really painful to add new features." -- Eric Ma [~39:36]
- "A skilled software developer will know how to do incremental refactors." -- Eric Ma [~42:42]
- "I haven't even opened up a single Svelte file till this point." -- Eric Ma [~01:01:54]
- "If Anthropic had to go under and the Claude models were lost forever, I'd be okay switching to other models because I'm not so used to the temperament or the personality." -- Eric Ma [~45:10]

## Highlights

- [~05:00] Canvas Chat demo: branching conversations, exploring quantum computing paper from multiple angles, merging branches for synthesis -- compelling demonstration of nonlinear thinking with AI
- [~10:00] LLM Council/Committee feature: three personas (quantum physics researcher, self-taught programmer, STEM educator) independently research, cross-review, and synthesize -- practical implementation of Karpathy's LLM Council
- [~16:00] Project scaffolding as "step zero": PDS CLI, cookie-cutter templates, and why opinionated tooling constrains the coding agent's design space
- [~24:00] Planning mode and spec-driven development: linking to current docs, MCP servers, agents.md -- the inputs that guide AI from intent to implementation
- [~30:00] When to use spec-driven development: never for first versions (feel out the problem), essential once problem/solution space is understood
- [~39:00] "Undoing vibecoded slop with AI": Eric's blog post on refactoring Canvas Chat from monolithic 8,500-line app.js to plugin architecture with small modules
- [~54:00] Cypress end-to-end tests as immediate feedback loops: catching dropped curly braces from GLM models and feeding JS console errors directly back to the coding agent
- [~01:00:00] Scientific paper ingestion challenges: PDF formulas remain unsolved; go to LaTeX source when possible, screenshot equations for multimodal processing

## Related Sources

- [[builders_club_brad]] -- Brad's session includes a rich debate on vibe coding, connecting to Eric's "undoing vibecoded slop" discussion and shared interest in coding agent workflows
- [[ws_6_building_ai_agents]] -- Eric's Moderna audit (everything was workflows, not agents) is referenced; the workshop covers the workflow vs. agent distinction Eric navigates
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Eric's audit is again referenced; the LLM Council concept (from Karpathy) that Eric implements as Canvas Chat's "committee" feature is discussed
- [[ws_4_testing_and_observability]] -- Stefan Krawczyk's testing framework and framework selection criteria relate to Eric's spec-driven development and feedback loop patterns
- [[llm_architecture_rasbt]] -- Sebastian Raschka, with whom Eric co-taught at SciPy 2017, provides the architectural context for the models Eric uses across providers
- [[builders_club_natalia_murat]] -- Murat's PDF processing challenges with local models parallel Eric's scientific paper ingestion difficulties
