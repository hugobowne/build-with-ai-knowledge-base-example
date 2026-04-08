---
type: guest_talk
title: "What I've Learned Building AI Products at Google"
date: 2026-03-19
speakers: [Ravin Kumar (Google DeepMind), Hugo Bowne-Anderson]
topics: [AI product development, Gemma models, Notebook LM, Gemini, developer tools, small models, on-device AI, context windows, retrieval, evaluation, UX design, abstraction layers]
source_file: raw/building_ai_products_at_google_ravin_kumar.md
word_count: ~12500
---

## Overview

A conversation with Ravin Kumar from Google DeepMind covering lessons learned from building AI products across the Google ecosystem -- including Notebook LM, Project Mariner, Gemma models, and Gemini. Ravin's current focus is on making Gemma models adaptable for diverse use cases: from the flagship 27B model down to the 270M "tiny" model, including specialized adaptations like Function Gemma (a local tool-calling router) and Dolphin Gemma (trained on dolphin communication data). Ravin also co-presented a fine-tuning livestream with Hugo, discussed further in [[ws_8_finetuning_and_production_ai]].

The discussion spans the full spectrum of AI product design: building for developers (HuggingFace, fine-tuning) versus consumers (Gemini app for "my mom"), how evaluation differs across these audiences, and the classic abstraction tradeoff between low-level control and ease of use. Ravin shares how he still reads all AI-generated code before committing, his personal stack (Anti-Gravity IDE with multiple models), and his philosophy of trying competing products to stay aware of the full ecosystem.

A substantial portion covers Notebook LM's evolution -- how retrieval internals changed as Gemini's context window grew from small to 1 million tokens, reducing the need for chunking. This connects directly to the retrieval and context engineering foundations covered in [[ws_5_context_engineering_and_information_retrieval]]. The conversation addresses practical questions about retrieval at scale, how to build products when the underlying models keep improving, and the timeless advice to "solve people's problems with whatever tools exist."

## Key Topics

- Gemma model family: 270M (tiny), 1B, 4B, 12B, 27B -- demand patterns and adaptation strategies
- Function Gemma: 270M model adapted for local tool-calling/routing -- relates to tool calling covered in [[ws_6_building_ai_agents]] and [[deep_research_agent_ivan_leo]]
- Dolphin Gemma: adapting language models for dolphin communication research
- Notebook LM: retrieval evolution as context windows expanded
- Building AI products for developers vs. consumers (different evals, UX, failure tolerances) -- see also [[next_level_evals_stella_eddie]] and [[ws_3_evals_and_feedback_loops]]
- How context windows growing from 8K to 1M changed retrieval architecture
- Stitch (Google Labs): new AI tool for UX/UI design
- Anti-Gravity IDE: multi-model support including Claude
- The abstraction spectrum: Python vs. C, Gemini App vs. AI Studio

## Key Insights

- Even a 270M parameter model had more demand than expected because people valued putting it in places where large models cannot go (phones, Raspberry Pi, persistent local processes) -- the fine-tuning of Gemma 270M is demonstrated hands-on in [[ws_8_finetuning_and_production_ai]]
- Both developers and consumers will churn from poor products -- developers just understand the failure modes better; they are not necessarily more forgiving
- As Gemini's context window grew to 1M tokens, much of Notebook LM's chunking infrastructure could be simplified or removed -- echoing how Python reduced need for manual memory management. See [[llm_architecture_rasbt]] for the architectural developments (KV cache, hybrid architectures) that enable these larger context windows
- The Gemini and Gemma teams at Google are not siloed -- people contribute across both, and lessons from one product feed into the other
- "Focus on a problem, not a tool" -- but also: the levels of abstraction are stacking up faster than ever, so the right depth depends on who you are and what you're building
- Best software engineering practices (unit tests, integration tests, reading code) still apply even when AI writes the code -- "your user still probably wants your app to work"

## People & Tools Mentioned

