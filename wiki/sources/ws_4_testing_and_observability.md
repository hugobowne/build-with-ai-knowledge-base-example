---
type: workshop
title: "Workshop 4: Testing, Observability, and Production AI"
date: March 2026
speakers: [Stefan Krawczyk, Hugo Bowne-Anderson]
topics: [testing AI applications, CI/CD for AI, PyTest, PyTest Harvest, observability, tracing, OpenTelemetry, frameworks, guardrails, agent harnesses, development loops, production loops, prompt tuning, software development lifecycle]
source_file: raw/_cleaned/WS-4.md
word_count: ~20000
---

## Overview

Workshop 4 is led primarily by Stefan Krawczyk and focuses on the practical engineering side of AI development: testing, observability, debugging, and getting AI applications to production. It builds on the eval foundations from [[ws_3_evals_and_feedback_loops]] and connects to Stefan's production case studies in [[ws_8_finetuning_and_production_ai]]. Stefan introduces a two-loop mental model for AI development -- an inner development loop (local testing, prompt tuning) and an outer production loop (deployed app, logging, feedback into development). He emphasizes that you cannot "set and forget" AI applications: models get deprecated, distributions shift, and ongoing maintenance is the dominant cost.

The workshop opens with polls establishing that most participants expect their applications to make many LLM API calls, that optimizing a single prompt takes days (not hours), and that AI apps cannot be set-and-forget. Stefan then introduces PyTest as a framework for systematically testing LLM outputs, demonstrating how vanilla PyTest's first-assert-stops behavior is insufficient for LLM development where you want data on multiple dimensions simultaneously. He introduces PyTest Harvest as a plugin that collects results across all assertions, enabling spreadsheet-exportable evaluation data that connects directly to Workshop 3's annotation processes.

A significant portion covers OpenTelemetry as the industry standard for instrumentation, with strong advice to avoid tools not compatible with it. Stefan stresses that observability is useful from development (not just production), differentiating AI from traditional software engineering. The framework discussion becomes the workshop's most heated segment: Stefan argues frameworks should be evaluated by what they optimize for (0-to-1 vs. 1-to-N), their origin story, and whether they replace code you don't care about. Natalia advocates building thin custom wrappers; William argues passionately against internal frameworks, preferring the OpenAI SDK with a LiteLLM gateway. Stefan's reconciliation: control the interface, hide the implementation, allowing framework swaps. The guardrails section demystifies input/output guardrails as often simple regex or keyword checks, with LLM-based guardrails reserved for contextual checks where latency trade-offs are acceptable.

## Key Topics

- Two-loop model: inner development loop + outer production loop
- Continuous integration / continuous deployment (CI/CD) for AI
- PyTest for LLM output testing
- PyTest Harvest for collecting multi-dimensional eval data
- OpenTelemetry as the instrumentation standard
- Traces, logging, and debugging in AI systems
- Framework selection criteria (0-to-1 vs. 1-to-N optimization)
- Llama Index vs. Apache Burr as framework examples
- Building thin custom wrappers vs. using established frameworks
- Input and output guardrails (regex, keyword, LLM-based)
- Prompt injection prevention and groundedness checking
- Agent harnesses: definition, debate, and skepticism
- Maintenance costs vs. setup costs for AI applications

## Key Insights

- AI development has two distinct iteration loops: a local test-driven loop for prompt tuning and a production loop where deployed app telemetry feeds back into development
- Unlike traditional software, observability in AI is useful from the very first day of development, not just in production
- Per-LLM-call evaluation datasets may be needed -- you cannot just test the overall system, you need datasets for each individual LLM API call in your pipeline
- PyTest's default behavior (stopping at first assertion failure) is insufficient for LLM testing; PyTest Harvest lets you collect results across all assertions for richer evaluation data
- OpenTelemetry should be adopted from day one; it prevents vendor lock-in and has longer half-life than most tools in the space
- Frameworks should be evaluated by their origin story (what were the creators optimizing for?), whether they help with 0-to-1 or 1-to-N, and whether they replace code you do not care about
- Most frameworks that oversimplify things gear toward 0-to-1 but are liabilities for 1-to-N maintenance
- Guardrails are not complex: many are just regex or keyword checks; LLM-based guardrails add latency and should be reserved for contextual checks. See [[katherine_jarmul_privacy]] for a three-layer guardrail taxonomy and [[william_horton_maven_clinic]] for production guardrails in healthcare
- Fine-tuned small models are most successful for specific guardrail use cases, not general-purpose frontier models
- Agent harnesses may be "marketing jargon to sell to execs" (Stefan's cynical take) -- or they may be a useful term of art for describing tool sets, context management, and state tracking (Hugo's counter)
- The total cost of ownership for AI software is dominated by maintenance, just like traditional software, but coding agents may help automate some maintenance

## People & Tools Mentioned

