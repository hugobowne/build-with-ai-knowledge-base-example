---
type: concept
title: "The API Call as the Atomic Unit"
related_concepts: [five_first_principles, context_engineering, tool_calling_and_function_calling, structured_output, guardrails, agent_harnesses]
---

## Overview

Stefan Krawczyk's unifying framework -- "it's all just an API call" -- provides the single most powerful tool for cutting through AI engineering hype. The insight is structural: everything in AI engineering reduces to understanding the components of an LLM API call. A call consists of a system prompt, a sequence of messages (user, assistant, tool), tool schemas, and structured output definitions. Every buzzword in the AI ecosystem maps to specific parts of this call, and understanding those mappings demystifies concepts that vendors deliberately make sound more complex than they are.

This framework first surfaces implicitly in [[ws_1_foundations]], where API calls are introduced as the first of five first principles for AI software development. Hugo describes the API call as the atomic unit with "knobs" like temperature and reasoning effort. But it is Stefan's masterclass in [[ws_8_finetuning_and_production_ai]] that fully develops the framework into a comprehensive mapping of industry terminology to API components. He has audience members actively map buzzwords to API structures in real time, grounding abstract concepts in concrete mechanics.

The framework's value is not just pedagogical -- it is a diagnostic tool. When Stefan says "ground your language as to what literally is actually happening in the API call," he is offering a method for evaluating claims, choosing tools, and debugging systems. If someone describes a product and you cannot map its functionality to specific parts of an API call, either you do not understand it or it is doing less than advertised. Natalia Rodnova's experience echoes this: after understanding the basics, RAG and MCP stop seeming complex and start seeming like obvious patterns ([[builders_club_natalia_murat]]).

## The Buzzword-to-API Mapping

Stefan's masterclass establishes explicit mappings between AI industry terminology and API call components ([[ws_8_finetuning_and_production_ai]]):

**RAG** populates the context -- it adds retrieved information to the messages that go into the API call. Whether that information comes from a vector database, BM25 search, or a knowledge graph, the end result is additional text in the messages array. Understanding this strips RAG of its mystique and makes it clear that retrieval quality matters because it determines what the model actually sees.

**MCP** (Model Context Protocol) populates the tools schema. When an MCP server connects, it provides tool definitions that get injected into the API call's tools parameter. Stefan's mapping makes it clear that MCP is a distribution protocol for tool schemas, not a new form of AI capability. Hugo's MCP tutorial in [[builders_club_natalia_murat]] reinforces this: MCP is "a protocol for letting LLMs access tools that other people have built," and its promise breaks down when you try to build something real.

**A2A** (Agent-to-Agent) is tool execution between agents. One agent calling another is structurally the same as an agent calling any tool -- it sends a request and receives a response that goes back into the messages.

**Guardrails** validate context (input guardrails) and validate responses (output guardrails). They operate on the data going into and coming out of the API call. Simple guardrails are regex or keyword checks on the messages; complex ones are additional LLM calls that evaluate the content.

**Skills** are progressive disclosure of context. The agent reads files that add information to its context as needed, rather than loading everything upfront. Mike Powers describes this as "meta-instructions that the harness uses to establish LLM calls with context" -- a loop around context where the skill instructs the agent what step to do next ([[ws_8_finetuning_and_production_ai]]).

## Grounding Through the API Call

The framework's diagnostic power comes from its universality. Stefan's veterinary transcription system -- 60+ LLM calls in a DAG -- can be understood as a graph of API calls, each with its own system prompt, messages, and tools ([[ws_8_finetuning_and_production_ai]]). Debugging becomes a question of inspecting what went into each call: what context was the model given? What tools were available? What structured output schema was it constrained to produce?

The per-LLM-call evaluation insight from [[ws_4_testing_and_observability]] follows directly from this framework. Stefan argues that you cannot just test the overall system -- you need evaluation datasets for each individual API call in your pipeline. This makes sense only when you think of each call as a distinct unit with distinct inputs that can be tested independently. The connection between observability and the API call model is also direct: "the only way that you can debug what happened is dependent on what you observe, because what you send to the LLM is context-dependent" ([[ws_4_testing_and_observability]]).

