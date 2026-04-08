---
type: workshop
title: "Workshop 2: LLM APIs, Prompt Engineering, and Context Engineering"
date: March 2026
speakers: [Hugo Bowne-Anderson]
topics: [LLM APIs, prompt engineering, system prompts, context engineering, memory in AI systems, reasoning effort, structured outputs, model comparison, Gemini, GPT-5.4, Claude Sonnet 4.5, guardrails, sycophancy, coding agents]
source_file: raw/_cleaned/WS-2.md
word_count: ~20100
---

## Overview

Workshop 2 shifts from the conceptual foundations of [[ws_1_foundations]] into hands-on work with LLM APIs, effective prompt engineering, and the beginnings of context engineering. Hugo walks participants through directly pinging Gemini 2.5 Flash, GPT-5.4 (recently released), and Claude Sonnet 4.5, comparing their behavioral differences on identical prompts. A striking example shows how Gemini appropriately disclaims being an AI when asked about headaches, while GPT-5.4 fires off seven rapid questions without disclaiming, and different models handle medical queries with varying levels of caution.

The core instructional content covers 10 principles of effective prompting: defining roles, giving instructions, output constraints, providing context, using delimiters (to prevent prompt injection), few-shot examples, explicit rules, handling ambiguity, saying what not to do, and chain-of-thought (which Hugo nearly removed given adjustable reasoning effort in modern models). A concrete example demonstrates extracting JSON from customer messages for a ticketing system, showing delimiter use to prevent prompt injection and PII exclusion.

The workshop features significant audience discussion on prompt iteration counts. Nathan from Carvana shares that he did 600+ iterations for Fortune 500 public-facing car descriptions, while Thomas Vicky from PiMC Labs achieved production-quality synthetic surveys for Colgate in just 8 iterations. Caleb Tutty contributes experience from legal transcription ASR work showing chain-of-thought still helps even with reasoning models. The session also covers system prompts, context engineering for memory (since LLMs are stateless), and the beginnings of how to give AI systems persistent memory. Discussion of Drew Brunig's research on coding agent harnesses having thousands of tokens "fighting the weights" adds depth to the system prompt discussion.

## Key Topics

- Working directly with LLM APIs (Gemini, OpenAI, Anthropic)
- Model behavioral differences on identical prompts
- 10 principles of effective prompting
- System prompts vs. user prompts
- Delimiters for prompt injection prevention
- Adjustable reasoning effort (GPT-5.4)
- Chain-of-thought prompting in the age of reasoning models
- Context engineering and memory in AI systems
- Prompt iteration counts across use cases
- Medical disclaimers and model safety behaviors
- Timeline of AI capabilities from Nov 2022 to present

## Key Insights

- Prompt engineering is not dead despite claims to the contrary; it remains one of the most important levers, especially early in the AI SDLC
- Different models have radically different default behaviors (Gemini disclaims being AI for medical queries; GPT-5.4 asks rapid-fire questions without disclaiming)
- William Horton ended up writing regex to strip Gemini's persistent medical disclaimers because system prompting could not override deeply trained safety behaviors -- see [[william_horton_maven_clinic]] for the full context on building Maven's health agent and [[llm_architecture_rasbt]] for why post-training behaviors are so difficult to override
- Prompt iteration counts vary enormously by use case: 8 iterations for Colgate synthetic surveys vs. 600+ for Carvana's public-facing car descriptions
- Chain-of-thought may be less necessary now with adjustable reasoning effort, but Caleb reports it still produces different/better results even with high-effort reasoning for sequential tasks
- Most attendees (poll) iterate 3 times on a prompt before shipping, which Hugo considers about right for most cases
- LLMs are stateless -- all memory must be engineered by the developer through system prompts, conversation history, or external storage
- Drew Brunig's research shows coding harnesses have thousands to tens of thousands of tokens that "fight the weights" -- system prompts can conflict with model training
- Vibe checks (manual data review) can get you very far before formal eval suites are needed

## People & Tools Mentioned

