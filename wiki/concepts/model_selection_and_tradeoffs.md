---
type: concept
title: "Model Selection and Trade-offs"
related_concepts: [the_api_call_mental_model, fine_tuning_and_distillation, agents_vs_workflows, framework_selection, production_ai_patterns, llm_architecture_and_inference]
---

## Overview

Choosing which LLM to use for a given task is one of the most consequential decisions in AI engineering, and the course reveals that model selection is not a one-time choice but an ongoing optimization problem across multiple dimensions: capability, latency, cost, safety behavior, and availability. The sources converge on a practical framework: a Pareto frontier from tiny models (270M parameters on a Raspberry Pi) through Flash-tier models (the enterprise workhorse) to frontier reasoning models (the most capable but too slow and expensive for most production use). The strategic pattern that emerges is to use smart models for planning and cheaper models for execution.

The course provides rich production evidence for how model selection plays out in practice. William Horton describes in [[william_horton_maven_clinic]] how Maven Clinic uses Gemini 2.5 Flash for latency-sensitive interactions despite its being worse at tool calling and empathy than newer models, GPT-5.4 Mini for health questions where clinical accuracy matters more than speed, and notes that GPT-5.4-XI thinking would ace all evaluations but is too slow for production. This three-way trade-off -- latency vs. capability vs. cost -- is the central tension that every production system navigates.

Ravin Kumar in [[ai_products_google_ravin_kumar]] describes the full Gemma model family from 270M to 27B and reveals that the tiny 270M model had more demand than expected because people valued putting it in places where large models cannot go: phones, Raspberry Pi devices, persistent local processes. His Flash vs. Pro strategy discussion articulates the Pareto frontier explicitly, from Waymo's millisecond decisions to deep research that can run for hours. Sebastian Raschka in [[llm_architecture_rasbt]] explains the architectural developments -- inference scaling, reasoning traces, adjustable reasoning effort -- that create the range of model behaviors builders must navigate. Ivan Leo in [[deep_research_agent_ivan_leo]] captures the temporal dimension: "spend today for the models of tomorrow" -- build for capabilities that will become cheaper rather than just what is cheap now.

## The Pareto Frontier

The model landscape can be understood as a frontier trading off capability against cost and latency. At one extreme sit tiny models: Ravin Kumar describes in [[ai_products_google_ravin_kumar]] how Gemma 270M serves a legitimate niche for edge deployment, on-device inference, and persistent local processes. Hugo demonstrates fine-tuning Gemma 270M in [[ws_8_finetuning_and_production_ai]], showing that a model scoring 0% on a classification task before fine-tuning can achieve 100% after -- but only on a narrow, well-defined task. Function Gemma, a 270M model adapted for local tool-calling and routing, illustrates how tiny models can serve specialized roles in larger systems.

In the middle sits what Alex Strick (ZenML, LLMOps database) and others call the enterprise workhorse tier: models like Gemini Flash that are fast enough for production, capable enough for most tasks, and cheap enough to run at scale. William Horton in [[william_horton_maven_clinic]] uses Gemini 2.5 Flash as the default for this reason, despite acknowledging it is "fast but relatively dumb" (his phrase from [[ws_5_context_engineering_and_information_retrieval]]). The Flash tier is where most production workloads run.

At the frontier sit reasoning models with extended chain-of-thought capabilities. Sebastian Raschka in [[llm_architecture_rasbt]] explains inference scaling -- longer reasoning chains, parallel sampling, sequential refinement, external judges -- as fundamentally about choosing how much compute to spend per query. GPT-5.4 in [[ws_2_prompting_and_context]] introduces adjustable reasoning effort, allowing developers to tune this trade-off at inference time. The practical implication is that the same model family can operate at different points on the Pareto frontier depending on how much reasoning effort you request.

## Smart Models for Planning, Cheap Models for Execution

A pattern that emerges across multiple sources is using more capable models for high-leverage decisions and cheaper models for routine execution. William Horton in [[william_horton_maven_clinic]] notes that smarter thinking models for lead agents with cheaper sub-agents is an effective pattern -- the lead agent makes routing decisions that determine what work gets done, while sub-agents execute specific tasks that require less intelligence. Ivan Leo's deep research agent in [[deep_research_agent_ivan_leo]] implicitly follows this pattern: the main orchestrator plans and delegates, while sub-agents execute focused search tasks.

Eric Ma in [[thinking_tools_eric_ma]] makes this explicit as a development strategy: use smart models for planning (where quality matters most) and cheaper models for execution (where speed and cost matter more). His LiteLLM-based provider-agnostic routing makes it practical to mix models within a single application, and his approach of cycling through whatever frontier models are available -- hitting rate limits then switching -- keeps him familiar with the full ecosystem.

