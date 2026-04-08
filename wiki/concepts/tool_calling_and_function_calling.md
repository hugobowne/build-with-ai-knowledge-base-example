---
type: concept
title: "Tool Calling and Function Calling"
related_concepts: [agents_vs_workflows, the_api_call_mental_model, coding_agents_as_general_purpose_agents, model_selection_and_tradeoffs, context_engineering, structured_output]
---

## Overview

Tool calling (also called function calling) is the mechanism by which LLMs interact with external systems -- databases, APIs, code execution environments, search engines, and any other capability beyond text generation. The fundamental mechanics are deceptively simple: the developer describes available tools in the API call, the LLM returns a function name and arguments as structured text, and the developer parses, executes the function, and sends the results back to the LLM. But the course reveals that making this work reliably across providers, evaluating whether tools were called correctly, and scaling from single tools to complex multi-tool agents introduces surprising complexity.

Hugo provides the definitive treatment in [[ws_6_building_ai_agents]], walking through function calling mechanics with both OpenAI and Gemini and revealing a striking difference: the same tool description works on GPT-5 but fails on Gemini 2.5 Flash, requiring prompt iteration per provider. This cross-provider inconsistency is a recurring theme. Ivan Leo in [[deep_research_agent_ivan_leo]] explains the evolution from XML tag parsing to JSON tool calls, showing how structured JSON output replaced earlier, more brittle approaches to tool invocation. William Horton in [[william_horton_maven_clinic]] uses binary tool-call checks -- did the agent call the right tool? -- as his primary evaluation metric, finding that this simple check covers most cases before resorting to more expensive LLM-as-judge evaluations.

The concept extends into MCP (Model Context Protocol), which multiple sources discuss as a distribution protocol for tools. Stefan Krawczyk in [[ws_8_finetuning_and_production_ai]] maps MCP to the tool schema population component of the API call, while the Builders Club discussion in [[builders_club_natalia_murat]] concludes that MCP is primarily useful for distributing tools to external users -- for personal or team use, plain tool calling suffices. Ravin Kumar in [[ai_products_google_ravin_kumar]] introduces Function Gemma, a 270M parameter model adapted for local tool-calling and routing, demonstrating that even tiny models can serve as tool-calling routers.

## The Mechanics of Tool Calling

The core insight that Hugo emphasizes in [[ws_6_building_ai_agents]] is that the LLM does not execute tools -- it returns text that describes which tool to call and with what arguments. The developer is responsible for parsing this text, executing the actual function, and sending the results back. SDKs abstract this cycle but reduce visibility into what is happening. Hugo characterizes function calling as "gnarly" precisely because the abstraction is leaky: the LLM's ability to generate correct function calls depends on the quality of tool descriptions, the model's training on function-calling patterns, and the specific formatting expectations of each provider.

Ivan Leo provides the historical context in [[deep_research_agent_ivan_leo]]: tool calling originally relied on XML tag parsing, where developers instructed the model to wrap tool calls in XML tags and then parsed the output with regex. The shift to native JSON tool calling -- where the model returns structured JSON conforming to a schema -- was a significant reliability improvement. Ivan builds a tool runtime abstraction in his deep research agent that cleanly separates tool definitions from execution, demonstrating how good engineering patterns make tool calling manageable even in complex multi-agent systems.

The cross-provider inconsistency that Hugo demonstrates is practically important. Gemini 2.5 Flash fails at function calling where GPT-5 succeeds with identical tool descriptions. Hugo notes that even within the same provider family, Gemini 3 Flash Preview works where Gemini 2.5 fails. This means tool descriptions require iteration per provider -- a form of provider-specific prompt engineering that adds maintenance burden. William Horton's pragmatic response in [[william_horton_maven_clinic]] is to match models to tasks: using models that are reliable at tool calling for tasks that depend on it, and falling back to different models when tool-calling reliability is critical.

## Tool Descriptions and Agent Ergonomics

Tool descriptions are effectively prompts for the model, and they require the same iterative refinement. Hugo demonstrates in [[ws_6_building_ai_agents]] that tool descriptions require iteration per provider -- the same description works on GPT-5 but fails on Gemini 2.5 Flash. Ivan Leo in [[deep_research_agent_ivan_leo]] introduces meta-prompting for this purpose: asking the model itself to improve its own tool descriptions and prompts, a technique he notes "wouldn't have been possible a year or two ago."

William Horton's experience at Maven Clinic in [[william_horton_maven_clinic]] reveals a particularly instructive pattern: the agent was given a dedicated "Day of Week for Date" tool because LLMs are unreliable at calendar reasoning. Rather than trying to fix the model's internal capabilities, the team externalized the computation into a tool. This exemplifies the broader principle that tool calling bridges the gap between what LLMs can reason about and what they cannot -- instead of fighting the weights, you give the model a tool that handles the computation deterministically.

The distinction between "context" (information in the prompt) and "capability" (tools the agent can execute) that Ivan Leo articulates in [[deep_research_agent_ivan_leo]] is fundamental to designing tool-calling systems. Context tells the model what it knows; tools tell it what it can do. Good agent design requires thoughtful decisions about which information belongs in context and which should be accessible through tool calls.

