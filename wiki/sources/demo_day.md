---
type: demo_day
title: "Demo Day: Student Projects Showcasing AI-Powered Applications Across Domains"
date: 2026-04-02
speakers: [Hugo Bowne-Anderson, Anonymized Student Y, Konrad Dabrowski, Natalia Rodnova, Michael Powers, Shubh Thomas, Pastor Soto, Caleb Tutty]
topics: [demo day, student projects, AI events platform, research assistant, Jira automation, Q&A distillation, cybersecurity training, AI education, 3D printing agents, Gemini, Modal, observability]
source_file: raw/_cleaned/demo_day_april_2_2026.md
word_count: ~8400
---

## Overview

The cohort's Demo Day features seven 5-minute presentations showcasing diverse AI projects built during the course. Each presenter demonstrates a working prototype or architecture, with questions deferred to Discord to respect time constraints.

Anonymized Student Y presents an architecture for a 5-day immersive AI-powered event system, outlining a progression from simple LLM core to RAG knowledge base, evals with LLM-as-judge, orchestration, and context engineering. He identifies future considerations including privacy, local models, edge deployment, and whether agents are overkill for event management.

Konrad Dabrowski demonstrates a research assistant built with Gemini File Store that helps query his technical book library. It features a library agent backed by SQLite that suggests relevant books based on queries, a deep research agent (expanded from [[deep_research_agent_ivan_leo]]), and RAG over selected books via Gemini. He notes the project has grown substantially in complexity.

Natalia Rodnova presents her AI Jira Assistant, a project spanning three cohorts (started July, continued November, now in production). Built with Shiny for Python, it triages incoming Jira issues (model errors, model questions, data requests), then runs an LLM with tool calls to pull database reports, run models, verify correctness, and post comments/send emails -- all in supervised mode where she reviews each action before approval. The observability layer showing each LLM call, tool invocation, and response is highlighted. Natalia also led the [[natalia_ines_guest_workshop]] on annotation with Prodigy and contributed to the MCP discussion in [[builders_club_natalia_murat]].

Michael Powers presents the Top 100 Q&A distillation pipeline that processed 1,300 Discord threads across four cohorts. The pipeline extracted first posts, filtered to ~750 content questions, consolidated into ~100 canonical questions using three approaches (embeddings/clustering, single API call, chat API), and then generated answers using curated knowledge bases and style guides extracted from Hugo's hand-written answers. The embedding and retrieval techniques build on [[ws_5_context_engineering_and_information_retrieval]]. Four rounds of generate-annotate-revise with a custom annotation tool produced the final Q&A set.

Shubh Thomas presents a cybersecurity training agent that generates personalized phishing simulations, creating realistic fake CTO emails with psychological manipulation tactics, then evaluating employee responses with feedback on threat type, correct actions, and real-world consequences.

Pastor Soto demonstrates TinyTorch, an educational platform for learning PyTorch fundamentals through exercises at multiple difficulty levels (beginner to advanced, Bloom taxonomy), combined with an AI tutor and an architecture drawing evaluation feature where users sketch neural network diagrams and AI evaluates their understanding.

Caleb Tutty presents a 3D printing agent that extends the deep research workshop to include OpenSCAD as a tool in a Docker container, allowing iterative generation of 3D-printable objects (vases, chess sets, drone assemblies) with automated validation scripts, web search for design research, and concept image generation.

## Key Topics

- Event management AI systems with RAG and orchestration
- Research assistants using Gemini File Store and deep research agents
- Jira automation with LLM tool calling and supervised execution
- Large-scale Q&A distillation from Discord community data
- Cybersecurity awareness training via AI-generated phishing simulations
- AI-powered educational platforms with multi-level tutoring
- 3D printing agents with OpenSCAD tool integration

## Key Insights

