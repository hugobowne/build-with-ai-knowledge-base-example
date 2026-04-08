---
type: concept
title: "Production AI Patterns"
related_concepts: [ai_sdlc, observability_and_tracing, model_selection_and_tradeoffs, multi_agent_architecture, proof_of_concept_purgatory, guardrails]
---

## Overview

Production AI patterns address the practical engineering of deploying and maintaining AI systems beyond the prototype stage. The central insight across sources is that maintenance costs dominate setup costs -- just like traditional software, but amplified by model deprecation, distribution shift, and the non-deterministic nature of LLM outputs. You cannot build an AI application and walk away. Models get deprecated (OpenAI deprecating models by end of year is cited as a concrete example), user behavior shifts, and the system requires ongoing gardener-like attention.

Stefan Krawczyk introduces the two-loop model that frames production AI development ([[ws_4_testing_and_observability]]): an inner development loop (local testing, prompt tuning, evaluation) and an outer production loop (deployed application, logging, telemetry feeding back into development). This connects directly to the [[ai_sdlc]] build-deploy-monitor-evaluate cycle from [[ws_1_foundations]]. The two loops are not sequential -- they operate continuously in parallel, with production insights driving development changes and development improvements deploying to production.

The course surfaces production patterns through concrete case studies rather than abstract principles. Stefan's veterinary transcription system (60+ LLM calls in a DAG) and restaurant voice agent provide detailed architecture studies ([[ws_8_finetuning_and_production_ai]]). William Horton's Maven Assistant demonstrates progressive rollout in healthcare ([[william_horton_maven_clinic]]). Student demo day projects show Modal deployment in practice ([[demo_day]], [[builders_club_brad]]). Together, these reveal recurring patterns: provider fallbacks, progressive rollout, cost management, voice agent architecture, and the critical importance of real user data.

## Progressive Rollout and the Value of Real Users

William Horton's Maven Clinic rollout provides the most detailed account of bringing an AI system to production users ([[william_horton_maven_clinic]]). The progression moved through distinct phases: prototyping tools and learning internal APIs (October-November), basic tool-calling evaluations, then internal user testing with progressive expansion -- first the team, then product and engineering, then all Maven employees, then 20% of external users. At each stage, the diversity of inputs increased and testing with the same people yielded diminishing returns.

The first 24 hours of external user data revealed needs the team had not anticipated: users frequently wanted to update profile data (name, address), a mundane but high-volume request that was not in the initial agent scope ([[william_horton_maven_clinic]]). William's observation -- "until you get the real user data, you don't actually know what people want it to do" -- captures why progressive rollout is not just risk management but discovery. The biggest lift in AI products often comes from UX improvements prompted by real usage, not model improvements.

This echoes Ravin Kumar's advice to "get users as soon as possible, get their feedback, and iterate on that" ([[ws_7_workflows_multiagent_and_context_engineering]]). The principle applies across domains: even for the student projects on demo day, the transition from synthetic test data to real usage consistently revealed surprises ([[demo_day]]).

## Provider Fallbacks and Cost Management

Stefan's veterinary transcription case study reveals the operational reality of depending on third-party model providers ([[ws_8_finetuning_and_production_ai]]). When OpenAI went down, the system needed to route to alternative providers without breaking the 60+ call DAG. Provider fallbacks are not optional in production -- they are essential infrastructure. William Horton's approach of using LiteLLM for provider-agnostic routing ([[ws_4_testing_and_observability]]) and Stefan's experience with Hamilton for DAG orchestration both address this challenge.

Cost management operates at multiple levels. At the API level, model selection matters: William Horton uses Gemini 2.5 Flash for most tasks (prioritizing latency) and GPT-5.4 Mini for health questions (prioritizing accuracy), with the observation that smarter thinking models would ace all evals but are too slow and expensive for production ([[william_horton_maven_clinic]]). At the infrastructure level, Modal's pay-for-compute model -- charging only for GPU time when actively processing -- represents a pattern where production costs scale with actual usage rather than reserved capacity ([[builders_club_brad]]).

The cost of observability itself is a production concern. Logs and traces are not free, and when you are essentially reselling API providers (calling a model and serving the result to users), margin management matters ([[ws_8_finetuning_and_production_ai]]). There is a tension between the principle of logging everything from day zero ([[ws_1_foundations]]) and the economic reality that comprehensive logging at scale has real costs.

## Voice Agent Architecture

The restaurant voice ordering agent from [[ws_8_finetuning_and_production_ai]] demonstrates a specific production pattern: the three-legged voice architecture of speech-to-text (STT) + LLM + text-to-speech (TTS). Despite rapid advances in unified multimodal models, this disaggregated architecture persists in production because latency of unified models is not yet production-ready.

