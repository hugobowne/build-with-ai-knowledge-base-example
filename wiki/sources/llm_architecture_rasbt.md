---
type: guest_talk
title: "What You Need to Know About LLM Architecture Developments in 2026"
date: 2026-03-23
speakers: [Sebastian Raschka, Hugo Bowne-Anderson]
topics: [LLM architecture, attention mechanisms, KV cache, hybrid architectures, Mamba, state space models, inference scaling, RLVR, reasoning models, multi-head latent attention, group query attention, sliding window attention, sparse attention, mixture of experts]
source_file: raw/llm_architecture_developments_2026_rasbt.md
word_count: ~17400
---

## Overview

A wide-ranging technical conversation with Sebastian Raschka -- LLM researcher, author of "Build LLMs from Scratch" and the upcoming "Build Reasoning Models from Scratch," and prolific educator. The discussion traces the evolution of LLM architectures from the GPT-2 era through the current frontier of hybrid architectures, with particular depth on attention mechanism innovations and inference scaling. Sebastian is referenced as a key resource in [[deep_research_agent_ivan_leo]] and [[ws_8_finetuning_and_production_ai]].

Sebastian walks through the key architectural developments of the past year: reinforcement learning with verifiable rewards (RLVR, popularized by DeepSeek R1), inference scaling techniques (longer reasoning chains, parallel sampling, sequential refinement, external judges), and the critical shift toward hybrid architectures. The hybrid trend -- replacing most transformer attention layers with linear-scaling alternatives like gated delta nets or Mamba-style layers while keeping some global attention -- is being adopted by Qwen 3.5, Nemotron 3 (Nvidia), and Kimi Linear, suggesting it may be the next standard.

The KV cache optimization trajectory is explained with exceptional clarity: from standard multi-head attention (quadratic cost), to grouped query attention (GQA, sharing keys/values across groups), to DeepSeek's multi-head latent attention (MLA, compressing KV through latent projections like LoRA), to various sparse attention schemes (sliding window, DeepSeek's learned sparse attention). Sebastian notes that while hybrid architectures should be faster at inference, current local inference stacks (llama.cpp) are not yet optimized for them, making them paradoxically slower on consumer hardware.

The conversation also covers the shift from pre-training to mid-training and post-training as the main source of capability gains, how reasoning traces in training data create a form of distillation, and predictions for DeepSeek's next release (likely process reward models for intermediate reasoning step verification).

## Key Topics

- Attention mechanism evolution: multi-head -> grouped query (GQA) -> multi-head latent (MLA) -> sparse attention
- KV cache optimization: the fundamental bottleneck for long-context inference
- Hybrid architectures: replacing most attention layers with linear alternatives (gated delta net, Mamba layers)
- State space models (Mamba) and their hybrids with transformers (Jamba, Samba, Qwen 3 Next)
- Inference scaling: longer reasoning chains, parallel sampling, sequential refinement, external judges
- RLVR (reinforcement learning with verifiable rewards): DeepSeek R1 and beyond
- Process reward models: checking intermediate reasoning steps, not just final answers
- Mid-training: training on longer context tasks and specific data subsets
- How reasoning traces in pre-training data create implicit distillation
- The quality-over-quantity shift in training data
- Routing and model selection: auto-mode, reasoning effort levels

## Key Insights

