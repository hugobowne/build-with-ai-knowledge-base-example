---
type: concept
title: "Structured Output and JSON Mode"
related_concepts: [the_api_call_mental_model, evaluation_driven_development, agents_vs_workflows, guardrails, tool_calling_and_function_calling]
---

## Overview

Structured output -- constraining LLM responses to conform to a predefined schema -- is a foundational building block that bridges multiple concerns in AI engineering: evaluation (is the output valid and parseable?), workflow design (structured output as an intermediate representation between pipeline stages), guardrails (many guardrails are themselves structured output classifiers), and tool calling (function calls are a form of structured output). The concept encompasses two related but distinct capabilities: JSON mode, which guarantees the output is valid JSON, and structured output with schema enforcement, which guarantees the output conforms to a specific schema defined via Pydantic or equivalent tools.

The distinction between these two capabilities matters in practice. Hugo traces the timeline in [[ws_2_prompting_and_context]]: JSON mode came first, ensuring syntactically valid JSON but not schema compliance; structured output followed, enabling developers to specify exact field names, types, and validation rules. Stefan Krawczyk maps structured output as a core component of the API call anatomy in [[ws_8_finetuning_and_production_ai]], where the structured output definition sits alongside system prompt, messages, and tool schemas as one of the fundamental "knobs" of the LLM API call. This positioning makes structured output not just a convenience feature but a load-bearing part of the [[the_api_call_mental_model]] that grounds everything else.

Structured output appears in practice across nearly every production pattern in the course. William Horton's Maven Assistant uses structured output for guardrail classifiers, LLM-as-judge evaluators, and tool call responses ([[william_horton_maven_clinic]]). The LinkedIn-to-email workflow in [[ws_6_building_ai_agents]] and [[ws_7_workflows_multiagent_and_context_engineering]] uses structured output as the first step -- extracting structured data from a LinkedIn profile before generating personalized outreach. The parallelization trick described in [[ws_7_workflows_multiagent_and_context_engineering]] runs multiple structured extractions in parallel and aggregates results, achieving higher accuracy than a single call.

## Structured Output as Workflow Gate

One of the most powerful applications of structured output is as a gate mechanism in LLM workflows. In [[ws_7_workflows_multiagent_and_context_engineering]], Hugo and the Anthropic workflow patterns demonstrate how structured output enables deterministic branching: an LLM produces a structured classification (e.g., "intent: appointment" or "intent: health_question"), and downstream code routes to different processing paths based on that classification. This pattern -- structured output plus if-else logic -- is the fundamental building block of what the course calls "workflows" as distinct from "agents" ([[agents_vs_workflows]]).

Stefan Krawczyk's veterinary transcription system in [[ws_8_finetuning_and_production_ai]] illustrates this at scale: a DAG of 60+ LLM calls where each call's structured output feeds as input to subsequent calls, with routing decisions based on extracted fields. The intermediate representations between pipeline stages are all structured, making the system debuggable (you can inspect what each call produced) and testable (you can evaluate each extraction independently). This connects directly to Stefan's argument in [[ws_4_testing_and_observability]] that per-LLM-call evaluation datasets are necessary -- structured output makes per-call evaluation possible by giving you a schema to validate against.

William Horton's Maven Assistant implements this same pattern in production: a lead agent uses structured output to classify incoming queries and route them to specialized sub-agents for appointments, health questions, provider search, or FAQ retrieval ([[william_horton_maven_clinic]]). The structured output is both the routing mechanism and the first point of evaluation -- if the classification is wrong, everything downstream fails.

## Structured Output for Evaluation and Guardrails

Structured output is the mechanism that makes many evaluation and guardrail patterns possible. When William Horton builds LLM-as-judge evaluators for Maven, the judges produce structured verdicts -- not free-text opinions but schema-compliant assessments with specific fields for clinical accuracy, completeness, and Maven-specific self-awareness ([[william_horton_maven_clinic]]). This structured format makes judge outputs programmatically consumable: you can aggregate scores, track trends, and trigger alerts automatically.

Similarly, guardrails frequently use structured output internally. Stefan demonstrates in [[ws_4_testing_and_observability]] that contextual guardrails -- those that require understanding the semantic content of a message, not just regex matching -- work by having an LLM produce a structured classification (e.g., "is_off_topic: true/false, is_prompt_injection: true/false") that feeds into deterministic control flow. The guardrail itself is an LLM call with structured output. This is why Hugo emphasizes in [[ws_1_foundations]] that structured output is a core component of the API call anatomy: it is not an add-on feature but a fundamental mechanism that enables other patterns.