- Students successfully combined multiple course concepts (Modal deployment from [[ws_1_foundations]], deep research agents from [[deep_research_agent_ivan_leo]], tool calling from [[ws_6_building_ai_agents]], evals from [[ws_3_evals_and_feedback_loops]]) into working prototypes within days of learning them
- Natalia's Jira Assistant spanning three cohorts demonstrates the value of iterative development and returning to projects with new knowledge
- Michael Powers' Q&A pipeline shows that LLM consolidation of similar questions requires explicit guidance on granularity to avoid over-merging or under-merging
- Supervised mode (human reviews each action) is a practical pattern for high-stakes agent deployments where full automation is premature -- relates to the agency vs. supervision discussion in [[ws_6_building_ai_agents]] and [[william_horton_maven_clinic]]
- The deep research agent workshop (Ivan Leo/Hugo) proved immediately reusable -- both Konrad and Caleb incorporated it into their projects within 5 days
- Carol Willing notes the Q&A distillation approach would be valuable for qualitative survey responses and could be a PyCon/SciPy tutorial

## People & Tools Mentioned

- Ivan Leo -- deep research agent workshop (see [[deep_research_agent_ivan_leo]]) that Konrad and Caleb both extended
- Ben Shibabo -- Modal project referenced
- Dan Becker -- generative AI for construction/CAD, 3D printing with AI
- Thomas Vicki -- upcoming Builders Club presenter
- Gemini File Store, Modal, Shiny for Python, SQLite, FastAPI, Textual, Rich, OpenSCAD, Pydantic, LogFire, Natto Banana (image generation)

## Quotable Moments

- "The course is very, very efficient, and helped me start very quickly." -- Konrad Dabrowski [~15:00]
- "I was not sure that it would happen, because I needed to de-identify data and make things, you know, kind of create fake stuff." -- Natalia Rodnova on preparing her demo [~15:00]
- "I didn't write any of these words, basically. I guided the creation of these." -- Michael Powers on his AI-generated presentation slides [~30:00]
- "This is better than Datacamp. I don't even know why that product exists anymore." -- Hugo Bowne-Anderson on Pastor's educational platform [~45:00]
- "When I saw the workshop with Hugo and Ivan, I thought, this is a runtime and a harness that could be used for pretty much anything that needs to use tools." -- Caleb Tutty [~55:00]

## Highlights

- [~10:00] Konrad's research assistant demo showing the full loop from library agent (SQLite) to book selection to Gemini RAG, all built by a self-described non-AI-expert
- [~15:00] Natalia's Jira Assistant with its layered observability showing each LLM call, tool invocation, inputs and outputs, and supervised approval workflow -- a real production-quality tool
- [~25:00] Michael Powers' detailed breakdown of the Q&A distillation pipeline methodology, including the key insight about granularity guidance when consolidating questions
- [~35:00] Shubh Thomas' cybersecurity phishing simulator generating contextually appropriate fake CTO emails with psychological manipulation tactics
- [~45:00] Pastor's TinyTorch platform combining exercises, multi-level AI tutoring, and architecture drawing evaluation -- Hugo calls it better than DataCamp
- [~50:00] Caleb's 3D printing agent generating chess sets and drone assemblies by putting OpenSCAD in Docker as a tool, with automated validation scripts

## Related Sources

- [[deep_research_agent_ivan_leo]] -- Ivan Leo's workshop was directly extended by both Konrad (research assistant) and Caleb (3D printing agent) in their demo day projects
- [[natalia_ines_guest_workshop]] -- Natalia Rodnova led the Prodigy annotation workshop and presents her Jira Assistant at demo day, demonstrating iterative development across cohorts
- [[builders_club_natalia_murat]] -- Natalia's Jira automation project discussed in the Builders Club context before being presented at demo day
- [[ws_3_evals_and_feedback_loops]] -- Michael Powers' Q&A distillation pipeline applies the annotation and evaluation techniques from this workshop at scale
- [[ws_5_context_engineering_and_information_retrieval]] -- The retrieval and embedding techniques underlying Konrad's research assistant and Michael's Q&A consolidation
- [[ws_1_foundations]] -- Modal deployment, introduced by Ben Shababo, used in several demo day projects
