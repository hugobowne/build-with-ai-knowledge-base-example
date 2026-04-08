---
type: person
name: "Sebastian Raschka"
role: "LLM Researcher / Author"
organization: "Independent (author of Build LLMs from Scratch)"
category: guest_speaker
---

## Appearances

- [[llm_architecture_rasbt]] — Guest speaker; delivered wide-ranging technical session on LLM architecture developments including attention mechanisms, KV cache optimization, hybrid architectures, inference scaling, and RLVR
- [[ws_2_prompting_and_context]] — Referenced as upcoming guest speaker
- [[ws_5_context_engineering_and_information_retrieval]] — Referenced for model internals session
- [[ws_8_finetuning_and_production_ai]] — Referenced for PEFT, LoRA, and QLoRA discussion
- [[deep_research_agent_ivan_leo]] — Referenced by [[ivan_leo]] as recent course guest on LLM internals
- [[thinking_tools_eric_ma]] — Referenced as co-teacher with [[eric_ma]] at SciPy 2017

## Key Contributions

- Provided the clearest explanation in the course of the KV cache optimization trajectory: multi-head attention to grouped query attention to multi-head latent attention (DeepSeek's MLA) to sparse attention
- Identified hybrid architectures (mixing attention with linear layers like gated delta nets) as the clearest new architectural trend, adopted by Qwen 3.5, Nemotron 3, and Kimi Linear
- Explained how reasoning traces in pre-training data create a form of implicit distillation, blurring the distinction between reasoning as prompting technique and trained behavior
- Offered the framework for staying current in AI: take a working model release as an anchor point, then explore in both directions -- agent applications or architecture internals

## Notable Quotes

- "Models learn faster when you have good quality data. If you give someone random internet data, it's really time-consuming. A high-quality textbook teaches faster." — [[llm_architecture_rasbt]]
- "You're watching an orchestra... and you're trying to kind of get everyone doing the thing you wanted to do and then it happens so quickly." — [[llm_architecture_rasbt]] (on supervising agents)
- "If you take a working LLM architecture as an anchor point... you can go in both directions: you can either plug them into an agent or look at what the model looks like under the hood." — [[llm_architecture_rasbt]]
