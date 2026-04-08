---
type: guest_talk
title: "Ground Truth for AI Evals: Annotation Pipelines in Practice with Ines Montani, Natalia Rodnova, and the Explosion Team"
date: 2026-03-26
speakers: [Ines Montani, Natalia Rodnova, Hugo Bowne-Anderson, Magda, Adrian Turcu, Nathan (Carvana), Carol Willing]
topics: [annotation, Prodigy, spaCy, data development, label scheme design, cognitive load, model assistance, structured RAG, information extraction, NLP, LLM evaluation, AB testing]
source_file: raw/_cleaned/Natalia-Ines-Guest-Workshop.md
word_count: ~15000
---

## Overview

This two-part session features a talk by Ines Montani (co-founder/CEO of Explosion, makers of spaCy and Prodigy) on data annotation best practices, followed by a hands-on Prodigy workshop led by Natalia Rodnova (VP of Data Science at Eon). This session provides the annotation foundations that connect to [[ws_3_evals_and_feedback_loops]] and [[next_level_evals_stella_eddie]]. The session covers foundational principles of annotation design that apply to both traditional NLP and modern LLM evaluation workflows.

Ines opens with real-world examples illustrating why label scheme design is critical. Her crime report extraction example shows how fine-grained labels (stabber/stabbee, crime location) require far more training data than generic labels (person, location) combined with follow-up business logic. A custody document anonymization case study demonstrates how trying to teach a model to identify "minor date of birth" fails because the concept of who is a minor changes over time -- the solution is to separate classification logic (finding dates) from business logic (computing age from dates). The key principle: factor out business logic from classification logic.

Her second major theme is reducing cognitive load. She presents pseudocode showing that iterating over annotation types first (one label at a time) then over examples is dramatically faster than iterating over examples and considering all labels simultaneously. The S&P Global commodities trading case study quantifies this: breaking multi-label annotation into single-label passes was 10x faster overall, with individual models requiring just 15 hours of single-annotator time to reach production quality.

Ines also covers model-assisted annotation (pre-populating annotations with model predictions, even at 50% accuracy, saves 50% of human effort), token boundary snapping (automatically aligning selections to valid token boundaries), and the train curve feature in Prodigy for knowing when more data will improve models.

During Q&A, Nathan from Carvana asks about annotation for content generation pipelines. Ines recommends AB evaluation and Prodigy's tournament workflow (using ELO-style ranking) for comparing prompt/model outputs. Hugo asks about when to use LLMs versus classic NLP: Ines argues LLMs are great for prototyping and cold-start, but once you need speed, privacy, cost-effectiveness, or accuracy at scale, investing in smaller trained models pays off. She emphasizes using LLMs to build the system (writing spaCy rules, generating training data) rather than being the system.

Natalia then leads a hands-on Prodigy workshop, demonstrating the annotation interface, database backend (SQLite/Postgres), recipe system, and command-line interface. She emphasizes the importance of annotating yourself (not just delegating to SMEs) to understand the data and uncover annotation guideline inconsistencies, and using model predictions in adjudication to find where human annotators and models diverge.

## Key Topics

- Label scheme design principles (factoring out business logic from classification logic)
- Cognitive load reduction in annotation (single-label passes vs. multi-label)
- S&P Global case study: 10x faster annotation through task decomposition
- Model-assisted annotation and pre-population
- AB evaluation and tournament workflows for LLM output comparison
- When to use LLMs versus smaller trained models
- Structured RAG (information extraction first, then retrieval)
- Prodigy annotation interface, recipes, and database architecture
- Annotation guidelines development as iterative process

## Key Insights

- Factoring business logic from classification logic is the single most impactful annotation design decision -- it makes tasks easier to annotate, train, and maintain
- Making multiple single-label passes over data is counterintuitively faster (10x in the S&P case) than one multi-label pass, because cognitive load reduction outweighs the extra iterations
- Even a 50% accurate model pre-annotating data saves 50% of human annotation effort
- LLMs should be used to build NLP systems (writing rules, generating training data) rather than being the production system, when speed, privacy, cost, or accuracy at scale matter -- see [[ws_8_finetuning_and_production_ai]] for the distillation approach and [[katherine_jarmul_privacy]] for the privacy dimension
- Annotation is an iterative process: design schema, annotate a few hundred examples, compare, discover inconsistencies, revise schema, repeat
- Annotating alongside your SMEs (even if you are not one) uncovers valuable differences between "model thinking" and "expert thinking"
- Structured RAG (extracting information into schemas first, then building retrieval on structured data) outperforms naive vector database approaches when the schema is known upfront -- compare with the retrieval approaches in [[ws_5_context_engineering_and_information_retrieval]] and [[search_agents_john_doug]]