- **Stefan Krawczyk** -- primary instructor, Salesforce, creator of Apache Hamilton and Burr
- **Hugo Bowne-Anderson** -- co-instructor, provides commentary and context
- **William Horton** -- strong opinions against internal frameworks, advocates OpenAI SDK + LiteLLM gateway pattern
- **Natalia Rodnova** -- prefers building thin custom wrappers, cites logging every cost as an advantage
- **Carol Willing** -- "good engineering is good engineering, you can name it My Pink Pony or the trapeze of the month"; draws parallels to established engineering principles
- **Anonymized Student Y** -- discusses maintenance costs being higher than setup, confirms planning-first approach with coding agents
- **Brad Morris** -- asks about Stefan's debugging workflow
- **Caleb Tutty** -- discusses model upgrade testing processes, still on GPT-5.1 in production
- **Shubh Fernandes** -- recent grad, Gen AI intern at Apexon, DataCamp follower
- **Nicholas Moy** -- built first multi-hop agent at Windsurf (acquired by Google DeepMind), cited for "ripping out harnesses to let models be free" (also mentioned in [[ai_products_google_ravin_kumar]] and [[deep_research_agent_ivan_leo]])
- **Swix** -- blog post on "agent lab thesis" (harnesses as defensible moats)
- **Samuel Colvin** -- Pydantic creator, cited for OpenTelemetry advocacy
- **PyTest** -- Python testing framework, demonstrated for LLM output testing
- **PyTest Harvest** -- plugin for collecting multi-dimensional test results
- **OpenTelemetry** -- industry standard for instrumentation and tracing
- **Apache Burr** -- Stefan's framework for agentic applications (checkpointing, state, observability)
- **Llama Index** -- contrasted with Burr as 0-to-1 focused
- **Langchain** -- characterized as "you don't know what you're doing, here's three lines of code"
- **Pydantic AI** -- ecosystem-based approach around Pydantic
- **FastAPI** -- cited as good 1-to-N framework example
- **LiteLLM** -- AI gateway for multi-provider routing (William's preferred approach)
- **Guardrails AI** -- Stefan's opinion: "out of sure if you want to share a cute demo" but just pull the open source code you need
- **Chroma Cloud** -- vector database, sponsor instructions shared

## Quotable Moments

- "If you really want to get your performance for your app really good, then you have to think of it on an LLM, per LLM call basis." -- Stefan Krawczyk [~15:00]
- "The only way that you can debug what happened is dependent on what you observe, because what you send to the LLM is context-dependent." -- Stefan Krawczyk [~20:00]
- "Langchain -- I want to say -- is like, you don't know what you're doing, here's three lines of code, magic." -- Stefan Krawczyk [~80:00]
- "Good engineering is good engineering, and you can name it anything you want, whether it's My Pink Pony, or the trapeze of the month, or whatever." -- Carol Willing [~110:00]
- "I honestly just want to pick up the OpenAI SDK. I don't want to use your wrapper." -- William Horton [~90:00]
- "People are ripping out their harnesses and simplifying them a huge amount... you rip out your harness to let your new model be free." -- Hugo Bowne-Anderson referencing Nicholas Moy [~105:00]
- "Agent harness -- to me, is marketing jargon that people use to sell to execs." -- Stefan Krawczyk [~110:00]

## Highlights

- [~05:00-15:00] Stefan's opening poll sequence establishes key intuitions: most participants expect many LLM calls per application, prompt optimization takes days not hours, and AI apps cannot be set-and-forget because models get deprecated (OpenAI deprecating models by end of year as concrete example). Sets up the entire rationale for systematic testing.

- [~20:00-35:00] The two-loop mental model (inner development + outer production) explained with CI/CD integration. Stefan walks through PyTest basics, then demonstrates the critical limitation of vanilla PyTest for LLM testing (stops at first assert), introducing PyTest Harvest as the solution for multi-dimensional evaluation data collection.

- [~70:00-80:00] OpenTelemetry deep dive with strong prescription: "Do your best in this space to avoid adopting tools that aren't compatible with OpenTelemetry." Hugo adds the longevity argument -- think about what will be around in 2, 5, and 10 years. Stefan discusses building custom debugging UIs with Claude Code to consume observability data.

- [~80:00-95:00] The framework debate becomes the session's most heated exchange. Stefan's framework selection criteria (origin story, 0-to-1 vs. 1-to-N, does it replace code you don't care about) are challenged by William's anti-internal-framework stance ("I just want the OpenAI SDK"), Natalia's thin-wrapper preference, and Carol's engineering fundamentalism. Stefan's reconciliation -- control the interface, hide the implementation -- is practical advice for threading the needle. [[thinking_tools_eric_ma]] covers Eric Ma's complementary perspective on opinionated project templates and provider-agnostic routing with LiteLLM.

- [~95:00-120:00] Guardrails demystified as often simple (regex, keyword checks), with LLM-based guardrails adding latency. The session then transitions into a spirited debate on terminology: is "agent harness" a useful term of art or marketing jargon? Stefan is cynical ("all it is, is a renaming of this interface concept"), while Hugo argues it usefully encapsulates tools, context management, and state tracking in five words. Carol's pragmatic take: "Lowering the cognitive load. Being very clear in what you're doing." William questions whether context engineering is really different from prompt engineering. The debate about whether models will subsume harnesses entirely is left open. See [[ws_5_context_engineering_and_information_retrieval]] for the full context engineering treatment and [[ws_8_finetuning_and_production_ai]] where Stefan grounds "skills" and "harnesses" in the API call mental model.

## Related Sources

- [[ws_3_evals_and_feedback_loops]] -- The preceding eval workshop that this session extends into systematic testing and observability
- [[ws_8_finetuning_and_production_ai]] -- Stefan returns with production case studies and the "it's all just an API call" framework that grounds the terminology debates from this session
- [[katherine_jarmul_privacy]] -- Katharine Jarmul's three-layer guardrail taxonomy (deterministic, algorithmic, alignment) complements the guardrail discussion here
- [[deep_research_agent_ivan_leo]] -- Ivan Leo's workshop uses OpenTelemetry/Logfire for agent observability, applying the principles advocated here
- [[thinking_tools_eric_ma]] -- Eric Ma's spec-driven development and Cypress testing feedback loops complement Stefan's inner/outer development loop model
- [[william_horton_maven_clinic]] -- William Horton's production healthcare guardrails (off-topic, prompt hacking, self-harm) demonstrate real-world application of the guardrail patterns discussed here
