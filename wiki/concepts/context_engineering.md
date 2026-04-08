---
type: concept
title: "Context Engineering"
related_concepts: [prompt_engineering, retrieval_augmented_generation, agents_vs_workflows, agent_harnesses, the_api_call_mental_model, multi_agent_architecture]
---

## Overview

Context engineering is the practice of building the machine that populates the prompt, as distinct from writing prompts by hand. Hugo Bowne-Anderson introduces the distinction in [[ws_5_context_engineering_and_information_retrieval]]: "Context engineering is far more about building the machine that then populates the prompt. We're starting to build the machine, to automate these things." While [[prompt_engineering]] concerns itself with crafting effective instructions, context engineering concerns itself with the automated systems that assemble the right information into the context window at the right time.

The concept represents a shift in how practitioners think about LLM applications. Early in the AI development lifecycle, a human carefully writes a prompt. As systems mature, the prompt is increasingly populated by automated processes -- retrieval systems pulling relevant documents, conversation history managers tracking multi-turn state, memory systems persisting information across sessions, and sub-agents contributing their findings. Andrej Karpathy's definition, cited repeatedly throughout the course, captures this well: "the delicate art and science of filling the context window with just the right information for the next step."

Lance Martin (Anthropic, formerly Langchain) provides the most structured framework, presented in [[ws_7_workflows_multiagent_and_context_engineering]]: four core strategies for managing context. Write -- offload information to scratchpads, files, or databases so it persists beyond the context window. Select -- retrieve relevant context back when needed, through keyword search, embeddings, or structured queries. Compress -- summarize long conversations or documents to fit within context limits. Isolate -- delegate to sub-agents that operate with their own focused context, preventing the main agent from being overwhelmed. These can be combined as three operations: reduce (compress), offload (write + select), and isolate.

Stefan Krawczyk provides a complementary grounding in [[ws_8_finetuning_and_production_ai]], mapping context engineering to the LLM API call: everything that populates the messages array, the system prompt, and the tool results is context engineering. "Skills" -- progressive disclosure of context where the agent reads files to add to its context as needed -- are "just a name for smart context engineering." This demystification connects context engineering to the [[the_api_call_mental_model]] and makes it concrete rather than abstract.

## The Four Strategies: Write, Select, Compress, Isolate

Hugo builds each of Lance Martin's four patterns in Python code during [[ws_7_workflows_multiagent_and_context_engineering]], demonstrating them incrementally in a search agent.

The write strategy addresses a fundamental constraint: LLMs are stateless, and context windows are finite. When an agent discovers important information during a long session, it needs somewhere to put it. Scratchpads (text files the agent writes to and reads from), databases, and the agent's own markdown files serve this purpose. Ivan Leo's deep research agent in [[deep_research_agent_ivan_leo]] uses to-do lists as a write mechanism -- the agent tracks research questions, marks them complete, and uses the list to guide its next actions. A practical subtlety: putting dynamic state in the system prompt breaks prompt caching, so Ivan recommends using tool responses to inject state updates instead.

The select strategy encompasses the full retrieval stack -- from BM25 keyword search through embeddings and vector databases to hybrid search -- covered in depth in [[ws_5_context_engineering_and_information_retrieval]]. The key insight is that retrieval is not a separate concern from context engineering; it is one of the four context engineering strategies. Ravin Kumar's account of Notebook LM's evolution in [[ai_products_google_ravin_kumar]] illustrates how growing context windows changed the select strategy: as Gemini's window grew to 1M tokens, much of Notebook LM's chunking infrastructure could be simplified.

The compress strategy becomes critical for long-running agents. Hugo demonstrates conversation compression in [[ws_7_workflows_multiagent_and_context_engineering]], where a summarizer LLM call condenses the conversation history to fit within context limits while preserving essential information. This is distinct from truncation -- compression preserves semantic content while reducing token count.

The isolate strategy is perhaps the most architecturally significant. Sub-agents each operate with their own focused context, preventing context overload in the main agent. Ivan Leo's deep research agent in [[deep_research_agent_ivan_leo]] exemplifies this: each sub-agent handles a focused research question with limited search iterations, and only the synthesized result flows back to the main orchestrator. This is the mechanism that makes deep research tractable -- without isolation, the main agent's context would quickly fill with raw search results.

