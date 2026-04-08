---
type: guest_talk
title: "Katharine Jarmul on Privacy in AI: Technical Definitions, Guardrails, and Practical Privacy Engineering"
date: 2026-04-01
speakers: [Katharine Jarmul, Hugo Bowne-Anderson, Carol Willing, Ilona Brinkmeier, Pastor Soto, Anonymized Student Y]
topics: [privacy, data privacy, guardrails, red teaming, federated learning, GDPR, HIPAA, differential privacy, anonymization, pseudonymization, memorization, privacy engineering, LlamaGuard, homomorphic encryption]
source_file: raw/_cleaned/katherine_jarmul_privacy_in_ai_april_1_2026.md
word_count: ~11200
---

## Overview

Katharine Jarmul, author of Practical Data Privacy and specialist in AI/ML privacy and security, delivers a comprehensive guest talk covering the full spectrum of privacy concerns for AI builders. The session spans definitions of privacy, practical controls, guardrail taxonomies, red teaming, federated learning, evaluation approaches, and actionable advice for engineers at all levels.

Jarmul opens by defining three categories of privacy: legal (GDPR, HIPAA, CCPA), social/cultural (how we grow up thinking about privacy, which varies by language, income, subgroup), and technical (mathematical and statistical definitions that allow implementation in systems). She frames privacy engineering as building systems that avoid design patterns leading to oversharing, data leaks, or "icky feelings" -- extending this to AI where the connection between privacy and information is direct and growing.

The core of the talk covers practical privacy controls in a progression. Basic controls include pseudonymization (replacing/masking data), redaction (removing fields), and input sanitization (scanning prompts for personal information). More advanced controls include anonymization (which does not work for every data type -- she uses Google Street View as an example of partial anonymization), data minimization, and privacy routing infrastructure.

Jarmul provides a particularly valuable taxonomy of guardrails across three categories: external deterministic (software-based filters like hash trees matching known copyright data), external algorithmic (separate classifier models like LlamaGuard that evaluate safety of prompts/outputs), and internal alignment training (RLHF, fine-tuning, policy-based tuning built into the model itself). This guardrail taxonomy complements the practical guardrail implementation covered in [[ws_4_testing_and_observability]] and the production guardrails in [[william_horton_maven_clinic]]. She recommends LlamaGuard from Meta as a starting point for external algorithmic guardrails.

The session covers red teaming as creative, attack-oriented exercises that should involve the whole organization (not just the security team), and should be structured as hack days to build engagement. On federated learning, she explains how model updates (gradients) can leak information, and describes how differential privacy and encrypted computation can be layered on top for stronger protections. She references her work at CAPE Privacy implementing the first encrypted federated learning system.

On evaluation and privacy, Jarmul emphasizes the field is still defining best practices. She suggests starting small -- testing pseudonymization in CI/CD, sampling flows for potential privacy violations, and building gradually. She draws a parallel to evals: the earlier you start, the easier it is; waiting creates compounding difficulty.

## Key Topics

- Three categories of privacy: legal, social/cultural, technical
- Privacy controls progression: pseudonymization, redaction, anonymization, data minimization
- Guardrail taxonomy: external deterministic, external algorithmic, internal alignment
- Red teaming as organizational practice
- Federated learning with differential privacy and encrypted computation
- Privacy observability and privacy routing
- System prompt exfiltration risks
- LLM memorization and re-identification attacks
- Data flows and purpose limitations
- Privacy engineering as a career path

## Key Insights

- Privacy is not binary (on/off) but a spectrum -- any step toward more privacy for the same utility is valuable
- System prompts should be treated as public; they can and will be exfiltrated, so never put anything in them you would not put on your website
- Any data fed into an LLM system (memories, context, vector databases) is potentially recoverable through reverse engineering -- a Carlini paper from Google Research used LLMs to re-identify hundreds of texts by author
- Guardrails have three distinct layers (deterministic filters, algorithmic classifiers, alignment training), and understanding which you are implementing is critical
- Privacy observability should be integrated into general observability, not treated as a separate concern -- see [[ws_4_testing_and_observability]] for the broader observability discussion with OpenTelemetry
- Red teaming should be organized as hack days involving the whole organization, not relegated to an overloaded security team
- The field of privacy evaluation is still nascent, with no established best practices -- there is room for builders to define these. [[next_level_evals_stella_eddie]] covers evaluation methodology broadly, which could be adapted for privacy evaluation
- Federated learning alone does not guarantee privacy; gradient updates can leak information without additional protections like differential privacy

