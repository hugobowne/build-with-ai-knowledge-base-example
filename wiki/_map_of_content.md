# Map of Content

How to navigate the conceptual landscape of this knowledge base. Concepts are grouped by theme; each links to the full article.

---

## Foundations and Mental Models

The ideas introduced on day one and referenced in every session after.

- [[five_first_principles|Five First Principles]] -- API calls, non-determinism, logging/tracing, evaluation, rapid iteration. The backbone of the course.
- [[the_api_call_mental_model|The API Call as the Atomic Unit]] -- Stefan Krawczyk's framework: every buzzword maps to a part of the LLM API call (system prompt, messages, tools, structured output).
- [[ai_sdlc|The AI Software Development Lifecycle]] -- Build, deploy, monitor, evaluate, iterate. The two-loop model (development + production) and why AI systems are "organic."
- [[non_determinism|Non-Determinism in AI Systems]] -- The "double entropy problem" -- non-determinism in both inputs and outputs. A property to build around, not a bug to fix.
- [[proof_of_concept_purgatory|Proof-of-Concept Purgatory]] -- Why demos dazzle but degrade. The inverted excitement curve and how to escape with evaluation, observability, and problem-first thinking.

## Prompting, Context, and Retrieval

The spectrum from writing a prompt by hand to building a machine that assembles context automatically.

- [[prompt_engineering|Prompt Engineering]] -- 10 principles, iteration counts (8 to 600+), system vs. user prompts, "fighting the weights," meta-prompting.
- [[context_engineering|Context Engineering]] -- Building the machine that populates the prompt. Four strategies: write, select, compress, isolate. Skills as progressive disclosure of context.
- [[retrieval_augmented_generation|RAG and Information Retrieval]] -- BM25 baselines through embeddings and hybrid search. The "Gather and Glean" framework. Why long context windows do not replace RAG.
- [[structured_output|Structured Output and JSON Mode]] -- Constraining LLM responses to a schema. JSON mode vs. structured output (Pydantic). A building block for workflows, evals, and guardrails.

## Evaluation and Data Quality

Measuring whether things work. The single most referenced theme across all 21 sessions.

- [[evaluation_driven_development|Evaluation-Driven Development]] -- From vibes to spreadsheets to automated eval harnesses. Includes comparative evaluation (A/B, ELO tournaments).
- [[llm_as_judge|LLM-as-Judge]] -- Using LLMs to evaluate other LLM outputs. Calibrating against human labels. The 66% agreement ceiling. Paired classifier pattern.
- [[annotation_and_data_labeling|Annotation and Data Labeling]] -- Label scheme design, cognitive load reduction, model-assisted annotation, annotating alongside your SMEs.
- [[synthetic_data_and_simulation|Synthetic Data Generation and Conversation Simulation]] -- Distillation for training data, synthetic eval datasets, multi-turn conversation simulation with the "moderator" pattern.

## Agents, Tools, and Multi-Agent Systems

From augmented LLMs through structured workflows to fully autonomous agents.

- [[agents_vs_workflows|Agents vs. Workflows]] -- The critical distinction. Most production AI is workflows, not agents. The agentic spectrum. Workflow building blocks: gates, chains, routers, orchestrator-worker.
- [[coding_agents_as_general_purpose_agents|Coding Agents as General-Purpose Agents]] -- A 125-line Python agent with read/write/edit/bash can do anything a computer can do. Self-extension, hot-reload, the Pi agent.
- [[tool_calling_and_function_calling|Tool Calling and Function Calling]] -- How LLMs interact with external tools. The surprising complexity across providers. MCP as a distribution protocol.
- [[multi_agent_architecture|Multi-Agent Architecture]] -- Lead/orchestrator agents delegating to specialists. Conway's Law for agents. Latency penalties per delegation. Sub-agent context isolation.
- [[agent_harnesses|Agent Harnesses]] -- Tooling and state tracking surrounding an LLM. Models absorbing harnesses via RLVR. Whether "harness" is useful terminology or marketing.

## Production, Safety, and Operations

Getting from prototype to production and keeping systems running.

- [[production_ai_patterns|Production AI Patterns]] -- Two-loop model, progressive rollout, provider fallbacks, cost management, voice agent architecture (STT + LLM + TTS). Maintenance costs dominate.
- [[guardrails|Guardrails for AI Systems]] -- Three-layer taxonomy: deterministic (regex), algorithmic (classifier models), alignment (RLHF). Often simpler than expected.
- [[observability_and_tracing|Observability and Tracing]] -- OpenTelemetry as the standard. AI observability is useful from development, not just production. Privacy observability.
- [[human_in_the_loop|Human-in-the-Loop and Supervised AI]] -- Agency vs. supervision 2x2, progressive rollout, domain requirements where full automation is premature. 95% is embarrassing in radiology.
- [[privacy_and_security|Privacy and Security in AI Systems]] -- GDPR, HIPAA, pseudonymization, differential privacy, system prompt exfiltration, memorization attacks. Conversational data is more sensitive than clickstream data.

## Models, Architecture, and Training

Understanding model internals and when to change them.

- [[model_selection_and_tradeoffs|Model Selection and Trade-offs]] -- Pareto frontier from tiny (270M) through Flash-tier to frontier reasoning. Smart models for planning, cheaper for execution.
- [[llm_architecture_and_inference|LLM Architecture and Inference Scaling]] -- Attention evolution (MHA to MLA to sparse), KV cache optimization, hybrid architectures, inference scaling, RLVR.
- [[fine_tuning_and_distillation|Fine-Tuning and Distillation]] -- Increasingly a last resort. Valid cases: edge devices, unique data, cost reduction. LoRA, QLoRA. Overfitting can be desirable for style enforcement.

## Engineering Practice

How practitioners work day to day.

- [[framework_selection|Framework Selection and Build vs. Buy]] -- Evaluate frameworks by origin story and whether they optimize for 0-to-1 or 1-to-N. Control the interface, hide the implementation.
- [[vibe_coding_and_ai_assisted_development|Vibe Coding and AI-Assisted Development]] -- The spectrum from pure vibe coding to spec-driven development. Specs and tests as double constraints for coding agents.
- [[domain_specific_ai|Domain-Specific AI Applications]] -- How patterns vary across healthcare, legal, e-commerce. Acceptable error rates, regulatory requirements, and the demo-to-production gap.

---

See also: [[_index]] (master landing page) / [[_glossary]] (term definitions) / [[_source_registry]] (all sources)