- Ravin Kumar -- Google DeepMind, worked on Notebook LM, Project Mariner, Gemma, Gemini
- StarCloud -- startup training models in space; happened to use both Falcon 9 (Ravin's SpaceX work) and Gemma
- Function Gemma -- 270M model fine-tuned for tool calling, demonstrated in prior workshop with Hugo
- Dolphin Gemma -- Gemma adaptation for dolphin communication research
- Notebook LM -- Google product for AI-assisted learning and research
- Stitch (Google Labs) -- new AI tool for UX/UI design
- Anti-Gravity -- Google IDE with multi-model support
- Gemini File Search -- Google's hosted retrieval system
- Nicholas Moy (DeepMind/ex-Windsurf) -- mentioned re: Anti-Gravity team
- Carol Willing -- CPython core developer, active in course community
- Pastor Stoll -- course builder in residence, uses Notebook LM for medical education

## Quotable Moments

- "I would be shocked one day if I saw my mom on a Hugging Face web page downloading models. As much as I love her, I would never assume that she would interact with an LLM through a HuggingFace transformers library." -- Ravin Kumar [~13:24]
- "Go talk to other people... think about what your problems are, go out in the world and see what challenges are... and then be aware of what modern tools exist. Just solve their problems. Just as we've been doing pre-AI, pre-MacBook, pre-computer." -- Ravin Kumar [~26:29]
- "I still read all the code as if I had wrote it before I put it into pull request." -- Ravin Kumar [~19:49]
- "Let your model spread its wings. Let it be free. Rip out the harness. See what's up." -- Hugo paraphrasing Nicholas Moy [~44:20]

## Highlights

- [~06:00] The full Gemma model family and surprising demand for tiny models -- 270M had more demand than expected, leading to Function Gemma for local tool calling
- [~09:50] Dolphin Gemma: adapting LLMs for dolphin communication research -- a striking example of how small adaptable models push boundaries of what's possible
- [~12:50] Building for developers vs. consumers: how failure modes and evaluation differ between a developer fine-tuning on HuggingFace and a consumer using Gemini app
- [~18:15] Anti-Gravity discussion: the bet on reading less code, future of development paradigms, comparison to Python's abstraction over C
- [~26:00] Timeless career advice: "the levels of abstraction are stacking up faster than ever" -- depth vs. breadth depends on who you are and what you're building
- [~34:00] Notebook LM's retrieval evolution: how growing context windows from small to 1M tokens progressively simplified the chunking and retrieval infrastructure
- [~39:00] Gemini File Search and the practical reality that anything under 100K tokens can just be thrown into context now, changing the economics of retrieval
- [~45:00] Flash vs. Pro strategy: the Pareto frontier of intelligence vs. latency/cost, from Waymo's millisecond decisions to deep research that can run for hours

## Related Sources

- [[llm_architecture_rasbt]] -- Sebastian Raschka covers the architectural developments (KV cache optimization, hybrid architectures, inference scaling) that underpin the Gemini and Gemma model families Ravin discusses
- [[ws_8_finetuning_and_production_ai]] -- Ravin co-presented a fine-tuning livestream with Hugo; the workshop fine-tunes Gemma 270M hands-on and discusses Dolphin Gemma
- [[ws_5_context_engineering_and_information_retrieval]] -- Ravin's discussion of Notebook LM's retrieval evolution connects directly to the retrieval foundations and context engineering patterns covered here
- [[builders_club_william_horton]] -- William Horton references Ravin's talk and Notebook LM; discusses building at the application layer vs. frontier labs
- [[deep_research_agent_ivan_leo]] -- Ivan Leo references Sebastian Raschka as a recent course guest; the deep research agent demonstrates the kind of agentic retrieval that could complement Notebook LM's approach
- [[ws_6_building_ai_agents]] -- Function Gemma's tool-calling capabilities connect to the function calling mechanics covered in the agents workshop