## Skills as Progressive Disclosure

The "skills" concept, popularized by Armin Ronacher's Pi agent (the minimal core agent with 4 tools) and OpenClaw (which extends Pi with sessions, cron jobs, channels, sub-agents, and a proactive loop), is reframed by Stefan Krawczyk in [[ws_8_finetuning_and_production_ai]] as a form of context engineering. Skills are "informational and procedural memory encoded in a Markdown file with YAML front matter." Rather than loading all possible instructions into the system prompt at once (which would consume the context window and fight the model's weights), skills are disclosed progressively -- the agent reads relevant skill files only when it encounters a task that requires them.

This progressive disclosure pattern predates the term by years. Stefan notes that "people two years ago doing really fine-tuned context engineering would see this is an obvious pattern." Mike Powers elaborates: skills are "meta-instructions that the harness uses to establish LLM calls with context" -- a loop around context where the skill instructs the agent what step to do next.

## Where Sources Agree

All sources agree that context engineering is distinct from prompt engineering and represents the direction the field is heading. They agree that LLMs are stateless and all memory must be engineered by the developer. They agree that retrieval is a subset of context engineering, not a parallel concern. And they agree that as systems grow more complex, automated context assembly becomes more important than hand-crafted prompts.

## Where Sources Disagree or Add Nuance

The most productive tension is about how much context engineering practitioners actually need to do themselves. Hugo predicts in [[ws_7_workflows_multiagent_and_context_engineering]] that models and APIs (like Gemini's Interactions API) will absorb much of the complexity, so builders may not need extensive context engineering for current applications (customer service, support bots). But as agents move toward higher context and action complexity, this will change. Nicholas Moy's "rip out the harness, let your model be free" advice (as paraphrased by Hugo) from [[ai_products_google_ravin_kumar]] suggests the models themselves are becoming better at managing their own context.

William Horton questions in [[ws_4_testing_and_observability]] whether context engineering is really different from prompt engineering -- a challenge that highlights the blurry boundary between the two. The resolution offered by multiple sources is one of automation: prompt engineering is what a human does; context engineering is building the system that does it automatically.

There is also a tension between simplicity and sophistication. Hugo emphasizes in [[ws_7_workflows_multiagent_and_context_engineering]] that for most current agent applications, you do not need sophisticated context engineering. But Eleanor Berger and Isaac Flaff's best practices (referenced in the same workshop) suggest that actively managing context -- planning with a powerful model, creating to-do lists, writing important things to markdown, starting new sessions -- is essential for long-running coding sessions. The right level of context engineering depends on the application's complexity.

## Related Concepts

- [[prompt_engineering]] -- The human-crafted counterpart; context engineering automates and scales what prompt engineering does manually
- [[retrieval_augmented_generation]] -- Retrieval is the "select" strategy within context engineering; RAG is a specific implementation pattern
- [[agents_vs_workflows]] -- Context engineering patterns differ between workflows (predictable context needs) and agents (dynamic context assembly)
- [[agent_harnesses]] -- Harnesses encompass the tooling and context management surrounding an LLM; skills are progressive disclosure of context
- [[the_api_call_mental_model]] -- Context engineering maps directly to what populates the messages, system prompt, and tool results in the API call
- [[multi_agent_architecture]] -- The "isolate" strategy is fundamental to multi-agent systems, where sub-agents maintain their own focused context

## Sources

- [[ws_2_prompting_and_context]] -- Introduction of context engineering and memory; the distinction from prompt engineering; LLMs as stateless systems
- [[ws_5_context_engineering_and_information_retrieval]] -- Full development of context engineering vs. prompt engineering; retrieval as the "select" strategy
- [[ws_7_workflows_multiagent_and_context_engineering]] -- Lance Martin's four patterns (write, select, compress, isolate); hands-on implementation; forward-looking analysis of agent evolution
- [[ws_8_finetuning_and_production_ai]] -- Skills as progressive disclosure of context; Stefan's API call framework grounding context engineering in the messages array
- [[deep_research_agent_ivan_leo]] -- Sub-agent context isolation, state management via to-do lists, caching strategies for cost control
- [[ai_products_google_ravin_kumar]] -- Notebook LM's retrieval evolution as context windows grew, illustrating how the "select" strategy adapts to new model capabilities