## People & Tools Mentioned

- Ines Montani -- co-founder/CEO of Explosion, creator of spaCy and Prodigy
- Matt Hannibal -- Explosion team, custom Claude Code skills for NLP development
- Magda -- Explosion team, Prodigy tournament workflow
- Natalia Rodnova -- VP Data Science at Eon, workshop leader
- Nathan (Carvana) -- content generation pipeline question
- Adrian Turcu -- data architect working on CV/document processing
- Guido van Rossum -- mentioned for Microsoft structured RAG talk
- Guardian -- annotation meetings case study
- Rotational Labs -- annotation edge case discussion screenshots
- S&P Global -- commodities trading case study (6MB models, 15 hours annotation per model)
- Prodigy, spaCy, Explosion, GitLab (structured database case study), PyMC, displaCy

## Quotable Moments

- "If you're working in machine learning, you've probably spent more time trying to get your GPU to work than it took a single person here to create data for one model that's now in production." -- Ines Montani [~20:00]
- "You are allowed to make the problem easier. This is not research, this is not a contest." -- Ines Montani [~25:00]
- "Instead of thinking of the LLM as the system, you can use the LLM to build the system, just like you're building using coding assistants." -- Ines Montani [~35:00]
- "I actually got this job because of spaCy's displaCy that visualizes named entities... I put it in a nice and colored way, and I was hired." -- Natalia Rodnova [~45:00]
- "When you have annotation projects, annotate yourself as well. You might not count as an SME, but it's very important to understand what is it you are modeling." -- Natalia Rodnova [~50:00]

## Highlights

- [~05:00] Crime report extraction example demonstrating why generic labels + business logic outperform fine-grained labels for both annotation efficiency and model training
- [~10:00] Custody document anonymization case: trying to teach a model temporal concepts (who is a minor) that change daily -- a common and costly mistake in label scheme design
- [~15:00] S&P Global case study quantifying the 10x speedup from single-label annotation passes, with production models trained on just 15 hours of single-annotator data
- [~25:00] Reframing relation extraction as hypothesis selection -- auto-generating human-readable sentences expressing relationships and asking annotators to check boxes, producing the same structured data far more efficiently
- [~30:00] Ines on when to use LLMs vs. classic NLP: LLMs for prototyping and cold-start, smaller models for production when you need speed, privacy, cost-effectiveness, or accuracy; use LLMs to generate spaCy rules and training data
- [~35:00] Nathan's question about annotation for content generation pipelines, leading to discussion of AB evaluation and ELO tournament workflows in Prodigy
- [~40:00] Adrian's question about processing CVs and documents at scale, leading to discussion of structured RAG and information extraction as an alternative to naive vector database approaches
- [~50:00] Natalia's advice on annotating alongside SMEs to discover discrepancies between model-like logical thinking and expert domain reasoning

## Related Sources

- [[ws_3_evals_and_feedback_loops]] -- Hugo's hands-on eval workshop builds directly on annotation concepts from this session; includes manual annotation, confusion matrices, and LLM-as-judge
- [[next_level_evals_stella_eddie]] -- Stella and Eddie cover the evaluation methodology that annotation feeds into, including LLM judges calibrated to human labels and the team sport nature of evals
- [[william_horton_maven_clinic]] -- William's LLM-as-judge alignment process uses two human labelers, directly applying the annotation principles Ines and Natalia discuss
- [[demo_day]] -- Natalia presents her Jira Assistant at demo day; Michael Powers' Q&A distillation pipeline uses annotation-driven approaches
- [[ws_5_context_engineering_and_information_retrieval]] -- Ines's structured RAG approach (information extraction then retrieval) offers an alternative to the vector database approaches covered here
- [[katherine_jarmul_privacy]] -- Privacy concerns around annotation data, especially when annotating sensitive or personal information
