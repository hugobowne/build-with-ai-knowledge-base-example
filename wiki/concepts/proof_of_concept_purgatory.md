---
type: concept
title: "Proof-of-Concept Purgatory"
related_concepts: [evaluation_driven_development, observability_and_tracing, five_first_principles, framework_selection, ai_sdlc, domain_specific_ai]
---

## Overview

Proof-of-concept purgatory is the central problem that motivates the entire course. Hugo Bowne-Anderson introduces it in [[ws_1_foundations]] as the phenomenon where flashy AI demos generate enormous excitement but quickly degrade as teams encounter hallucinations, monitoring challenges, and integration issues. The excitement curve for AI is inverted compared to traditional software: you get the wow moment first -- the demo that makes stakeholders gasp -- then fall into difficulty as you try to turn that demo into something reliable, maintainable, and trustworthy.

The concept resonates across nearly every session in the course because it describes an experience that every practitioner recognizes. Brad Morris captures it succinctly in [[builders_club_brad]]: "the idea and what you see on Twitter doesn't really line up." You watch a viral demo, attempt to replicate it, and discover that the gap between working-on-stage and working-in-production is enormous. Stella Liu and Eddie Wharton identify a specific mechanism in [[next_level_evals_stella_eddie]]: product requirements documents are often missing because teams go straight from prototyping to production. Without a clear specification of what the system should and should not do, there is no way to measure progress or identify failure. Eric Ma adds a complementary insight in [[thinking_tools_eric_ma]]: "you can't know your problem deeply until you've built a wrong solution." The first prototype is not purgatory -- purgatory is staying there without the tools and practices to iterate out of it.

The antidote to purgatory, as the course frames it, is not a single technique but a combination: [[evaluation_driven_development]] to measure quality, [[observability_and_tracing]] to see what is happening inside the system, systematic iteration through the build-deploy-monitor-evaluate cycle, and problem-first thinking that scopes to specific user pain points before reaching for an LLM. Hugo's framing is direct: "You can't test something that doesn't have a goal."

## The Inverted Excitement Curve

Traditional software development follows a predictable curve: initial difficulty learning the technology, followed by increasing capability as you build expertise, leading to a system that does what you expect. AI flips this curve. The Llama Index 5-line quickstart demonstrated in [[ws_1_foundations]] produces an impressive result in minutes, but Hugo immediately shows it giving a nonsensical answer ("Hugo hired Yashes Roy") that you cannot debug because the framework hides the model, the prompt, and all retrieval internals. The wow moment is real, but it creates false confidence.

Stefan Krawczyk reinforces this in [[ws_4_testing_and_observability]] with the observation that AI applications cannot be set-and-forget. Models get deprecated (OpenAI deprecating models by end of year is cited as a concrete example), distributions shift, and ongoing maintenance is the dominant cost -- just as in traditional software, but with less predictability. His opening polls in that workshop establish that most participants already understand this intuitively: they expect many LLM calls per application, prompt optimization takes days not hours, and AI apps require ongoing attention.

Ravin Kumar in [[ai_products_google_ravin_kumar]] adds the product perspective: the timeless advice is to "solve people's problems with whatever tools exist." Building because a technology is exciting rather than because a problem needs solving is a direct path into purgatory. William Horton's practical heuristic in [[builders_club_william_horton]] is to get people to describe their desired inputs and outputs without using hype terms like "agentic" -- if you cannot describe what you want without buzzwords, you do not yet understand the problem well enough to build a solution.

## What Keeps Teams Stuck

Several sources identify specific mechanisms that keep teams stuck in purgatory rather than iterating out of it.

The first is a lack of evaluation. Stella and Eddie note in [[next_level_evals_stella_eddie]] that the biggest eval mistake is "standing up evals without actually looking at your data" -- or worse, not standing up evals at all. Hamel Hussein's insight, cited in [[ws_3_evals_and_feedback_loops]], is that most people focus on changing system behavior without evaluating or debugging first, which prevents improvement. If you do not know how well your system works, you cannot know whether changes improve it.

