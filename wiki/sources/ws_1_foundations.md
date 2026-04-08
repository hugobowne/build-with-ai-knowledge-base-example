---
type: workshop
title: "Workshop 1: Foundations of the AI Software Development Lifecycle"
date: March 2026
speakers: [Hugo Bowne-Anderson, Stefan Krawczyk, Ben Shababo]
topics: [AI SDLC, proof-of-concept purgatory, evaluation-driven development, non-determinism, logging and tracing, Llama Index, Gradio, Modal, SQLite, Datasette, retrieval systems]
source_file: raw/_cleaned/WS-1.md
word_count: ~19900
---

## Overview

Workshop 1 opens the "Building AI Applications" course (Cohort 5) with Hugo Bowne-Anderson and Stefan Krawczyk introducing the foundational principles of the AI software development lifecycle (AI SDLC). Hugo frames the central problem as "proof-of-concept purgatory" -- the phenomenon where flashy AI demos generate enormous excitement but quickly degrade as teams encounter hallucinations, monitoring challenges, and integration issues. The workshops that follow build on these foundations: [[ws_2_prompting_and_context]], [[ws_3_evals_and_feedback_loops]], [[ws_4_testing_and_observability]], and beyond. The excitement curve for AI is inverted compared to traditional software: you get the wow moment first, then fall into difficulty.

The workshop establishes five first principles for AI software development: (1) API calls as the atomic unit (input/output with knobs like temperature and reasoning effort), (2) non-determinism as a fundamental property (the "double entropy problem" -- non-determinism in both outputs and user inputs), (3) logging, monitoring, and tracing from day zero, (4) evaluation as the backbone of improvement, and (5) rapid iteration through the build-deploy-monitor-evaluate cycle. Hugo emphasizes that AI systems are "organic" -- constantly shifting -- and require gardener-like attention.

The hands-on portion walks through building a retrieval app using Llama Index's 5-line quickstart, demonstrating both its power and its pitfalls as a framework that abstracts away things developers need to understand. They show the app with OpenAI, Claude, and Gemini backends, add a Gradio frontend, and introduce SQLite-based logging with Simon Willison's Datasette tool for trace visualization. The workshop concludes with a guest talk from Ben Shababo (ML Engineer at Modal) covering serverless compute, deploying Gradio apps on Modal, self-hosting LLMs with VLLM, and a voice-to-voice RAG bot architecture using PipeCat.

## Key Topics

- Proof-of-concept purgatory and how to escape it
- The AI software development lifecycle (build, deploy, monitor, evaluate, iterate)
- Five first principles: API calls, non-determinism, logging/tracing, evaluation, iteration
- The "double entropy problem" (non-determinism in both inputs and outputs)
- Premature framework adoption and abstracting away things you need to understand
- LLM sycophancy and model behavioral differences
- Logging with SQLite and viewing traces with Datasette
- Modal serverless compute, sandboxes, and deployment
- Voice AI architecture with PipeCat (speech-to-text, LLM, text-to-speech)
- Agent Developer Experience as an emerging role

## Key Insights

