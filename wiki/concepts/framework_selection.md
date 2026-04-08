---
type: concept
title: "Framework Selection and the Build vs. Buy Decision"
related_concepts: [the_api_call_mental_model, proof_of_concept_purgatory, agents_vs_workflows, production_ai_patterns, observability_and_tracing, prompt_engineering]
---

## Overview

Framework selection -- choosing which libraries, SDKs, and abstractions to build AI applications with -- is one of the most debated topics across the course. The debate is not merely technical but philosophical: frameworks trade control for speed, and the right trade-off depends on whether you are building a prototype or a production system, whether you need to understand the internals, and how quickly the underlying models are changing. The course surfaces a genuine multi-sided disagreement among experienced practitioners, with Stefan Krawczyk, William Horton, Natalia Rodnova, and Eric Ma each bringing distinct perspectives grounded in production experience.

Stefan Krawczyk provides the most systematic framework for framework evaluation in [[ws_4_testing_and_observability]]: assess by origin story (what were the creators optimizing for?), whether the tool helps with 0-to-1 (prototype) or 1-to-N (production maintenance), and whether it replaces code you do not care about. His critique of frameworks that oversimplify is sharp -- they gear toward 0-to-1 but become liabilities for 1-to-N maintenance. This connects directly to Hugo's demonstration in [[ws_1_foundations]] of Llama Index's 5-line quickstart that hides the model being used, the prompt, and all retrieval internals, prompting Hamel Hussein's "F You, Show Me the Prompt" reaction.

The tension is real because AI frameworks operate in an unusually volatile environment. Models are improving rapidly, APIs change, and what was hard six months ago may now be a single API call. Ivan Leo in [[deep_research_agent_ivan_leo]] builds from raw API calls to demonstrate full understanding, then notes that provider SDKs like Pydantic AI are reasonable for one-person shops. Stefan in [[ws_8_finetuning_and_production_ai]] grounds the entire debate with his "it's all just an API call" framework, arguing that understanding the API call structure lets you evaluate any framework by what it does to each component of that call.

## The Multi-Sided Debate

The framework discussion in [[ws_4_testing_and_observability]] becomes the course's most heated exchange, revealing at least four distinct positions that are worth understanding in detail.

Stefan Krawczyk argues for evaluating frameworks by their origin story and whether they optimize for prototyping or production. He characterizes Langchain as "you don't know what you're doing, here's three lines of code, magic" and contrasts it with frameworks like FastAPI that serve production use cases well. His reconciliation principle -- control the interface, hide the implementation, allowing framework swaps -- is the most portable advice from the debate.

William Horton takes the strongest anti-framework position: "I honestly just want to pick up the OpenAI SDK. I don't want to use your wrapper." His preferred pattern is the OpenAI SDK with a LiteLLM gateway for multi-provider routing, keeping the abstraction layer as thin as possible. He argues passionately against internal frameworks, which tend to become maintenance burdens that nobody wants to own. Eric Ma in [[thinking_tools_eric_ma]] shares the LiteLLM approach for provider-agnostic routing, independently arriving at the same thin-wrapper pattern.

Natalia Rodnova advocates building thin custom wrappers, citing the advantage of logging every cost as a benefit of controlling your own abstraction layer. Her approach is pragmatic: if you are going to wrap the SDK anyway for logging and cost tracking, you might as well control the interface entirely.

Carol Willing cuts through the terminology debate with characteristic pragmatism: "Good engineering is good engineering, and you can name it anything you want." She draws parallels to established engineering principles, arguing that the patterns are not new even if the tools are.

## Framework Failure Modes

The course provides concrete evidence of framework failure modes that justify skepticism. Hugo demonstrates in [[ws_7_workflows_multiagent_and_context_engineering]] that Crew AI, despite being a well-designed framework, failed to execute the expected number of tool calls -- median 4-5 out of 9 requested across 100 runs. He also discovered that Crew AI had installed LiteLLM under the hood without transparency, violating the principle that frameworks should not hide important implementation details.