- **Hugo Bowne-Anderson** -- instructor
- **Nathan (Carvana)** -- 600+ prompt iterations for Fortune 500 car descriptions, Carvana is one of the fastest-growing Fortune 500 companies
- **Thomas Vicky (PiMC Labs)** -- achieved production-quality synthetic surveys for Colgate in 8 iterations; preserving demographic distributions
- **Caleb Tutty** -- consultant in Jakarta, legal transcription ASR, experience with chain-of-thought
- **William Horton** -- staff AI/ML engineer at Maven Clinic, regex stripping of Gemini disclaimers
- **Natalia Rodnova** -- builder in residence, "after 50 iterations I'm just gonna give up"
- **Brad Morris** -- builder in residence, shared Drew Brunig's research
- **Anonymized Student X** -- audience participant, context engineering discussion
- **Anonymized Student Y** -- audience, prompted system prompt experimentation discussion
- **Drew Brunig** -- research on coding agent system prompts "fighting the weights"
- **Ravin Kumar** -- Google DeepMind, upcoming Q&A (see [[ai_products_google_ravin_kumar]]; worked on Notebook LM, Mariner, Gemma)
- **Sebastian Rajkar** -- upcoming guest speaker (see [[llm_architecture_rasbt]])
- **Gemini 2.5 Flash / GPT-5.4 / Claude Sonnet 4.5** -- models compared
- **Manus** -- mentioned for visual feedback loop in slide generation

## Quotable Moments

- "Prompt engineering is dead -- that's just so far from the truth." -- Hugo Bowne-Anderson [~35:00]
- "The last thing you want is 7 rapid-fire questions when you have a headache." -- Hugo Bowne-Anderson [~20:00]
- "After 50 iterations, I'm just gonna give up and try something else." -- Natalia Rodnova [~25:00]
- "This stuff's probably trained very deeply into the model, so it's very hard to override that with the instructions sometimes, so you might need to resort to more heavy-handed tactics." -- William Horton [~20:00]
- "These coding harnesses have thousands to tens of thousands of tokens that are essentially fighting the weights." -- Brad Morris referencing Drew Brunig [~80:00]

## Highlights

- [~05:00-10:00] Hugo presents a timeline of AI capabilities from November 2022 to present, showing the progression from prompt engineering and fine-tuning through chain-of-thought, function calling, RAG, JSON mode, reasoning models, MCP, agentic loops, multi-agent orchestration, context engineering, agent harnesses, and adjustable reasoning effort.

- [~15:00-25:00] Side-by-side comparison of Gemini, GPT-5.4, and Claude on the "I have a headache" prompt, revealing dramatically different safety/disclaimer behaviors. William Horton shares the real-world consequence: he had to write regex to strip Gemini disclaimers from his healthcare app because system prompting could not override them.

- [~25:00-35:00] Rich audience discussion on prompt iteration counts. Nathan from Carvana explains why 600+ iterations were warranted for public-facing content at a Fortune 500 company, contrasting with Thomas Vicky's 8-iteration success for Colgate synthetic surveys. Key insight: iteration count depends on risk profile and whether output is public-facing.

- [~35:00-40:00] The 10 principles of effective prompting laid out, including the surprising note that Hugo almost deleted chain-of-thought from the list given modern reasoning models. Caleb pushes back, sharing that explicit step-by-step instructions still change outputs "quite dramatically" even with reasoning enabled.

- [~75:00-80:00] Discussion of context engineering and memory, with Brad sharing Drew Brunig's research on system prompts "fighting the weights" in coding agents -- a concrete example of how prompt engineering and model training can conflict.

## Related Sources

- [[ws_1_foundations]] -- The foundational workshop that precedes this one, establishing the five first principles including API calls and non-determinism
- [[ws_5_context_engineering_and_information_retrieval]] -- Takes the context engineering concepts introduced here and develops them fully with retrieval techniques, embeddings, and RAG
- [[ws_3_evals_and_feedback_loops]] -- The next workshop, covering evaluation of the outputs produced by the prompting techniques taught here
- [[llm_architecture_rasbt]] -- Sebastian Raschka's session provides the architectural understanding of why reasoning effort, chain-of-thought, and model behaviors work as they do
- [[william_horton_maven_clinic]] -- William Horton's real-world experience with prompt engineering challenges (Gemini disclaimers, "beat-it-over-the-head prompting") in production healthcare AI
- [[ai_products_google_ravin_kumar]] -- Ravin Kumar's upcoming Q&A referenced in this workshop, covering AI product development at Google
