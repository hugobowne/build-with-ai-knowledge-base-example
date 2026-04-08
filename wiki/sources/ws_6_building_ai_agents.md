---
type: workshop
title: "Workshop 6: Building AI Agents"
date: 2025-03-25
speakers: [Hugo Bowne-Anderson, Pastor Soto, Anonymized Student Y, Natalia Rodnova, Caleb Tutty, William Horton, Piyush Shah, Franklin, Anonymized Student X]
topics: [AI agents, function calling, tool calling, agentic loop, coding agents, search agents, LLM workflows, Pi agent, OpenClaw, Manus, computer use agents, Pydantic Logfire, EXA, guardrails, security, agent autonomy, agent rollout]
source_file: raw/_cleaned/WS-6.md
word_count: ~17898
---

## Overview

Workshop 6 is the definitive agents session of the course, taking participants from the theoretical definitions of agents through to building functional coding agents and search agents from scratch. This workshop builds on the retrieval and search agent foundations from [[ws_5_context_engineering_and_information_retrieval]] and leads into [[ws_7_workflows_multiagent_and_context_engineering]]. Hugo grounds the discussion with three definitions of "agent" (LLM calling tools in a loop, a microservice, or something that replaces a human) and establishes the key distinction: workflows are systems with predefined code paths, while agents are systems where LLMs dynamically direct their own processes and tool usage.

The session opens with a compelling Manus demonstration -- Hugo shows how he used Manus's email interface to get comprehensive podcast research done in 10 minutes (a task that normally takes 3-4 hours), including the agent navigating websites, downloading a book from Dropbox, and synthesizing findings. This motivates the practical value of agents while Hugo maintains that most production applications should use workflows, not agents.

The heart of the workshop is hands-on building. Hugo walks through function calling mechanics with both OpenAI and Gemini (demonstrating that Gemini 2.5 Flash fails where GPT-5 succeeds on the same tool description), then builds a search agent step-by-step: (1) ping an LLM, (2) add an EXA search tool, (3) build the agentic loop, (4) add a conversational loop. Then he builds a coding agent with read, write, edit, and bash tools -- demonstrating it can organize a desktop, write and execute Python scripts, and even write its own guardrails. All of this is instrumented with Pydantic Logfire.

A key thread throughout is the discussion of agent safety and autonomy. Hugo introduces his 2x2 framework of agency vs. supervision, notes Simon Willison's lethal trifecta (private data access + external communication + untrusted content exposure), and has the agent write its own bash confirmation guardrail. The session also covers Pi (the minimal agent inside OpenClaw), Anthropic's blog post on building effective agents, and the emerging pattern of coding agents as general-purpose computer use agents.

## Key Topics

- Definition of agents: LLM calling tools in a loop vs. workflows (predefined code paths)
- Function calling mechanics with OpenAI and Gemini APIs
- Building a search agent from scratch (LLM + EXA tool + agentic loop + conversational loop)
- Building a coding agent with read, write, edit, and bash tools
- Pi: the minimal agent inside OpenClaw (4 tools, agents.md, extensible with skills)
- Manus demonstration: email-based research agent
- Agent safety: YOLO mode, guardrails, Simon Willison's lethal trifecta
- Agent autonomy spectrum: high agency + low supervision = danger zone
- Pydantic Logfire instrumentation for agent observability
- When to use agents vs. workflows vs. augmented LLMs
- Claude's computer use, Perplexity computer use, OpenClaw
- Token cost concerns with agentic workflows
- Model capability improvements enabling agent development

## Key Insights

