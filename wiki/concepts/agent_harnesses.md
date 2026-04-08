---
type: concept
title: "Agent Harnesses"
related_concepts: [the_api_call_mental_model, context_engineering, agents_vs_workflows, coding_agents_as_general_purpose_agents, framework_selection, llm_architecture_and_inference]
---

## Overview

An agent harness refers to the tooling, context management, and state tracking that surrounds an LLM within an agent system. It encompasses everything outside the model itself: the code that assembles prompts, manages conversation history, defines and executes tools, tracks agent state, handles errors, and processes outputs. Whether "harness" is a useful term of art or marketing jargon is one of the more spirited debates in the course, but the engineering reality it describes is not in dispute -- every agent system has some form of surrounding infrastructure, regardless of what you call it.

The debate crystallizes in [[ws_4_testing_and_observability]], where Stefan Krawczyk dismisses the term as "marketing jargon that people use to sell to execs," while Hugo argues it usefully encapsulates tools, context management, and state tracking in five words. Carol Willing takes the pragmatic middle ground: "good engineering is good engineering, you can name it My Pink Pony or the trapeze of the month." The terminological dispute masks a substantive agreement -- all parties acknowledge that the surrounding infrastructure matters and requires deliberate engineering.

What makes the harness concept particularly dynamic is the observation that models are absorbing harnesses. Through reinforcement learning with verifiable rewards (RLVR), models are being trained on agent traces, learning to perform behaviors that previously required external scaffolding ([[ws_7_workflows_multiagent_and_context_engineering]]). Doug Turnbull's analogy, referenced by Hugo, captures this vividly: models are like Kirby from Nintendo, absorbing the harnesses around them. Labs report ripping out their harnesses with each new model release because the model now handles what the harness used to do ([[ws_4_testing_and_observability]]). Nicholas Moy's advice -- "rip out the harness, let your model be free" -- represents the aggressive end of this trend ([[ai_products_google_ravin_kumar]]).

## The Harness in Practice

Concrete examples make the concept tangible. Armin Ronacher's Pi agent -- the minimal core agent with four tools (read, write, edit, bash), an agents.md file for context, and a hot-reloading mechanism that allows the agent to create new skills at runtime -- provides a minimal harness ([[ws_6_building_ai_agents]]). OpenClaw extends Pi with sessions, cron jobs, channels, sub-agents, and a proactive loop, but Pi itself is the minimal core. Pi's philosophical decision to not include MCP is itself a harness design choice -- rather than providing pre-built tool integrations, the harness enables the agent to extend itself by writing code.

Ivan Leo's deep research agent demonstrates a more sophisticated harness: state management with to-do lists and iteration counts, dynamic sub-agent spawning, context isolation between agents, and OpenTelemetry instrumentation for trace inspection ([[deep_research_agent_ivan_leo]]). Ivan's insight about keeping dynamic state out of system prompts (to preserve prompt caching) is a harness-level optimization -- the harness must manage state injection through tool responses rather than prompt modification.

Stefan Krawczyk's production systems use Hamilton for DAG orchestration (veterinary transcription) and Apache Burr for agent state management (restaurant voice agent) ([[ws_8_finetuning_and_production_ai]]). These frameworks are harnesses in the functional sense -- they manage the flow of information, track state, handle errors, and provide observability -- even if Stefan himself resists the terminology.

## Skills as Progressive Disclosure of Context

The "skills" pattern represents a specific harness capability that bridges into [[context_engineering]]. Stefan describes skills as "smart context engineering" -- progressive disclosure where the agent reads files to add information to its context as needed, rather than loading everything upfront ([[ws_8_finetuning_and_production_ai]]). Mike Powers elaborates: skills are "meta-instructions that the harness uses to establish LLM calls with context," creating a loop where the skill file tells the agent what step to do next and what context to gather.

In the [[ws_7_workflows_multiagent_and_context_engineering]] formulation, agent skills are "informational and procedural memory encoded in a Markdown file with YAML front matter." This encompasses tool calls, scripts, MCP access, and sub-agent invocations. The harness's job is to determine which skills are relevant for a given task and progressively inject their content into the agent's context.

Stefan's observation that "people two years ago doing really fine-tuned context engineering would see this is an obvious pattern" ([[ws_8_finetuning_and_production_ai]]) grounds skills in established engineering practice. The pattern of loading configuration and instructions on demand, rather than all at once, is not new to AI systems. What is new is the LLM's ability to reason about which instructions to load and when.

## Models Absorbing Harnesses

