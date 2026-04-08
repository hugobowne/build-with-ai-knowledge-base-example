---
type: concept
title: "Agents vs. Workflows"
related_concepts: [coding_agents_as_general_purpose_agents, multi_agent_architecture, context_engineering, human_in_the_loop, the_api_call_mental_model, proof_of_concept_purgatory]
---

## Overview

The distinction between agents and workflows is one of the most consequential design decisions in AI application development. Workflows are systems with predefined code paths where the developer controls the sequence of operations -- the LLM is called at specific points with specific inputs, and the flow between calls is determined by code, not by the model. Agents are systems where the LLM dynamically directs its own processes and tool usage, deciding at each step what to do next based on the results of previous steps. Hugo Bowne-Anderson introduces the distinction in [[ws_6_building_ai_agents]] with three definitions of "agent": the AI person's definition (an LLM calling tools in a loop), the infrastructure person's definition (a microservice), and the business person's definition (something that can replace a human).

The course's central thesis on this topic is blunt: most production AI applications are workflows, not agents, even when stakeholders call them "agents." Hugo cites Eric Ma's audit at Moderna, detailed in [[ws_7_workflows_multiagent_and_context_engineering]], which found that everything in production was a workflow. Hugo wrote an essay titled "Stop Building AI Agents" that hit number one on Hacker News. Yet his position evolved -- the concern was never about AI autonomy per se, but about AI autonomy without proper human supervision. Agents can shine inside testable, observable systems, and models have gotten dramatically better at agentic tasks due to reinforcement learning with verifiable rewards (RLVR).

The distinction matters practically because agents introduce complexity, latency, cost, and unpredictability that workflows avoid. Each agent delegation adds another LLM call and at least another second of latency, as William Horton notes from experience at Maven Clinic in [[builders_club_william_horton]]. Crew AI, tested in [[ws_7_workflows_multiagent_and_context_engineering]], failed to execute the expected number of tool calls -- median 4-5 out of 9 requested across 100 runs -- illustrating how agentic abstractions can hide failures. Yet for tasks requiring dynamic adaptation (deep research, multi-step reasoning, open-ended exploration), agents are necessary and increasingly capable.

## The Agentic Spectrum

Rather than a binary choice, Anthropic's taxonomy (presented in [[ws_7_workflows_multiagent_and_context_engineering]]) describes a spectrum with four levels. Plain LLMs handle single-turn text generation. Augmented LLMs add tools and retrieval to single interactions. Workflows chain multiple LLM calls in predefined patterns. And agents give the LLM control over multi-step processes with dynamic tool selection.

Hugo provides concrete rules of thumb: use an LLM for text generation, an augmented LLM or workflow for retrieval, tools, or multi-step predefined tasks, and an agent only when the LLM needs to control multi-step tasks and adapt dynamically. The boundary between workflow and agent can be blurry -- you can embed agentic components within workflows (an email generator with an inner evaluation loop within a deterministic pipeline) or constrain agents with workflow-like guardrails.

William Horton's Maven Assistant, described in [[william_horton_maven_clinic]], occupies an interesting middle ground. A lead agent routes to specialized sub-agents for appointments, provider search, health questions, and FAQ queries. The routing decision is agentic (the model decides which sub-agent to call), but each sub-agent follows relatively constrained paths. This architecture -- agentic orchestration with workflow-like sub-components -- may be the most common production pattern.

## Workflow Building Blocks

The course covers Anthropic's workflow patterns in detail through [[ws_7_workflows_multiagent_and_context_engineering]]: prompt chaining (output of one call feeds the next), routing (classifying input to select a processing path), parallelization (multiple calls executing simultaneously), orchestrator-worker (a coordinator dispatching tasks to workers), and evaluator-optimizer (generating then evaluating and refining output in a loop).

Stefan Krawczyk's veterinary transcription system from [[ws_8_finetuning_and_production_ai]] is the course's most complex workflow example: 60+ LLM calls organized in a directed acyclic graph (DAG), running on AWS Lambda with Hamilton for graph orchestration. This system grew organically from a simple starting point, illustrating both the power and the debugging challenges of complex workflows. Stefan emphasizes that graph frameworks like Hamilton make dependency chains visible, which is essential when you need to understand what context fed into which call when a particular extraction goes wrong.

The gate pattern deserves special mention: structured output combined with if-else logic creates decision points where code (not the model) determines the next step based on model output. This is the fundamental mechanism that keeps workflows deterministic while leveraging LLM intelligence at each step. As Stefan maps it in [[ws_8_finetuning_and_production_ai]], structured output is an API call component, and the if-else branching is just code -- demystifying what might sound complex.