- Most production AI applications don't need agents -- workflows suffice. Even Moderna's audit found everything was a workflow (see [[thinking_tools_eric_ma]] for Eric Ma's perspective from Moderna). Non-technical stakeholders often call workflows "agents" because they "do stuff."
- Coding agents are really general-purpose computer use agents that happen to be great at writing code. This reframing (prompted by Claude's computer use release, OpenClaw, Manus, Perplexity) is fundamental to understanding the space.
- Function calling is "gnarly" -- the LLM doesn't execute tools, it returns a function name and arguments as text. The developer must parse, execute, and send results back. SDKs abstract this but reduce visibility.
- Gemini 2.5 Flash fails at function calling where GPT-5 (and even GPT-4) succeeds with the same tool description. Tool descriptions require iteration per provider. Gemini 3 Flash Preview works where 2.5 fails.
- A general-purpose coding agent can be built in ~125 lines of Python (without the conversational loop) or ~185 lines with it. No system prompt is needed for basic operation because models have gotten that good.
- Models are getting so good at agentic tasks because of reinforcement learning with verifiable rewards (RLVR) on agent traces, causing labs to "rip out their harnesses" with each new model release. [[llm_architecture_rasbt]] covers RLVR and inference scaling from the architecture perspective.
- The Pi agent's philosophical decision to not include MCP is deliberate: instead of downloading extensions, you ask the agent to extend itself. Code writing code.
- Agent costs are a real concern. Claude Code's $200/month tier, OpenClaw costs -- but routing to smaller models for subtasks will drive efficiency.

## People & Tools Mentioned

- Samuel Colvin (Pydantic) -- three definitions of agents joke; observability will just be "observability" once things stabilize
- Armin Ronacher (Flask creator) -- blog post on agent design; built Pi, the minimal agent inside OpenClaw
- Doug Turnbull and John Berryman -- upcoming search agents workshop (see [[search_agents_john_doug]])
- Ivan Leo -- upcoming deep research agent workshop (see [[deep_research_agent_ivan_leo]]); formerly at Manus (acquired by Meta), now at DeepMind
- Simon Willison -- lethal trifecta for agent security
- Andrej Karpathy -- coding agents as computer use agents; No Priors podcast on OpenClaw
- Boris Cherney (Claude Code) -- "agentic search works better than RAG and a local vector database"
- Eric Ma (Moderna) -- audit found no agents in production, only workflows; teaches agentic data science workshop (see [[thinking_tools_eric_ma]])
- Manus -- email-based research agent; acquired by Meta
- OpenClaw/Pi -- minimal coding agent with 4 tools, hot reloading, proactive loop
- EXA -- web search API
- Pydantic Logfire -- $500 credits for students; instrumentation shown live
- Anthropic -- "Building Effective AI Agents" blog post

## Quotable Moments

- "There are three definitions. The LLM or AI person's definition: an LLM calling tools in a loop. Infra person says it's a microservice. Business person says it's something that can replace a human and take their salary away." -- Hugo, citing Samuel Colvin [~20:00]
- "Gemini 2.5 Flash is fast but relatively dumb." -- William Horton [~40:00]
- "Agents, wait, it's just a for loop? Always has been." -- Hugging Face meme, cited by Hugo [~25:00]
- "If you have a handful of tools, they can do a huge number of things." -- Hugo on why less MCP is often more [~50:00]
- "The most organized desktop is actually an empty desktop." -- William Horton, on the agent that could delete everything [~100:00]

## Highlights

- [~15:00] Live Manus demonstration. Hugo shows the full trace of Manus doing podcast research via email: navigating Google Docs, reading a Luma page, downloading a book from Dropbox (clicking past the dark pattern), running terminal commands, and synthesizing research -- all in 10 minutes. Powerful motivating example for agent capabilities.

- [~30:00] Function calling deep dive comparing OpenAI and Gemini. The same tool description works on GPT-5 but fails on Gemini 2.5 Flash, requiring prompt iteration. Hugo highlights the surprising intelligence of GPT-5 converting "Sydney" to latitude/longitude coordinates from its weights alone.

- [~50:00] Discussion of Pi's design philosophy. No MCP integration is deliberate -- the agent should extend itself by writing code. Hot reloading enables agents to create and immediately use new skills. This represents a fundamentally different approach to agent extensibility.

- [~80:00] Live coding of a general-purpose coding agent in ~125 lines. Hugo demonstrates it organizing a fake desktop, writing and executing Python scripts, and then -- most dramatically -- asks the agent to write its own bash confirmation guardrail in a new file, which he then runs to show the guardrail working.

- [~100:00] Critical safety discussion. William and Caleb express concern about running the agent on a real filesystem. Hugo introduces Pi's YOLO mode, Simon Willison's lethal trifecta, and the tension between open exploration and locked-down production systems. Caleb asks the key open question: "Is there a compromise where guardrails let something have access to tools in maybe an unexpected way?"

- [~110:00] Discussion about agency, autonomy, and human-in-the-loop as dimensions for agent design. Hugo explains why he stopped telling people to stop building agents: it was not AI autonomy that concerned him, but AI autonomy without proper human supervision.

- [~125:00] Candid discussion about agent costs. Pastor asks about rising token costs with agentic workflows. Hugo, Caleb, and Anonymized Student X discuss the business case challenges, routing to cheaper models, and the tension between best-model demands and cost optimization.

## Related Sources

- [[deep_research_agent_ivan_leo]] -- Ivan Leo's hands-on workshop building a deep research agent from scratch, extending the agent foundations taught here with sub-agents, planning, and observability
- [[ws_7_workflows_multiagent_and_context_engineering]] -- The next workshop, covering workflows vs. agents, multi-agent systems, and context engineering patterns that build on the agent foundations here
- [[builders_club_brad]] -- Brad's session demos the same 131-line coding agent and discusses coding agents as general-purpose tools, with rich vibe coding debate
- [[search_agents_john_doug]] -- John and Doug's workshop on wrapping BM25 with agentic search, complementing the EXA-based search agent built here
- [[katherine_jarmul_privacy]] -- Katharine Jarmul's discussion of agent security complements the safety discussion here (Simon Willison's lethal trifecta, YOLO mode, guardrails)
- [[william_horton_maven_clinic]] -- William Horton's Maven Assistant is a production multi-agent system, demonstrating real-world application of the agent patterns taught here
