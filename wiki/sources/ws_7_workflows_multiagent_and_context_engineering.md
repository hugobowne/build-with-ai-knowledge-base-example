---
type: workshop
title: "Workshop 7: LLM Workflows, Multi-Agent Systems, and Context Engineering"
date: 2025-03-30
speakers: [Hugo Bowne-Anderson, Pastor Soto, Anonymized Student Y, Carol Willing, Caleb Tutty, Anonymized Student X, Ilona Brinkmeier, Charles Pepe-Ranney, Ryan Rodriguez]
topics: [LLM workflows, multi-agent systems, agentic spectrum, context engineering, workflow patterns, prompt chaining, routing, parallelization, evaluator-optimizer, agent evals, Crew AI, agent failure modes, agentic retrieval, context writing, context selection, context compression, context isolation, sub-agents, AI autonomy, two cultures of agents]
source_file: raw/_cleaned/WS-7.md
word_count: ~21223
---

## Overview

Workshop 7 marks a strategic pivot in the course, focusing on when and how to use LLM workflows versus fully-fledged agents, and diving deep into context engineering patterns for agentic retrieval. Hugo opens by reflecting on [[deep_research_agent_ivan_leo]] (Ivan is now at DeepMind working on Gemini, previously at Manus which was acquired by Meta), and highlighting key patterns from it: meta-prompting, swapping tool calls in real time, to-do lists, and isolating context. This workshop builds on the agent foundations from [[ws_6_building_ai_agents]] and the retrieval foundations from [[ws_5_context_engineering_and_information_retrieval]].

The first major section covers the agentic spectrum. Hugo presents Anthropic's taxonomy (LLMs, augmented LLMs, workflows, agents) and provides concrete rules of thumb: use an LLM for text generation, an augmented LLM or workflow for retrieval/tools/multi-step predefined tasks, and an agent only when the LLM needs to control multi-step tasks and adapt dynamically. He shares his essay "Stop Building AI Agents" (which hit #1 on Hacker News) and explains his evolving position: agents can shine, but only inside testable, observable systems. The models have gotten dramatically better at agentic tasks due to RLVR.

The workshop then walks through Anthropic's workflow patterns (prompt chaining, routing, parallelization, orchestrator-worker, evaluator-optimizer) with live code examples using the LinkedIn structured-output-to-email pipeline. A notable discussion emerges around Carol Willing's practice of having multiple LLMs audit code files in parallel, which Hugo connects to Karpathy's LLM Council.

The second half addresses what classic retrieval fails at (summarization queries, multi-document comparison, multi-step reasoning) and introduces agentic retrieval patterns: hello world summary tools, tool calling for metadata-rich context, and agent reasoning loops with orchestrators and workers. Hugo then presents Lance Martin's four context engineering strategies -- write, select, compress, and isolate -- and builds each pattern in Python code in a GitHub Codespace, demonstrating scratchpads, keyword-based context selection, conversation compression, and sub-agent context isolation.

