---
type: concept
title: "Retrieval-Augmented Generation (RAG) and Information Retrieval"
related_concepts: [context_engineering, agents_vs_workflows, evaluation_driven_development, the_api_call_mental_model, structured_output, llm_architecture_and_inference]
---

## Overview

Retrieval-Augmented Generation (RAG) refers to the practice of supplementing LLMs with external knowledge by retrieving relevant documents or passages and including them in the prompt context. The concept spans a wide spectrum of complexity across the course sources, from simple keyword search baselines through embedding-based vector retrieval to sophisticated agentic retrieval systems where the LLM itself orchestrates multi-step search strategies.

Hugo introduces the foundations in [[ws_5_context_engineering_and_information_retrieval]], tracing the history of retrieval from bag of words and TF-IDF through Word2Vec and modern sentence-transformer embeddings. His central argument is that too many people jump straight to embeddings when simpler methods often work: coding agents successfully use grep and keyword search, and BM25 should be a baseline before adding vector search complexity. John Berryman and Doug Turnbull reinforce this in [[search_agents_john_doug]], demonstrating a pandas/numpy BM25 implementation that achieves 0.52 NDCG@10 on the Wayfair WANDS dataset -- a reasonable starting point that costs nothing to run. At the other end of the spectrum, Ivan Leo's deep research agent in [[deep_research_agent_ivan_leo]] uses sub-agents that spawn dynamically to research individual questions, each with its own search tool and iteration limits, representing fully agentic retrieval. Between these extremes sits the practical reality that most production RAG systems use some combination of keyword and vector search, evaluated rigorously with metrics like precision, recall, and NDCG.

A recurring question across sources is whether growing context windows will make RAG obsolete. Ravin Kumar in [[ai_products_google_ravin_kumar]] describes how Notebook LM's retrieval internals were progressively simplified as Gemini's context window grew to one million tokens. Yet Hugo demonstrates in [[ws_5_context_engineering_and_information_retrieval]] that Gemini's near-perfect needle-in-a-haystack recall degrades sharply with duplicate information, contradicting information, or multi-needle queries. The consensus is that long context windows do not replace RAG -- they change what RAG needs to do.

## The Full Retrieval Stack

The retrieval stack progresses through several layers of sophistication. At the base sits keyword search -- BM25, grep, and simple text matching -- which Hugo and Doug Turnbull both advocate as a starting point. Hugo emphasizes in [[ws_5_context_engineering_and_information_retrieval]] that the starting recommendation should be "one stop until BM25 is a baseline for RAG," citing Eugene Yang from Amazon. Doug's search array library in [[search_agents_john_doug]] makes this concrete with a pandas-based BM25 implementation designed for rapid prototyping.

The next layer adds embedding-based retrieval using vector databases like ChromaDB. Hugo demonstrates building a RAG system from scratch with GPT-2, NumPy arrays, and ChromaDB in [[ws_5_context_engineering_and_information_retrieval]], with the practical advice to start with NumPy arrays and move to vector databases only when things get slow or do not fit in memory. Hybrid search -- combining keyword and vector approaches -- outperforms either alone, with Jason Liu's blog post cited showing 85% recall with hybrid search out of the box.

Beyond basic retrieval, the "Gather and Glean" framework from Jeff Huber (Chroma CEO) provides a guiding principle: first prioritize recall to get all potentially relevant chunks, then re-rank with precision. Doug Turnbull describes the same pattern in [[search_agents_john_doug]] as the L0/L1/L2 retrieval stages: L0 casts a wide net, L1 and L2 progressively refine and re-rank within that set. Three reranking approaches are covered: classic learning-to-rank with tree-based models, cross encoders (transformer classifiers), and late interaction models like ColBERT.

## What Classic RAG Fails At

Hugo addresses the limitations of classic single-pass RAG directly in [[ws_7_workflows_multiagent_and_context_engineering]], identifying three categories of queries where it breaks down: summarization queries ("what are these docs about?" requires a summary tool, not chunk retrieval), multi-document comparison queries (comparing techniques across documents requires multiple searches plus comparison), and multi-step reasoning queries ("what are the three foundation models? Give me detail on the second one" requires maintaining state across steps).

These failure modes motivate agentic retrieval -- putting the LLM in a loop with search tools so it can formulate queries, evaluate results, and iterate. Ivan Leo's deep research agent in [[deep_research_agent_ivan_leo]] represents the most sophisticated implementation: a main agent spawns sub-agents to research individual questions, each limited in iteration count, with results flowing back to the orchestrator for synthesis. John and Doug's approach in [[search_agents_john_doug]] is complementary but simpler: wrapping BM25 with an LLM agent that reasons about synonyms, query reformulations, and result quality.

