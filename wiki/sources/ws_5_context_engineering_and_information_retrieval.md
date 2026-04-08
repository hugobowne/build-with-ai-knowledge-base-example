---
type: workshop
title: "Workshop 5: Context Engineering and Information Retrieval"
date: 2025-03-19
speakers: [Hugo Bowne-Anderson, Pastor Soto, William Horton, Carol Willing, Piyush Shah, Franklin, Anonymized Student X, Natalia Rodnova, Caleb Tutty, Brad W Morris]
topics: [context engineering, information retrieval, RAG, embeddings, vector databases, bag of words, TF-IDF, Word2Vec, BM25, hybrid search, ChromaDB, retrieval evaluation, agentic retrieval, search agents, EXA, Pydantic Logfire]
source_file: raw/_cleaned/WS-5.md
word_count: ~20578
---

## Overview

Workshop 5 covers the foundations of context engineering and information retrieval for LLM applications, extending the context engineering concepts introduced in [[ws_2_prompting_and_context]]. Hugo begins by explaining why LLMs need external context -- they are trained on fixed datasets and cannot know everything, so context supplements them with domain-specific, proprietary, or time-sensitive knowledge. The workshop distinguishes between prompt engineering (what a human writes) and context engineering (building the machine that populates the prompt).

The session provides a historical tour of retrieval techniques: bag of words, TF-IDF, Word2Vec, and transformer-based embeddings (Modern BERT). Hugo emphasizes that too many people focus solely on embeddings when coding agents do a lot of grep and keyword search successfully, and advocates for BM25 as a baseline with hybrid search approaches. The workshop includes hands-on coding in a GitHub Codespace, demonstrating bag of words, TF-IDF, Word2Vec, and sentence-transformer embeddings on the AG News dataset, building up to a full RAG system using GPT-2, NumPy arrays, and ChromaDB.

A significant portion addresses retrieval evaluation: precision at K, recall at K, hit rate, and NDCG. Hugo introduces Jeff Huber's "Gather and Glean" framework -- first prioritize recall to get all potentially relevant chunks, then re-rank with precision. The workshop demonstrates Chroma's generative benchmarking approach for creating gold evaluation datasets, showing dramatically better results (90-95% NDCG) on a well-curated course Q&A document versus Chroma's own documentation (70-76% NDCG).

For those who stayed after the official session, Hugo builds a search agent from scratch: pinging an LLM, adding an EXA web search tool, building the agentic loop, and adding a conversational loop -- all instrumented with Pydantic Logfire for observability.

## Key Topics

- Why LLMs need external context (knowledge gaps, grounding, explainability)
- Context engineering vs. prompt engineering
- Historical retrieval methods: bag of words, TF-IDF, Word2Vec
- Modern BERT and sentence transformers for embeddings
- BM25 as a retrieval baseline; hybrid search
- Building a RAG system from scratch (GPT-2 + NumPy + ChromaDB)
- Retrieval evaluation metrics: precision@K, recall@K, hit rate, NDCG
- Jeff Huber's "Gather and Glean" framework
- Synthetic gold dataset generation for retrieval evaluation
- Context window limitations (needle-in-a-haystack vs. real-world queries)
- Agentic retrieval and search agents with EXA
- Pydantic Logfire for observability and tracing

## Key Insights

- Context engineering is about building the machine that populates the prompt, not just writing the prompt yourself.
- Too many people focus exclusively on embeddings for retrieval; coding agents successfully use grep and keyword search. BM25 should be a baseline before moving to vector search.
- Long context windows are not a replacement for RAG. Gemini demonstrated near-perfect needle-in-a-haystack recall at 1M tokens, but performance degrades sharply with duplicate information, contradicting information, or multi-needle queries. See [[ai_products_google_ravin_kumar]] for how Notebook LM's retrieval evolved as context windows grew and [[llm_architecture_rasbt]] for the KV cache optimizations enabling longer contexts.
- A well-curated, high-signal document dramatically improves retrieval quality. The course's curated 97 Q&A pairs achieved 90-95% NDCG vs. 70-76% for less curated docs.
- Latency scales quadratically with token length for attention-based transformers, though generation latency can dominate in shorter regimes.
- Start with NumPy arrays for embeddings; move to vector databases only when things get slow or don't fit in memory.
- The recall-first strategy (Gather and Glean) is the right approach for most retrieval systems: get everything potentially relevant, then re-rank.
- Agentic retrieval -- putting the LLM in a loop with search tools -- is more capable than single-pass RAG for multi-step queries. See [[search_agents_john_doug]] for wrapping BM25 with agentic intelligence and [[deep_research_agent_ivan_leo]] for a full deep research agent with sub-agents.

## People & Tools Mentioned

