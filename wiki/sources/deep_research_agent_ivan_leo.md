---
type: guest_talk
title: "Build Your Own Deep Research Agent from Scratch with Gemini"
date: 2026-03-28
speakers: [Ivan Leo (Google DeepMind), Hugo Bowne-Anderson]
topics: [deep research agents, tool calling, sub-agents, agent loops, state management, observability, Gemini API, open telemetry, context management, meta-prompting]
source_file: raw/build_your_own_deep_research_agent_ivan_leo.md
word_count: ~21000
---

## Overview

A hands-on workshop where Ivan Leo (recently joined Google DeepMind, formerly at Manis) and Hugo build a deep research agent from scratch using the Gemini API. This workshop builds on the agent foundations from [[ws_6_building_ai_agents]] and is reflected upon in [[ws_7_workflows_multiagent_and_context_engineering]]. The session progresses through a carefully scaffolded series of steps: starting with a raw API call, adding tool calling, building a tool runtime abstraction, introducing agent state and hooks, constructing the agent loop, and finally adding sub-agents with planning and observability via OpenTelemetry/Logfire.

The deep research agent they build can receive a query, ask clarifying questions, generate a research plan with todos, spawn dynamic sub-agents to research individual questions (using Exa for web search), manage context across those sub-agents, and synthesize a final cited report. Ivan demonstrates the completed agent's trace in Logfire, showing how sub-agents are dispatched, limited in iteration count, and how results flow back to the main orchestrator. The entire system is roughly 1,500 lines of Python.

A significant portion of the session covers when deep research agents are actually needed versus simpler LLM workflows or single-turn agents. Ivan emphasizes starting with the best model to verify task feasibility, then optimizing for cost and latency -- the inverse of classical ML baselines. They discuss meta-prompting (asking models to improve their own tool descriptions and prompts), the importance of caching for cost control, and why coding agents are essentially general-purpose computer-use agents.

## Key Topics

- Building a deep research agent step by step from raw API calls to full sub-agent orchestration
- Tool calling mechanics: why structured JSON output replaced XML tag parsing
- Tool runtime abstraction for cleaner tool definition and agent ergonomics
- Agent state management (todos, iteration counts, phase tracking, user config)
- Sub-agent architecture: dynamic spawning, iteration limits, context compartmentalization
- Planning phase vs. execution phase in research agents
- Caching strategies and prompt cache invalidation awareness
- OpenTelemetry and Logfire for agent observability and trace inspection -- see [[ws_4_testing_and_observability]] for the foundational discussion of OpenTelemetry adoption
- Meta-prompting: using models to improve their own prompts and tool descriptions
- Gemini Interactions API (beta) as the future of agent building on Gemini

## Key Insights

- Start prototyping with the most capable model available (e.g., Gemini 3.1 Pro Preview, Opus 4.6) to verify task feasibility, then optimize downward for cost -- the inverse of classical ML baseline approaches
- "Spend today for the models of tomorrow" -- build for capabilities that will become cheaper, not just what is cheap now
- Every useful general-purpose agent ends up being a coding agent because code execution gives access to the entire computer -- a theme shared with [[builders_club_brad]] and [[ws_6_building_ai_agents]]
- Sub-agents are the key mechanism for managing context in deep research: each sub-agent handles a focused question with limited search iterations, preventing context overload in the main agent -- this is the "isolate" pattern from Lance Martin's context engineering framework in [[ws_7_workflows_multiagent_and_context_engineering]]
- Think about agent ergonomics early because coding agents will eventually be writing your agent code -- clean abstractions matter
- Don't put dynamic state (todos, phase) in the system prompt because it breaks prompt caching; use tool responses to inject state updates instead
- Models have memorized enough of the internet (APIs, URLs) that they can often bypass search for well-known information
- The distinction between "context" (information in the prompt) and "capability" (tools the agent can execute) is fundamental to agent design

## People & Tools Mentioned

