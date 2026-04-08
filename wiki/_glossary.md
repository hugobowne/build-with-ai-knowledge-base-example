# Glossary

Key terms used across this knowledge base, with brief definitions and links to the concept articles that cover them. Intended for someone new to the course material.

---

## A

**A2A (Agent-to-Agent Protocol)**
Google's protocol for agents to communicate with each other. Mapped as a tool-schema population mechanism in the API call framework. See [[the_api_call_mental_model]], [[agent_harnesses]].

**Agentic Spectrum**
The continuum from augmented LLMs (LLM + tools) through structured workflows to fully autonomous agents. Most production systems sit closer to the workflow end. See [[agents_vs_workflows]].

**Agent Harness**
The tooling, context management, and state tracking that surrounds an LLM in an agent system. Models are absorbing harnesses via RLVR. See [[agent_harnesses]].

**Annotation**
The process of labeling data for training or evaluation. Includes label scheme design, model-assisted annotation, and the principle of annotating alongside your SMEs. See [[annotation_and_data_labeling]].

**API Call (LLM)**
The atomic unit of AI engineering: system prompt + messages + tools + structured output, with knobs for temperature and reasoning effort. Every AI buzzword maps to a part of this call. See [[the_api_call_mental_model]], [[five_first_principles]].

## B

**BM25**
A classical keyword-based retrieval algorithm. Still a strong baseline -- search agents wrap BM25 with agentic intelligence rather than replacing it. See [[retrieval_augmented_generation]].

**Build vs. Buy**
The decision framework for AI tools and frameworks: build custom wrappers, adopt SDKs with LiteLLM gateways, or use full frameworks. Control the interface, hide the implementation. See [[framework_selection]].

## C

**Chain-of-Thought (CoT)**
A prompting technique where the model reasons step by step before producing a final answer. Reasoning models internalize this. See [[prompt_engineering]], [[llm_architecture_and_inference]].

**ChromaDB**
An open-source vector database used in the course for embedding-based retrieval. See [[retrieval_augmented_generation]].

**Coding Agent**
An LLM-based agent with read, write, edit, and bash tools that can function as a general-purpose computer-use agent. A 125-line Python implementation can self-extend with new tools. See [[coding_agents_as_general_purpose_agents]].

**Comparative Evaluation**
Evaluating by comparing System A vs. System B rather than rating individually. People overthink absolute ratings but quickly identify which is better. Includes A/B and ELO tournament patterns. See [[evaluation_driven_development]].

**Context Engineering**
Building the machine that populates the prompt, as distinct from hand-crafting prompts. Four strategies: write, select, compress, isolate. See [[context_engineering]].

**Context Window**
The maximum amount of text an LLM can process in a single call. Growing windows reduce but do not eliminate the need for retrieval. See [[retrieval_augmented_generation]], [[llm_architecture_and_inference]].

**Conway's Law (for Agents)**
The observation that multi-agent architectures tend to mirror the organizational structure of the team that builds them. See [[multi_agent_architecture]].

## D

**Datasette**
A tool for exploring SQLite databases. Used in the course for inspecting logged LLM interactions from day zero. See [[observability_and_tracing]].

**Deep Research Agent**
An agent that performs multi-step research by spawning sub-agents, gathering information iteratively, and synthesizing results. Ivan Leo's guest talk builds one from scratch. See [[coding_agents_as_general_purpose_agents]], [[multi_agent_architecture]].

**Differential Privacy**
A mathematical framework for quantifying privacy guarantees when sharing data or model outputs. See [[privacy_and_security]].

**Distillation**
Generating training data from a larger (more expensive) model to fine-tune a smaller (cheaper) model. Example: 14,000 training examples for $5. See [[fine_tuning_and_distillation]], [[synthetic_data_and_simulation]].

**Double Entropy Problem**
Hugo's framing of non-determinism in AI: entropy in both inputs (users say unpredictable things) and outputs (models respond non-deterministically). See [[non_determinism]], [[five_first_principles]].

## E

**Embeddings**
Dense vector representations of text used for semantic similarity search. A core component of RAG pipelines. See [[retrieval_augmented_generation]].

**Evaluation-Driven Development**
Making evaluation the backbone of the AI SDLC. Three-stage maturity: vibes, failure analysis, automated eval harnesses. See [[evaluation_driven_development]].

## F

**Federated Learning**
Training models across distributed datasets without centralizing data. A privacy-preserving approach. See [[privacy_and_security]].

**Fine-Tuning**
Adapting a pre-trained model for a specific task. Increasingly a last resort as prompting and retrieval handle most cases. See [[fine_tuning_and_distillation]].