Hugo's introduction of the five first principles positions the API call as the foundation that all other principles build upon ([[ws_1_foundations]]). Non-determinism is a property of the API call's output. Logging and tracing capture the API call's inputs and outputs. Evaluation measures the API call's quality. Rapid iteration modifies what goes into the API call. The entire AI software development lifecycle, in this framing, is the practice of systematically improving API calls.

## From Mental Model to Engineering Practice

The API call framework translates directly into engineering decisions. When Stefan describes skills as "smart context engineering" and notes that "people two years ago doing really fine-tuned context engineering would see this is an obvious pattern" ([[ws_8_finetuning_and_production_ai]]), he is pointing to how the framework reveals that new terminology often describes established practices.

For framework selection, the mental model provides a clear evaluation criterion: does this framework help me control what goes into my API calls, or does it hide it? Stefan's framework selection criteria in [[ws_4_testing_and_observability]] -- evaluating by origin story, 0-to-1 vs. 1-to-N optimization, and whether the framework replaces code you do not care about -- all connect to the question of visibility into the API call. Frameworks that hide the prompt, like Llama Index's 5-line quickstart ([[ws_1_foundations]]), violate the principle that you must understand what you are sending.

The framework also resolves terminology debates. The [[ws_4_testing_and_observability]] discussion of whether "agent harness" is useful terminology or marketing jargon becomes clearer through the API call lens: a harness is whatever surrounds the API call -- the code that assembles the prompt, manages the tools, tracks state, and processes the response. Whether you call it a harness, a wrapper, or just "the rest of the code" is a naming choice, not a technical distinction.

## Where Sources Agree

All sources that engage with this framework agree on its clarifying power. Stefan's presentation is enthusiastically received, and Natalia's experience of RAG and MCP seeming simple once you understand the basics confirms the framework's pedagogical effectiveness. Hugo's five first principles are structurally compatible, with the API call as the foundation. There is consensus that vendors benefit from making things sound complex and that grounding terminology in API mechanics is an effective countermeasure.

## Where Sources Disagree or Add Nuance

The main tension is between the framework's reductive clarity and the genuine complexity of production systems. Stefan's 60+ call DAG can be described as "just API calls," but the emergent behavior of those calls in concert -- context dependencies, error propagation, latency chains -- is not captured by understanding any single call in isolation. The framework is excellent for understanding components but less helpful for understanding system dynamics.

William Horton's question in [[ws_4_testing_and_observability]] about whether context engineering is really different from prompt engineering touches on a deeper issue: if everything is just an API call, are the distinctions between concepts (RAG, MCP, skills, context engineering) merely organizational, or do they represent genuinely different engineering challenges? Stefan's framework says the former; practitioners wrestling with multi-agent systems might argue the latter.

## Related Concepts

- [[five_first_principles]] -- The API call is the first principle; the other four principles describe properties of and practices around the API call
- [[context_engineering]] -- The practice of building the machine that populates the API call's context, as distinct from hand-crafting individual prompts
- [[tool_calling_and_function_calling]] -- The tool schema component of the API call, which MCP populates and agents use for external interaction
- [[structured_output]] -- The output schema component of the API call that constrains what the model produces
- [[guardrails]] -- Input and output validation mapped to specific points in the API call flow
- [[agent_harnesses]] -- The surrounding code and infrastructure that assembles and processes API calls

## Sources

- [[ws_1_foundations]] -- API calls introduced as the first of five first principles, establishing the atomic unit concept
- [[ws_8_finetuning_and_production_ai]] -- Stefan's masterclass mapping every buzzword to API components, with real-time audience participation and production case studies grounding the framework
- [[ws_4_testing_and_observability]] -- Per-LLM-call evaluation, the observability-depends-on-what-you-send insight, and the agent harness terminology debate resolved through the API call lens
- [[builders_club_natalia_murat]] -- Natalia's experience of RAG and MCP seeming simple once you understand the basics, confirming the framework's clarifying power
