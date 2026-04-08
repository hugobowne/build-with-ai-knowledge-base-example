---
type: concept
title: "Fine-Tuning and Distillation"
related_concepts: [model_selection_and_tradeoffs, the_api_call_mental_model, prompt_engineering, llm_architecture_and_inference, annotation_and_data_labeling, production_ai_patterns]
---

## Overview

Fine-tuning -- adapting a pre-trained model's weights for a specific task -- has shifted from a common necessity in 2023-2024 to an increasingly last-resort technique in 2025-2026. As base models have grown more capable, context windows longer, and prompting and retrieval techniques more sophisticated, most use cases that previously required fine-tuning can now be handled with better prompts, retrieval-augmented generation, or agentic approaches. Yet fine-tuning retains a critical role in a narrowing set of scenarios, and distillation -- training small models from the outputs of larger ones -- has emerged as perhaps the most practical remaining application.

Hugo Bowne-Anderson traces this evolution explicitly in [[ws_8_finetuning_and_production_ai]]: in 2023-2024, models were brittle, context windows short, and tools immature, making fine-tuning essential for many tasks. By 2025-2026, powerful base models, longer contexts, and better harnesses have absorbed most of those use cases. The practical advice is emphatic: try prompting, retrieval, and agentic approaches first. The remaining valid cases cluster around three scenarios: deploying small models on edge devices where large models cannot run, working with genuinely unique data not present in training corpora, and distillation for cost reduction at scale.

Sebastian Raschka provides the technical foundations, covering parameter-efficient fine-tuning (PEFT), LoRA (Low-Rank Adaptation), and QLoRA (quantized LoRA), which dramatically reduce the compute needed for fine-tuning by training only a small subset of parameters ([[llm_architecture_rasbt]]). Ines Montani offers a different perspective entirely, arguing that LLMs should be used to build smaller, faster systems rather than being the production system themselves -- using LLMs to generate training data and write spaCy rules, then deploying the resulting lightweight models ([[natalia_ines_guest_workshop]]).

## When Fine-Tuning Still Makes Sense

The remaining valid use cases for fine-tuning reflect situations where prompting and retrieval fundamentally cannot solve the problem. Edge deployment is the clearest case: a 270M parameter model running on a Raspberry Pi or phone has no API to call and no context window to stuff ([[ai_products_google_ravin_kumar]]). Ravin Kumar describes how Google's Gemma 270M model had more demand than expected precisely because people needed models in places where large models cannot go. Function Gemma, a 270M model adapted for local tool-calling and routing, exemplifies this pattern.

Unique data that does not exist in training corpora is the second case. Dolphin Gemma, a fine-tune of Gemma deployed in the ocean to analyze dolphin communication patterns ([[ai_products_google_ravin_kumar]], [[ws_8_finetuning_and_production_ai]]), is the course's most striking example. No amount of prompting can teach a base model patterns it has never seen. Hugo's hands-on exercise in [[ws_8_finetuning_and_production_ai]] demonstrates this concretely: Gemma 270M scores 0% on a football team classification task before fine-tuning (it cannot even output the requested labels) and 100% on one run after fine-tuning (though a prior run yielded 98%, and Hugo explicitly flags possible overfitting).

Style enforcement is a surprising third case where overfitting -- normally a problem -- becomes desirable. When fine-tuning a model to generate alien NPC dialogue, you want the model to always speak in that style, making aggressive overfitting a feature rather than a bug ([[ws_8_finetuning_and_production_ai]]).

## Distillation as the Practical Sweet Spot

Distillation -- generating training examples from a large capable model and using them to train a smaller, cheaper model -- has emerged as the most cost-effective application of fine-tuning. Zach Muller's example is particularly compelling: he generated 14,000 training examples from a 30B parameter model for approximately $5, then distilled these into a tiny Qwen model that translates natural language to bash commands locally on a laptop ([[ws_8_finetuning_and_production_ai]]). The economics make distillation accessible to individual developers, not just well-funded teams.

