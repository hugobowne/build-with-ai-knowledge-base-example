---
type: concept
title: "Observability and Tracing"
related_concepts: [evaluation_driven_development, the_api_call_mental_model, ai_sdlc, production_ai_patterns, privacy_and_security, five_first_principles]
---

## Overview

Observability and tracing in AI systems refers to the practice of logging, monitoring, and instrumenting LLM applications so that developers can see what is happening inside their systems at every level -- from individual API calls to multi-agent orchestrations. What distinguishes AI observability from traditional software monitoring is a critical insight that emerges across multiple sources in this course: observability is useful from development, not just production. In traditional software engineering, observability is primarily a production concern. In AI engineering, the non-deterministic nature of LLM outputs means that understanding what the system is doing is essential from the very first day of building.

Hugo Bowne-Anderson introduces logging as one of the [[five_first_principles]] in [[ws_1_foundations]], arguing that you cannot evaluate what you cannot observe. He demonstrates lightweight logging with SQLite and Simon Willison's Datasette tool for trace visualization -- an approach that gets you far before investing in heavier infrastructure. Stefan Krawczyk deepens this in [[ws_4_testing_and_observability]], advocating strongly for OpenTelemetry as the industry standard for instrumentation and warning against adopting tools that are not compatible with it. Ivan Leo's deep research agent workshop in [[deep_research_agent_ivan_leo]] puts these principles into practice with Pydantic Logfire, showing how tracing sub-agent dispatching, search calls, and report synthesis makes complex agent behavior legible. Meanwhile, Katharine Jarmul in [[katherine_jarmul_privacy]] extends the concept by arguing that privacy observability should be integrated into general observability rather than treated as a separate concern. At the production end, Stefan notes in [[ws_8_finetuning_and_production_ai]] that the cost of observability is itself a production concern -- logs and traces are not free, and margin management matters when reselling API providers.

## Why Observability Starts at Development Time

The fundamental reason AI observability differs from traditional software observability is the [[non_determinism]] inherent in LLM systems. As Stefan explains in [[ws_4_testing_and_observability]], "the only way that you can debug what happened is dependent on what you observe, because what you send to the LLM is context-dependent." In traditional software, a bug is reproducible: you can set a breakpoint, step through code, and find the issue. In AI systems, the same input may produce different outputs, and the context feeding into each call determines behavior in ways that are invisible without instrumentation.

This insight drives a practical recommendation that appears across multiple sessions: instrument from day zero. Hugo demonstrates this in [[ws_1_foundations]] with SQLite logging that captures every LLM call, showing how a Llama Index quickstart that appears to work can hide the model being used, the prompt, and all retrieval internals. The progression from framework-obscured calls to transparent, logged interactions is what Hugo calls "the practical heart of getting out of purgatory" -- connecting observability directly to escaping [[proof_of_concept_purgatory]].

Stefan's two-loop mental model in [[ws_4_testing_and_observability]] formalizes this: the inner development loop (local testing, prompt tuning) and the outer production loop (deployed app, logging, feedback into development) both depend on observability. Per-LLM-call evaluation datasets may be needed because debugging depends on understanding what context fed into which call, particularly in systems like the veterinary transcription workflow in [[ws_8_finetuning_and_production_ai]] that grew to 60+ LLM calls in a DAG.

## OpenTelemetry as the Standard

Multiple sources converge on OpenTelemetry as the instrumentation standard for AI applications. Stefan's prescription in [[ws_4_testing_and_observability]] is emphatic: "Do your best in this space to avoid adopting tools that aren't compatible with OpenTelemetry." Hugo adds a longevity argument, urging builders to think about what will still be around in 2, 5, and 10 years. Samuel Colvin (creator of Pydantic) is cited for the same advocacy.