- Sebastian Rajka -- guest speaker from prior session on model internals (see [[llm_architecture_rasbt]])
- Jeff Huber (Chroma CEO) -- "Gather and Glean" framework, context throughput blog post
- Jason Liu (Instructor) -- "6 types of RAG evals" blog post
- Doug Turnbull and John Berryman -- upcoming search agents workshop (see [[search_agents_john_doug]]); Doug led search at Shopify and Reddit, John was early engineer on GitHub Copilot
- Ivan Leo -- upcoming deep research agent workshop (see [[deep_research_agent_ivan_leo]]); formerly at Manus, joining Google DeepMind
- Mike Powers -- built top 100 Q&A distillation from course transcripts
- Konrad -- student who built a private knowledge base with Gemini File Search + Modal + Gradio in under an hour
- Matt Honnable (spaCy) -- "How many labelled examples to beat GPT-4" talk
- Lance Martin (Anthropic, formerly Langchain) -- context engineering patterns
- Karpathy -- context engineering quote: "the delicate art and science of filling the context window"
- ChromaDB -- vector database, $250 credits for students
- Modern BERT -- 4.5M downloads/month, up from 800K when course was last taught
- Sentence Transformers (all-MiniLM-L6-V2) -- 200M+ downloads/month
- Pydantic Logfire -- observability tool, $500 credits for students
- EXA -- web search API for agentic search

## Quotable Moments

- "Context engineering is far more about building the machine that then populates the prompt. We're starting to build the machine, to automate these things." -- Hugo Bowne-Anderson [~15:00]
- "One stop until BM25 is a baseline for RAG." -- Eugene Yang (Amazon), cited by Hugo [~20:00]
- "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." -- Andrej Karpathy, cited by Hugo [~45:00]
- "Gemini 2.5 Flash is fast but relatively dumb." -- William Horton [~40:00]
- "Agent is model plus tools within a for loop, or a while loop, plus some environment where it's operating." -- Eugene Yang, cited by Hugo [~115:00]

## Highlights

- [~10:00] Hugo introduces the distinction between prompt engineering and context engineering, explaining that context engineering is about building the machine that populates the prompt, not just writing human prompts. This framing sets up the rest of the course's direction.

- [~20:00] Strong argument against the embeddings-only mindset: coding agents use grep and keyword search effectively, BM25 should be a baseline, and hybrid search outperforms either alone. Cites Jason Liu's blog post showing 85% recall with hybrid search out of the box.

- [~45:00] Critical discussion of context window limitations. Despite Gemini claiming near-perfect recall at 1M tokens, Chroma's technical report showed serious performance drop-off with duplicate words, contradicting information, or even simple repeated patterns. This is a key counterargument to "RAG is dead."

- [~65:00] Rich audience Q&A about memory in RAG systems. Franklin asks about adding memory via vector databases for LLM responses. Hugo, William, and Franklin have a nuanced exchange about the progression: put it in context first, then text files, then vector databases -- only adding complexity when needed.

- [~70:00] Natalia shares her Word2Vec visualization from radiology reports, showing semantic clusters of medical terms that emerged naturally, including an unexpected cluster of patient occupations (firefighter in a radiology report). This grounds the embedding discussion in real clinical work.

- [~100:00] Dramatic comparison of retrieval quality: Chroma's own docs achieve 70-76% NDCG, while Mike Powers' curated 97 Q&A pairs from the course achieve 90-95% NDCG. Makes a compelling case that data curation can matter more than model choice for retrieval.

- [~120:00] After-hours live coding session building a search agent from scratch: ping LLM, add EXA tool, build agentic loop, add conversational loop -- all instrumented with Logfire. Shows the full progression from single API call to multi-turn agentic search in about 25 minutes.

## Related Sources

- [[ws_7_workflows_multiagent_and_context_engineering]] -- Extends the context engineering concepts from here into Lance Martin's four patterns (write, select, compress, isolate) and agentic retrieval for what classic RAG fails at
- [[search_agents_john_doug]] -- John Berryman and Doug Turnbull's workshop on wrapping BM25 with agentic intelligence, providing a complementary approach to the retrieval foundations taught here
- [[deep_research_agent_ivan_leo]] -- Ivan Leo's deep research agent demonstrates advanced agentic retrieval with sub-agents, building on the search agent built in the after-hours session here
- [[ai_products_google_ravin_kumar]] -- Ravin Kumar's discussion of Notebook LM's retrieval evolution as context windows grew, illustrating the product implications of the retrieval architecture taught here
- [[ws_2_prompting_and_context]] -- The earlier workshop that introduces context engineering concepts before this workshop develops them fully
- [[llm_architecture_rasbt]] -- Sebastian Raschka's session on attention mechanisms and KV cache optimization explains why context window limitations exist at the architectural level
