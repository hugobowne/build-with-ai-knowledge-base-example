---
type: concept
title: "Five First Principles for AI Software Development"
related_concepts: [ai_sdlc, the_api_call_mental_model, non_determinism, observability_and_tracing, evaluation_driven_development, prompt_engineering]
---

## Overview

The five first principles for AI software development form the foundational framework for the entire course, introduced systematically in [[ws_1_foundations]] and referenced or expanded upon in every subsequent session. Hugo frames these principles as the minimum viable understanding needed to escape [[proof_of_concept_purgatory]] and build AI systems that work beyond the demo stage. The five principles are: (1) API calls as the atomic unit, (2) non-determinism -- the "double entropy problem," (3) logging, monitoring, and tracing from day zero, (4) evaluation as the backbone, and (5) rapid iteration through prompt engineering, tool use, and business logic changes.

What makes these principles powerful is not their individual novelty but their interaction. Understanding the API call anatomy means you can see exactly what feeds into the non-deterministic process. Logging from day zero means you can observe non-determinism in practice. Evaluation gives you a measurement framework for that observed behavior. And rapid iteration closes the loop, using all the previous principles to systematically improve the system. Hugo describes AI systems as "organic" -- constantly shifting, requiring gardener-like attention rather than the build-once-deploy-forever mindset of traditional software. The five principles are the gardener's essential tools.

The principles were validated across the course's diverse case studies: Stefan Krawczyk grounds them in the API call structure in [[ws_8_finetuning_and_production_ai]], William Horton applies them in production healthcare at Maven Clinic ([[william_horton_maven_clinic]]), and the demo day students demonstrate they can be productively applied within weeks of learning them ([[demo_day]]).

## Principle 1: API Calls as the Atomic Unit

Every interaction with an LLM reduces to an API call with specific components: a system prompt, messages (user, assistant, and tool), tool schemas, structured output definitions, and configuration parameters like temperature and reasoning effort. Stefan Krawczyk's masterclass in [[ws_8_finetuning_and_production_ai]] demonstrates how this mental model demystifies every buzzword in the space: RAG populates context, MCP populates tool schemas, guardrails validate context and responses, and skills are progressive disclosure of context. Understanding the API call is treated as a prerequisite for everything else -- you cannot debug what you do not understand, and you cannot understand a system whose fundamental unit is hidden behind framework abstractions.

Hugo demonstrates this in [[ws_1_foundations]] by showing how Llama Index's 5-line quickstart hides the model being used, the prompt, and all retrieval internals -- a convenience that becomes a liability when the system misbehaves. The antidote is Hamel Hussein's "F You, Show Me the Prompt" ethos: always know what is being sent to the model. This principle is explored in depth in [[the_api_call_mental_model]].

## Principle 2: Non-Determinism and the Double Entropy Problem

LLM outputs vary across runs -- but the non-determinism runs deeper than temperature settings. Hugo introduces the "double entropy problem": there is entropy in both the model's outputs and in the user's inputs. Users phrase the same request differently every time, and models respond differently to the same prompt. William Horton references this framing by name at Maven Clinic ([[william_horton_maven_clinic]]), where the combination of variable patient queries and variable model responses creates a combinatorial challenge for healthcare accuracy.

The critical insight, established in [[ws_1_foundations]] and reinforced in [[next_level_evals_stella_eddie]], is that non-determinism is not a bug to fix but a property to build systems around. In some contexts it is even a feature: Stella Liu argues that non-determinism is a superpower for deep research and creative writing tools, where diverse outputs are desirable. Natalia Rodnova suggests Monte Carlo-style repeated runs as a practical testing strategy ([[ws_3_evals_and_feedback_loops]]). The architectural underpinnings of non-determinism -- temperature, sampling, and inference scaling -- are covered in [[llm_architecture_and_inference]]. This principle is explored further in [[non_determinism]].

## Principle 3: Logging, Monitoring, and Tracing from Day Zero

Unlike traditional software where observability is primarily a production concern, AI systems benefit from observability from the very first day of development. Stefan Krawczyk makes this case forcefully in [[ws_4_testing_and_observability]]: "The only way that you can debug what happened is dependent on what you observe, because what you send to the LLM is context-dependent." Hugo demonstrates the practical starting point in [[ws_1_foundations]] with SQLite-based logging and Simon Willison's Datasette tool for trace visualization -- lightweight, immediate, and sufficient for early development.

As systems mature, OpenTelemetry becomes the industry standard for instrumentation ([[ws_4_testing_and_observability]]), with the strong prescription to avoid tools not compatible with it. Ivan Leo's deep research agent uses Logfire for trace inspection ([[deep_research_agent_ivan_leo]]), and Natalia Rodnova's Jira Assistant demonstrates layered observability showing each LLM call, tool invocation, and response ([[demo_day]]). Katherine Jarmul adds privacy observability as an additional dimension ([[privacy_and_security]]). This principle is explored in depth in [[observability_and_tracing]].

## Principle 4: Evaluation as the Backbone

