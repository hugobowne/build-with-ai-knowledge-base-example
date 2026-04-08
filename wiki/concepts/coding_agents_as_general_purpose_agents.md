---
type: concept
title: "Coding Agents as General-Purpose Computer-Use Agents"
related_concepts: [agents_vs_workflows, agent_harnesses, tool_calling_and_function_calling, vibe_coding_and_ai_assisted_development, context_engineering]
---

## Overview

The reframing of coding agents from tools that write code to general-purpose agents that can do anything a computer can do is one of the course's most provocative claims. Hugo Bowne-Anderson states it directly in [[ws_3_evals_and_feedback_loops]]: "We should stop thinking of them as coding agents. We should start thinking of them as general-purpose computer-using agents that are great at writing code." The insight is structural: a coding agent with a bash tool has access to everything the operating system can do -- file manipulation, network requests, process management, software installation, and arbitrary script execution. Code writing happens to be the task these agents are best at, but it is not the boundary of their capability.

The concept crystallizes around a concrete artifact: a coding agent built in ~131 lines of Python. Hugo demonstrates this agent across multiple sessions -- first as a teaser in [[ws_3_evals_and_feedback_loops]] where it organizes a messy desktop from 32 scattered items into 6 organized folders, then built step-by-step in [[ws_6_building_ai_agents]], and again in [[builders_club_brad]]. The agent has just four tools: read, write, edit, and bash. No system prompt is needed for basic operation because models have gotten good enough at interpreting tool descriptions alone. This minimalism is the point -- with a handful of well-designed tools, the agent can accomplish a vast range of tasks.

Ivan Leo captures the philosophical implication in [[deep_research_agent_ivan_leo]] when Hugo recalls him asking: "Hugo, isn't every agent a coding agent?" The logic is that any useful general-purpose agent eventually needs to execute arbitrary operations, and code execution is the universal interface to computer capabilities. This does not mean every agent should be implemented as a coding agent, but it suggests that the ceiling of what coding agents can do is much higher than "writing software."

The concept also points toward a new relationship between agents and tools. Rather than pre-defining all tools an agent might need, coding agents can write their own tools at runtime and hot-reload them. Hugo demonstrates in [[ws_6_building_ai_agents]] how a coding agent, when asked to write its own bash confirmation guardrail, creates a new file containing the guardrail code, which then functions as a new tool. Armin Ronacher's Pi agent, the minimal agent inside OpenClaw, makes this a design principle: no MCP integration is deliberate, because instead of downloading extensions, you ask the agent to extend itself. Code writing code.

## The Minimal Agent Architecture

The ~131-line agent that threads through the course is pedagogically powerful because it demonstrates that the core agent architecture is simple. Four tools provide the foundation: read (view file contents), write (create or overwrite files), edit (modify existing files with targeted replacements), and bash (execute arbitrary shell commands). The agentic loop is a while loop that sends messages to an LLM, checks for tool calls in the response, executes them, sends results back, and repeats until the model produces a final text response.

This architecture maps directly to Pi, the minimal core agent created by Armin Ronacher, discussed in [[ws_6_building_ai_agents]]. Pi has four core tools and an extensibility mechanism through "skills" -- markdown files that encode procedural and informational knowledge. The hot-reload capability means new skills take effect immediately without restarting the agent. Pi's philosophical decision to exclude MCP is deliberate and consequential: rather than a marketplace of pre-built extensions, the agent writes its own capabilities as needed. OpenClaw extends Pi with sessions, cron jobs, channels, sub-agents, and a proactive loop -- they are related but distinct, with Pi as the minimal core and OpenClaw as the full-featured system built around it.

Hugo recounts in [[builders_club_brad]] how OpenClaw, running on a Mac Mini, autonomously cloned a repository, combined it with an existing script, and delivered video clips with burned-in captions within 10 minutes -- all initiated from a cafe via message. This was not programming assistance; it was a general-purpose agent performing a media production task. Brad Morris describes building his own "Zoo" Discord-based assistant inspired by the same architecture.

## Self-Extension and Tool Creation

The most striking capability of coding agents is self-extension. Hugo demonstrates in [[ws_6_building_ai_agents]] how a coding agent, when it receives a voice message it cannot process, writes its own Whisper transcription tool, saves it to a file, and then uses it to process the message. This hot-reload pattern -- the agent creates a new tool and immediately begins using it -- is fundamentally different from pre-configured tool sets.

