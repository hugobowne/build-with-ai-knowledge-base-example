---
type: concept
title: "Multi-Agent Architecture"
related_concepts: [agents_vs_workflows, context_engineering, tool_calling_and_function_calling, production_ai_patterns, agent_harnesses, model_selection_and_tradeoffs]
---

## Overview

Multi-agent architecture refers to the design of AI systems composed of multiple specialized agents that coordinate through a lead or orchestrator agent. Rather than building a single monolithic agent that handles every task, multi-agent systems decompose problems across agents with distinct responsibilities, each with its own prompts, tools, and context. This pattern appears across domains from healthcare to research, but it remains one of the most genuinely difficult engineering challenges in AI application development.

The fundamental architecture follows the orchestrator-worker pattern described in [[ws_7_workflows_multiagent_and_context_engineering]]: a lead agent receives user input, reasons about what is needed, and delegates to specialized sub-agents. William Horton's Maven Assistant at Maven Clinic exemplifies this in production -- a lead agent routes to sub-agents for appointments, provider search, health questions, and "how does Maven work" queries backed by Zendesk RAG ([[william_horton_maven_clinic]]). Ivan Leo's deep research agent demonstrates the same pattern for knowledge work, with a main orchestrator that spawns sub-agents dynamically to research individual questions, each with iteration limits and compartmentalized context ([[deep_research_agent_ivan_leo]]).

The design space for multi-agent systems is vast and underspecified. Key decisions include whether sub-agents respond directly to users or pass results through the lead agent, whether sub-agents can invoke other sub-agents, whether execution is parallel or sequential, and how much context each agent receives. William Horton describes wrestling with these decisions for six months, calling multi-agent architecture "the hardest problem" he has faced ([[builders_club_william_horton]]). Stefan Krawczyk's veterinary transcription system illustrates the extreme end of the spectrum -- a DAG of 60+ LLM calls orchestrated through Hamilton, where debugging which context fed into which call becomes a major engineering challenge ([[ws_8_finetuning_and_production_ai]]).

## Delegation Patterns and Organizational Mapping

A central design question in multi-agent systems is how delegation flows. In the Maven Clinic architecture, the lead agent decides which sub-agent to invoke and presents results to the user. This raises Conway's Law for agents -- the observation that agent architecture tends to mirror organizational structure ([[builders_club_william_horton]]). If different teams own different capabilities (appointments, benefits, clinical content), the agent decomposition often follows those boundaries.

Ivan Leo's deep research agent takes a different approach to delegation: the orchestrator creates a plan with a to-do list, then dynamically spawns sub-agents to handle individual research questions ([[deep_research_agent_ivan_leo]]). Each sub-agent is limited in iterations and operates with isolated context, preventing the main agent's context window from being overwhelmed. This dynamic spawning pattern contrasts with Maven's more fixed routing structure and reflects the different demands of open-ended research versus structured service delivery.

The [[ws_7_workflows_multiagent_and_context_engineering]] session formalizes these as variations on Anthropic's orchestrator-worker pattern, alongside parallelization (running multiple agents simultaneously) and prompt chaining (one agent's output feeding the next). Carol Willing's practice of having three different LLMs audit code files in parallel demonstrates parallelization for code review, connecting to Andrej Karpathy's LLM Council concept.

## Context Isolation and State Management

One of the most critical challenges in multi-agent systems is managing context across agents. The "isolate" pattern from Lance Martin's context engineering framework ([[ws_7_workflows_multiagent_and_context_engineering]]) addresses this directly: each sub-agent operates with its own context window, receiving only the information relevant to its task rather than the full conversation history. This prevents context pollution and keeps individual agents focused.

Ivan Leo emphasizes the distinction between context (information in the prompt) and capability (tools the agent can execute) as fundamental to agent design ([[deep_research_agent_ivan_leo]]). He also warns against putting dynamic state -- to-do lists, phase tracking -- in system prompts, because doing so breaks prompt caching. Instead, state should be injected through tool responses, keeping the system prompt stable for caching while allowing state to evolve across turns.

