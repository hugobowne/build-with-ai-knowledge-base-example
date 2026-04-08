---
type: concept
title: "LLM Architecture and Inference Scaling"
related_concepts: [model_selection_and_tradeoffs, non_determinism, fine_tuning_and_distillation, the_api_call_mental_model, context_engineering]
---

## Overview

The architectural developments underpinning modern LLMs shape everything downstream: how models behave, what they cost, how fast they respond, and why certain prompting strategies work. Sebastian Raschka's deep dive in [[llm_architecture_rasbt]] traces the evolution from the original multi-head attention mechanism through grouped query attention (GQA), DeepSeek's multi-head latent attention (MLA), and various sparse attention schemes. Each innovation targets the same fundamental bottleneck -- the KV cache, which grows with sequence length and makes long-context inference expensive. MLA compresses the KV cache through latent projections (a pattern reminiscent of LoRA's down-up architecture), and has been widely adopted by Mistral, GLM5, and Sarv.

The clearest new architectural direction is the hybrid approach: replacing most transformer attention layers with linear-scaling alternatives like gated delta nets or Mamba-style state space model layers while retaining some global attention layers. Qwen 3.5, Nvidia's Nemotron 3, and Kimi Linear have all adopted this pattern, suggesting it will become standard. However, as Raschka notes, current local inference stacks like llama.cpp are not yet optimized for these hybrids, making them paradoxically slower on consumer hardware despite their theoretical advantages.

Inference scaling -- the practice of spending more compute at inference time rather than training time -- has become a primary axis for improving model outputs. This encompasses longer reasoning chains, parallel sampling (running multiple attempts and selecting the best), sequential refinement, and external judges that verify intermediate steps. These techniques manifest in user-facing features like adjustable reasoning effort levels, explored in [[ws_2_prompting_and_context]], and connect directly to reinforcement learning with verifiable rewards (RLVR), which trains models on agent traces to improve agentic behavior.

## Attention Mechanisms and KV Cache Optimization

The trajectory of attention mechanism innovation follows a clear compression logic. Standard multi-head attention has quadratic cost in sequence length. Grouped query attention (GQA) shares keys and values across groups of attention heads, reducing the KV cache by a constant factor. DeepSeek's multi-head latent attention (MLA) goes further, compressing the KV representation through learned latent projections -- Raschka explains this as analogous to LoRA's pattern of projecting down to a low-rank space and back up ([[llm_architecture_rasbt]]). Sparse attention schemes, including sliding window attention and DeepSeek's learned sparse attention, add another dimension by attending to only a subset of positions.

These are not academic exercises. The KV cache is the practical bottleneck that determines how many concurrent users a deployment can serve and what context lengths are feasible. As Ravin Kumar describes in [[ai_products_google_ravin_kumar]], the growth of context windows from 8K to 1 million tokens progressively simplified Notebook LM's retrieval infrastructure -- but that growth was only possible because of these architectural innovations. The practical implications for builders are explored in [[ws_5_context_engineering_and_information_retrieval]], where Hugo demonstrates that latency scales quadratically with token length for attention-based transformers.

## Inference Scaling and Reasoning Models

Inference scaling represents a fundamental shift in where compute is spent. Rather than solely investing in larger pre-training runs, models now invest compute at inference time through longer reasoning chains. Raschka identifies four axes of inference scaling: longer chains of thought, parallel sampling (generating multiple candidate answers), sequential refinement (iterating on a single answer), and external judges that verify reasoning steps ([[llm_architecture_rasbt]]).

RLVR (reinforcement learning with verifiable rewards), popularized by DeepSeek R1, trains models to produce better reasoning traces by rewarding verifiable outputs. This has a cascading effect on the agent ecosystem: models trained on agent traces become better at agentic tasks, leading labs to "rip out their harnesses" with each new model release, as Hugo describes citing Nicholas Moy ([[ws_7_workflows_multiagent_and_context_engineering]]). The practical side surfaces in [[ws_2_prompting_and_context]], where GPT-5.4's adjustable reasoning effort lets developers trade compute for quality per query. Caleb Tutty reports that explicit chain-of-thought instructions still produce different results even with reasoning models, suggesting the boundary between prompting technique and trained behavior remains blurry -- as Raschka notes, base models already contain reasoning traces from their pre-training data, creating a form of implicit distillation.

## The Shift to Post-Training and Data Quality

A less visible but equally important trend is the shift in where capability gains originate. Pre-training on massive datasets was once the primary lever; now, mid-training (training on longer-context tasks and specific data subsets) and post-training (RLHF, RLVR, instruction tuning) contribute the dominant share of capability improvements. Raschka draws an analogy to human learning: "If you give someone random internet data, it's really time-consuming. A high-quality textbook teaches faster" ([[llm_architecture_rasbt]]). This quality-over-quantity shift in training data has practical implications for fine-tuning decisions, explored in [[ws_8_finetuning_and_production_ai]], where Hugo argues that better base models and post-training have made fine-tuning a last resort for most use cases.

Raschka predicts that DeepSeek's next release will incorporate process reward models -- checking intermediate reasoning steps rather than just final answers. This connects to the broader evaluation discussion: if models can be rewarded for correct intermediate steps, the same principle applies to how we evaluate agent workflows, where per-step evaluation is advocated by Stefan Krawczyk in [[ws_4_testing_and_observability]].

## Where Sources Agree

All sources converge on the practical importance of understanding architecture even for application builders. Raschka's framework -- take a working model as an anchor, then explore in both directions (applications or internals) -- is endorsed implicitly by Ivan Leo in [[deep_research_agent_ivan_leo]], who emphasizes starting with the best model to verify feasibility before optimizing. The sources uniformly recognize that inference scaling is now a first-class lever alongside model size, and that RLVR is the mechanism driving rapid improvements in agentic capabilities. There is broad agreement that context windows will continue to grow, but that retrieval remains necessary because performance degrades with contradicting or duplicate information even within large windows ([[ws_5_context_engineering_and_information_retrieval]]).

## Where Sources Disagree or Add Nuance

The most significant tension is between theoretical architectural advantages and practical deployment reality. Raschka notes that hybrid architectures should be faster but are paradoxically slower on current local inference stacks ([[llm_architecture_rasbt]]), while Ravin Kumar focuses on the product-level implication that anything under 100K tokens can now simply be thrown into context ([[ai_products_google_ravin_kumar]]). These are not contradictions but different vantage points: architecture researchers see the gap between theory and implementation, while product builders see the gap closing fast enough to simplify their systems.

On reasoning models specifically, there is a subtle disagreement about whether chain-of-thought is becoming obsolete. Hugo nearly removed chain-of-thought from his prompting principles given adjustable reasoning effort ([[ws_2_prompting_and_context]]), but Caleb Tutty pushed back with evidence that explicit step-by-step instructions still change outputs "quite dramatically" even with reasoning enabled. Raschka's explanation that reasoning traces are already embedded in pre-training data suggests the boundary will remain blurry rather than resolving cleanly.

Ivan Leo's pragmatic advice to "spend today for the models of tomorrow" ([[deep_research_agent_ivan_leo]]) contrasts with the architectural picture Raschka paints of a field still actively experimenting with fundamental building blocks. The tension is productive: builders should assume capabilities will improve, but architects know the path is neither linear nor guaranteed.

## Related Concepts

- [[model_selection_and_tradeoffs]] -- Architecture directly determines the cost, latency, and capability trade-offs that drive model selection
- [[non_determinism]] -- Temperature, sampling, and inference scaling all contribute to the non-determinism that builders must design around
- [[fine_tuning_and_distillation]] -- LoRA, QLoRA, and PEFT techniques are grounded in the same low-rank projection principles as MLA
- [[the_api_call_mental_model]] -- Architecture is invisible through the API, but understanding it explains why certain API behaviors exist
- [[context_engineering]] -- KV cache optimization and context window growth directly determine what context engineering strategies are feasible
- [[agents_vs_workflows]] -- RLVR-driven improvements in agentic capabilities are reshaping what agents can do without harness support

## Sources

- [[llm_architecture_rasbt]] -- The primary architectural deep dive covering attention evolution, KV cache optimization, hybrid architectures, RLVR, and inference scaling
- [[ws_2_prompting_and_context]] -- Covers the user-facing side of inference scaling: adjustable reasoning effort, chain-of-thought in the age of reasoning models, and model behavioral differences
- [[ai_products_google_ravin_kumar]] -- Provides the product perspective on architecture: the Gemma model family, context window evolution, and the Flash vs. Pro strategy on the Pareto frontier
- [[deep_research_agent_ivan_leo]] -- Connects architecture to agent building through model selection, caching strategies, and the "spend today for models of tomorrow" philosophy
- [[ws_8_finetuning_and_production_ai]] -- Covers Software 2.0 (computation stored in neural network weights), fine-tuning mechanics, and how architectural understanding grounds production decisions