In [[builders_club_brad]], Hugo describes the same pattern at work: the agent encounters a task it cannot handle with its current tools, recognizes the gap, writes a Python script to handle it, and continues. This self-extending behavior emerges naturally from the combination of a bash tool and a capable model -- no special architecture is needed.

The implication for [[agent_harnesses]] is significant. If agents can write their own tools, the harness around the agent becomes less about providing capabilities and more about providing constraints -- the guardrails, context management, and state tracking that keep the agent safe and on-task. Hugo's demonstration of the agent writing its own bash confirmation guardrail in [[ws_6_building_ai_agents]] illustrates this: the agent can even help build its own safety infrastructure.

## Models Absorbing Harnesses

A related development discussed in [[ws_7_workflows_multiagent_and_context_engineering]] is that models are absorbing the capabilities that harnesses previously provided. Doug's "Kirby analogy" (cited by Hugo) from Nintendo -- models absorb the harnesses around them through RLVR (reinforcement learning with verifiable rewards) on agent traces. Labs "rip out their harnesses with each new model release" because the model itself has learned the behaviors that the harness previously enforced.

This trend suggests that the minimal coding agent architecture may become even more minimal over time. As models internalize tool use patterns, context management strategies, and planning capabilities, the surrounding code becomes thinner. Nicholas Moy (DeepMind/ex-Windsurf), who built the first multi-hop agent at Windsurf, is cited (as paraphrased by Hugo) as advocating "ripping out harnesses to let models be free." Ivan Leo notes in [[deep_research_agent_ivan_leo]] that his roughly 1,500-line deep research agent is "actually quite not that much code" for the capabilities it provides -- and future models may reduce it further.

## Where Sources Agree

All sources that discuss coding agents agree on the fundamental reframing: these are general-purpose computer-use agents, not just programming assistants. They agree that the bash tool is the key enabling capability -- it provides access to everything the operating system can do. They agree that the core architecture is surprisingly simple (~131 lines of Python). And they agree that self-extension (agents writing their own tools) is a real and significant capability.

## Where Sources Disagree or Add Nuance

The safety implications generate the most productive disagreement. William Horton and Caleb Tutty express concern in [[ws_6_building_ai_agents]] about running agents on real filesystems. Hugo introduces Pi's YOLO mode and Simon Willison's lethal trifecta (private data access + external communication + untrusted content exposure) as the framework for understanding risk. Caleb asks the key open question: "Is there a compromise where guardrails let something have access to tools in maybe an unexpected way?"

Token cost is another area of tension. Pastor Soto raises in [[ws_6_building_ai_agents]] the concern about rising costs with agentic workflows. Hugo, Caleb, and Anonymized Student X discuss the business case challenges, routing to cheaper models for subtasks, and the tension between using the best model for reliability and managing costs. The resolution -- using smart models for planning and cheaper models for execution -- is a practical but not universal answer.

Ivan Leo's perspective from [[deep_research_agent_ivan_leo]] adds nuance about when a coding agent framing is appropriate. While he agrees every agent is essentially a coding agent, his deep research agent is designed around specific tools (web search, sub-agent spawning) rather than general-purpose bash access. The coding agent framing is most powerful when the task is genuinely open-ended; for well-defined tasks, purpose-built tools may be more reliable and efficient.

## Related Concepts

- [[agents_vs_workflows]] -- Coding agents sit at the most autonomous end of the agentic spectrum; most production systems use workflows instead
- [[agent_harnesses]] -- The tooling, context, and state management around agents; models are absorbing harnesses via RLVR
- [[tool_calling_and_function_calling]] -- The mechanism by which agents interact with tools; coding agents use a minimal set of tools (read, write, edit, bash)
- [[vibe_coding_and_ai_assisted_development]] -- Coding agents are the tools powering AI-assisted development; the vibe coding debate concerns how much understanding developers need
- [[context_engineering]] -- Coding agents that write their own tools are a form of self-directed context engineering

## Sources

- [[ws_3_evals_and_feedback_loops]] -- The 131-line coding agent demo as a teaser; reframing coding agents as general-purpose computer-use agents
- [[ws_6_building_ai_agents]] -- Building a coding agent from scratch; Pi agent and OpenClaw; agent self-extension; safety discussion with YOLO mode and lethal trifecta
- [[builders_club_brad]] -- Coding agents as general-purpose tools; OpenClaw usage from a cafe; agent self-creating tools; vibe coding debate
- [[deep_research_agent_ivan_leo]] -- "Isn't every agent a coding agent?"; 1,500-line deep research agent as example of what minimal code can accomplish
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Models absorbing harnesses via RLVR; the Kirby analogy; labs ripping out harnesses with each model release
