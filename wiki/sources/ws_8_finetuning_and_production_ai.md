---
type: workshop
title: "Workshop 8: Fine-Tuning and Production AI Applications"
date: 2025-04-02
speakers: [Hugo Bowne-Anderson, Stefan Krawczyk, Pastor Soto, Anonymized Student Y, Caleb Tutty, William Horton, Ilona Brinkmeier, Joey, Natalia Rodnova, Ryan Rodriguez, Michael Powers, Franklin]
topics: [fine-tuning, production AI, neural networks, backpropagation, LoRA, QLoRA, PEFT, Gemma 270M, PyTorch, Hugging Face, LLM as judge, distillation, production patterns, Hamilton, Apache Burr, veterinary transcription, restaurant voice agent, API call mental model, MCP, A2A, skills, progressive disclosure, cost management, observability, fallbacks, change management]
source_file: raw/_cleaned/WS-8.md
word_count: ~22103
---

## Overview

Workshop 8 is the final workshop of the course, split into two major parts: fine-tuning with Hugo and production AI patterns with Stefan Krawczyk. It builds on Stefan's testing and observability framework from [[ws_4_testing_and_observability]] and the agent/workflow patterns from [[ws_7_workflows_multiagent_and_context_engineering]]. Hugo covers when fine-tuning is still relevant (increasingly rare), the mechanics of how it works, and a hands-on Colab session fine-tuning Gemma 3 270M to classify American vs. Australian football teams. Stefan then presents two production case studies -- a veterinary transcription workflow with 60+ LLM calls and a restaurant voice ordering agent -- and distills everything into the fundamental insight that it's all just an API call.

Hugo's fine-tuning section opens by establishing that fine-tuning is less relevant than it was in 2023-2024, because longer contexts, better prompting, and improved retrieval tools now handle most use cases. He walks through the history: 2023-2024 (brittle models, short contexts, immature tools) to 2025 (powerful base models, longer contexts, better harnesses) to 2026 (all improving further). The remaining valid use cases are: small models on edge devices, distillation, improving performance on unique data (dolphin communication patterns), and adapting to specialized domains. The practical advice is emphatic: try prompting, retrieval, and agentic approaches first.