- Ivan Leo -- Google DeepMind (previously Manis, worked with Jason Liu on Instructor)
- Kura -- Ivan's open-source tool for clustering and observability of agentic traces
- Manis Agent / Manis Mail -- products Ivan built at Manis
- Exa -- web search API used as the search tool (chosen for provider-agnostic portability)
- Gemini 3 Flash, Gemini 3.1 Pro Preview -- models used in the workshop
- Gemini Interactions API -- new beta API for simplified agent building
- Logfire / OpenTelemetry -- observability stack for viewing agent traces
- Pydantic AI -- mentioned as a good SDK option for one-person shops
- Nicholas Moy (DeepMind/ex-Windsurf) -- built first multi-hop agent at Windsurf
- Sebastian Raschka -- referenced as recent course guest on LLM internals (see [[llm_architecture_rasbt]])
- Anthropic blog post on building effective AI agents -- referenced for workflow vs agent distinction

## Quotable Moments

- "I know a lot of people for example like to throw Opus 4.6 at everything but the simple truth is if you have a very well-defined task... you can actually start experimenting with your evaluation set to start going down to cheaper models" -- Ivan Leo [~08:00]
- "Spend today for the models of tomorrow" -- Ivan Leo [~13:13]
- "Hugo, isn't every agent a coding agent?" -- Ivan Leo (recalled by Hugo) [~40:47]
- "If your agent can write code it then becomes a general purpose computer use agent... it isn't just about building software. It's about using computers." -- Hugo [~42:35]
- "This is like 1,500 lines of code. But this is like a pretty robust repository that has sub agent support, todos that can be tracked, the ability to set the maximum number of iterations... it's actually quite not that much code" -- Ivan Leo [~25:10]

## Highlights

- [~05:00] Architectural overview of the deep research agent: clarifying questions, planner, dynamic sub-agent spawning, and report synthesis -- good conceptual framing before diving into code
- [~07:00] Discussion of when deep research is actually needed vs simpler workflows -- Ivan's framework for matching agent complexity to use case metrics
- [~10:00] Meta-prompting: Ivan describes asking Gemini to improve its own tool descriptions and system prompts, a technique that "wouldn't have been possible a year or two ago"
- [~17:00] Logfire trace walkthrough of a completed deep research run on Apple AirPods -- concrete visualization of sub-agent dispatching, search calls, and report synthesis
- [~28:00] Tool calling explained from first principles: why JSON tool calls replaced XML tag parsing, with clear before/after comparison
- [~40:00] "Isn't every agent a coding agent?" -- provocative discussion on why coding capabilities make agents general-purpose, with references to Pi (4-tool coding agent) and open claw
- [~45:00] State management deep dive: why putting dynamic state in system prompts breaks caching, and the pattern of using tool responses for state injection
- [~48:00] Audience Q&A: "If frontier providers are fast-forwarding agent workflows, why build our own?" -- thoughtful answers about understanding what you're adopting, provider lock-in risks, and SDK breakage

## Related Sources

- [[ws_6_building_ai_agents]] -- The foundational agents workshop covering tool calling mechanics, agentic loops, and agent safety that precedes Ivan's deeper exploration
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Hugo reflects on Ivan's workshop and connects the patterns (meta-prompting, to-do lists, context isolation) to Lance Martin's context engineering framework
- [[demo_day]] -- Both Konrad Dabrowski and Caleb Tutty extended Ivan's deep research agent into their demo day projects (research assistant and 3D printing agent respectively)
- [[search_agents_john_doug]] -- John and Doug's search agents workshop covers agentic search from a different angle (BM25 + LLM wrapper), complementing Ivan's web search approach with Exa
- [[builders_club_brad]] -- Brad references Ivan's upcoming workshop; shares the "coding agents as general-purpose agents" theme
- [[llm_architecture_rasbt]] -- Sebastian Raschka's session on model internals, which Ivan references; provides architectural context for model selection decisions in agent building