- Hybrid architectures (mixing attention with linear layers like gated delta nets) are the clearest new architectural trend: adopted by Qwen 3.5, Nemotron 3, Kimi Linear -- likely to become standard
- Multi-head latent attention (MLA, from DeepSeek) compresses KV cache through latent projections (like LoRA's down-up pattern) and is being widely adopted (Mistral, GLM5, Sarv) as a more capable alternative to grouped query attention
- Models learn faster from higher-quality data (reasoning traces, curated content) -- "it's almost like how we humans learn. If you give someone random internet data it's really time-consuming; a high-quality textbook teaches faster"
- Current local inference stacks are not yet optimized for hybrid architectures -- they should be faster but are paradoxically slower on consumer hardware (llama.cpp)
- The distinction between reasoning as prompting technique vs. trained behavior is blurry: base models can already produce reasoning traces because those traces are in their pre-training data (a form of distillation)
- DeepSeek's next model likely incorporates process reward models -- checking intermediate reasoning steps, which they attempted but noted didn't work in R1
- Inference scaling is fundamentally about choosing how much compute to spend per query, now exposed through auto-mode selectors and reasoning effort levels -- the practical implications of adjustable reasoning effort are explored in [[ws_2_prompting_and_context]]
- "Supervising agents which are self-supervising themselves" creates cognitive load that we haven't yet learned to manage well -- the conductor analogy for orchestrating AI. See [[ws_7_workflows_multiagent_and_context_engineering]] for multi-agent orchestration patterns and [[ws_6_building_ai_agents]] for the agency vs. supervision framework

## People & Tools Mentioned

- Sebastian Raschka -- LLM researcher, author of "Build LLMs from Scratch" and "Build Reasoning Models from Scratch" (Manning)
- DeepSeek -- R1, v3.2, sparse attention, multi-head latent attention, process reward models
- Qwen 3 / 3.5 -- adopted hybrid architecture with gated delta nets
- Qwen 3 Next -- experimental model replacing attention with hybrid layers
- Nemotron 3 (Nvidia) -- hybrid architecture with Mamba layers
- Kimi / Kimi Linear -- their own version of gated delta architectures
- Sarv (India) -- 105B model adopting MLA
- Mamba -- state space model, alternative to autoregressive transformer
- Jamba, Samba -- early transformer-Mamba hybrids
- GPT-o-SS -- open-weight model with selectable reasoning effort levels
- PinchBench -- benchmarking website for models in open claw context
- Andrej Karpathy -- referenced for skills-based teaching and agent debugging
- Eric Ma -- referenced as co-teacher of Bayesian inference tutorial at SciPy 2017 (see [[thinking_tools_eric_ma]] for Eric's guest talk on Canvas Chat and spec-driven development)
- Alan Downey, Stefan, Michael Chiao -- referenced from SciPy 2017

## Quotable Moments

- "Models learn faster when you have good quality data. If you give someone random internet data, it's really time-consuming. A high-quality textbook teaches faster. You only maybe need to read that one thing." -- Sebastian Raschka [~22:02]
- "You're watching an orchestra... and you're trying to kind of get everyone doing the thing you wanted to do and then it happens so quickly" -- Sebastian Raschka on supervising agents [~33:23]
- "If he can't get these LLMs or agents to do stuff in the short term, it's most likely a skills issue on his part now." -- Hugo quoting Karpathy [~33:47]
- "If you take a working LLM architecture as an anchor point... you can go in both directions: you can either plug them into an agent or look at what the model looks like under the hood." -- Sebastian Raschka [~13:33]
- "We had the luxury... there were not that many options so it was quite the quieter more reflective time for machine learning." -- Sebastian Raschka on 2016-17 era [~06:03]

## Highlights

- [~13:30] Sebastian's framework for staying current: take a working model release as anchor, then explore in both directions -- agent applications or architecture internals
- [~19:00] Chain-of-thought blurriness: the boundary between prompting technique and trained behavior is unclear because reasoning traces are already in pre-training data, creating implicit distillation
- [~22:00] Quality-over-quantity in training data: high-quality reasoning traces allow better models with less data, shifting compute budget to post-training
- [~27:00] Inference scaling deep dive: longer reasoning chains, parallel sampling (ensembles), sequential refinement, external judges -- each axis of scaling explained with DeepSeek Math v2 as case study
- [~33:00] "AI psychosis" discussion: the cognitive load of supervising self-supervising agents, Karpathy's framing that failures are likely operator skill issues
- [~44:00] KV cache optimization trajectory explained: multi-head attention -> GQA -> MLA (DeepSeek's latent compression) -> sparse attention, with clear explanation of why each innovation matters
- [~51:00] Hybrid architecture trend: Qwen 3.5, Nemotron 3, Kimi Linear all adopting linear layers (gated delta nets, Mamba) to replace most attention layers -- the clearest new architectural direction
- [~57:00] DeepSeek predictions: likely process reward models (checking intermediate reasoning steps) plus potentially hybrid architecture, though combining MLA + sparse attention + hybrid is complex

## Related Sources

- [[ai_products_google_ravin_kumar]] -- Ravin Kumar discusses the Gemma model family and context window evolution from the product side, complementing Sebastian's architectural perspective
- [[ws_8_finetuning_and_production_ai]] -- Sebastian's session on PEFT, LoRA, and QLoRA is referenced; the workshop fine-tunes Gemma 270M and discusses when fine-tuning is still relevant
- [[deep_research_agent_ivan_leo]] -- Ivan Leo references Sebastian's session and discusses model selection for agents, connecting architecture to practical agent building
- [[ws_2_prompting_and_context]] -- Covers adjustable reasoning effort in GPT-5.4 and chain-of-thought prompting, the practical user-facing side of the inference scaling Sebastian describes
- [[ws_5_context_engineering_and_information_retrieval]] -- The context window limitations and retrieval techniques discussed here build on the architectural understanding of attention and KV cache that Sebastian provides
- [[thinking_tools_eric_ma]] -- Eric Ma, referenced for their SciPy collaboration, presents on AI-assisted development and multi-model workflows