The hands-on portion fine-tunes Gemma 270M in Google Colab with a free T4 GPU. The base model scores 0% on the classification task (it can't even output the requested labels, let alone classify correctly), but after fine-tuning, it achieves 100% accuracy. Hugo also references a second notebook fine-tuning for alien NPC dialogue, where overfitting is actually desirable and an LLM-as-judge evaluator assesses whether outputs sound sufficiently extraterrestrial.

Stefan's production section is grounded in two real-world case studies. The first is a veterinary transcription system that grew to 60+ LLM calls in a DAG, running on AWS Lambda with Hamilton for graph orchestration, facing challenges around debugging context chains, parallelization, and provider fallbacks. The second is a restaurant voice ordering bot using FastAPI with Apache Burr for agent orchestration, speech-to-text/text-to-speech pipeline, and synthetic data generation for eval. Stefan's master class moment is his "it's all just an API call" framework, where he uses the LLM API structure (system prompt, messages, tools, structured output) to demystify every buzzword: RAG populates context, MCP populates tools, A2A is tool execution, guardrails protect context and validate responses, and skills are progressive disclosure of context.

The workshop concludes with Hugo's course recap, covering all eight workshops and the AI software development lifecycle.

## Key Topics

- When fine-tuning is (and isn't) relevant in 2025-2026
- Fine-tuning mechanics: backpropagation, SGD, hyperparameters (learning rate, epochs, batch size, optimizer, dropout)
- Software 2.0 (Karpathy): computation stored in neural network weights
- Hands-on fine-tuning Gemma 270M for classification (0% to 100% accuracy)
- LLM-as-judge for evaluating stylistic fine-tuning (alien NPC dialogue)
- Fine-tuning frameworks: Axolotl, Unsloth, TorchTune, TRL
- Distillation: training small models from large model outputs
- Production case study 1: veterinary transcription workflow (60+ LLM calls, Hamilton, AWS Lambda)
- Production case study 2: restaurant voice ordering agent (FastAPI, Apache Burr, speech pipeline)
- "It's all just an API call" -- grounding framework for understanding AI buzzwords
- MCP, A2A, and skills explained via the API call mental model
- Provider fallbacks and cost management in production
- Change management and observability trade-offs
- Course recap and AI software development lifecycle

## Key Insights

- Fine-tuning is increasingly a last resort. Better prompting (see [[ws_2_prompting_and_context]]), retrieval (see [[ws_5_context_engineering_and_information_retrieval]]), and agentic approaches (see [[ws_6_building_ai_agents]]) handle most use cases. The valid remaining cases are: small models on edge devices, unique data not in training corpora, and distillation for cost reduction.
- The practical cost of fine-tuning extends far beyond compute: maintaining fine-tuned models, re-fine-tuning when new base models release, and hiring/retaining people with PyTorch expertise are all expensive.
- Overfitting, usually a problem, can be desirable for fine-tuning specialized output styles (e.g., ensuring an NPC always speaks in alien dialect).
- Production LLM workflows can grow to 60+ LLM calls in a DAG, creating debugging challenges around understanding what context fed into which call. Graph frameworks like Hamilton make dependency chains visible.
- Voice agents still predominantly use a three-legged architecture (speech-to-text + LLM + text-to-speech) because latency of unified models isn't production-ready.
- Everything in AI engineering reduces to understanding the LLM API call: system prompt, messages (user/assistant/tool), tool schemas, and structured output definitions. Every buzzword (RAG from [[ws_5_context_engineering_and_information_retrieval]], MCP from [[builders_club_natalia_murat]], guardrails from [[katherine_jarmul_privacy]], skills) maps to specific parts of this call.
- Skills are "smart context engineering" -- progressive disclosure where the agent reads files to add to its context as needed. This pattern predates the term by years in fine-tuned context engineering.
- Cost of observability is a real production concern. Logs and traces aren't free, and margin management matters when you're essentially reselling API providers.
- Synthetic data was crucial for the restaurant voice agent: scraping real menus and having LLMs generate example dialogues for eval and prompt tuning.

## People & Tools Mentioned

- Stefan Krawczyk -- created Hamilton (Apache incubating) and Apache Burr; production AI expert
- Sebastian Rajka -- prior session on model internals (see [[llm_architecture_rasbt]]); discussed PEFT, LoRA, QLoRA
- Ravin Kumar (DeepMind) -- co-presented fine-tuning livestream with Hugo (see [[ai_products_google_ravin_kumar]]); worked on Dolphin Gemma and a fine-tune on a SpaceX rocket
- Zach Muller (Hugging Face) -- technical lead for Accelerate; built a local Bash assistant by distilling 14K examples from a 30B model into small Qwen
- William Horton (Maven Clinic) -- health agent discussion (see [[william_horton_maven_clinic]]); BAAs with providers; deterministic checks for model self-identification
- Charles Fry (Modal) -- fine-tuned Flux on 3 images of housemate's dog
- Charmaine -- Cohort 1 talk on building customer service agent with decision trees
- Karpathy -- Software 2.0 and Software 3.0 (English as programming language)
- Gemma 3 270M -- base model for fine-tuning exercise
- Dolphin Gemma -- fine-tune for studying dolphin communication, deployed in ocean
- Hamilton (Apache) -- Python DAG framework for LLM workflows
- Apache Burr -- agent orchestration framework
- Axolotl, Unsloth, TorchTune, TRL -- fine-tuning frameworks
- Modal -- $250 credits; Flux fine-tuning example
- Langfuse -- open-source observability (used in restaurant agent)

## Quotable Moments

- "The zen of watching the epochs roll on in." -- Hugo Bowne-Anderson on fine-tuning monitoring [~50:00]
- "Remember, everything we do in this course is really around an API call... a lot of people forget that fact, and part of it is all the vendors want to sell you something, so they make it sound more complex than it really is." -- Stefan Krawczyk [~95:00]
- "Fine-tuning is super cool, but it's often overkill." -- Hugo Bowne-Anderson [~25:00]
- "Ground your language as to what literally is actually happening in the API call. Then you'll get a better understanding of what these things are actually doing." -- Stefan Krawczyk [~100:00]
- "Skills is just a name for smart context engineering. People two years ago doing really fine-tuned context engineering would see this is an obvious pattern." -- Stefan Krawczyk [~110:00]

## Highlights

- [~10:00] Hugo shares a new interactive resource he built: an HTML-based navigator for the AI software development lifecycle, with all guest talks, blog posts, and videos organized by topic and filterable by type and duration. Work in progress, to be updated with wiki content.

- [~15:00] Critical discussion of when fine-tuning makes sense. Hugo walks through the 2023-2024 to 2025-2026 evolution, arguing that most fine-tuning use cases have been absorbed by better prompting and retrieval. The remaining valid cases: edge devices, unique data (dolphin communication), and distillation.

- [~25:00] Zach Muller's distillation example: generated 14,000 training examples for ~$5 from a 30B parameter model, distilled into a tiny Qwen model that translates natural language to bash commands locally on a laptop. Concrete demonstration that distillation can be cheap and practical.

- [~45:00] Live fine-tuning in Colab. Gemma 270M scores 0% on football team classification (can't even output the requested labels). After fine-tuning, it achieves 100%. The training loss and validation loss curves are shown and discussed. Second notebook on alien NPC dialogue shows overfitting being desirable for style enforcement.

- [~55:00] LLM-as-judge for evaluating alien dialogue fine-tuning. When you want to test that a model speaks "like an extraterrestrial," code checks won't work -- this is a perfect case for an LLM judge with clear evaluation criteria.

- [~65:00] Stefan's veterinary transcription case study. Started simple, grew to 60+ LLM calls in a DAG. Key pains: debugging which context fed into a bad extraction, parallelization for latency (turnaround needed in minutes), provider fallbacks when OpenAI went down, and iteration speed for product-market fit.

- [~85:00] Restaurant voice agent case study. Three-legged architecture (STT + LLM + TTS) because unified models aren't fast enough. Burr orchestrates an agent graph with intent classification routing to different states (find order item, update cart, checkout). Synthetic data from scraped menus was crucial for reliability.

- [~95:00] Stefan's "it's all just an API call" masterclass. He uses the API call structure to ground every buzzword: RAG = context population, MCP = tool schema population, A2A = tool execution between agents, guardrails = context validation + response validation, skills = progressive disclosure of context via tool results. Has audience members map buzzwords to API components in real time.

- [~110:00] Mike Powers explains skills as "meta-instructions that the harness uses to establish LLM calls with context" -- a loop around context where the skill instructs the agent what step to do next. Stefan confirms: it's progressive disclosure, where the agent reads files to incrementally add context.

- [~125:00] Hugo's comprehensive course recap covering all 8 workshops and the full AI software development lifecycle, from evaluation-driven development through APIs, prompting, evals, testing, context engineering, retrieval, agents, workflows, fine-tuning, and production patterns.

## Related Sources

- [[ai_products_google_ravin_kumar]] -- Ravin Kumar co-presented the fine-tuning livestream with Hugo; his discussion of Gemma models and Dolphin Gemma provides the product context for fine-tuning
- [[llm_architecture_rasbt]] -- Sebastian Raschka's session on model architecture, PEFT, LoRA, and QLoRA provides the theoretical foundations for the fine-tuning covered here
- [[ws_4_testing_and_observability]] -- Stefan Krawczyk's earlier workshop on testing and observability; the production patterns here extend that framework with real case studies
- [[ws_7_workflows_multiagent_and_context_engineering]] -- The workflow and multi-agent patterns that Stefan's production case studies implement in practice
- [[william_horton_maven_clinic]] -- William Horton's Maven Assistant is a production health agent that applies many of the patterns Stefan discusses (multi-agent, guardrails, model selection)
- [[builders_club_natalia_murat]] -- The MCP discussion that Stefan grounds in the "it's all just an API call" framework here