The second is a lack of observability. Hugo's demonstration in [[ws_1_foundations]] of the progression from framework-obscured calls to transparent, logged interactions is the practical heart of escaping purgatory. You cannot improve what you cannot see. The five first principles established in that workshop -- API calls, non-determinism, logging/tracing, evaluation, and iteration -- are specifically designed as an escape route.

The third is premature framework adoption, covered in [[ws_1_foundations]] and debated extensively in [[ws_4_testing_and_observability]]. Frameworks that abstract away internals provide the initial wow but prevent the understanding needed to debug, evaluate, and iterate. Stefan's criterion -- does the framework optimize for 0-to-1 or 1-to-N? -- directly addresses whether a tool helps you escape purgatory or keeps you there.

## Problem-First Thinking as Antidote

Multiple sources converge on problem-first thinking as the primary antidote to purgatory. Ravin Kumar in [[ai_products_google_ravin_kumar]] advocates solving people's problems with whatever tools exist rather than building from technology excitement. William Horton in [[builders_club_william_horton]] recommends describing desired inputs and outputs without hype terms. Eric Ma in [[thinking_tools_eric_ma]] adds nuance: the first solution should be exploratory, but once you understand the problem, specs and tests become the double constraints that prevent the system from drifting.

Hugo synthesizes these perspectives in [[ws_1_foundations]]: "You can't test something that doesn't have a goal." Scoping to specific user pain points is essential before building. This is not an argument against experimentation -- Eric Ma explicitly argues you should build a wrong solution first -- but an argument that the demo should be the beginning of a disciplined process, not an end in itself.

## Where Sources Agree

All sources agree that purgatory is real and widespread. There is strong consensus that the inverted excitement curve accurately describes the AI development experience, that evaluation and observability are essential for escaping it, and that problem-first thinking prevents entering it in the first place. The course's entire structure -- from foundations through evaluation, testing, retrieval, agents, and production patterns -- is designed as a systematic path out of purgatory.

## Where Sources Disagree or Add Nuance

The sources disagree on how long teams should spend in the exploratory phase before imposing structure. Eric Ma argues that first versions should never use strict spec-driven development and that you should feel out the problem first. Stefan's framework evaluation criteria suggest more rigor from the start. Brad Morris's experience suggests that the gap between Twitter demos and reality is larger than most people expect, implying more caution is warranted. William Horton's emphasis on looking at documents and understanding the problem before building contrasts with Eric Ma's build-first philosophy, though both arrive at the same destination: systematic iteration once the problem is understood. The tension between moving fast (to discover what users actually need) and moving carefully (to avoid building the wrong thing) is not fully resolved -- it may be inherently situational.

## Related Concepts

- [[evaluation_driven_development]] -- Evaluation is the primary tool for measuring progress out of purgatory; without it, you cannot know if changes improve the system
- [[observability_and_tracing]] -- You cannot improve what you cannot see; observability is the prerequisite for debugging and evaluation
- [[five_first_principles]] -- The five principles are explicitly designed as the escape route from purgatory
- [[framework_selection]] -- Premature framework adoption is a direct path into purgatory; frameworks that hide internals prevent debugging
- [[ai_sdlc]] -- The build-deploy-monitor-evaluate cycle is the systematic process for iterating out of purgatory
- [[domain_specific_ai]] -- Domain-specific requirements (accuracy thresholds, regulatory constraints) make purgatory deeper in regulated industries

## Sources

- [[ws_1_foundations]] -- The primary source: defines proof-of-concept purgatory, the inverted excitement curve, and establishes the five first principles as the escape route
- [[ws_4_testing_and_observability]] -- Maintenance costs dominate, AI apps cannot be set-and-forget, and systematic testing provides the structure for iteration
- [[next_level_evals_stella_eddie]] -- Product requirements often missing; teams go straight from prototype to production without defining what the system should and should not do
- [[thinking_tools_eric_ma]] -- "You can't know your problem deeply until you've built a wrong solution" -- the first prototype is not purgatory, staying there is
- [[builders_club_brad]] -- "The idea and what you see on Twitter doesn't really line up" -- the gap between demos and reality
- [[ai_products_google_ravin_kumar]] -- Problem-first thinking: solve people's problems with whatever tools exist, not hype-driven building