**Five First Principles**
The foundational framework: (1) API calls, (2) non-determinism, (3) logging/tracing, (4) evaluation, (5) rapid iteration. See [[five_first_principles]].

**Flash-Tier Models**
Mid-range models optimized for speed and cost (e.g., Gemini Flash). The enterprise workhorse -- fast enough for production, capable enough for most tasks. See [[model_selection_and_tradeoffs]].

**Function Calling**
The mechanism by which LLMs invoke external tools -- the model returns a function name and arguments as text, the developer parses, executes, and returns results. See [[tool_calling_and_function_calling]].

## G

**Gather and Glean**
A recall-first retrieval framework: gather broadly (maximize recall), then glean (filter and rank). See [[retrieval_augmented_generation]].

**Guardrails**
Input and output safeguards for AI systems. Three layers: deterministic (regex, keyword), algorithmic (classifier models like LlamaGuard), alignment (RLHF, fine-tuning). See [[guardrails]].

**GDPR**
EU General Data Protection Regulation. Relevant to AI systems processing personal data. See [[privacy_and_security]].

## H

**HIPAA**
US Health Insurance Portability and Accountability Act. Sets requirements for healthcare AI systems including BAAs (Business Associate Agreements). See [[privacy_and_security]], [[domain_specific_ai]].

**Human-in-the-Loop (HITL)**
Keeping humans involved in AI system decisions -- from annotation to supervised agent execution. See [[human_in_the_loop]].

**Hybrid Search**
Combining keyword-based (BM25) and semantic (embedding) retrieval for better results than either alone. See [[retrieval_augmented_generation]].

## I

**Inference Scaling**
Improving model performance at inference time by using more compute -- longer reasoning chains, parallel sampling, adjustable reasoning effort. See [[llm_architecture_and_inference]].

**Inter-Annotator Agreement**
The degree to which human annotators agree on labels. Sets a ceiling for LLM-as-judge performance: if humans agree only 66% of the time, the judge cannot reliably exceed that. See [[llm_as_judge]], [[annotation_and_data_labeling]].

## J

**JSON Mode**
An LLM output mode that guarantees syntactically valid JSON but does not enforce a specific schema. Contrast with structured output. See [[structured_output]].

## K

**KV Cache**
Key-Value cache that stores intermediate computation during autoregressive generation. Optimization target for efficient inference. See [[llm_architecture_and_inference]].

## L

**Lethal Trifecta**
Simon Willison's warning: access to private data + ability to take actions + exposure to untrusted input = dangerous agent. See [[guardrails]], [[privacy_and_security]].

**LiteLLM**
A gateway that provides a unified interface across LLM providers, enabling provider-agnostic routing. See [[framework_selection]], [[model_selection_and_tradeoffs]].

**LLM-as-Judge**
Using one LLM to evaluate outputs from another. Requires calibration against human labels and a paired classifier to determine applicability. See [[llm_as_judge]].

**Logfire**
An observability tool used for agent trace inspection and sub-agent monitoring. See [[observability_and_tracing]].

**LoRA / QLoRA**
Low-Rank Adaptation / Quantized LoRA. Parameter-efficient fine-tuning methods that train a small number of added parameters rather than the full model. See [[fine_tuning_and_distillation]].

## M

**MCP (Model Context Protocol)**
Anthropic's protocol for distributing tool schemas to LLMs. Populates the tools field of the API call. See [[tool_calling_and_function_calling]], [[the_api_call_mental_model]].

**Meta-Prompting**
Having models improve their own prompts through iterative self-refinement. See [[prompt_engineering]].

**MLA (Multi-Latent Attention)**
A compressed attention variant (used in DeepSeek) that reduces KV cache size. Part of the evolution of attention mechanisms. See [[llm_architecture_and_inference]].

**Modal**
A cloud platform for deploying AI applications. Used throughout the course for deployment examples. See [[production_ai_patterns]].

**Monte Carlo Evaluation**
Running the same prompt multiple times and analyzing the distribution of outputs to handle non-determinism. See [[non_determinism]], [[evaluation_driven_development]].

**Multi-Agent Architecture**
Systems with multiple specialized agents coordinated by a lead/orchestrator agent. See [[multi_agent_architecture]].

## N

**NDCG (Normalized Discounted Cumulative Gain)**
A retrieval quality metric that measures ranking quality with position-weighted scoring. See [[retrieval_augmented_generation]].

## O