The evaluation connection runs deeper. In [[ws_3_evals_and_feedback_loops]], Hugo emphasizes that code-based checks should handle everything they can before resorting to LLM judges. Structured output makes many code-based checks possible that would otherwise require LLM evaluation: did the output include the required fields? Are the values within expected ranges? Does the classification match one of the valid categories? These checks are cheaper, faster, and more reliable than LLM-based evaluation.

## The Parallelization Pattern

An advanced application of structured output is the parallelization trick for higher accuracy. In [[ws_7_workflows_multiagent_and_context_engineering]], Hugo describes running multiple structured extractions in parallel on the same input and aggregating the results -- essentially an ensemble approach applied to structured extraction. If three parallel calls extract different structured representations from a LinkedIn profile, a simple majority vote or union operation can produce a more accurate result than any single call.

Carol Willing's practice of having three different LLMs audit code files in parallel ([[ws_7_workflows_multiagent_and_context_engineering]]) is a variant of this pattern, connected by Hugo to Karpathy's LLM Council concept. The feasibility of this pattern depends entirely on structured output: you can only aggregate and compare results programmatically when they conform to a shared schema. Free-text outputs from multiple models would require another LLM call to reconcile, negating much of the benefit.

## Where Sources Agree

All sources treat structured output as a fundamental capability rather than a convenience feature. Stefan's API call framework ([[ws_8_finetuning_and_production_ai]]) positions it as a first-class component alongside system prompts and tools. Hugo's workflow patterns ([[ws_7_workflows_multiagent_and_context_engineering]]) depend on it for routing and gating. William Horton's production system ([[william_horton_maven_clinic]]) uses it pervasively for guardrails, judges, and inter-agent communication. There is consensus that structured output transformed LLM applications from text-in-text-out systems to components that can participate in typed, validated data pipelines.

The sources also agree that the JSON mode vs. structured output distinction is practically important. JSON mode alone is insufficient for production systems because it does not guarantee schema compliance -- you can get valid JSON that is missing required fields or has unexpected types. The evolution from JSON mode to full structured output (with Pydantic schema enforcement) is treated as one of the key capability milestones in the timeline Hugo presents in [[ws_2_prompting_and_context]].

## Where Sources Disagree or Add Nuance

The primary nuance concerns how tightly to couple system design to structured output. Stefan's approach in [[ws_8_finetuning_and_production_ai]] treats structured output as a design-time contract -- you define schemas upfront and build your system around them. Ivan Leo's approach in [[deep_research_agent_ivan_leo]] is more dynamic, using tool calling (itself a form of structured output) with schemas that the agent can modify or extend at runtime. The tension is between the reliability of static schemas and the flexibility of dynamic ones.

There is also a subtle question about what to do when models fail to conform to structured output schemas despite schema enforcement. William Horton's experience with Gemini 2.5 Flash being worse at tool calling (a structured output task) than newer models ([[william_horton_maven_clinic]]) suggests that schema enforcement is not a guarantee but a strong constraint that models can still struggle with, especially on complex nested schemas or when the requested structure conflicts with the model's trained behaviors. The practical implication is that structured output validation should still be treated as a potential failure point, not an absolute guarantee.

## Related Concepts

- [[the_api_call_mental_model]] -- Structured output is one of the fundamental components of the API call anatomy
- [[agents_vs_workflows]] -- Structured output as gate mechanism is the building block that distinguishes workflows from free-form agent behavior
- [[evaluation_driven_development]] -- Structured output enables code-based checks and makes LLM-as-judge outputs programmatically consumable
- [[guardrails]] -- Many guardrails are structured output classifiers; the pattern is structured output + deterministic logic
- [[tool_calling_and_function_calling]] -- Tool calls are a specialized form of structured output; the two capabilities share the same underlying mechanism

## Sources

- [[ws_1_foundations]] -- Introduces structured output as a core component of API call anatomy
- [[ws_2_prompting_and_context]] -- Traces the timeline from JSON mode to structured output with schema enforcement
- [[ws_6_building_ai_agents]] -- Demonstrates structured output as the first step in the LinkedIn-to-email workflow
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Structured output as gate mechanism in workflows and the parallelization trick for higher accuracy
- [[ws_8_finetuning_and_production_ai]] -- Stefan maps structured output as an API call component; the veterinary transcription DAG uses it throughout
- [[william_horton_maven_clinic]] -- Production use of structured output for guardrails, LLM-as-judge evaluators, and inter-agent routing
- [[ws_4_testing_and_observability]] -- Contextual guardrails via structured output; per-LLM-call evaluation enabled by structured schemas