The workshop concludes with a forward-looking analysis of where agents sit on a context-complexity vs. action-complexity 2x2, predicting that all agents will move toward higher context and action complexity, but that models and APIs (like Gemini's Interactions API) will absorb much of that complexity.

## Key Topics

- Agentic spectrum: LLM to augmented LLM to workflow to agent
- When to stop building agents (and when to start)
- Anthropic workflow patterns: chaining, routing, parallelization, orchestrator-worker, evaluator-optimizer
- "Stop Building AI Agents" essay and the evolving case for agents
- Two cultures of AI agents: high agency with/without supervision
- Agent failure modes: observability, brittle systems, complexity creep, misaligned autonomy
- What classic RAG fails at (summarization, comparison, multi-step queries)
- Agentic retrieval patterns: summary tools, metadata tool calling, reasoning loops
- Context engineering: write, select, compress, isolate (Lance Martin's patterns)
- Hands-on implementation of context engineering in Python
- Agent evals: end-to-end evaluation, error analysis, transition failure matrices
- Models absorbing harnesses via RLVR (reinforcement learning with verifiable rewards)
- Karpathy's LLM Council for parallel LLM auditing
- Forward-looking analysis of agent evolution and abstraction layers

## Key Insights

- Most of the time, when you think you need an agent, a workflow will suffice. Eric Ma's audit at Moderna found everything was a workflow -- though that has since changed. See [[thinking_tools_eric_ma]] for Eric's perspective on building tools for thinking with AI.
- The distinction between workflow and agent can be blurry. You can have agentic components embedded in workflows (e.g., an email generator with an inner evaluation loop within a deterministic pipeline).
- Hugo's "Stop Building AI Agents" position evolved: the concern was never about AI autonomy per se, but about AI autonomy without a human in the loop in the right way. High agency + strong supervision = powerful (Cursor, Claude Code, deep research). See [[ws_6_building_ai_agents]] for the agency vs. supervision 2x2 framework and [[william_horton_maven_clinic]] for supervised mode in production healthcare AI.
- Agent skills are "informational and procedural memory encoded in a Markdown file with YAML front matter" -- a term that encompasses tool calls, scripts, MCP access, and sub-agents.
- Crew AI, despite being a nice framework, failed to execute the expected number of tool calls (median 4-5 out of 9 requested across 100 runs). Abstractions can hide failures.
- Context engineering has four core strategies (from Lance Martin): write (offload to scratchpads/files/databases), select (retrieve relevant context back), compress (summarize to shrink), and isolate (delegate to sub-agents with their own context). These can be combined as three: reduce (compress), offload (write + select), and isolate.
- For most current agent applications (customer service, support bots), you don't need sophisticated context engineering. But as agents move toward higher context and action complexity, this will change.
- The best practice for long-running coding sessions is not to wait for compaction but to actively manage context: plan with a powerful model, create a to-do list, execute with a smaller model, write important things to agent's markdown, and start new sessions.

## People & Tools Mentioned

- Ivan Leo -- deep research agent workshop; now at DeepMind, formerly at Manus; meta-prompting and to-do list patterns
- Lance Martin (Anthropic, formerly Langchain) -- four context engineering patterns: write, select, compress, isolate
- Andrej Karpathy -- LLM Council for parallel auditing; LLMs as operating systems analogy (context window = RAM); auto research
- Anthropic -- "Building Effective AI Agents" blog post; "How We Built Our Multi-Agent Research System"
- Carol Willing -- practice of having 3 LLMs audit code in parallel
- Samuel Colvin (Pydantic) -- observability
- Alex (ZenML) -- LLM Ops database of 1,500+ production deployments; rollout patterns
- Hamel Husain -- evaluation blog post and practices
- Crew AI -- framework example showing tool call reliability issues
- Kura -- Ivan Leo's framework for clustering agent traces
- Clio -- Anthropic's internal tool for trace analysis
- Eleanor Berger and Isaac Flaff (Elite AI Assisted Coding) -- context management best practices
- Gemini Interactions API -- future abstraction for state management and tool orchestration

## Quotable Moments

- "I wrote an essay called Stop Building AI Agents. It hit number one on Hacker News... The world was awash with, let's build agents, and I was like, can we stop building these?" -- Hugo Bowne-Anderson [~30:00]
- "Agent is a marketing term as well as a somewhat technical term, just as AI was." -- Hugo Bowne-Anderson [~45:00]
- "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." -- Karpathy, cited by Hugo [~100:00]
- "Models are getting so good at agentic tasks because they're being trained on agent traces... Labs rip out their harnesses with each new model release. Doug referred to this as Kirby from Nintendo -- the models absorb the harnesses around them." -- Hugo Bowne-Anderson [~35:00]
- "Get users as soon as possible. And get their feedback, and iterate on that." -- Ravin Kumar (DeepMind), on agent evals, cited by Hugo [~80:00]

## Highlights

- [~25:00] Hugo presents the evaluator-optimizer pattern and Caleb raises practical concerns: you need very good exit conditions to avoid infinite loops, and it may not be the first pattern you reach for -- pull it in after seeing production behavior. Hugo shares his personal use: an evaluator loop on Gemini outputs for blog posts before his human editing pass.

- [~30:00] Hugo's nuanced evolution on "Stop Building AI Agents" -- from telling people to stop, to recognizing the hypocrisy (he used agents daily while saying this), to understanding the real issue was AI autonomy without proper human-in-the-loop design.

- [~45:00] Sharp exchange about "agent" as a marketing term. Ilona raises the tension between using Crew AI to create workflows that are marketed as agents. Hugo and Carol agree this is common and acceptable -- the term means different things to builders vs. stakeholders, and picking battles on terminology is pragmatic.

- [~55:00] Carol Willing shares her practice of having 3 different LLMs audit code files in parallel, which Hugo connects to Karpathy's LLM Council. Raises interesting questions about ensemble approaches to code review.

- [~65:00] Agent failure modes deep dive, illustrated with Crew AI. Hugo ran a specific test 100 times where he requested 9 search tool calls -- the median result was only 4-5 tool calls completed. Also discovered Crew AI had installed Lite LLM under the hood without transparency.

- [~90:00] Concrete limitations of classic RAG that motivate agentic retrieval: "what are these docs about?" (needs summary tool), comparing techniques across documents (needs multiple searches + comparison), and multi-step reasoning queries like "what are the three foundation models? Give me detail on the second one."

- [~105:00] Live coding of context engineering patterns. Hugo builds scratchpad (write), keyword-based selection (select), conversation compression (compress), and sub-agent isolation -- demonstrating each pattern incrementally in a search agent. The date injection fix (the LLM didn't know its own date) is a practical illustration of why system instructions matter.

- [~130:00] Forward-looking 2x2 analysis: most current agents are low-context, low-action complexity (customer service, support bots), while cultural attention focuses on coding agents and deep research. Hugo predicts all agents will move up and to the right but believes models and APIs will absorb the complexity, so builders may not need to do extensive context engineering themselves.

- [~140:00] Rich philosophical discussion between Hugo, Carol, Anonymized Student Y, and Ryan about the pace of AI change. Carol argues the velocity isn't as different from previous tech shifts as it seems -- what's different is how quickly hype propagates. Ryan notes the feedback loop where AI improves itself. Hugo references Nassim Taleb: looking at AI daily is looking at noise.

## Related Sources

- [[deep_research_agent_ivan_leo]] -- Ivan Leo's workshop that Hugo reflects on at the start of this session; the sub-agent context isolation pattern is formalized here as one of Lance Martin's four strategies
- [[ws_6_building_ai_agents]] -- The preceding agents workshop covering agent definitions, function calling, and the agency vs. supervision framework that this workshop extends into workflows and multi-agent patterns
- [[ws_5_context_engineering_and_information_retrieval]] -- The retrieval foundations that this workshop extends into agentic retrieval patterns and the four context engineering strategies
- [[builders_club_william_horton]] -- William Horton's discussion of multi-agent architecture challenges at Maven Clinic, which this workshop addresses with systematic workflow and orchestration patterns
- [[thinking_tools_eric_ma]] -- Eric Ma's Moderna audit referenced here; his LLM Council implementation in Canvas Chat relates to Karpathy's LLM Council discussed in this session
- [[ws_8_finetuning_and_production_ai]] -- The next workshop where Stefan Krawczyk grounds the concepts from this workshop (MCP, skills, harnesses) in the "it's all just an API call" framework