**OpenTelemetry (OTel)**
The industry standard for instrumenting, generating, collecting, and exporting telemetry data. The recommended observability foundation for AI systems. See [[observability_and_tracing]].

**Orchestrator-Worker Pattern**
A multi-agent pattern where one orchestrator agent delegates tasks to specialized worker agents. See [[multi_agent_architecture]], [[agents_vs_workflows]].

## P

**Paired Classifier Pattern**
A pattern where a classifier first determines whether an LLM-as-judge should even apply to a given output, reducing irrelevant judgments. See [[llm_as_judge]].

**Pareto Frontier (Model Selection)**
The curve of optimal trade-offs between capability, latency, and cost when choosing models. See [[model_selection_and_tradeoffs]].

**PEFT (Parameter-Efficient Fine-Tuning)**
Fine-tuning methods (LoRA, QLoRA, etc.) that train only a fraction of model parameters. See [[fine_tuning_and_distillation]].

**PoC Purgatory**
See Proof-of-Concept Purgatory.

**Prodigy**
Ines Montani's annotation tool. Supports model-assisted annotation, AB evaluation, and ELO tournament workflows. See [[annotation_and_data_labeling]], [[evaluation_driven_development]].

**Progressive Rollout**
Deploying AI features to increasingly larger user groups (e.g., internal team, then 20% of users, then all). See [[production_ai_patterns]], [[human_in_the_loop]].

**Prompt Engineering**
Writing effective instructions for LLMs. Includes 10 principles, iteration counts, and the relationship to context engineering. See [[prompt_engineering]].

**Proof-of-Concept Purgatory**
The gap between a dazzling demo and a production system. AI flips the traditional excitement curve -- wow moment first, then difficulty. See [[proof_of_concept_purgatory]].

**Pseudonymization**
Replacing personally identifiable information with artificial identifiers. A privacy-preserving technique. See [[privacy_and_security]].

## R

**RAG (Retrieval-Augmented Generation)**
Supplementing LLMs with external knowledge through retrieval. Spans BM25 through embeddings to hybrid search and agentic retrieval. See [[retrieval_augmented_generation]].

**RLHF (Reinforcement Learning from Human Feedback)**
A training technique that aligns model behavior with human preferences. Part of the alignment layer of guardrails. See [[guardrails]], [[fine_tuning_and_distillation]].

**RLVR (Reinforcement Learning with Verifiable Rewards)**
A training technique where models learn from automatically verifiable outcomes (e.g., code execution, math proofs). Causes models to absorb capabilities that previously required external harnesses. See [[agent_harnesses]], [[llm_architecture_and_inference]].

## S

**Skills (in Agent Systems)**
Progressive disclosure of context -- making additional instructions and tools available to an agent based on task requirements. "Skills is just a name for smart context engineering." See [[context_engineering]], [[agent_harnesses]].

**Software 2.0**
The paradigm where behavior is defined by neural network weights rather than explicit code. See [[llm_architecture_and_inference]], [[fine_tuning_and_distillation]].

**Structured Output**
Constraining LLM responses to conform to a specific schema (e.g., via Pydantic). Stronger than JSON mode -- guarantees schema compliance, not just valid JSON. See [[structured_output]].

**Synthetic Data**
Data generated by LLMs for training, evaluation, or testing purposes. Includes distillation, synthetic eval datasets, and conversation simulation. See [[synthetic_data_and_simulation]].

## T

**Temperature**
A parameter controlling randomness in LLM output. Higher temperature = more varied responses. Part of the API call knobs. See [[the_api_call_mental_model]], [[non_determinism]].

**Tool Calling**
See Function Calling.

**Two-Loop Model**
The development lifecycle model: an inner loop (development: prompt, test, iterate) and an outer loop (production: deploy, monitor, evaluate, iterate). See [[ai_sdlc]], [[production_ai_patterns]].

## V

**Vector Database**
A database optimized for storing and querying high-dimensional vectors (embeddings). ChromaDB is the example used in the course. See [[retrieval_augmented_generation]].

**Vibe Coding**
Generating code with AI without fully understanding it. The opposite end of the spectrum from spec-driven AI-assisted development. See [[vibe_coding_and_ai_assisted_development]].

**Voice Agent Architecture**
The STT + LLM + TTS pipeline for building conversational voice agents. See [[production_ai_patterns]].

## Y

**YOLO Mode**
Running an agent with minimal or no human oversight. Contrasted with supervised/human-in-the-loop execution. See [[human_in_the_loop]], [[guardrails]].

---

See also: [[_index]] (master landing page) / [[_map_of_content]] (concepts by theme) / [[_source_registry]] (all sources)