Ines Montani offers a fundamentally different alternative in [[natalia_ines_guest_workshop]]: structured RAG, where information is first extracted into schemas using NLP or LLMs, and retrieval then operates on structured data rather than raw text. When the schema is known upfront, this approach can outperform naive vector database approaches because it separates the extraction problem from the retrieval problem.

## Evaluation and Data Quality

Retrieval evaluation is a substantial topic across the sources. Hugo covers precision at K, recall at K, hit rate, and NDCG in [[ws_5_context_engineering_and_information_retrieval]], demonstrating Chroma's generative benchmarking for creating gold evaluation datasets. The results are striking: a well-curated course Q&A document achieves 90-95% NDCG versus 70-76% for Chroma's own less curated documentation, making a compelling case that data curation can matter more than model choice.

Doug Turnbull provides an accessible explanation of NDCG in [[search_agents_john_doug]] -- describing it as adding up weighted relevance labels where top positions get more weight, then normalizing by ideal ordering -- while noting that every search team defines it slightly differently. His deeper insight is that the labels feeding into NDCG matter more than the statistic itself: if someone outside the target user group labels results, it may not reflect what users actually care about. The domain context matters enormously: legal discovery demands recall (catch everything), while consumer e-commerce demands precision (top results must be right, or users lose trust).

## Where Sources Agree

All sources agree that RAG remains essential despite growing context windows. There is strong consensus that BM25 should be a baseline before adding complexity, that hybrid search outperforms either keyword or vector search alone, and that evaluation metrics (especially NDCG) are crucial for measuring retrieval quality. The recall-first-then-precision pattern (Gather and Glean / L0-L1-L2) is endorsed by both the retrieval workshop and the search agents session. Everyone agrees that agentic retrieval is more capable than single-pass RAG for complex queries.

## Where Sources Disagree or Add Nuance

The sources diverge on how much retrieval complexity is appropriate. Hugo's starting point in [[ws_5_context_engineering_and_information_retrieval]] and Doug's in [[search_agents_john_doug]] is deliberately simple -- NumPy arrays, pandas-based BM25, start small. Ivan Leo's deep research agent represents the opposite end: dynamic sub-agent spawning with web search tools. The right level depends on the use case. Ines Montani's structured RAG approach in [[natalia_ines_guest_workshop]] challenges the vector-database-first mindset entirely, arguing that when schemas are known upfront, extraction-then-retrieval beats embedding-based search. Ravin Kumar's account of Notebook LM simplifying its chunking infrastructure as context windows grew suggests the retrieval layer may thin out over time, while Hugo's evidence of needle-in-a-haystack degradation with messy data suggests it will not disappear. The tension between "RAG is dead" and "RAG is essential" remains productive rather than resolved.

## Related Concepts

- [[context_engineering]] -- RAG is one of the "select" strategies in Lance Martin's four-pattern framework for context engineering
- [[evaluation_driven_development]] -- Retrieval quality must be measured rigorously; NDCG, precision, and recall are the key metrics
- [[the_api_call_mental_model]] -- Stefan maps RAG to the context population component of the LLM API call
- [[agents_vs_workflows]] -- Agentic retrieval blurs the line between retrieval and agent orchestration
- [[annotation_and_data_labeling]] -- The quality of relevance labels determines the quality of retrieval evaluation

## Sources

- [[ws_5_context_engineering_and_information_retrieval]] -- The definitive retrieval session: historical methods, BM25 baselines, embeddings, ChromaDB, Gather and Glean framework, and retrieval evaluation metrics
- [[search_agents_john_doug]] -- Wrapping BM25 with agentic intelligence, NDCG evaluation, precision vs. recall for different domains, and three reranking approaches
- [[ai_products_google_ravin_kumar]] -- Notebook LM's retrieval evolution as context windows grew, demonstrating how product architecture adapts to model capabilities
- [[ws_7_workflows_multiagent_and_context_engineering]] -- What classic RAG fails at and the agentic retrieval patterns that address those failures
- [[natalia_ines_guest_workshop]] -- Structured RAG as an alternative: information extraction first, then retrieval on structured data
- [[deep_research_agent_ivan_leo]] -- Multi-step agentic retrieval with dynamic sub-agents, representing the most sophisticated retrieval pattern in the course
