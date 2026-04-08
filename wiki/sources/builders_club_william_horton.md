---
type: builders_club
title: "William Horton Builders Club: AI Engineering Careers, Eval Design, and Multi-Agent Architecture Challenges"
date: 2026-03-19
speakers: [William Horton, Hugo Bowne-Anderson, Carol Willing, Anonymized Student Y, Murat Bilici, Ryan Rodriguez, Michael Powers]
topics: [AI engineering careers, evaluation design, multi-agent architecture, hiring, healthcare AI, career transitions, LLM capabilities, text classification, agentic solutions]
source_file: raw/_cleaned/builders_club_william_horton_march_19_2026.md
word_count: ~9500
---

## Overview

William Horton, staff ML engineer at Maven Clinic and returning builder in residence, leads an open-format Builders Club session that evolves into a wide-ranging discussion about AI engineering careers, evaluation practices, multi-agent architecture challenges, and practical advice for builders at various career stages. For William's detailed account of building and launching Maven Assistant, see [[william_horton_maven_clinic]].

William shares his background -- social sciences at Harvard, coding bootcamp, full-stack engineering, pivot to ML via FastAI, then roles at Compass (real estate recommendations), Included Health (where "NLP 2.0" became their LLM strategy), and now Maven Clinic building a women's health AI agent. He reveals that his boss suggesting he look into LLMs in 2023 proved to be a pivotal career moment.

The session features a substantial discussion about the most important skills for AI engineers. William argues the biggest skill is getting an LLM to do what you want -- a combination of prompt engineering and evaluation, with emphasis on evaluation. He describes wanting to hire people who can diagnose agent misbehavior, fix it, and confidently say they improved it by a measurable amount. He candidly notes that gaining employment has "a lot to do with" factors beyond skills, citing his own experience where people were more excited about his Harvard degree than his actual abilities.

A pivotal exchange occurs when Ryan asks about criteria for determining when agentic solutions make sense. William's advice: get the person to describe their desired input and output without using hype terms like "agentic," then figure out the technical approach. Carol adds the importance of helping people who may not know what they want by providing constraints. William emphasizes educating organizations about what is easy versus hard with LLMs -- text classification is essentially a solved problem, while multi-agent architectures remain genuinely challenging.

The session's most technically rich segment covers multi-agent architecture challenges. William describes this as the hardest problem he has wrestled with in six months: whether sub-agents respond directly to users or through a lead agent, whether sub-agents can call other sub-agents, parallel versus sequential delegation, and how organizational structure maps onto agent architecture (Conway's Law for agents). Michael Powers raises the cost dimension, and William notes latency is the bigger concern in practice -- each agent delegation adds another LLM call and at least another second of latency.

## Key Topics

- AI engineering career paths and skill requirements
- Evaluation as the most important AI engineering skill
- When to use agentic solutions versus simpler approaches
- Multi-agent architecture design decisions and trade-offs
- Text classification as an essentially solved problem
- Career transition advice for medical professionals
- The application layer versus frontier labs
- Conway's Law applied to multi-agent systems

## Key Insights

- The most important AI engineering skill is evaluation: being able to diagnose agent misbehavior, fix it, and confidently quantify improvement -- see [[next_level_evals_stella_eddie]] for a deep dive on eval methodology and [[ws_3_evals_and_feedback_loops]] for hands-on eval building
- Gaining employment often depends more on signaling (credentials, etc.) than actual skills, which is a systemic challenge for career changers
- When someone asks for an "agentic solution," get them to describe desired inputs and outputs without hype terms; the technical approach follows from there
- Text classification is essentially a solved problem for most business use cases using models like GPT-5.4 Mini
- Multi-agent architecture is genuinely hard with near-infinite design choices: delegation patterns, response routing, parallel execution, and organizational mapping -- explored further in [[ws_7_workflows_multiagent_and_context_engineering]] and [[deep_research_agent_ivan_leo]]
- Latency, not cost, is the primary concern with multi-agent systems in production -- each delegation adds another LLM call and another second
- Going wide before going deep is useful in this fast-moving field; the 8,000 token context window constraint of 2023 became irrelevant within months
- The application layer is where the most exciting building is happening; if research stopped today, there would be 5+ years of things to build

## People & Tools Mentioned

- William Horton -- staff ML engineer at Maven Clinic, background spanning Harvard, coding bootcamp, Compass, Included Health
- Ravin (Google) -- previous guest speaker (see [[ai_products_google_ravin_kumar]]), mentioned for Notebook LM and working on both frontier and open-weight models
- Andrej Karpathy -- teaching perspective, noted research at frontier labs may be deterministic
- Dan Becker -- guest talk on generative AI for construction/CAD
- FastAI, Maven Clinic, Compass, Included Health, spaCy, BigQuery, Google ADK

## Quotable Moments

- "The biggest skill to me is how to get an LLM to do what you want... a combination of prompt engineering and evaluation, with more emphasis on evaluation." -- William Horton [~10:00]
- "Sadly, I don't think that gaining employment has a lot to do with skills." -- William Horton [~15:00]
- "Show me your documents. You're telling me about this problem -- what I want to do is look at it." -- William Horton on evaluating agentic solution requests [~35:00]
- "Text classification... more or less a solved problem. Someone at your company could build that in a week." -- William Horton [~35:00]
- "I would rather be building now than at a Frontier Lab... the opportunity I have is to put something in someone's hands that just didn't exist." -- William Horton [~45:00]

## Highlights

- [~10:00] William's description of the ideal AI engineer hire -- someone who can take a buggy agent, look at prompts and tools, figure out how to fix it, and report back with confidence in the improvement
- [~15:00] Candid discussion about the disconnect between actual skills and hiring signals, with William's Harvard anecdote
- [~25:00] Murat (surgeon transitioning careers) asks for advice on building healthcare AI tools, getting practical guidance from both William and Carol about rapid prototyping and leveraging domain expertise
- [~35:00] Ryan's question about criteria for agentic solutions leads to practical heuristics: describe desired inputs/outputs without hype terms, and understand what LLMs find easy (text classification) versus hard
- [~40:00] Deep discussion on how much transformer internals knowledge is useful -- William argues knowing "one layer down" is sufficient, but understanding why changing one token changes output is practically useful
- [~50:00] Detailed breakdown of multi-agent architecture challenges at Maven Clinic, including Conway's Law for agents and the latency penalty of multi-agent delegation
- [~55:00] Michael Powers raises cost concerns with agentic approaches; William pivots to latency as the real constraint, noting each sub-agent delegation adds another second minimum

## Related Sources

- [[william_horton_maven_clinic]] -- William's detailed Q&A the day after launching Maven Assistant, covering the multi-agent architecture, LLM-as-judge design, guardrails, and first-day discoveries
- [[next_level_evals_stella_eddie]] -- Stella Liu and Eddie Wharton's deep dive on evaluation methodology, complementing William's emphasis on evaluation as the most important AI engineering skill
- [[ws_3_evals_and_feedback_loops]] -- William contributes extensively to this workshop, advocating for comparative evaluation and free-text feedback columns
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Covers multi-agent patterns and context engineering that relate to William's Maven Clinic architecture challenges
- [[ai_products_google_ravin_kumar]] -- Ravin Kumar's talk, which William references; both discuss building AI products at the application layer
