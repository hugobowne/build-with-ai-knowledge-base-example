# Cross-Cutting Concepts for the Wiki

Extracted from 21 source summaries. Each concept appears in at least 2-3 sources and represents a distinct, meaningful idea that threads across multiple sessions with complementary or contrasting perspectives.

**Reviewed:** Three parallel reviews (coverage gaps, boundary analysis, accuracy spot-check) led to the following changes:
- Added: Five First Principles (#28), Structured Output (#29), Synthetic Data Generation (#30)
- Merged: Comparative Evaluation (#24) absorbed into Evaluation-Driven Development (#1)
- Fixed: Moderna audit attribution (WS-7, not Eric Ma), double entropy confirmed verbatim, dark patterns attribution corrected, LLM-as-judge 66% details corrected
- Boundary clarifications: skills content moved from #23 to #4, workflow primitives folded into #6, problem-first thinking folded into #14

---

1. **Filename:** `evaluation_driven_development.md`
   **Title:** Evaluation-Driven Development
   **Description:** The practice of making evaluation the backbone of the AI software development lifecycle -- from manual "vibes" through failure analysis to automated eval harnesses. Spans the full maturity arc from looking at data in spreadsheets to LLM-as-judge systems calibrated against human experts. Includes comparative evaluation (System A vs. System B) as a key technique — more efficient because people overthink individual ratings but quickly identify which is better (William Horton's strong advocacy; Prodigy's AB/ELO workflows).
   **Sources:**
   - `ws_1_foundations.md` (evaluation as one of five first principles)
   - `ws_3_evals_and_feedback_loops.md` (three-stage eval framework: vibes, failure analysis, automated)
   - `ws_4_testing_and_observability.md` (PyTest/PyTest Harvest for systematic eval data collection)
   - `next_level_evals_stella_eddie.md` (statistical rigor, causal inference, evals as team sport)
   - `builders_club_william_horton.md` (evaluation as the most important AI engineering skill)
   - `william_horton_maven_clinic.md` (LLM-as-judge design and judge alignment in production)
   - `natalia_ines_guest_workshop.md` (annotation pipelines that feed evaluation)
   - `demo_day.md` (students applying eval techniques in projects)

2. **Filename:** `llm_as_judge.md`
   **Title:** LLM-as-Judge
   **Description:** Using LLMs to evaluate other LLM outputs, including when to use code checks first, how to calibrate judges against human labels, the critical role of inter-annotator agreement as a performance ceiling (William Horton: 3 annotators achieved only 66% unanimous agreement on a 12-class intent classification at a previous job — that ceiling limits judge performance), and the paired classifier pattern that determines whether the judge should even apply.
   **Sources:**
   - `ws_3_evals_and_feedback_loops.md` (building an LLM-as-judge for personalized outreach emails)
   - `next_level_evals_stella_eddie.md` (CJ package for calibrating LLM judges to human experts)
   - `william_horton_maven_clinic.md` (judge alignment with two human labelers, 66% agreement ceiling)
   - `ws_8_finetuning_and_production_ai.md` (LLM-as-judge for evaluating alien NPC dialogue fine-tuning)
   - `natalia_ines_guest_workshop.md` (AB evaluation and ELO tournament workflows)

3. **Filename:** `non_determinism.md`
   **Title:** Non-Determinism in AI Systems
   **Description:** The fundamental property that LLM outputs vary across runs, framed as the "double entropy problem" (non-determinism in both inputs and outputs). Not a bug to fix but a property to build systems around -- and in some contexts like deep research and creative writing, a feature to embrace.
   **Sources:**
   - `ws_1_foundations.md` (double entropy problem, building systems around non-determinism)
   - `ws_3_evals_and_feedback_loops.md` (Monte Carlo-style repeated runs as testing strategy)
   - `next_level_evals_stella_eddie.md` (non-determinism as superpower for deep research; hallucination as spectrum)
   - `llm_architecture_rasbt.md` (inference scaling, reasoning traces, temperature and sampling)
   - `ws_2_prompting_and_context.md` (adjustable reasoning effort, model behavioral differences)

4. **Filename:** `context_engineering.md`
   **Title:** Context Engineering
   **Description:** Building the machine that populates the prompt, as distinct from writing prompts by hand. Encompasses four core strategies -- write (offload to scratchpads/files), select (retrieve relevant context), compress (summarize to shrink), and isolate (delegate to sub-agents) -- and represents the shift from human-crafted prompts to automated context assembly. Includes "skills" as progressive disclosure of context (Stefan: "skills is just a name for smart context engineering").
   **Sources:**
   - `ws_2_prompting_and_context.md` (introduction of context engineering and memory)
   - `ws_5_context_engineering_and_information_retrieval.md` (full development of context engineering vs. prompt engineering)
   - `ws_7_workflows_multiagent_and_context_engineering.md` (Lance Martin's four patterns: write, select, compress, isolate)
   - `ws_8_finetuning_and_production_ai.md` (skills as progressive disclosure of context)
   - `deep_research_agent_ivan_leo.md` (sub-agent context isolation, state management, caching)
   - `ai_products_google_ravin_kumar.md` (Notebook LM retrieval evolution as context windows grew)

5. **Filename:** `prompt_engineering.md`
   **Title:** Prompt Engineering
   **Description:** The art and practice of writing effective instructions for LLMs, including 10 principles of effective prompting, the role of iteration counts (8 to 600+ depending on use case), and why prompt engineering is not dead despite claims to the contrary. Addresses the tension between prompt engineering and model training ("fighting the weights").
   **Sources:**
   - `ws_2_prompting_and_context.md` (10 principles, iteration counts, system vs. user prompts)
   - `william_horton_maven_clinic.md` ("beat-it-over-the-head prompting," regex stripping of model safety behaviors)
   - `ws_4_testing_and_observability.md` (prompt tuning in development loops, system prompts fighting the weights)
   - `deep_research_agent_ivan_leo.md` (meta-prompting: models improving their own prompts)
   - `search_agents_john_doug.md` (tool descriptions requiring iteration per provider)

6. **Filename:** `agents_vs_workflows.md`
   **Title:** Agents vs. Workflows
   **Description:** The critical distinction between systems where LLMs dynamically direct their own processes (agents) and systems with predefined code paths (workflows). Most production AI applications are workflows, not agents -- even when stakeholders call them "agents." Includes the agentic spectrum from augmented LLMs through workflows to fully autonomous agents. Also covers workflow building blocks: gates (structured output + if-else), chains (output feeds next call), routers, parallelization, orchestrator-worker pattern, and DAG composition (e.g. Stefan's veterinary transcription system: 60+ LLM calls).
   **Sources:**
   - `ws_6_building_ai_agents.md` (three definitions of agent; when agents vs. workflows)
   - `ws_7_workflows_multiagent_and_context_engineering.md` (Anthropic's taxonomy, agentic spectrum, "Stop Building AI Agents")
   - `ws_7_workflows_multiagent_and_context_engineering.md` (Hugo cites Eric Ma's Moderna audit: everything was workflows, not agents)
   - `william_horton_maven_clinic.md` (multi-agent architecture in production healthcare)
   - `ws_8_finetuning_and_production_ai.md` (production case studies grounding agents/workflows in API calls)
   - `builders_club_william_horton.md` (when agentic solutions make sense; describe inputs/outputs without hype terms)

7. **Filename:** `coding_agents_as_general_purpose_agents.md`
   **Title:** Coding Agents as General-Purpose Computer-Use Agents
   **Description:** The reframing of coding agents from tools that write code to general-purpose agents that can do anything a computer can do via bash. A 125-line Python agent with read, write, edit, and bash tools can organize files, write scripts, self-extend with new tools, and hot-reload capabilities at runtime.
   **Sources:**
   - `ws_3_evals_and_feedback_loops.md` (131-line coding agent demo as teaser)
   - `ws_6_building_ai_agents.md` (building a coding agent from scratch, Pi agent, OpenClaw)
   - `builders_club_brad.md` (coding agents as general-purpose tools, agent self-creating tools)
   - `deep_research_agent_ivan_leo.md` ("isn't every agent a coding agent?")
   - `ws_7_workflows_multiagent_and_context_engineering.md` (models absorbing harnesses via RLVR)

8. **Filename:** `guardrails.md`
   **Title:** Guardrails for AI Systems
   **Description:** Input and output safeguards for AI applications, spanning a three-layer taxonomy: external deterministic (regex, keyword checks), external algorithmic (classifier models like LlamaGuard), and internal alignment (RLHF, fine-tuning). Often simpler than expected -- many production guardrails are just regex or keyword checks.
   **Sources:**
   - `ws_4_testing_and_observability.md` (guardrails demystified as regex/keyword checks, LLM-based for contextual)
   - `katherine_jarmul_privacy.md` (three-layer taxonomy: deterministic, algorithmic, alignment)
   - `william_horton_maven_clinic.md` (production guardrails: off-topic, prompt hacking, self-harm detection)
   - `ws_6_building_ai_agents.md` (agent writing its own guardrails, Simon Willison's lethal trifecta)
   - `ws_8_finetuning_and_production_ai.md` (guardrails as context validation + response validation in the API call)

9. **Filename:** `observability_and_tracing.md`
   **Title:** Observability and Tracing
   **Description:** Logging, monitoring, and tracing AI systems from day zero -- not just in production. OpenTelemetry as the industry standard for instrumentation, with the key insight that AI observability is useful from development (unlike traditional software where it is production-focused). Includes privacy observability as a dimension.
   **Sources:**
   - `ws_1_foundations.md` (logging with SQLite and Datasette from day zero)
   - `ws_4_testing_and_observability.md` (OpenTelemetry as standard, observability from development not just production)
   - `deep_research_agent_ivan_leo.md` (Logfire for agent trace inspection, sub-agent observability)
   - `katherine_jarmul_privacy.md` (privacy observability integrated into general observability)
   - `demo_day.md` (Natalia's Jira Assistant with layered observability)
   - `ws_8_finetuning_and_production_ai.md` (cost of observability as production concern)

10. **Filename:** `retrieval_augmented_generation.md`
    **Title:** Retrieval-Augmented Generation (RAG) and Information Retrieval
    **Description:** Supplementing LLMs with external knowledge through retrieval systems. Covers the full stack from BM25 baselines through embeddings and vector databases to hybrid search, the "Gather and Glean" recall-first framework, why long context windows do not replace RAG, and the progression from naive RAG to agentic retrieval.
    **Sources:**
    - `ws_5_context_engineering_and_information_retrieval.md` (historical retrieval methods, BM25, embeddings, ChromaDB, Gather and Glean)
    - `search_agents_john_doug.md` (wrapping BM25 with agentic intelligence, NDCG evaluation)
    - `ai_products_google_ravin_kumar.md` (Notebook LM retrieval evolution as context windows grew)
    - `ws_7_workflows_multiagent_and_context_engineering.md` (what classic RAG fails at, agentic retrieval patterns)
    - `natalia_ines_guest_workshop.md` (structured RAG: information extraction then retrieval)
    - `deep_research_agent_ivan_leo.md` (multi-step agentic retrieval with sub-agents)

11. **Filename:** `human_in_the_loop.md`
    **Title:** Human-in-the-Loop and Supervised AI
    **Description:** The practice of keeping humans involved in AI system decisions, from annotation and evaluation to supervised agent execution. Encompasses the agency vs. supervision 2x2 framework, progressive rollout strategies, and domain-specific requirements where full automation is premature or dangerous.
    **Sources:**
    - `ws_6_building_ai_agents.md` (agency vs. supervision 2x2, YOLO mode, Simon Willison's lethal trifecta)
    - `william_horton_maven_clinic.md` (supervised mode for health agent, progressive rollout from team to 20% of users)
    - `ws_3_evals_and_feedback_loops.md` (Natalia: 95% is embarrassing in radiology, above 99% target with HITL)
    - `demo_day.md` (Natalia's Jira Assistant in supervised mode)
    - `natalia_ines_guest_workshop.md` (annotating alongside SMEs, model-assisted annotation)
    - `next_level_evals_stella_eddie.md` (human judgment remains essential; fully automated evals would have solved the problem)

12. **Filename:** `annotation_and_data_labeling.md`
    **Title:** Annotation and Data Labeling
    **Description:** The foundational practice of creating labeled data for training and evaluation, including label scheme design principles (factor out business logic), cognitive load reduction (single-label passes are 10x faster), model-assisted annotation, and why annotating alongside your SMEs is essential even if you are not an expert.
    **Sources:**
    - `natalia_ines_guest_workshop.md` (Prodigy, label scheme design, S&P Global case study, structured RAG)
    - `ws_3_evals_and_feedback_loops.md` (manual annotation, confusion matrices, free-text feedback columns)
    - `next_level_evals_stella_eddie.md` (annotation disagreement as organizational problem, benevolent dictator model)
    - `william_horton_maven_clinic.md` (two human labelers for judge calibration, 66% agreement ceiling)

13. **Filename:** `framework_selection.md`
    **Title:** Framework Selection and the Build vs. Buy Decision
    **Description:** How to evaluate AI frameworks by their origin story, whether they optimize for 0-to-1 or 1-to-N, and whether they replace code you do not care about. Includes the debate between thin custom wrappers, established SDKs with LiteLLM gateways, and full frameworks -- with the reconciliation to control the interface and hide the implementation.
    **Sources:**
    - `ws_1_foundations.md` (premature framework adoption, Llama Index hiding internals)
    - `ws_4_testing_and_observability.md` (framework selection criteria, Natalia vs. William vs. Stefan debate)
    - `thinking_tools_eric_ma.md` (opinionated project templates, LiteLLM for provider-agnostic routing)
    - `ws_7_workflows_multiagent_and_context_engineering.md` (Crew AI failing to execute expected tool calls)
    - `deep_research_agent_ivan_leo.md` (building from raw API calls vs. adopting provider SDKs)
    - `ws_8_finetuning_and_production_ai.md` ("it's all just an API call" as the grounding framework)

14. **Filename:** `proof_of_concept_purgatory.md`
    **Title:** Proof-of-Concept Purgatory
    **Description:** The phenomenon where flashy AI demos generate excitement but quickly degrade as teams encounter hallucinations, monitoring challenges, and integration issues. AI flips the traditional software excitement curve -- you get the wow moment first, then fall into difficulty. Escaping purgatory requires evaluation, observability, and systematic iteration. Includes the antidote: problem-first thinking — describe what you want to build without using the word "AI," scope to specific user pain points, understand inputs and outputs before reaching for an LLM (William Horton, Ravin Kumar).
    **Sources:**
    - `ws_1_foundations.md` (central problem definition, inverted excitement curve)
    - `ws_4_testing_and_observability.md` (maintenance costs dominate, cannot set-and-forget)
    - `next_level_evals_stella_eddie.md` (product requirements often missing; teams go straight from prototype to production)
    - `thinking_tools_eric_ma.md` ("you can't know your problem deeply until you've built a wrong solution")
    - `builders_club_brad.md` ("the idea and what you see on Twitter doesn't really line up")
    - `ai_products_google_ravin_kumar.md` (solve people's problems with whatever tools exist, not hype-driven building)

15. **Filename:** `model_selection_and_tradeoffs.md`
    **Title:** Model Selection and Trade-offs
    **Description:** Choosing between models based on capability, latency, cost, and safety behavior. Covers the Pareto frontier from tiny models (270M on Raspberry Pi) through Flash-tier (enterprise workhorse) to frontier reasoning models (too slow for production). Includes the strategy of smart models for planning and cheaper models for execution.
    **Sources:**
    - `ws_2_prompting_and_context.md` (model behavioral differences on identical prompts, Gemini vs. GPT vs. Claude)
    - `ai_products_google_ravin_kumar.md` (Gemma family from 270M to 27B, Flash vs. Pro strategy)
    - `william_horton_maven_clinic.md` (Gemini Flash for latency, GPT-5.4 Mini for health, smarter models for lead agents)
    - `deep_research_agent_ivan_leo.md` (start with best model, optimize downward; "spend today for models of tomorrow")
    - `llm_architecture_rasbt.md` (hybrid architectures, inference scaling, reasoning effort levels)
    - `ws_8_finetuning_and_production_ai.md` (when fine-tuning vs. prompting vs. retrieval)

16. **Filename:** `tool_calling_and_function_calling.md`
    **Title:** Tool Calling and Function Calling
    **Description:** The mechanism by which LLMs interact with external tools -- the LLM returns a function name and arguments as text, and the developer parses, executes, and returns results. Includes the surprising complexity of making this work across providers, the role of tool descriptions, and MCP as a distribution protocol for tools.
    **Sources:**
    - `ws_6_building_ai_agents.md` (function calling mechanics, Gemini fails where GPT succeeds)
    - `deep_research_agent_ivan_leo.md` (tool runtime abstraction, JSON replacing XML parsing)
    - `builders_club_natalia_murat.md` (MCP explained and debated, when plain tool calling suffices)
    - `ws_8_finetuning_and_production_ai.md` (MCP as tool schema population in the API call framework)
    - `ai_products_google_ravin_kumar.md` (Function Gemma for local tool-calling/routing)
    - `william_horton_maven_clinic.md` (tool-call checks as primary evaluation, agent date awareness via dedicated tool)

17. **Filename:** `multi_agent_architecture.md`
    **Title:** Multi-Agent Architecture
    **Description:** Designing systems with multiple specialized agents that coordinate through a lead/orchestrator agent. Covers delegation patterns (direct user response vs. through lead agent), parallel vs. sequential execution, Conway's Law for agents, latency penalties per delegation, and sub-agent context isolation.
    **Sources:**
    - `builders_club_william_horton.md` (multi-agent as hardest problem, Conway's Law for agents, latency concerns)
    - `william_horton_maven_clinic.md` (lead agent routing to sub-agents for appointments, health, provider search)
    - `ws_7_workflows_multiagent_and_context_engineering.md` (orchestrator-worker pattern, parallelization, context isolation)
    - `deep_research_agent_ivan_leo.md` (dynamic sub-agent spawning with iteration limits)
    - `ws_8_finetuning_and_production_ai.md` (veterinary transcription: 60+ LLM calls in a DAG)

18. **Filename:** `fine_tuning_and_distillation.md`
    **Title:** Fine-Tuning and Distillation
    **Description:** Training or adapting models for specific tasks, increasingly a last resort as better prompting and retrieval handle most use cases. Remaining valid cases: small models on edge devices, unique data not in training corpora (dolphin communication), and distillation for cost reduction. Includes LoRA, QLoRA, and the practical insight that overfitting can be desirable for style enforcement.
    **Sources:**
    - `ws_8_finetuning_and_production_ai.md` (when fine-tuning makes sense, hands-on Gemma 270M, distillation)
    - `llm_architecture_rasbt.md` (PEFT, LoRA, QLoRA, training data quality)
    - `ai_products_google_ravin_kumar.md` (Dolphin Gemma, Function Gemma, small model demand)
    - `natalia_ines_guest_workshop.md` (use LLMs to build the system rather than being the system; train smaller models)

19. **Filename:** `privacy_and_security.md`
    **Title:** Privacy and Security in AI Systems
    **Description:** Protecting user data and system integrity in AI applications, spanning legal (GDPR, HIPAA), technical (pseudonymization, differential privacy), and system-level concerns (system prompt exfiltration, memorization attacks). Includes the practical advice that system prompts should be treated as public and that conversational data is qualitatively more sensitive than clickstream data.
    **Sources:**
    - `katherine_jarmul_privacy.md` (three-category privacy framework, red teaming, federated learning)
    - `ws_6_building_ai_agents.md` (Simon Willison's lethal trifecta, YOLO mode, agent safety)
    - `william_horton_maven_clinic.md` (healthcare guardrails, HIPAA, prompt injection on day one)
    - `builders_club_natalia_murat.md` (local models for sensitive data, data sensitivity motivating architecture)

20. **Filename:** `vibe_coding_and_ai_assisted_development.md`
    **Title:** Vibe Coding and AI-Assisted Development
    **Description:** The spectrum from pure vibe coding (generating code without understanding) to structured AI-assisted development with specs, tests, and architectural control. Includes the debate about whether abstraction layers make understanding optional, the danger of "opusmaxing" without structure, and the pattern of using specs and tests as double constraints for coding agents.
    **Sources:**
    - `builders_club_brad.md` (Jeremy Howard critique, Carol Willing on abstraction layers, Hugo on dark patterns in AI-generated e-commerce components)
    - `thinking_tools_eric_ma.md` (undoing vibecoded slop, spec-driven development, feedback loops with Cypress tests)
    - `ws_4_testing_and_observability.md` (Stefan's development loops, framework selection for maintainability)
    - `search_agents_john_doug.md` (live pair programming with Claude Code, spectrum from vibe coding to incremental progress)

21. **Filename:** `the_api_call_mental_model.md`
    **Title:** The API Call as the Atomic Unit
    **Description:** Stefan Krawczyk's unifying framework: everything in AI engineering reduces to understanding the LLM API call (system prompt, messages, tools, structured output). Every buzzword maps to specific parts of this call -- RAG populates context, MCP populates tools, guardrails validate context and responses, skills are progressive disclosure of context. A powerful tool for cutting through hype.
    **Sources:**
    - `ws_1_foundations.md` (API calls as first of five first principles)
    - `ws_8_finetuning_and_production_ai.md` (Stefan's masterclass mapping buzzwords to API components)
    - `ws_4_testing_and_observability.md` (per-LLM-call evaluation, debugging depends on what you send)
    - `builders_club_natalia_murat.md` (MCP and RAG seeming simple once you understand the basics)

22. **Filename:** `production_ai_patterns.md`
    **Title:** Production AI Patterns
    **Description:** Practical patterns for deploying and maintaining AI systems in production, including the two-loop model (inner development + outer production), progressive rollout strategies, provider fallbacks, cost management, voice agent architecture (STT + LLM + TTS), and the insight that maintenance costs dominate setup costs -- just like traditional software.
    **Sources:**
    - `ws_4_testing_and_observability.md` (two-loop model, CI/CD for AI, maintenance costs)
    - `ws_8_finetuning_and_production_ai.md` (veterinary transcription DAG, restaurant voice agent, provider fallbacks)
    - `william_horton_maven_clinic.md` (progressive rollout, first-day surprises, real user data)
    - `ws_1_foundations.md` (build-deploy-monitor-evaluate cycle, Modal deployment)
    - `demo_day.md` (multiple projects using Modal for deployment)
    - `builders_club_brad.md` (Modal deployment workshop, Discord bot deployment)

23. **Filename:** `agent_harnesses.md`
    **Title:** Agent Harnesses
    **Description:** The tooling, context management, and state tracking that surrounds an LLM in an agent system. Whether "harness" is useful terminology or marketing jargon is debated. Models are absorbing harnesses via RLVR, causing labs to "rip out their harnesses" with each new model release. (Skills content moved to Context Engineering #4.)
    **Sources:**
    - `ws_4_testing_and_observability.md` (agent harness debate: useful term vs. marketing jargon)
    - `ws_7_workflows_multiagent_and_context_engineering.md` (models absorbing harnesses via RLVR, Kirby analogy)
    - `ws_8_finetuning_and_production_ai.md` (skills as progressive disclosure of context, MCP/A2A via API call)
    - `ws_6_building_ai_agents.md` (Pi agent, OpenClaw, agent self-extension)
    - `ai_products_google_ravin_kumar.md` ("rip out the harness, let your model be free")

24. **MERGED into #1 (Evaluation-Driven Development)** — Comparative evaluation absorbed as a subsection.

25. **Filename:** `llm_architecture_and_inference.md`
    **Title:** LLM Architecture and Inference Scaling
    **Description:** The architectural developments underpinning modern LLMs: attention mechanism evolution (multi-head to MLA to sparse), KV cache optimization, hybrid architectures mixing attention with linear layers, and inference scaling (longer reasoning chains, parallel sampling, adjustable reasoning effort). Provides the "why" behind model behaviors that builders observe.
    **Sources:**
    - `llm_architecture_rasbt.md` (full architecture deep dive, hybrid trend, RLVR)
    - `ws_2_prompting_and_context.md` (adjustable reasoning effort, chain-of-thought in the age of reasoning models)
    - `ai_products_google_ravin_kumar.md` (Gemma family, context window evolution, Flash vs. Pro)
    - `deep_research_agent_ivan_leo.md` (model selection, caching strategies, "spend today for models of tomorrow")
    - `ws_8_finetuning_and_production_ai.md` (Software 2.0, neural network mechanics for fine-tuning)

26. **Filename:** `ai_sdlc.md`
    **Title:** The AI Software Development Lifecycle
    **Description:** The overarching framework for the course: build, deploy, monitor, evaluate, iterate. Encompasses five first principles (API calls, non-determinism, logging/tracing, evaluation, rapid iteration), the two-loop model (development + production), and the insight that AI systems are "organic" and require gardener-like ongoing attention rather than set-and-forget deployment.
    **Sources:**
    - `ws_1_foundations.md` (five first principles, build-deploy-monitor-evaluate cycle)
    - `ws_4_testing_and_observability.md` (two-loop model, CI/CD for AI, maintenance costs dominate)
    - `ws_8_finetuning_and_production_ai.md` (course recap, full lifecycle coverage)
    - `william_horton_maven_clinic.md` (agent development lifecycle from prototype to production)
    - `next_level_evals_stella_eddie.md` (evals as compass and gate in the product development cycle)
    - `demo_day.md` (students applying the full lifecycle)

27. **Filename:** `domain_specific_ai.md`
    **Title:** Domain-Specific AI Applications
    **Description:** How AI application patterns vary across domains -- healthcare demands above 99% accuracy with human-in-the-loop, legal discovery prioritizes recall over precision, e-commerce demands precision in top results. Acceptable error rates, regulatory requirements (HIPAA, BAAs), and the gap between general-purpose demos and domain-specific production requirements.
    **Sources:**
    - `william_horton_maven_clinic.md` (healthcare: clinical accuracy, self-harm detection, benefits exclusion)
    - `ws_3_evals_and_feedback_loops.md` (Natalia: 95% embarrassing in radiology, above 99% target)
    - `search_agents_john_doug.md` (legal discovery demands recall, e-commerce demands precision)
    - `next_level_evals_stella_eddie.md` (regulated industries add compliance dimension to evals)
    - `natalia_ines_guest_workshop.md` (S&P Global commodities trading, crime report extraction)
    - `builders_club_natalia_murat.md` (medical scribe prototyping, surgeon building PDF tools)

28. **Filename:** `five_first_principles.md`
    **Title:** Five First Principles for AI Software Development
    **Description:** The foundational framework for the entire course, introduced in Workshop 1 and referenced throughout. The five principles: (1) API calls as the atomic unit (input/output with knobs like temperature and reasoning effort), (2) non-determinism — the "double entropy problem" with entropy in both inputs and outputs, (3) logging, monitoring, and tracing from day zero, (4) evaluation — look at your data, quantify performance, is it good or bad?, (5) rapid iteration using prompt engineering, tool use, and business logic changes. Hugo frames AI systems as "organic" — constantly shifting, requiring gardener-like attention.
    **Sources:**
    - `ws_1_foundations.md` (primary source: all five principles laid out systematically)
    - `ws_3_evals_and_feedback_loops.md` (evaluation principle in depth)
    - `ws_4_testing_and_observability.md` (logging/tracing and iteration principles in depth)
    - `ws_8_finetuning_and_production_ai.md` (course recap, principles revisited)
    - `william_horton_maven_clinic.md` (double entropy problem referenced by name)

29. **Filename:** `structured_output.md`
    **Title:** Structured Output and JSON Mode
    **Description:** Constraining LLM responses to conform to a schema — JSON mode (guarantees valid JSON) vs. structured output (guarantees schema compliance via Pydantic). A foundational building block that bridges evaluation (is the output valid?), workflow design (structured output as gate/intermediate representation between pipeline stages), and guardrails (guardrails often use structured output). Includes the parallelization trick: run multiple structured extractions in parallel and aggregate for higher accuracy than a single call.
    **Sources:**
    - `ws_1_foundations.md` (structured output as core component of API call anatomy)
    - `ws_2_prompting_and_context.md` (JSON mode vs. structured output distinction, timeline)
    - `ws_6_building_ai_agents.md` (structured output as first step in LinkedIn-to-email workflow)
    - `ws_7_workflows_multiagent_and_context_engineering.md` (structured output as gate mechanism, parallelization for accuracy)
    - `ws_8_finetuning_and_production_ai.md` (mapped as API call component in Stefan's masterclass)
    - `william_horton_maven_clinic.md` (guardrails and judges all use structured output)
    - `ws_4_testing_and_observability.md` (contextual guardrails via structured output)

30. **Filename:** `synthetic_data_and_simulation.md`
    **Title:** Synthetic Data Generation and Conversation Simulation
    **Description:** Using LLMs to generate training data, evaluation datasets, and simulated user conversations. Covers distillation (generating training examples cheaply from larger models), synthetic eval dataset creation for retrieval testing, multi-turn conversation simulation (requiring a third "moderator" component to detect when conversations should end — neither the agent LLM nor the user LLM wants to stop talking), and model-assisted annotation as a form of synthetic pre-labeling.
    **Sources:**
    - `ws_8_finetuning_and_production_ai.md` (distillation: 14,000 examples for $5; restaurant voice agent synthetic menu dialogues)
    - `william_horton_maven_clinic.md` (multi-turn conversation simulation with moderator pattern)
    - `ws_5_context_engineering_and_information_retrieval.md` (synthetic queries for RAG evaluation)
    - `natalia_ines_guest_workshop.md` (model-assisted annotation, generative hypothesis sentences)
    - `ws_4_testing_and_observability.md` (iterative dataset curation, parameterized test runs)
