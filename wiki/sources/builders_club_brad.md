---
type: builders_club
title: "Brad Morris Builders Club: Modal Deployment, Discord Bots, and Coding Agents as General-Purpose Tools"
date: 2026-03-26
speakers: [Brad W Morris, Hugo Bowne-Anderson, Carol Willing, Anonymized Student X, Anonymized Student Y, Adrian Turcu]
topics: [Modal, Discord bots, GPU deployment, vibe coding, coding agents, OpenClaw, computer use agents, Cursor, Replicate, Hugging Face]
source_file: raw/_cleaned/Builders_Club_Brad.md
word_count: ~12800
---

## Overview

Brad Morris, a returning builder in residence, leads a hands-on workshop on deploying a music-generating Discord bot ("Hugo BoomBot") using Modal's cloud infrastructure. The session opens with a rich discussion about vibe coding -- Brad references a Jeremy Howard podcast arguing that pure vibe coding without understanding is dangerous, while Carol Willing and Hugo push back with nuance about abstraction layers and the importance of critical evaluation of AI-generated code. The group discusses how LLMs replicate dark patterns in generated code (citing a paper on AI-generated e-commerce components).

The core workshop walks through cloning a Modal example repo (the "Boom Bot"), understanding its two key files (bot.py for the Discord gateway via FastAPI, and main.py for running a Facebook audio generation model on an A10G GPU), authenticating with Modal, and deploying the app. Modal was introduced as a deployment platform in [[ws_1_foundations]] by Ben Shababo. Brad explains that Modal abstracts away containerization (similar to Docker) and only charges for GPU time when the bot is actively processing. He demonstrates the full workflow from `pip install modal` through `modal serve` and ultimately `modal deploy`, and deploys Hugo BoomBot live for the cohort to generate music from text prompts in Discord.

The session then pivots to two major tangents. First, Hugo shares his experience with OpenClaw -- a personal AI assistant running on a Mac Mini that autonomously cloned a repo, combined it with an existing script, and delivered video clips with burned-in captions within 10 minutes, all messaged from a cafe. Brad shares his own "Zoo" Discord-based assistant inspired by OpenClaw. Second, Hugo demonstrates a minimal coding agent written in 131 lines of Python that can organize a messy desktop folder (the same agent demoed in [[ws_3_evals_and_feedback_loops]] and built step-by-step in [[ws_6_building_ai_agents]]), arguing that coding agents should be reconceptualized as general-purpose computer-using agents -- anything a computer can do via bash, an agent can do. He shows how such agents can write and hot-reload their own tools at runtime.

## Key Topics

- Modal as cloud deployment platform for Python apps with GPU access
- Building and deploying Discord bots with Modal
- The vibe coding debate (Jeremy Howard, Karpathy perspectives)
- LLMs replicating dark patterns in generated code
- OpenClaw and personal AI assistants
- Coding agents as general-purpose computer-use agents
- Agent tool self-creation and hot-reloading
- Developer tooling landscape (Cursor, AMP, Zed, Claude Code)

## Key Insights

- Modal extracts away infrastructure complexity so builders can focus on code; it only charges for GPU time when actively processing
- The vibe coding debate has real nuance: abstraction layers are not new (Python over machine code), but understanding what you build remains critical
- OpenClaw-style personal assistants represent a qualitatively new type of utility -- Hugo describes it as the first time outside AI-assisted coding that he found extreme new utility
- Coding agents with bash tools should be thought of as general-purpose computer-using agents, not just coding tools -- a theme echoed in [[deep_research_agent_ivan_leo]] ("isn't every agent a coding agent?") and [[ws_6_building_ai_agents]]
- Agents that can write their own tools and hot-reload them represent a significant emerging capability
- Carol Willing argues that people with ideas and domain knowledge will be more valuable than those who only know how to code, given the new paradigm of natural language interfaces

## People & Tools Mentioned

- Jeremy Howard -- podcast on vibe coding dangers and the importance of fundamentals
- Andrej Karpathy -- noted the term "vibe coding" is used pejoratively
- Ivan Leo -- workshop on deep research agents and agent-building with Pydantic (see [[deep_research_agent_ivan_leo]])
- Ben Shibabo -- real-time voice-to-speech Modal project
- Armin Ronacher -- Flask creator, wrote about the Pi agent philosophy of letting agents write their own tools
- Eric Maher -- heavy Cursor user, PersonalOS with Obsidian and Claude Code (see also [[thinking_tools_eric_ma]] for Eric Ma's tools-for-thinking session)
- Modal, Cursor, AMP, Zed, Replicate, Hugging Face, FastAPI, OpenClaw, Discord API

## Quotable Moments

- "Pure vibe coding makes me sick. It makes me ill, because he's basically saying, like, your intelligence is atrophying if you're completely not understanding the modularity of what you're doing." -- Brad W Morris (paraphrasing Jeremy Howard) [~10:00]
- "I think we all should start thinking of coding agents more as general-purpose computer-using agents. Anything that a computer can do, whether it's writing code or otherwise, an agent can do." -- Hugo Bowne-Anderson [~60:00]
- "I fundamentally believe that people with ideas like you, Brad, are going to be far more valuable than people who understand how to code." -- Carol Willing [~70:00]
- "I still have to sit down, carefully scope the whole thing end-to-end... the idea and what you see on Twitter doesn't really line up." -- Brad W Morris [~70:00]

## Highlights

- [~05:00] Rich debate on vibe coding featuring Jeremy Howard's podcast critique, Carol's JetBrains talk on problem-solving with AI tools, and Hugo's point about abstraction layers being fundamental to computing history
- [~10:00] Discussion of LLMs replicating dark patterns in generated code, with Hugo citing an arXiv paper showing 30% of AI-generated e-commerce components contain dark patterns
- [~15:00] Brad explains Modal's value proposition in a way accessible to non-technical builders, including the Hugging Face weights download workflow
- [~40:00] Hugo's detailed account of using OpenClaw from a cafe to build a video clipping pipeline in under 10 minutes -- a concrete, compelling example of personal AI assistant utility
- [~60:00] Live demo of a 131-line Python coding agent that organizes a messy desktop, making the case for agents as general-purpose computer-use tools
- [~65:00] Hugo describes how an agent wrote its own Whisper tool when it received a voice message it could not process, paralleling the OpenClaw origin story
- [~70:00] Carol Willing's perspective on literate problem-solving as the next evolution from literate programming and literate computing, and the value of domain expertise over pure coding skill

## Related Sources

- [[deep_research_agent_ivan_leo]] -- Ivan Leo's workshop on building a deep research agent from scratch, referenced during this session; shares the "coding agents as general-purpose agents" theme
- [[ws_6_building_ai_agents]] -- The agents workshop where Hugo builds the same 131-line coding agent step-by-step and covers function calling, agent safety, and the Pi agent
- [[ws_1_foundations]] -- Ben Shababo's Modal guest talk provides the foundational context for Brad's Modal deployment workshop
- [[thinking_tools_eric_ma]] -- Eric Ma's session on AI-assisted development workflows, complementing Brad's discussion of vibe coding and developer tooling
- [[demo_day]] -- Several demo day projects (Caleb's 3D printing agent, Konrad's research assistant) used Modal for deployment, building on Brad's workshop
