---
type: guest_talk
title: "Building Search Agents: Wrapping BM25 with Agentic Intelligence"
date: 2026-03-23
speakers: [John Berryman, Doug Turnbull, Hugo Bowne-Anderson]
topics: [agentic search, BM25, search relevance, NDCG, evaluation metrics, search array, keyword search, reranking, learning to rank, cross encoders, late interaction models, OpenAI Agents SDK]
source_file: raw/building_search_agents_john_doug.md
word_count: ~18000
---

## Overview

A live coding workshop with search legends John Berryman (GitHub) and Doug Turnbull (search consultant, formerly Shopify/Reddit), co-authors of "Relevant Search." This session builds on the retrieval foundations from [[ws_5_context_engineering_and_information_retrieval]] and complements the agentic search approach in [[deep_research_agent_ivan_leo]]. The session demonstrates how to wrap a basic BM25 keyword search engine with an LLM-powered agentic layer and rigorously evaluate whether the agent actually improves search quality.

The core experiment: take Doug's "search array" library (a pandas/numpy-based BM25 implementation), index the WANDS dataset (Wayfair Annotated Dataset, ~50K products), establish baseline NDCG@10 scores, then build an agentic wrapper using the OpenAI Agents SDK that can issue keyword searches, reason about synonyms and query reformulations, and return ranked results. The key question is whether an LLM's common-sense knowledge about language (synonyms, misspellings, product categories) can improve search quality beyond dumb keyword matching.

Doug provides an excellent accessible explanation of NDCG (Normalized Discounted Cumulative Gain): adding up weighted relevance labels where top positions get more weight, then normalizing by the ideal ordering. The discussion of precision vs. recall use cases is particularly valuable -- legal discovery demands recall (catch everything), while consumer e-commerce demands precision (top results must be right, or users lose trust). Three reranking approaches are covered: classic learning-to-rank (tree-based models on tabular features), cross encoders (transformer classifiers), and late interaction models (ColBERT-style per-token embeddings).

## Key Topics

- BM25 as the universal search baseline -- always start here before adding complexity
- WANDS (Wayfair Annotated Dataset): corpus of 50K products with 480 queries and relevance judgments (exact/partial/irrelevant)
- Search array library: Doug's pandas/numpy in-memory BM25 implementation for rapid prototyping
- NDCG@10 explained accessibly: discounted cumulative gain normalized by ideal ordering
- Agentic search: wrapping basic keyword search in an LLM agent that reasons about queries
- Precision vs. recall tradeoffs: legal discovery (recall) vs. e-commerce (precision)
- Three reranking approaches: learning-to-rank, cross encoders, late interaction models
- L0/L1/L2 retrieval stages: widening the net then progressively refining
- Judgment lists and relevance labels as the foundation of search evaluation
- The assumption that unlabeled items are irrelevant in benchmark datasets

## Key Insights

- The agentic search premise: LLMs have common-sense knowledge about language (synonyms, misspellings, that "dress shoes" is a shoe not a dress) -- wrapping them around keyword search can overcome lexical mismatch
- BM25 baseline on WANDS scored 0.52 NDCG@10 -- "halfway to perfection" but the absolute number matters less than using it as a comparison point for variants
- The labels that go into NDCG matter more than the statistic itself -- if Bob from accounting labels results, it may not reflect what users actually care about. See [[natalia_ines_guest_workshop]] for annotation best practices and [[next_level_evals_stella_eddie]] for calibrating judges to human experts
- "Every search team I go to has a slightly different definition of NDCG" -- better to explain the spirit than get bogged in edge cases
- In production search, recall-first then precision is the mature pattern: L0 casts a wide net, L1/L2 refine and rerank within that set
- Tree-based models (classic ML) still dominate reranking where tabular features matter (price, availability, reviews) -- deep learning is not always the answer
- Late interaction models (ColBERT-style) offer a middle ground between expensive cross-encoders and cheaper bi-encoders, with per-token embeddings and reusable representations
- Google AI Overview and snippets removed one of the most important search signals: time spent on page / click-through data

