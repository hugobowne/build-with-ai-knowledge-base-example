---
type: concept
title: "The AI Software Development Lifecycle"
related_concepts: [five_first_principles, evaluation_driven_development, observability_and_tracing, proof_of_concept_purgatory, production_ai_patterns]
---

## Overview

The AI software development lifecycle (AI SDLC) is the overarching framework for the entire course: build, deploy, monitor, evaluate, iterate. Introduced in [[ws_1_foundations]] and revisited throughout every subsequent session, it represents both a practical methodology and a philosophical stance -- that AI systems are fundamentally "organic," requiring gardener-like ongoing attention rather than the set-and-forget deployment patterns of traditional software. Hugo frames this as one of the core lessons: AI flips the traditional software excitement curve. You get the wow moment first (the flashy demo), then fall into difficulty as hallucinations, monitoring gaps, and integration issues compound. The AI SDLC is the systematic answer to what Hugo calls [[proof_of_concept_purgatory]].

The lifecycle rests on the [[five_first_principles]] established in Workshop 1: API calls as the atomic unit, non-determinism as a fundamental property, logging and tracing from day zero, evaluation as the backbone, and rapid iteration through prompt engineering, tool use, and business logic changes. These principles are not sequential stages but concurrent disciplines. Stefan Krawczyk's two-loop model in [[ws_4_testing_and_observability]] provides the operational structure: an inner development loop (local testing, prompt tuning, eval data collection) and an outer production loop (deployed application, user telemetry, feedback flowing back into development). Unlike traditional CI/CD where the outer loop dominates engineering attention, AI development demands constant attention to the inner loop because models get deprecated, distributions shift, and small prompt changes can cascade unpredictably.

The AI SDLC was validated across the course through diverse real-world applications: William Horton's multi-month progression from prototype to production launch of Maven's health agent ([[william_horton_maven_clinic]]), Stella and Eddie's framing of evals as both compass and gate in the product development cycle ([[next_level_evals_stella_eddie]]), and the demo day projects where students applied the full lifecycle within weeks ([[demo_day]]).

## The Build-Deploy-Monitor-Evaluate Cycle

The cycle as Hugo presents it in [[ws_1_foundations]] is deceptively simple: build an AI application, deploy it, monitor its behavior, evaluate its performance, and iterate. The depth emerges in how each phase interacts with the others. Building is not just writing code -- it requires understanding the API call anatomy ([[the_api_call_mental_model]]), choosing models ([[model_selection_and_tradeoffs]]), and engineering context ([[context_engineering]]). Deployment involves serverless infrastructure like Modal ([[ws_1_foundations]]), provider fallback strategies, and cost management. Monitoring means logging every LLM call with tools like SQLite/Datasette or OpenTelemetry from the first line of code, not as an afterthought ([[observability_and_tracing]]). Evaluation spans the full maturity arc from manual "vibes" through failure analysis to automated eval harnesses ([[evaluation_driven_development]]).

What makes the AI SDLC distinctive is that iteration is not optional maintenance -- it is the primary mode of development. Hugo emphasizes that AI systems cannot be set-and-forget: models get deprecated (OpenAI deprecating models by end of year, as Stefan notes in [[ws_4_testing_and_observability]]), user input distributions shift, and the cost-quality frontier moves with every new model release. Stefan's veterinary transcription case study in [[ws_8_finetuning_and_production_ai]] illustrates this concretely: a system that grew from simple beginnings to 60+ LLM calls in a DAG, requiring continuous iteration on debugging, parallelization, and provider fallbacks.

## The Two-Loop Model

Stefan Krawczyk's two-loop mental model, introduced in [[ws_4_testing_and_observability]], provides the operational mechanics of the AI SDLC. The inner development loop is where prompt tuning, testing, and local evaluation happen. Stefan demonstrates this with PyTest and PyTest Harvest, showing how LLM outputs can be systematically tested across multiple dimensions simultaneously rather than stopping at the first failure. The key insight is that you need per-LLM-call evaluation datasets -- not just end-to-end system tests, but datasets for each individual API call in your pipeline.

The outer production loop captures real user behavior, system telemetry, and cost data, feeding these back into the development loop. William Horton's Maven Assistant launch ([[william_horton_maven_clinic]]) demonstrates the outer loop in action: the first 24 hours of real user data revealed that people frequently wanted to update profile data (names, addresses) -- a mundane but high-volume need the team had not prioritized. This kind of discovery only happens in the production loop and drives the next iteration of the development loop.

The interaction between the two loops is what distinguishes AI development from traditional software engineering. Stefan argues that observability is useful from the very first day of development -- not just in production -- because what you send to the LLM is context-dependent and the only way to debug is to observe what was actually sent ([[ws_4_testing_and_observability]]). This is a break from traditional software engineering where observability is primarily a production concern.