Ivan Leo demonstrates this standard in practice in [[deep_research_agent_ivan_leo]], using Logfire (built on OpenTelemetry) to visualize deep research agent traces. His walkthrough of a completed research run -- showing sub-agents dispatched, iteration limits enforced, search calls made, and results flowing back to the main orchestrator -- illustrates why standardized tracing matters for complex multi-agent systems. Natalia Rodnova's Jira Assistant, presented at [[demo_day]], implements layered observability that shows each LLM call, tool invocation, inputs, and outputs, demonstrating that even student projects can achieve production-quality trace visibility.

## Privacy and Cost Dimensions

Two often-overlooked dimensions of observability emerge from the sources. Katharine Jarmul in [[katherine_jarmul_privacy]] argues that privacy observability should not be a separate system bolted on after the fact but should be woven into the same observability infrastructure. If your tracing captures what data flows through the system, privacy monitoring becomes a natural extension rather than an afterthought. She connects this to the broader insight that if you have never had a privacy or security incident reported, it does not mean one has not occurred -- it means your reporting is broken.

Stefan raises the cost dimension in [[ws_8_finetuning_and_production_ai]], noting that observability infrastructure has real costs in production. When your business model involves reselling API providers with a margin, every log line and trace span has a cost that must be managed. This creates a tension between the "log everything from day zero" principle and the economic reality of production systems, requiring thoughtful decisions about what to observe at what granularity.

## Where Sources Agree

All sources agree that observability is not optional for AI systems -- it is foundational. The connection between observability and the ability to improve systems is treated as axiomatic: you cannot evaluate what you cannot see. There is strong consensus on OpenTelemetry as the right instrumentation standard, and agreement that AI observability should start during development rather than being added later for production monitoring. Every source that discusses debugging or evaluation implicitly depends on observability being in place.

## Where Sources Disagree or Add Nuance

The sources differ primarily on the appropriate level of investment in observability tooling. Hugo's starting point in [[ws_1_foundations]] is deliberately lightweight -- SQLite and Datasette -- emphasizing that you should not let tooling complexity delay getting started. Stefan and Ivan work at a higher level of tooling sophistication with OpenTelemetry and Logfire. The tension between "log everything" and Stefan's own note about cost in production is not fully resolved. Samuel Colvin's prediction that AI observability will eventually just be called "observability" once the field stabilizes suggests the current specialized tooling may be temporary. Katharine Jarmul's privacy observability dimension adds a concern that most other sources do not address, suggesting that the observability conversation in the broader community may be incomplete.

## Related Concepts

- [[five_first_principles]] -- Logging, monitoring, and tracing is the third of the five first principles for AI software development
- [[evaluation_driven_development]] -- Observability provides the raw data that evaluation consumes; you cannot evaluate what you cannot observe
- [[proof_of_concept_purgatory]] -- Lack of observability is a key reason teams get stuck in purgatory; you cannot improve a system you cannot see into
- [[the_api_call_mental_model]] -- Understanding the API call structure determines what to observe and where to instrument
- [[privacy_and_security]] -- Privacy observability should be integrated into general observability, not treated separately
- [[production_ai_patterns]] -- The two-loop model and cost management both depend on observability infrastructure

## Sources

- [[ws_1_foundations]] -- Introduces logging as one of the five first principles, demonstrates SQLite and Datasette for lightweight trace visualization from day zero
- [[ws_4_testing_and_observability]] -- The definitive observability session: OpenTelemetry as standard, observability from development not just production, the two-loop model, and per-LLM-call debugging requirements
- [[deep_research_agent_ivan_leo]] -- Demonstrates Logfire for agent trace inspection with sub-agent observability, showing practical application of OpenTelemetry in complex multi-agent systems
- [[katherine_jarmul_privacy]] -- Introduces privacy observability as a dimension that should be integrated into general observability infrastructure
- [[demo_day]] -- Natalia's Jira Assistant showcases layered observability in a student project, demonstrating accessibility of these practices
- [[ws_8_finetuning_and_production_ai]] -- Raises the cost of observability as a production concern and grounds observability in the API call mental model