Stefan Krawczyk's veterinary transcription DAG illustrates how context chains become debugging nightmares at scale ([[ws_8_finetuning_and_production_ai]]). When one of 60+ LLM calls produces a bad extraction, tracing which upstream context caused the error requires graph-level visibility that most tools do not provide. Frameworks like Hamilton make dependency chains visible, which becomes essential as systems grow.

## Latency, Cost, and Production Realities

The practical constraints on multi-agent systems center on latency more than cost. William Horton notes that each agent delegation adds another LLM call and at least another second of latency ([[builders_club_william_horton]]). In Maven's healthcare context, where users expect responsive chat, this means every delegation decision has a direct impact on user experience. The strategy of using smarter, more expensive models for the lead agent (which makes fewer but more consequential routing decisions) and cheaper, faster models for sub-agents reflects this constraint ([[william_horton_maven_clinic]]).

Stefan's production case studies reinforce that parallelization is essential for managing latency in complex workflows -- running independent extraction steps simultaneously rather than sequentially ([[ws_8_finetuning_and_production_ai]]). Provider fallbacks also matter: when a primary model provider goes down, the system needs to route to alternatives without breaking the multi-agent coordination.

## Where Sources Agree

All sources agree that multi-agent architecture is genuinely difficult and requires careful design. There is consensus that the orchestrator-worker pattern is the dominant structure, that context isolation between agents is essential, and that latency is a more immediate concern than cost in production systems. Sources also converge on the importance of limiting scope -- both William Horton and Ivan Leo emphasize iteration limits and deliberate constraints on what each agent can do.

## Where Sources Disagree or Add Nuance

The sources diverge on how dynamic multi-agent systems should be. Ivan Leo's approach favors dynamic sub-agent spawning where the number and type of agents are determined at runtime ([[deep_research_agent_ivan_leo]]), while William Horton's Maven system uses a more fixed routing structure with predetermined sub-agents ([[william_horton_maven_clinic]]). This likely reflects their different domains -- open-ended research benefits from flexibility, while healthcare requires predictability.

There is also tension around the question of whether multi-agent is even the right framing. Hugo's earlier audit of Eric Ma's work at Moderna found that everything in production was workflows, not agents ([[ws_7_workflows_multiagent_and_context_engineering]]). Stefan Krawczyk's veterinary transcription system with 60+ LLM calls is technically a workflow DAG, not a multi-agent system in the dynamic sense, yet faces many of the same coordination challenges. The boundary between a complex workflow and a multi-agent system remains blurry, and whether "multi-agent" as a term clarifies or obscures the engineering decisions is an open question.

## Related Concepts

- [[agents_vs_workflows]] -- The foundational distinction; multi-agent architecture sits at the agent end of the spectrum but often contains workflow components
- [[context_engineering]] -- Context isolation is one of the four core patterns and is essential for multi-agent systems
- [[model_selection_and_tradeoffs]] -- The strategy of smarter lead agents with cheaper sub-agents is a key cost/latency optimization
- [[tool_calling_and_function_calling]] -- The mechanism by which agents delegate to sub-agents and interact with external systems
- [[production_ai_patterns]] -- Multi-agent systems face amplified versions of production challenges: latency, fallbacks, observability
- [[observability_and_tracing]] -- Debugging multi-agent systems requires trace-level visibility into each agent's context and decisions

## Sources

- [[builders_club_william_horton]] -- William Horton's candid account of multi-agent architecture as the hardest problem at Maven Clinic, including Conway's Law for agents and latency concerns
- [[william_horton_maven_clinic]] -- The production multi-agent system in detail: lead agent routing to sub-agents for appointments, health, provider search, with model selection trade-offs
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Anthropic's taxonomy, the orchestrator-worker pattern, parallelization, and context isolation as a formal strategy
- [[deep_research_agent_ivan_leo]] -- Dynamic sub-agent spawning with iteration limits, context compartmentalization, and the context vs. capability distinction
- [[ws_8_finetuning_and_production_ai]] -- Stefan Krawczyk's veterinary transcription DAG (60+ LLM calls) as a production case study in complex multi-step AI systems