- AI flips the traditional software excitement curve: flashy demo first, then diminishing returns as you try to productionize
- You cannot test something that does not have a goal -- scoping to specific user pain points is essential before building
- Frameworks are wonderful, but premature adoption leads to purgatory; Llama Index's 5-line quickstart hides the model being used, the prompt, and all retrieval internals
- Non-determinism is not a bug to fix but a property to build systems around; in some cases (deep research agents), variance is actually a superpower -- see [[next_level_evals_stella_eddie]] where Stella argues non-determinism can be desirable for writing tools and deep research
- "F You, Show Me the Prompt" (Hamel Hussein) became necessary because frameworks hid prompts from developers
- From day zero, log everything -- you cannot evaluate what you cannot observe. See [[ws_4_testing_and_observability]] for the full observability discussion with OpenTelemetry
- The lion's share of AI utility still comes from strict, predefined workflows rather than fully autonomous agents
- When building for agents, developer experience design is its own emerging discipline (Modal's "Agent DX Researcher" role)

## People & Tools Mentioned

- **Hugo Bowne-Anderson** -- course instructor, background in biology/math/physics, podcaster (Vanishing Gradients, High Signal)
- **Stefan Krawczyk** -- co-instructor, Salesforce (agent graph efforts), creator of Apache Hamilton and Burr
- **Ben Shababo** -- ML Engineer / Forward Deployed Engineer at Modal, guest speaker
- **Michael Waskom** -- developer of Seaborn, working on Agent DX at Modal
- **Hamel Hussein** -- ML engineer, author of "F You, Show Me the Prompt"
- **Simon Willison** -- creator of Datasette
- **Tim O'Reilly** -- compared OpenAI/Anthropic to "AOL of AI" on Hugo's podcast
- **Wes McKinney** -- referenced regarding code reading
- **Llama Index** -- RAG framework (demonstrated as both useful and problematic when adopted prematurely)
- **Modal** -- serverless compute platform, course sponsor ($500 credits per student)
- **Gradio** -- rapid UI prototyping for AI apps
- **SQLite + Datasette** -- lightweight logging and trace visualization
- **VLLM / SGLANG** -- LLM serving frameworks
- **PipeCat** -- voice AI framework
- **Pydantic Logfire** -- observability for LLM apps (course sponsor)
- **Prodigy** -- human-in-the-loop annotation from Explosion AI (course sponsor)
- **Chroma Cloud** -- vector database (course sponsor)
- Builders in residence: Natalia Rodnova (see [[builders_club_natalia_murat]], [[natalia_ines_guest_workshop]]), Brad Morris (see [[builders_club_brad]]), Pastor Soto, William Horton (see [[builders_club_william_horton]], [[william_horton_maven_clinic]]), Carol Willing

## Quotable Moments

- "You can't test something that doesn't have a goal." -- Hugo Bowne-Anderson [~30:00]
- "You don't solve nondeterminism, you build systems around it that minimize risk." -- Hugo Bowne-Anderson [~50:00]
- "Not only do we not need to write code, we don't even need to read it. I'm joking, okay?" -- Hugo Bowne-Anderson [~00:00]
- "These days, when you're developing a software library or an API or an SDK, you're not just building it for humans anymore, you're building it for agents." -- Ben Shababo [~95:00]
- "I wouldn't be surprised if what's happening now will be an order of magnitude bigger than the advent of the internet." -- Hugo Bowne-Anderson [~65:00]

## Highlights

- [~28:00-35:00] The proof-of-concept purgatory concept explained in depth, with the inverted excitement curve for AI vs. traditional software. Hugo walks through a concrete RAG example where the system gives a nonsensical answer ("Hugo hired Yashes Roy") and shows why you cannot improve a system you cannot see into.

- [~44:00-50:00] The five first principles of AI software development laid out systematically. Notable discussion of temperature deprecation in GPT-5.x and its return, and the "double entropy problem" framing of non-determinism.

- [~55:00-65:00] Deep audience Q&A led by Anonymized Student Y's provocative question about when LLMs are "the bug, not the feature." Hugo's response includes the Tim O'Reilly "AOL of AI" comparison and a sweeping claim about AI potentially being an order of magnitude bigger than the internet. William Horton adds the Pets.com/Chewy analogy about being "too early."

- [~80:00-90:00] Live coding demo introducing SQLite logging and Datasette for trace visualization. Hugo demonstrates the progression from framework-obscured calls to transparent, logged interactions -- the practical heart of "getting out of purgatory."

- [~95:00-125:00] Ben Shababo's Modal guest talk covering serverless compute, the Gradio wrapper architecture, self-hosting LLMs with VLLM, and a full voice bot architecture (speech-to-text + LLM + text-to-speech on independent Modal services). Includes discussion of Modal's $500 credit code and the emerging "Agent DX" role.

## Related Sources

- [[ws_2_prompting_and_context]] -- The next workshop, building directly on these foundations with hands-on LLM API work, prompt engineering principles, and context engineering
- [[ws_3_evals_and_feedback_loops]] -- Deepens the evaluation principle introduced here into a full workshop on vibes, failure analysis, and automated evaluation
- [[ws_4_testing_and_observability]] -- Expands the logging/tracing principle into systematic testing with PyTest and observability with OpenTelemetry
- [[builders_club_brad]] -- Brad Morris leads a hands-on Modal deployment workshop, building on Ben Shababo's introduction here
- [[next_level_evals_stella_eddie]] -- Stella and Eddie provide the "next level" evaluation methodology that builds on the eval-driven development principle established here
- [[demo_day]] -- Students combine the foundations from this workshop with subsequent learning into working demo day projects