## Why Most Production Systems Are Workflows

Several forces push production systems toward workflows. Predictability: workflows follow known paths, making them testable and debuggable. Latency: each agentic decision adds a round trip, while workflows can be optimized and parallelized along known paths. Cost: workflow calls are bounded, while agent token usage is open-ended. Reliability: Crew AI's median 4-5 out of 9 requested tool calls completed across 100 runs (as documented in [[ws_7_workflows_multiagent_and_context_engineering]]) illustrates that agentic systems can fail silently.

William Horton offers a practical heuristic in [[builders_club_william_horton]]: when someone asks for an "agentic solution," get them to describe desired inputs and outputs without using hype terms like "agentic." Then figure out the technical approach. Text classification is "more or less a solved problem" that does not need agents. Multi-agent architectures remain genuinely hard. The gap between what stakeholders call "agents" and what builders should actually build is a recurring source of confusion.

Hugo's "Stop Building AI Agents" essay, discussed in [[ws_7_workflows_multiagent_and_context_engineering]], captures the nuance: the issue was not agents themselves but agents deployed without evaluation, observability, and human oversight. The essay's thesis evolved as models improved -- Hugo acknowledged the hypocrisy of using agents daily while telling others to stop building them. The reconciliation: agents inside testable, observable systems with appropriate human-in-the-loop design.

## Where Sources Agree

All sources agree that the default should be the simplest sufficient approach -- do not use an agent when a workflow suffices. They agree that "agent" is used loosely by non-technical stakeholders and that this creates confusion. They agree that workflows dominate production today. And they agree that models are getting better at agentic tasks (due to RLVR), shifting the cost-benefit calculation over time.

## Where Sources Disagree or Add Nuance

The Moderna audit finding -- "everything was a workflow" -- has become a repeated reference point, but Hugo notes in [[ws_7_workflows_multiagent_and_context_engineering]] that this has since changed at Moderna, suggesting the field is evolving rapidly. The question of when agents become the right default rather than the exception remains open.

There is also a terminology tension. Ilona raises in [[ws_7_workflows_multiagent_and_context_engineering]] that frameworks like Crew AI market workflow products as "agents," and Hugo and Carol agree this is common and pragmatically acceptable -- the term means different things to builders versus stakeholders. Stefan Krawczyk takes a harder line in [[ws_4_testing_and_observability]], calling "agent" a "marketing term" alongside "agent harness." Carol Willing's pragmatic take: "Good engineering is good engineering, you can name it My Pink Pony or the trapeze of the month."

The forward-looking prediction from [[ws_7_workflows_multiagent_and_context_engineering]] is that all agents will move toward higher context and action complexity, but that models and APIs will absorb that complexity. If true, the distinction between agents and workflows may eventually dissolve as the infrastructure handles what developers currently manage manually.

## Related Concepts

- [[coding_agents_as_general_purpose_agents]] -- Coding agents represent the most capable end of the agentic spectrum, where bash access makes any computer task possible
- [[multi_agent_architecture]] -- The design patterns for systems with multiple specialized agents coordinating through orchestrators
- [[context_engineering]] -- Context management differs fundamentally between workflows (predictable needs) and agents (dynamic assembly)
- [[human_in_the_loop]] -- The supervision dimension that determines whether agent autonomy is safe; the 2x2 of agency vs. supervision
- [[the_api_call_mental_model]] -- Stefan's framework demystifies both agents and workflows as patterns of API calls with different control flow
- [[proof_of_concept_purgatory]] -- Agentic demos are particularly susceptible to purgatory; the wow moment comes first, then the difficulty of productionizing

## Sources

- [[ws_6_building_ai_agents]] -- Three definitions of agent; when agents vs. workflows; function calling mechanics; agency vs. supervision 2x2
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Anthropic's taxonomy; agentic spectrum; "Stop Building AI Agents" evolution; workflow patterns; Crew AI failure modes; forward-looking predictions
- [[william_horton_maven_clinic]] -- Multi-agent architecture in production healthcare, occupying the middle ground between pure workflow and pure agent
- [[ws_8_finetuning_and_production_ai]] -- 60+ LLM call veterinary transcription DAG; restaurant voice agent; grounding agents/workflows in the API call framework
- [[builders_club_william_horton]] -- When agentic solutions make sense; describe inputs/outputs without hype terms; latency as the real constraint
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Eric Ma's Moderna audit (Hugo citing Eric Ma's work in WS-7): everything was workflows, not agents