Stefan's implementation uses FastAPI with Apache Burr for agent orchestration, with intent classification routing to different agent states (find order item, update cart, checkout). Synthetic data generated from scraped real menus was crucial for reliability -- the system needed to understand actual menu items and their variations. Ben Shababo's voice-to-voice RAG bot architecture from [[ws_1_foundations]], using PipeCat with speech-to-text and text-to-speech on independent Modal services, demonstrates the same disaggregated pattern.

This voice architecture illustrates a broader production principle: production systems often use disaggregated architectures that seem less elegant than unified approaches but provide better latency, debuggability, and fallback options. Each leg of the voice pipeline can be independently monitored, scaled, and swapped.

## Deployment Infrastructure

Modal emerges as the primary deployment platform across the course, introduced by Ben Shababo in [[ws_1_foundations]] and used extensively in student projects ([[demo_day]]). Brad Morris's Discord bot deployment workshop walks through the full workflow from local development through `modal serve` to `modal deploy`, demonstrating how Modal abstracts away containerization while maintaining control over GPU selection and scaling ([[builders_club_brad]]).

The deployment pattern for AI applications differs from traditional web applications in important ways. GPU requirements create cost sensitivity -- you want GPU instances running only when processing requests, not idling. Modal's on-demand model addresses this. The combination of fast iteration needs (frequent prompt changes, model swaps) and reliability requirements (production uptime, fallbacks) creates tension between agility and stability that the two-loop model helps manage.

Stefan's production systems use different infrastructure choices: AWS Lambda for the veterinary transcription DAG (serverless, pay-per-invocation), FastAPI with Burr for the restaurant agent (persistent service for voice latency requirements) ([[ws_8_finetuning_and_production_ai]]). The infrastructure choice follows from the application's latency and scaling requirements.

## Where Sources Agree

All sources agree that production AI requires ongoing maintenance, that real user data reveals needs that testing cannot anticipate, and that provider fallbacks are essential. There is consensus that the two-loop development model (inner development + outer production) provides the right framework, and that progressive rollout is the safest path to production. Sources also converge on the importance of cost awareness -- both API costs and infrastructure costs -- as AI systems scale.

## Where Sources Disagree or Add Nuance

The sources reflect different production contexts that shape their patterns. Stefan's systems are backend processing pipelines where latency is measured in minutes and batch processing is acceptable ([[ws_8_finetuning_and_production_ai]]). William Horton's Maven Assistant is a real-time chat interface where each additional second of latency degrades user experience ([[william_horton_maven_clinic]]). These different contexts lead to different architectural decisions: DAGs with parallelization for throughput versus model selection optimized for response time.

There is also an implicit debate about the level of infrastructure abstraction appropriate for AI applications. Modal offers high abstraction (no containers to manage), while Stefan's AWS Lambda + Hamilton approach provides more control but more operational complexity. Brad Morris and Hugo advocate for Modal's simplicity ([[builders_club_brad]]), but production teams at companies like Maven Clinic need the control that lower-level infrastructure provides.

The question of when coding agents will handle production maintenance tasks is raised but not resolved. Anonymized Student Y discusses using coding agents for a planning-first approach to maintenance ([[ws_4_testing_and_observability]]), and Stefan notes that coding agents may automate some maintenance costs. Whether this will fundamentally change the maintenance burden or simply shift it remains an open question.

## Related Concepts

- [[ai_sdlc]] -- The overarching lifecycle framework that production patterns implement in practice
- [[observability_and_tracing]] -- Logging and monitoring are essential from day zero and become the outer loop's primary input
- [[model_selection_and_tradeoffs]] -- Production constraints (latency, cost, reliability) drive model selection more than raw capability
- [[multi_agent_architecture]] -- Multi-agent systems amplify every production challenge: latency, debugging, fallbacks, cost
- [[proof_of_concept_purgatory]] -- Production patterns are the systematic antidote to the demo-to-deployment gap
- [[guardrails]] -- Production systems require input and output safeguards that prototypes can skip

## Sources

- [[ws_4_testing_and_observability]] -- The two-loop model (inner development + outer production), CI/CD for AI, maintenance cost reality, and the framework for systematic production AI engineering
- [[ws_8_finetuning_and_production_ai]] -- Veterinary transcription DAG (60+ LLM calls), restaurant voice agent, provider fallbacks, cost management, and observability trade-offs as concrete production case studies
- [[william_horton_maven_clinic]] -- Progressive rollout from team to 20% of external users, first-day production surprises, model selection for latency, and the value of real user data
- [[ws_1_foundations]] -- The build-deploy-monitor-evaluate cycle, Modal deployment introduction, and the foundational principle of logging from day zero
- [[demo_day]] -- Multiple student projects using Modal for deployment, demonstrating production patterns applied to diverse use cases
- [[builders_club_brad]] -- Modal deployment workshop with Discord bot, demonstrating the full deployment workflow and pay-for-compute economics
