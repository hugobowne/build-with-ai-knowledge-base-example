# AI Software Development Lifecycle -- Knowledge Base

From the fifth and final quarter of [Building AI Applications for Data Scientists and Software Engineers -- from First Principles](https://maven.com/hugo-stefan/building-ai-apps-ds-and-swe-from-first-principles) on Maven.

A wiki distilled from 21 sessions (~341,000 words) of workshops, guest talks, builders clubs, and demo day (March--April 2026).

---

## Navigation

| File | Purpose |
|------|---------|
| [[_map_of_content]] | Concepts grouped by theme -- the conceptual landscape |
| [[_glossary]] | Key terms defined with links to concept articles |
| [[_source_registry]] | All 21 sources with type, date, speakers, word count |
| [[_concept_list]] | Full concept extraction log with source mappings |

---

## Concepts by Cluster

### Foundations and Mental Models
The bedrock ideas that frame everything else in the course.

- [[five_first_principles|Five First Principles for AI Software Development]]
- [[the_api_call_mental_model|The API Call as the Atomic Unit]]
- [[ai_sdlc|The AI Software Development Lifecycle]]
- [[non_determinism|Non-Determinism in AI Systems]]
- [[proof_of_concept_purgatory|Proof-of-Concept Purgatory]]

### Prompting, Context, and Retrieval
How information gets into the model -- from hand-crafted prompts to automated retrieval pipelines.

- [[prompt_engineering|Prompt Engineering]]
- [[context_engineering|Context Engineering]]
- [[retrieval_augmented_generation|Retrieval-Augmented Generation (RAG) and Information Retrieval]]
- [[structured_output|Structured Output and JSON Mode]]

### Evaluation and Data Quality
Measuring whether AI systems work -- and building the datasets to prove it.

- [[evaluation_driven_development|Evaluation-Driven Development]]
- [[llm_as_judge|LLM-as-Judge]]
- [[annotation_and_data_labeling|Annotation and Data Labeling]]
- [[synthetic_data_and_simulation|Synthetic Data Generation and Conversation Simulation]]

### Agents, Tools, and Multi-Agent Systems
Building systems where LLMs take actions, use tools, and coordinate with each other.

- [[agents_vs_workflows|Agents vs. Workflows]]
- [[coding_agents_as_general_purpose_agents|Coding Agents as General-Purpose Computer-Use Agents]]
- [[tool_calling_and_function_calling|Tool Calling and Function Calling]]
- [[multi_agent_architecture|Multi-Agent Architecture]]
- [[agent_harnesses|Agent Harnesses]]

### Production, Safety, and Operations
Getting AI systems into production and keeping them running safely.

- [[production_ai_patterns|Production AI Patterns]]
- [[guardrails|Guardrails for AI Systems]]
- [[observability_and_tracing|Observability and Tracing]]
- [[human_in_the_loop|Human-in-the-Loop and Supervised AI]]
- [[privacy_and_security|Privacy and Security in AI Systems]]

### Models, Architecture, and Training
Understanding what is inside the models and when to change them.

- [[model_selection_and_tradeoffs|Model Selection and Trade-offs]]
- [[llm_architecture_and_inference|LLM Architecture and Inference Scaling]]
- [[fine_tuning_and_distillation|Fine-Tuning and Distillation]]

### Engineering Practice
How practitioners actually build, choose tools, and write code with AI.

- [[framework_selection|Framework Selection and the Build vs. Buy Decision]]
- [[vibe_coding_and_ai_assisted_development|Vibe Coding and AI-Assisted Development]]
- [[domain_specific_ai|Domain-Specific AI Applications]]

---

## Sources by Type

### Workshops (8)

| # | Source | Speakers |
|---|--------|----------|
| 1 | [[ws_1_foundations|WS 1: Foundations of the AI SDLC]] | Hugo Bowne-Anderson, Stefan Krawczyk, Ben Shababo |
| 2 | [[ws_2_prompting_and_context|WS 2: LLM APIs, Prompt Engineering, and Context Engineering]] | Hugo Bowne-Anderson |
| 3 | [[ws_3_evals_and_feedback_loops|WS 3: AI Evals and Software Feedback Loops]] | Hugo Bowne-Anderson |
| 4 | [[ws_4_testing_and_observability|WS 4: Testing, Observability, and Production AI]] | Stefan Krawczyk, Hugo Bowne-Anderson |
| 5 | [[ws_5_context_engineering_and_information_retrieval|WS 5: Context Engineering and Information Retrieval]] | Hugo Bowne-Anderson, Pastor Soto, William Horton, Carol Willing + others |
| 6 | [[ws_6_building_ai_agents|WS 6: Building AI Agents]] | Hugo Bowne-Anderson, Pastor Soto, Anonymized Student Y, Natalia Rodnova + others |
| 7 | [[ws_7_workflows_multiagent_and_context_engineering|WS 7: LLM Workflows, Multi-Agent Systems, and Context Engineering]] | Hugo Bowne-Anderson, Pastor Soto, Anonymized Student Y, Carol Willing + others |
| 8 | [[ws_8_finetuning_and_production_ai|WS 8: Fine-Tuning and Production AI Applications]] | Hugo Bowne-Anderson, Stefan Krawczyk, Pastor Soto, Anonymized Student Y + others |

### Guest Talks (10)

| Source | Speaker(s) |
|--------|------------|
| [[next_level_evals_stella_eddie|Next Level Evals in 2026]] | Stella Liu, Eddie Wharton |
| [[ai_products_google_ravin_kumar|Building AI Products at Google]] | Ravin Kumar |
| [[search_agents_john_doug|Building Search Agents]] | John Berryman, Doug Turnbull |
| [[llm_architecture_rasbt|LLM Architecture Developments in 2026]] | Sebastian Raschka |
| [[natalia_ines_guest_workshop|Ground Truth for AI Evals: Annotation Pipelines]] | Ines Montani, Natalia Rodnova |
| [[deep_research_agent_ivan_leo|Build Your Own Deep Research Agent]] | Ivan Leo |
| [[william_horton_maven_clinic|Maven Clinic's AI Health Agent]] | William Horton |
| [[katherine_jarmul_privacy|Privacy in AI]] | Katharine Jarmul |
| [[thinking_tools_eric_ma|Building Tools for Thinking with AI]] | Eric Ma |
| [[builders_club_william_horton|William Horton Builders Club]] | William Horton |

### Builders Clubs (3)

| Source | Speaker(s) |
|--------|------------|
| [[builders_club_brad|Brad Morris Builders Club]] | Brad W Morris |
| [[builders_club_natalia_murat|Natalia & Murat Builders Club]] | Natalia Rodnova, Murat Bilici |
| [[builders_club_william_horton|William Horton Builders Club]] | William Horton |

### Demo Day (1)

| Source | Description |
|--------|-------------|
| [[demo_day|Demo Day]] | Student projects showcasing AI-powered applications across domains |

---

*29 concept articles / 21 source summaries / ~341,000 words distilled*