## From Prototype to Production

The AI SDLC is not just a framework for greenfield development -- it describes the maturation path from prototype to production system. William Horton's account of building Maven Assistant provides the most detailed case study ([[william_horton_maven_clinic]]). The progression moved through distinct phases: prototyping tools and learning internal APIs (October-November), basic tool-calling evaluations, internal user testing with progressive expansion (team, then product/engineering, then all employees, then 20% of external users), and qualitative LLM-as-judge evaluations for subtler criteria. Each phase involved different evaluation criteria and different feedback loops.

Stella and Eddie frame evals as serving dual purposes in this lifecycle: as a compass for product iteration (guiding where to invest development effort) and as a pass/fail gate for releases (deciding whether to ship) ([[next_level_evals_stella_eddie]]). Eddie adds the critical insight that offline evals measure against the product owner's expectations, while online experiments reveal what real users actually need -- and these often diverge. The Amazon Rufus chatbot is cited as a cautionary example of missing product constraints.

The demo day projects ([[demo_day]]) demonstrate that the lifecycle is accessible even for newcomers: students combined multiple course concepts -- Modal deployment, deep research agents, tool calling, and evals -- into working prototypes within days. Natalia Rodnova's Jira Assistant, spanning three cohorts, exemplifies the iterative nature of the SDLC at its best: each return to the project brought new knowledge and new capabilities.

## Where Sources Agree

All sources converge on the central thesis that AI development is fundamentally iterative and that evaluation is its backbone. Hugo's framing of AI systems as "organic" ([[ws_1_foundations]]) is echoed by Stefan's insistence that maintenance costs dominate setup costs ([[ws_4_testing_and_observability]]), William's progressive rollout strategy ([[william_horton_maven_clinic]]), and Stella's dual compass-and-gate framing of evals ([[next_level_evals_stella_eddie]]). There is unanimous agreement that AI cannot be set-and-forget, that logging from day zero is non-negotiable, and that real user data reveals things no amount of internal testing anticipates.

The sources also agree that the AI SDLC borrows heavily from established software engineering -- CI/CD, testing frameworks, observability -- but adapts these practices to handle non-determinism and the rapid pace of model evolution. Carol Willing repeatedly emphasizes that "good engineering is good engineering" regardless of what you call it ([[ws_4_testing_and_observability]]).

## Where Sources Disagree or Add Nuance

The primary tension is around how much structure the lifecycle requires at different stages. Hugo and Stefan present a relatively structured framework with distinct phases and tools, but early-stage exploration is often messier — especially when you don't yet know what you're building.

Eddie Wharton's critique that teams often skip from prototype to production without defining product requirements ([[next_level_evals_stella_eddie]]) points to a gap in the SDLC as commonly practiced: the framework assumes you know what you are building, but many AI projects start without clear specifications. Eric Ma's observation that "you can't know your problem deeply until you've built a wrong solution" ([[proof_of_concept_purgatory]]) suggests the first iteration of the SDLC may be deliberately throwaway -- a tension the framework does not fully resolve.

There is also nuance around the two-loop model's universality. Stefan's model works well for applications with clear production deployments, but for internal tools (like Natalia's Jira Assistant) or research-oriented applications (like Konrad's research assistant at demo day), the distinction between inner and outer loops blurs. The lifecycle adapts, but differently than the clean two-loop diagram suggests.

## Related Concepts

- [[five_first_principles]] -- The foundational framework that the AI SDLC operationalizes
- [[evaluation_driven_development]] -- Evaluation is the backbone of the SDLC, driving every iteration
- [[observability_and_tracing]] -- Logging and monitoring from day zero enable the feedback loops the lifecycle depends on
- [[proof_of_concept_purgatory]] -- The problem the AI SDLC is designed to solve
- [[production_ai_patterns]] -- Practical patterns for the deployment and maintenance phases of the lifecycle
- [[the_api_call_mental_model]] -- Understanding the API call is the first principle that grounds every phase of the lifecycle

## Sources

- [[ws_1_foundations]] -- The primary source for the five first principles, the build-deploy-monitor-evaluate cycle, and the framing of AI systems as organic
- [[ws_4_testing_and_observability]] -- Stefan Krawczyk's two-loop model, CI/CD for AI, and the argument that maintenance costs dominate
- [[ws_8_finetuning_and_production_ai]] -- The course recap revisiting the full lifecycle, plus production case studies that demonstrate the SDLC in practice
- [[william_horton_maven_clinic]] -- The most detailed case study of the agent development lifecycle from prototype through progressive rollout to production launch
- [[next_level_evals_stella_eddie]] -- Frames evals as compass and gate in the product development cycle, adding the distinction between offline and online evaluation
- [[demo_day]] -- Students applying the full lifecycle in diverse projects, demonstrating its accessibility and adaptability