Hugo's Llama Index demonstration in [[ws_1_foundations]] shows the opposite problem: a framework that works perfectly for the demo but hides critical information. The 5-line quickstart abstracts away the model, the prompt, and all retrieval internals, making it impossible to debug when things go wrong. This is the prototype-to-production trap that Stefan warns about: frameworks optimized for 0-to-1 become liabilities at 1-to-N.

Ivan Leo's approach in [[deep_research_agent_ivan_leo]] provides an alternative model: build from raw API calls to understand the mechanics, then adopt lightweight SDKs (like Pydantic AI) when the abstractions match your needs. His ~1,500-line deep research agent is built without heavy frameworks, demonstrating that complex agentic systems do not require them.

## The Grounding Framework

Stefan's "it's all just an API call" masterclass in [[ws_8_finetuning_and_production_ai]] provides the meta-framework for evaluating all frameworks. By understanding that every LLM interaction reduces to a system prompt, messages, tool schemas, and structured output definitions, you can assess any framework by asking what it does to each of these components. RAG populates context, MCP populates tools, guardrails validate context and responses, skills are progressive disclosure of context. This mental model lets you evaluate new tools without getting swept up in hype, because you can always ask: which part of the API call does this framework modify, and could I do that myself?

## Where Sources Agree

All sources agree that understanding the underlying API call is essential regardless of which framework you adopt. There is consensus that premature framework adoption leads to problems, that frameworks should be evaluated by whether they help with production maintenance (not just prototyping), and that provider lock-in is a real risk that should be mitigated. The principle of controlling the interface while hiding the implementation is accepted as sound engineering practice.

## Where Sources Disagree or Add Nuance

The disagreement is genuine and productive. William Horton's anti-framework stance conflicts with Stefan's more measured "evaluate by origin story" approach -- William would rather not use any wrapper, while Stefan acknowledges that the right framework can replace code you genuinely do not care about. Eric Ma's opinionated project templates represent yet another position: structure the project from the start with strong conventions, but keep the LLM interaction layer thin.

The volatility of the space adds a temporal dimension to the debate. Ivan Leo's advice to build from raw API calls might be essential today but unnecessary tomorrow as SDKs stabilize. Stefan's observation that Guardrails AI is "cute for a demo" but that you should just pull the open-source code you need reflects a pragmatic middle ground: use frameworks for learning, extract what you need for production. The pace of model improvement -- with models absorbing capabilities that frameworks previously provided -- means framework choices may need to be revisited more frequently than in traditional software engineering.

## Related Concepts

- [[the_api_call_mental_model]] -- Stefan's API call framework is the meta-tool for evaluating any framework by what it does to each component of the call
- [[proof_of_concept_purgatory]] -- Premature framework adoption is a direct path into purgatory; frameworks that hide internals prevent debugging
- [[observability_and_tracing]] -- OpenTelemetry compatibility is a key framework selection criterion; frameworks must not break observability
- [[production_ai_patterns]] -- The 1-to-N production maintenance perspective should drive framework selection more than the 0-to-1 prototyping perspective
- [[agents_vs_workflows]] -- Agent frameworks like Crew AI can hide failures in tool calling reliability

## Sources

- [[ws_1_foundations]] -- Demonstrates premature framework adoption with Llama Index's 5-line quickstart that hides critical internals
- [[ws_4_testing_and_observability]] -- The definitive framework debate: Stefan's evaluation criteria, William's anti-framework stance, Natalia's thin wrappers, and Stefan's reconciliation principle
- [[thinking_tools_eric_ma]] -- Opinionated project templates and LiteLLM for provider-agnostic routing as an alternative to heavy frameworks
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Crew AI failure to execute expected tool calls, demonstrating framework reliability concerns
- [[deep_research_agent_ivan_leo]] -- Building from raw API calls as an alternative to framework adoption, with provider SDKs as a lightweight option
- [[ws_8_finetuning_and_production_ai]] -- Stefan's "it's all just an API call" framework as the grounding mental model for evaluating all frameworks and buzzwords