Evaluation is not a late-stage quality gate but the backbone of the entire development process. The progression from manual "vibes" (looking at data in spreadsheets) through failure analysis (systematic error categorization) to automated evaluation (code checks and LLM-as-judge) is laid out in [[ws_3_evals_and_feedback_loops]] and extended with statistical rigor in [[next_level_evals_stella_eddie]]. Hugo emphasizes that most people focus on changing system behavior without evaluating or debugging first -- the most common mistake in AI development.

William Horton calls evaluation "the most important AI engineering skill" ([[builders_club_william_horton]]), and his Maven launch demonstrates the principle in practice: binary tool-call checks covering most cases, LLM-as-judge for subtler criteria like empathy and clinical accuracy, and the critical insight that saturated metrics (99% before launch) prevent you from measuring improvement. This principle is explored in depth in [[evaluation_driven_development]].

## Principle 5: Rapid Iteration

The fifth principle closes the loop: use prompt engineering, tool use, and business logic changes to iterate rapidly on the system. Hugo frames this as the antidote to the waterfall approach where teams spend months perfecting a system before testing it with users. Prompt iteration counts vary enormously by use case -- 8 iterations for Colgate synthetic surveys vs. 600+ for Carvana's public-facing car descriptions ([[ws_2_prompting_and_context]]) -- but the principle of iterating systematically rather than guessing remains constant.

Stefan's two-loop model ([[ws_4_testing_and_observability]]) provides the operational structure for rapid iteration: the inner loop for local testing and prompt tuning, the outer loop for production telemetry feeding back into development. William Horton's progressive rollout strategy -- team, then company, then 20% of users -- is a disciplined approach to iteration that balances speed with risk ([[william_horton_maven_clinic]]). Eric Ma's complementary perspective adds that "you can't know your problem deeply until you've built a wrong solution" ([[proof_of_concept_purgatory]]), suggesting the first iteration may be deliberately throwaway. This principle connects to [[prompt_engineering]] and [[production_ai_patterns]].

## Where Sources Agree

The five principles enjoy near-universal endorsement across the sources. Every workshop session references at least one principle, and the guest speakers uniformly validate them through their own practice. Stefan Krawczyk's "it's all just an API call" framework in [[ws_8_finetuning_and_production_ai]] is an explicit grounding of Principle 1. William Horton's Maven development lifecycle validates all five principles in a production healthcare context. Stella and Eddie's eval methodology builds directly on Principle 4. The agreement is not superficial -- each source adds depth and practical nuance to principles that might otherwise seem like platitudes.

The ordering matters: API calls first (understand the unit), non-determinism second (understand its behavior), logging third (observe it), evaluation fourth (measure it), iteration fifth (improve it). This sequence is pedagogical and practical simultaneously.

## Where Sources Disagree or Add Nuance

The most significant nuance is around how the principles apply at different stages of development. Hugo presents them as non-negotiable from day one, but Eric Ma's observation that "you can't know your problem deeply until you've built a wrong solution" ([[thinking_tools_eric_ma]]) suggests the first iteration may be deliberately rough. The principles describe both the ideal and the direction of travel — teams may not implement all five perfectly from the start, but knowing the destination shapes even early decisions.

There is also nuance around Principle 2 (non-determinism). Hugo frames it as a property to build around, Stella argues it can be a superpower for certain use cases ([[next_level_evals_stella_eddie]]), and Ryan Rodriguez raises the fascinating question of whether LLM determinism is achievable by controlling inference batch size ([[ws_3_evals_and_feedback_loops]]). The architectural view from [[llm_architecture_rasbt]] adds complexity: reasoning models introduce structured non-determinism through inference scaling, making the simple "temperature = 0 for determinism" advice increasingly incomplete.

Carol Willing's recurring reminder that "good engineering is good engineering" ([[ws_4_testing_and_observability]]) provides a counterpoint to the framing of these as specifically "AI" principles. Many -- logging, evaluation, iteration -- are established software engineering practices adapted for a new context. Whether they constitute genuinely new principles or repackaged wisdom applied to a new domain is left as a productive tension.

## Related Concepts

- [[ai_sdlc]] -- The lifecycle that the five principles support and enable
- [[the_api_call_mental_model]] -- Principle 1 developed into a full conceptual framework
- [[non_determinism]] -- Principle 2 explored in depth with architectural and practical dimensions
- [[observability_and_tracing]] -- Principle 3 developed into tooling and practice recommendations
- [[evaluation_driven_development]] -- Principle 4 as the backbone of the entire development process
- [[proof_of_concept_purgatory]] -- The problem the five principles are designed to solve

## Sources

- [[ws_1_foundations]] -- The primary source where all five principles are laid out systematically, with the "organic systems" and "double entropy" framings
- [[ws_3_evals_and_feedback_loops]] -- Develops the evaluation principle into a three-stage framework (vibes, failure analysis, automated evaluation)
- [[ws_4_testing_and_observability]] -- Develops the logging/tracing and iteration principles through the two-loop model and OpenTelemetry
- [[ws_8_finetuning_and_production_ai]] -- The course recap where principles are revisited and grounded in Stefan's "it's all just an API call" framework
- [[william_horton_maven_clinic]] -- Validates all five principles through a production healthcare case study, including the "double entropy problem" referenced by name