Stefan's production case studies in [[ws_8_finetuning_and_production_ai]] show this pattern at scale: the veterinary transcription workflow with 60+ LLM calls in a DAG uses different models for different stages, and provider fallbacks are essential when a primary provider goes down. The restaurant voice agent similarly uses different components (speech-to-text, LLM reasoning, text-to-speech) that may use different models optimized for each modality.

## Behavioral Differences and Safety

Beyond raw capability and cost, models differ significantly in default behavior, and these differences matter for production systems. Hugo demonstrates in [[ws_2_prompting_and_context]] how Gemini appropriately disclaims being an AI when asked about headaches, while GPT-5.4 fires off seven rapid questions without disclaiming. Different models handle medical queries with varying levels of caution, and these deeply trained safety behaviors can be difficult to override with system prompts.

William Horton's experience in [[william_horton_maven_clinic]] makes this concrete: he had to write regex to strip Gemini's persistent medical disclaimers because system prompting could not override them. Sebastian Raschka in [[llm_architecture_rasbt]] explains why: post-training behaviors are deeply embedded through RLHF and are fundamentally resistant to prompt-level overrides. Brad Morris cites Drew Brunig's research in [[ws_2_prompting_and_context]] showing that coding harnesses have thousands to tens of thousands of tokens "fighting the weights" -- system prompts that try to override trained behaviors.

This creates a model selection criterion that is often overlooked: which model's default behavior is closest to what you want? If you are building a healthcare application, a model that defaults to caution may require less prompt engineering than one that defaults to helpfulness. Ivan Leo's advice in [[deep_research_agent_ivan_leo]] to start with the best model and optimize downward reflects this: begin with the most capable model to verify task feasibility, understand its behavior, then figure out which cheaper model can approximate that behavior adequately.

## Where Sources Agree

All sources agree that model selection is a multi-dimensional optimization problem involving capability, latency, cost, and behavioral characteristics. There is consensus that no single model is best for all use cases, that mixing models within an application is a valid and often necessary strategy, and that the Flash/workhorse tier handles most production workloads. Everyone agrees that starting with the most capable model to verify feasibility, then optimizing for cost and latency, is the right order of operations.

## Where Sources Disagree or Add Nuance

Ivan Leo's "spend today for the models of tomorrow" philosophy suggests over-investing in capability with the expectation that costs will drop. This sits in tension with William Horton's pragmatic approach of using Gemini Flash despite its limitations because latency matters today. The question of when fine-tuning justifies the investment versus when prompt engineering with a larger model suffices is debated across [[ws_8_finetuning_and_production_ai]] and [[ai_products_google_ravin_kumar]] -- Hugo argues fine-tuning is increasingly a last resort, while Ravin shows cases (Dolphin Gemma for dolphin communication) where it remains essential. Sebastian Raschka's observation that local inference stacks are not yet optimized for hybrid architectures adds a practical wrinkle: theoretically faster models may be paradoxically slower on consumer hardware, meaning model selection must account for deployment infrastructure, not just model capabilities.

## Related Concepts

- [[the_api_call_mental_model]] -- Model selection determines the model parameter of the API call; understanding the call structure helps evaluate what changes with different models
- [[fine_tuning_and_distillation]] -- Fine-tuning is one strategy for getting smaller models to perform like larger ones on specific tasks
- [[production_ai_patterns]] -- Provider fallbacks and cost management in production are direct consequences of model selection decisions
- [[llm_architecture_and_inference]] -- Architectural developments (inference scaling, hybrid architectures) create the range of model behaviors builders must navigate
- [[agents_vs_workflows]] -- Multi-agent architectures use different models for different roles, making model selection a per-agent decision
- [[prompt_engineering]] -- Model behavioral differences mean prompt engineering strategies must be adapted per model

## Sources

- [[ws_2_prompting_and_context]] -- Model behavioral differences on identical prompts across Gemini, GPT, and Claude; adjustable reasoning effort as an inference-time model selection lever
- [[ai_products_google_ravin_kumar]] -- The Gemma model family from 270M to 27B, Function Gemma for local routing, Flash vs. Pro Pareto frontier strategy
- [[william_horton_maven_clinic]] -- Production model selection at Maven Clinic: Gemini Flash for latency, GPT-5.4 Mini for health, smarter models for lead agents in multi-agent architectures
- [[deep_research_agent_ivan_leo]] -- Start with the best model and optimize downward; "spend today for the models of tomorrow"; model selection as a temporal bet
- [[llm_architecture_rasbt]] -- Architectural underpinnings of model differences: hybrid architectures, inference scaling, reasoning effort levels, and why post-training behaviors resist override
- [[ws_8_finetuning_and_production_ai]] -- When fine-tuning vs. prompting vs. retrieval; the decision framework for whether to adapt a model or use a different one
