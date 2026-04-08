---
type: concept
title: "Domain-Specific AI Applications"
related_concepts: [evaluation_driven_development, human_in_the_loop, guardrails, model_selection_and_tradeoffs, privacy_and_security]
---

## Overview

AI application patterns vary significantly across domains. What counts as acceptable accuracy, how errors are weighed, what regulatory constraints apply, and what failure modes matter most all shift depending on whether you are building for healthcare, legal discovery, e-commerce, commodities trading, or education. This concept serves as an index pointing to where domain-specific treatments live across the wiki, rather than attempting to consolidate domain knowledge that is better understood in the context of the specific concepts it shapes.

The central insight threading through the sources is that general-purpose demos and benchmarks are poor predictors of domain-specific production requirements. Natalia Rodnova's observation that 95% accuracy is "embarrassing" in radiology, with targets above 99% and always with human-in-the-loop ([[ws_3_evals_and_feedback_loops]]), stands in stark contrast to the coding assistant space where tools were widely accepted well below 80% before late 2025 model improvements. Doug Turnbull and John Berryman demonstrate in [[search_agents_john_doug]] that even the definition of "good search" depends on domain: legal discovery demands recall (you must find everything), while consumer e-commerce demands precision (the top results must be right, or users lose trust). These are not minor calibration differences but fundamentally different optimization targets.

## Where Domain-Specific Treatments Live

**Healthcare** is the most extensively covered domain. For clinical accuracy requirements, self-harm detection guardrails, benefits exclusion decisions, and the full agent development lifecycle in a healthcare setting, see [[human_in_the_loop]] and the primary source [[william_horton_maven_clinic]]. For healthcare-specific guardrail patterns (off-topic detection, prompt hacking, automatic human transfer for self-harm expressions), see [[guardrails]]. For model selection trade-offs driven by healthcare latency and accuracy requirements (Gemini Flash for speed, GPT-5.4 Mini for health questions), see [[model_selection_and_tradeoffs]]. For the regulatory dimension (HIPAA, BAAs with providers), see [[privacy_and_security]].

**Legal discovery and search** are treated in [[retrieval_augmented_generation]], where the recall-first strategy and NDCG evaluation are grounded in Doug Turnbull's search expertise. The precision-vs-recall trade-off across domains is discussed in [[evaluation_driven_development]], where domain-specific acceptable error rates shape evaluation design.

**Commodities trading and financial services** are covered through the S&P Global case study in [[annotation_and_data_labeling]], where Ines Montani demonstrates that single-label annotation passes were 10x faster for commodities trading classification, with production models trained on just 15 hours of single-annotator data ([[natalia_ines_guest_workshop]]).

**Education and regulated industries** appear in [[evaluation_driven_development]], where Stella Liu adds the compliance dimension from her work in education ([[next_level_evals_stella_eddie]]). Regulated industries must layer compliance evaluation on top of standard quality metrics.

**Medical scribing and clinical note generation** are treated in [[human_in_the_loop]] and referenced in [[builders_club_natalia_murat]], where Anonymized Student X demonstrates a clinical note generation prototype built in Google AI Studio in under 5 minutes, and Murat Bilici works on PDF organization for medical and scientific documents using local models due to data sensitivity.

## Where Sources Agree

All sources converge on the principle that domain-specific requirements must drive system design, not the other way around. William Horton's deliberate decision about what Maven Assistant cannot do -- no diagnoses, initially no benefits question-answering due to high financial stakes -- is as important as what it can do ([[william_horton_maven_clinic]]). Stella and Eddie emphasize that product requirements documents are often missing because teams go straight from prototype to production, and defining what the product is designed NOT to do is essential ([[next_level_evals_stella_eddie]]). Ravin Kumar's advice to "solve people's problems with whatever tools exist" ([[ai_products_google_ravin_kumar]]) applies uniformly: start from the domain problem, not the technology.

## Where Sources Disagree or Add Nuance

The sources present a spectrum of views on how much domain expertise is required to build domain-specific AI. Ines Montani argues strongly that you should annotate alongside your SMEs even if you are not an expert ([[natalia_ines_guest_workshop]]), while William Horton's Maven team invested heavily in clinical domain expertise and specialized guardrails. In contrast, Anonymized Student X's rapid medical scribe prototype in [[builders_club_natalia_murat]] suggests that early prototyping can proceed with less domain depth, with domain expertise becoming critical at the evaluation and production stages. The tension is between the speed of general-purpose tooling and the rigor that domain-specific deployment demands.

There is also nuance around whether local models are necessary for domain-specific applications. Murat Bilici uses local Qwen models for document processing due to data sensitivity ([[builders_club_natalia_murat]]), while William Horton uses cloud-hosted Gemini and GPT models with BAAs and guardrails for healthcare ([[william_horton_maven_clinic]]). The choice depends on regulatory environment, data sensitivity, and available infrastructure -- there is no universal answer.

## Related Concepts

- [[evaluation_driven_development]] -- Domain-specific accuracy requirements and acceptable error rates drive evaluation design
- [[human_in_the_loop]] -- Domains like healthcare require supervised AI with human oversight at critical decision points
- [[guardrails]] -- Healthcare, finance, and other regulated domains demand domain-specific input and output safeguards
- [[model_selection_and_tradeoffs]] -- Domain requirements (latency, accuracy, regulatory compliance) constrain model choices
- [[privacy_and_security]] -- HIPAA, GDPR, and other regulatory frameworks impose domain-specific privacy requirements
- [[annotation_and_data_labeling]] -- Domain expertise shapes label scheme design and annotation quality standards

## Sources

- [[william_horton_maven_clinic]] -- The most detailed domain-specific case study: healthcare AI agent with clinical accuracy requirements, self-harm detection, and benefits exclusion
- [[ws_3_evals_and_feedback_loops]] -- Natalia's radiology perspective (95% is embarrassing, above 99% target) and domain-specific acceptable error rates
- [[search_agents_john_doug]] -- Legal discovery demands recall, e-commerce demands precision -- domain shapes the definition of search quality
- [[next_level_evals_stella_eddie]] -- Regulated industries add compliance dimensions to evaluation; product requirements often missing
- [[natalia_ines_guest_workshop]] -- S&P Global commodities trading case study and crime report extraction demonstrating domain-specific annotation design
- [[builders_club_natalia_murat]] -- Medical scribe prototyping and local model deployment for sensitive document processing