The most forward-looking aspect of the harness concept is its impermanence. Models trained via RLVR on agent traces are learning to perform harness functions internally ([[ws_7_workflows_multiagent_and_context_engineering]]). Behaviors that once required explicit harness code -- planning before acting, breaking tasks into sub-steps, checking work, asking for clarification -- are increasingly native to frontier models. Hugo notes that models have gotten "dramatically better at agentic tasks" due to this training.

Nicholas Moy's advice (as paraphrased by Hugo) to "rip out the harness, let your model be free" ([[ai_products_google_ravin_kumar]]) reflects the practical implication: with each new model release, teams should re-evaluate which harness components are still needed. A harness built for a model that could not plan might be unnecessary for a model that plans natively. The Gemini Interactions API, mentioned in [[ws_7_workflows_multiagent_and_context_engineering]] as a future abstraction, represents providers absorbing harness functionality into their APIs.

This creates a strategic question for builders: how much to invest in harness infrastructure that may become obsolete. The forward-looking 2x2 analysis from [[ws_7_workflows_multiagent_and_context_engineering]] predicts that while all agents will move toward higher context and action complexity, models and APIs will absorb much of that complexity. For most current agent applications (customer service, support bots), sophisticated harnesses may not be needed. For applications at the frontier of complexity, harnesses remain essential but their specific components keep shifting.

## Where Sources Agree

All sources agree on the underlying engineering reality: agent systems require infrastructure surrounding the model for tool management, state tracking, context assembly, and observability. There is also consensus that models are absorbing harness functionality through RLVR training, and that this trend will continue. Sources converge on the practical advice to regularly re-evaluate which harness components remain necessary as models improve.

## Where Sources Disagree or Add Nuance

The terminological debate is genuine. Stefan views "harness" as a rebranding of standard interface design to sell consulting ([[ws_4_testing_and_observability]]). Hugo sees it as a useful shorthand that encompasses tools, context, and state in a way that "wrapper" or "framework" does not. Carol's position -- that good engineering needs good engineering regardless of terminology -- suggests the debate matters less than the practice.

More substantively, there is tension about how quickly harnesses will become unnecessary. Nicholas Moy (as paraphrased by Hugo) represents the aggressive position: rip it out, models are ready ([[ai_products_google_ravin_kumar]]). Ivan Leo and William Horton represent the cautious position: production systems need explicit control over agent behavior, especially in sensitive domains ([[deep_research_agent_ivan_leo]], [[william_horton_maven_clinic]]). The right answer likely depends on the domain and risk tolerance -- a coding assistant can afford more model autonomy than a healthcare agent.

The Crew AI failure documented in [[ws_7_workflows_multiagent_and_context_engineering]] -- median 4-5 out of 9 expected tool calls completed across 100 runs -- illustrates that framework-level harnesses can themselves be unreliable. The abstraction that is supposed to make agent building easier can hide failures. This argues for simpler harnesses where possible and thorough testing of harness behavior, not just model behavior.

## Related Concepts

- [[the_api_call_mental_model]] -- The harness is everything surrounding the API call; Stefan's framework grounds harness functions in specific API components
- [[context_engineering]] -- Skills and progressive context disclosure are harness-managed context engineering patterns
- [[agents_vs_workflows]] -- The harness determines whether a system behaves as a workflow (deterministic paths) or agent (dynamic control)
- [[coding_agents_as_general_purpose_agents]] -- Pi's minimal harness (four tools + hot-reloading) demonstrates how little infrastructure a capable agent needs
- [[framework_selection]] -- Choosing a framework is choosing a harness; the debate about custom wrappers vs. established SDKs is a harness design decision
- [[llm_architecture_and_inference]] -- RLVR training is the mechanism by which models absorb harness behaviors

## Sources

- [[ws_4_testing_and_observability]] -- The agent harness debate between Stefan (marketing jargon), Hugo (useful term), and Carol (good engineering is good engineering), plus the observation about ripping out harnesses with new models
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Models absorbing harnesses via RLVR, the Kirby analogy, skills as procedural memory in Markdown, and the forward-looking prediction about model/API complexity absorption
- [[ws_8_finetuning_and_production_ai]] -- Skills as progressive disclosure of context, MCP and A2A grounded in the API call framework, and Stefan's production harness implementations with Hamilton and Burr
- [[ws_6_building_ai_agents]] -- Pi agent's minimal harness design, agent self-extension through code writing, and the OpenClaw philosophy of agents extending themselves rather than relying on pre-built integrations
- [[ai_products_google_ravin_kumar]] -- Nicholas Moy's "rip out the harness, let your model be free" as the aggressive end of the harness-absorption trend