## People & Tools Mentioned

- John Berryman -- search engineer at GitHub, co-author of "Relevant Search"
- Doug Turnbull -- search consultant (formerly Shopify, Reddit), co-author of "Relevant Search", creator of search array library
- "Relevant Search" (book) -- the industry standard for bridging business requirements and search configuration
- WANDS -- Wayfair Annotated Dataset for search evaluation
- Search array -- Doug's pandas/numpy BM25 library for in-memory search prototyping
- OpenAI Agents SDK -- used to build the agentic search wrapper
- Claude Code -- used for live coding during the workshop
- Exa -- search API used in [[ws_5_context_engineering_and_information_retrieval]], [[ws_6_building_ai_agents]], and [[deep_research_agent_ivan_leo]] for agentic retrieval
- Chroma BM25 -- linked as another BM25 implementation option

## Quotable Moments

- "What happens when you make a search tool and build an agent that is accessing the search? Rather than that straight pass-through deterministic code, you allow the agent to have access to the search tool, the agent has common sense knowledge because these models have been trained on everything." -- John Berryman [~06:05]
- "These are really big words for grade school math." -- Doug Turnbull on NDCG [~51:42]
- "Every search team I go to has a slightly different definition of NDCG." -- Doug Turnbull [~53:00]
- "Pair programming in the Claude Code age is like copy editing in real time." -- Hugo [~34:05]
- "It's sometimes nice just to have everything in memory, do it the dumb, naive way." -- Doug Turnbull on search array [~28:02]

## Highlights

- [~06:00] John's clear framing of agentic search: the LLM becomes the semantic intelligence layer that understands synonyms, misspellings, and intent on top of dumb keyword matching
- [~11:30] Doug explains WANDS dataset and judgment lists -- excellent foundation for anyone new to search evaluation terminology
- [~20:00] Search array library walkthrough: BM25 implemented as pandas columns with numpy scoring, showing how lexical search indexes work under the hood
- [~29:00] Establishing BM25 baseline: NDCG@10 of 0.52 on WANDS -- the starting point for measuring whether agentic search improves quality
- [~34:00] Live pair programming with Claude Code: John and Doug discuss prompt specificity, referencing PRD files, and the spectrum from vibe coding to incremental progress
- [~41:00] Doug's precision vs. recall discussion: legal discovery demands recall, consumer e-commerce demands precision, with clear examples of how wrong results destroy user trust
- [~44:50] Three reranking approaches explained: learning-to-rank (tree models on tabular data), cross encoders (transformer classifiers), and late interaction models (per-token embeddings)
- [~50:00] NDCG explained accessibly: "adding up weighted relevance labels" with top positions getting more weight, normalized by ideal ordering -- Doug notes the spirit matters more than the formula
- [~59:00] Connection between search evaluation metrics and real business outcomes -- the labels matter more than the statistic, and clickstream data from real users is very different from Bob from accounting's labels

## Related Sources

- [[ws_5_context_engineering_and_information_retrieval]] -- Covers BM25, hybrid search, retrieval evaluation metrics (precision@K, recall@K, NDCG), and the "Gather and Glean" framework that complements Doug and John's search evaluation approach
- [[deep_research_agent_ivan_leo]] -- Ivan Leo's deep research agent uses Exa for web search in a multi-step agentic approach, complementing John and Doug's BM25-wrapping approach
- [[ws_6_building_ai_agents]] -- Hugo builds a search agent from scratch using EXA and an agentic loop, providing foundational context for the agentic search wrapper John and Doug build here
- [[next_level_evals_stella_eddie]] -- Stella and Eddie discuss evaluation methodology at a higher level; Doug's NDCG explanation and label quality concerns connect directly to their work on judge calibration
- [[natalia_ines_guest_workshop]] -- Ines Montani's structured RAG approach (information extraction then retrieval) offers an alternative to the keyword-based search approach here
- [[ai_products_google_ravin_kumar]] -- Ravin's discussion of Notebook LM's retrieval evolution and Gemini File Search provides the product perspective on retrieval that complements this technical session