## People & Tools Mentioned

- Katharine Jarmul -- author of Practical Data Privacy, former principal data scientist at ThoughtWorks, CAPE Privacy
- Nicholas Carlini -- Google Research, work on extracting training data and re-identification attacks
- Pliny the Liberator (formerly Pliny the Prompter) -- system prompt exfiltrator
- Shoshana Zuboff -- Surveillance Capitalism book on Google Street View history
- Emmanuel (Maddie) Moss -- paper on corporate ethics institutionalization with Dana Boyd and Jacob Metcalf
- Ilona Brinkmeier -- former Philips Medical Systems, asked about federated learning
- Martin Tingley -- head of experimentation at Windows
- LlamaGuard (Meta), Microsoft Presidio (with spaCy), CAPE Privacy, ThoughtWorks privacy championship program, Apple privacy infrastructure

## Quotable Moments

- "Anything that you write in your system prompt, you should be comfortable writing on your public website." -- Katharine Jarmul [~45:00]
- "If you've never had a privacy incident reported, or you never had a security incident reported, it doesn't mean it didn't happen, it just means your reporting is broken." -- Katharine Jarmul [~40:00]
- "We need at least twice as many privacy engineers as we need builders right now to just help keep up with the pace." -- Katharine Jarmul [~65:00]
- "We're getting closer and more personal to lots of people... we're kind of entrusted with people's deepest, darkest secrets that might be lying in our database." -- Katharine Jarmul [~65:00]
- "If you're handling other people's data, know that you're handling potentially super sensitive stuff... there is a serious qualitative difference between handling clickstream data and conversational data with large language models." -- Hugo Bowne-Anderson [~70:00]

## Highlights

- [~05:00] Three-category privacy framework (legal, social/cultural, technical) providing a clear mental model for approaching privacy from any angle
- [~10:00] Discussion of information asymmetry -- Google knows everything about users but users cannot find out about Google; large organizations demand privacy while denying it to individuals
- [~20:00] Detailed progression of privacy controls from basic (pseudonymization, redaction) to advanced (anonymization, privacy routing), with Google Street View as a case study in partial anonymization
- [~25:00] System prompt exfiltration risk discussion, including the leaked system prompts repository and Pliny the Liberator's activities
- [~30:00] Three-layer guardrail taxonomy (external deterministic, external algorithmic, internal alignment) -- one of the most structured breakdowns of guardrails available
- [~40:00] ThoughtWorks privacy championship program as a model for distributing privacy responsibility across organizations (~1,000 engineers in initial program)
- [~45:00] Red teaming discussion emphasizing creative hack days over isolated security team work
- [~55:00] Practical tool recommendations: Microsoft Presidio for text pseudonymization, database-level masking/hashing, starting small with basic data minimization before advanced techniques
- [~60:00] Federated learning deep dive with Ilona Brinkmeier from Philips Medical, covering gradient leakage risks and encrypted federated learning at CAPE Privacy

## Related Sources

- [[ws_4_testing_and_observability]] -- Covers guardrail implementation (regex, keyword, LLM-based) and observability with OpenTelemetry, which Jarmul argues should integrate privacy observability
- [[william_horton_maven_clinic]] -- William Horton's Maven Assistant implements production guardrails for healthcare (off-topic, prompt hacking, self-harm detection), a concrete application of Jarmul's guardrail taxonomy
- [[ws_6_building_ai_agents]] -- Agent safety discussion including Simon Willison's lethal trifecta (private data + external communication + untrusted content), directly related to Jarmul's privacy concerns
- [[next_level_evals_stella_eddie]] -- Evaluation methodology that could be adapted for privacy evaluation, which Jarmul notes is still a nascent field
- [[builders_club_natalia_murat]] -- Murat's local model deployment for sensitive PDF data exemplifies the privacy-motivated approach Jarmul discusses
- [[ws_8_finetuning_and_production_ai]] -- Fine-tuning for edge devices and local models addresses the data sensitivity concerns Jarmul raises about sending data to external providers