## MCP as a Distribution Protocol

MCP (Model Context Protocol) emerges as a topic of significant discussion and some disagreement. Hugo introduces it in [[builders_club_natalia_murat]] as "a protocol for letting LLMs access tools that other people have built," analogizing it to USB-C as a unified interface. Stefan Krawczyk in [[ws_8_finetuning_and_production_ai]] maps it precisely onto the API call: MCP populates the tool schema section of the call. This demystifies the protocol -- it is a standardized way to describe tools so that different LLM clients can discover and use them.

The practical debate centers on when MCP adds value versus when it is overhead. The consensus in [[builders_club_natalia_murat]] is that MCP servers are primarily useful for distributing tools and data to external users. For personal or team use, plain tool calling is simpler and sufficient. Natalia Rodnova admits she built an MCP server "because I wanted to" even though she could have used plain tool calling, and Anonymized Student Y observes that knowing when to use what "differentiates an average AI engineer with a top-end AI engineer." Hugo adds a reality check: "This promise breaks down a lot when you try to build something real."

## Evaluation and Reliability

Tool calling evaluation is simpler than many assume, at least at the first level. William Horton in [[william_horton_maven_clinic]] finds that binary tool-call checks -- did the agent call the expected tool with the expected arguments? -- cover most evaluation needs. This is a reference-based metric that can be checked with code, without needing an LLM judge. Only for subjective criteria (was the response appropriately empathetic? was it clinically accurate?) does he escalate to more expensive evaluation approaches.

The reliability dimension is critical for production systems. Hugo's Crew AI test in [[ws_7_workflows_multiagent_and_context_engineering]] -- requesting 9 tool calls and getting a median of 4-5 across 100 runs -- demonstrates that tool calling reliability can be surprisingly poor even with well-designed frameworks. This makes systematic evaluation of tool calling essential and argues for simpler tool interfaces: as Hugo observes in [[ws_6_building_ai_agents]], "if you have a handful of tools, they can do a huge number of things."

## Where Sources Agree

All sources agree that tool calling is the fundamental mechanism enabling agents and that understanding its mechanics -- rather than relying on SDK abstractions -- is important for debugging. There is consensus that tool descriptions require iteration per provider, that binary tool-call checks are an effective first-level evaluation, and that the LLM returning text (not executing tools directly) is a key mental model. The mapping of MCP to tool schema population in the API call is accepted as the clearest explanation of the protocol.

## Where Sources Disagree or Add Nuance

The sources diverge on how much the cross-provider inconsistency matters in practice. Hugo treats it as a significant concern requiring per-provider testing; William Horton's approach is more pragmatic, choosing models that happen to be reliable for the tool-calling tasks he needs. The value of MCP is actively debated -- Stefan's API call mapping makes it seem simple, but Hugo and Natalia both note that the reality of building and using MCP servers is rougher than the concept suggests. The question of whether models will eventually internalize tool-calling reliability (making provider inconsistencies disappear) or whether this will remain a persistent engineering challenge is open. Ravin Kumar's Function Gemma suggests that specialized fine-tuning for tool calling is one path forward, while improvements in base model training (RLVR on agent traces) suggest another.

## Related Concepts

- [[agents_vs_workflows]] -- Tool calling is what makes agents possible; an agent is essentially an LLM calling tools in a loop
- [[the_api_call_mental_model]] -- Tool schemas are a specific component of the API call that Stefan maps buzzwords onto
- [[coding_agents_as_general_purpose_agents]] -- The bash tool transforms a coding agent into a general-purpose agent; tool design determines agent capability
- [[model_selection_and_tradeoffs]] -- Different models have different tool-calling reliability; model selection must account for this
- [[structured_output]] -- Tool calls return structured data; structured output and tool calling are complementary mechanisms
- [[context_engineering]] -- The distinction between information in context and capabilities available through tools is fundamental to agent design

## Sources

- [[ws_6_building_ai_agents]] -- The definitive tool calling session: function calling mechanics with OpenAI and Gemini, cross-provider differences, building search and coding agents with tools
- [[deep_research_agent_ivan_leo]] -- Tool runtime abstraction, JSON replacing XML parsing, meta-prompting for tool descriptions, and the context vs. capability distinction
- [[builders_club_natalia_murat]] -- MCP explained and debated; when plain tool calling suffices versus when MCP adds value; the hype cycle around new tools
- [[ws_8_finetuning_and_production_ai]] -- MCP mapped to tool schema population in the API call framework; skills as progressive disclosure of context via tool results
- [[ai_products_google_ravin_kumar]] -- Function Gemma as a 270M model for local tool-calling and routing, demonstrating specialized tiny models for tool selection
- [[william_horton_maven_clinic]] -- Tool-call checks as primary evaluation metric; the "Day of Week for Date" tool for externalizing unreliable LLM computation; model selection based on tool-calling reliability