Ines Montani's perspective from [[natalia_ines_guest_workshop]] frames this differently but arrives at the same conclusion: use LLMs for prototyping and cold-start, then invest in smaller trained models when you need speed, privacy, cost-effectiveness, or accuracy at scale. The S&P Global case study she presents shows production models trained on just 15 hours of single-annotator data, producing tiny 6MB models that replaced expensive API calls. The principle is the same as distillation: large models bootstrap the training data, small models serve the production traffic.

Lance Martin's observation that R1 reasoning traces can be distilled into smaller models for ReAct-style agent flows adds another dimension ([[william_horton_maven_clinic]]). This suggests that distillation can capture not just factual knowledge but reasoning patterns, potentially enabling cheaper models to exhibit behaviors previously restricted to frontier models.

## The Hidden Costs of Fine-Tuning

The practical cost of fine-tuning extends well beyond compute. Hugo emphasizes that maintaining fine-tuned models is expensive: when a new base model releases, you must re-fine-tune to take advantage of improvements, and hiring and retaining people with PyTorch expertise adds ongoing cost ([[ws_8_finetuning_and_production_ai]]). Sebastian Raschka adds that training data quality matters more than quantity -- higher-quality examples allow models to learn faster, but curating that quality is itself labor-intensive ([[llm_architecture_rasbt]]).

The tooling landscape for fine-tuning has matured considerably, with frameworks like Axolotl, Unsloth, TorchTune, and TRL reducing boilerplate. But the decision to fine-tune should account for the full lifecycle: initial training, evaluation, deployment, monitoring for degradation, and re-training as base models evolve. For many teams, this ongoing maintenance burden makes prompting and retrieval the pragmatic choice even when fine-tuning might yield marginally better results.

## Where Sources Agree

All sources agree that fine-tuning is less necessary than it was two years ago and should be the last approach tried, not the first. There is strong consensus that distillation is the most practical remaining application and that the cost of maintaining fine-tuned models is underappreciated. Sources also converge on the importance of data quality over quantity in training.

## Where Sources Disagree or Add Nuance

The sources offer genuinely different framings of what fine-tuning is for. Hugo and Sebastian approach it as model adaptation -- making a model better at a specific task ([[ws_8_finetuning_and_production_ai]], [[llm_architecture_rasbt]]). Ines Montani frames it as system design -- the goal is not to improve an LLM but to replace the LLM with something smaller and more controlled ([[natalia_ines_guest_workshop]]). Ravin Kumar adds the hardware perspective -- fine-tuning enables deployment in physical environments where API calls are impossible ([[ai_products_google_ravin_kumar]]).

There is also a tension around how soon fine-tuning becomes relevant in a project. Hugo's advice is emphatic about trying everything else first. But Ines's annotation-driven pipeline suggests that teams should be thinking about training data collection from the start, even if they begin with LLM-powered prototypes. The disagreement is less about whether to fine-tune and more about when to start preparing for it.

## Related Concepts

- [[model_selection_and_tradeoffs]] -- Fine-tuning is one strategy on the model selection spectrum, trading upfront effort for lower per-inference cost
- [[the_api_call_mental_model]] -- Fine-tuning changes what happens inside the model, while prompting and retrieval change what goes into the API call
- [[annotation_and_data_labeling]] -- Creating training data for fine-tuning requires the same annotation discipline as evaluation
- [[llm_architecture_and_inference]] -- LoRA, QLoRA, and PEFT techniques depend on architectural understanding of how model weights are organized
- [[prompt_engineering]] -- The primary alternative to fine-tuning; the tension between "fighting the weights" and adapting them

## Sources

- [[ws_8_finetuning_and_production_ai]] -- When fine-tuning makes sense, hands-on Gemma 270M fine-tuning, distillation economics, and the historical shift from necessity to last resort
- [[llm_architecture_rasbt]] -- PEFT, LoRA, QLoRA technical foundations, training data quality, and the architectural context for fine-tuning techniques
- [[ai_products_google_ravin_kumar]] -- Dolphin Gemma, Function Gemma, and the demand for small adaptable models that motivates fine-tuning on edge devices
- [[natalia_ines_guest_workshop]] -- Using LLMs to build smaller systems rather than being the system; annotation-driven training pipelines as an alternative framing of fine-tuning
