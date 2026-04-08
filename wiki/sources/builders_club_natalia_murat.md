---
type: builders_club
title: "Natalia & Murat Builders Club: MCP Servers, PDF Organization, and When Not to Use New Tools"
date: 2026-03-26
speakers: [Natalia Rodnova, Hugo Bowne-Anderson, Murat Bilici, Anonymized Student Y, Anonymized Student X, Pastor Soto]
topics: [MCP, Model Context Protocol, PDF processing, local models, Qwen, Google AI Studio, Jira automation, tool calling, when to use MCP]
source_file: raw/_cleaned/builders_club_natalia_murat_bilici_march_26_2026.md
word_count: ~8300
---

## Overview

This Builders Club session features an informal but substantive discussion covering three main threads: Murat's PDF organization project using local models, Hugo's introduction to MCP (Model Context Protocol) with live demos, and a rich debate about when new tools like MCP are actually necessary versus overhyped.

Murat shares his ongoing project to organize a decades-old collection of 150,000+ files (PDFs, ebooks, scientific publications) on his NAS using multi-agent tools and local models (Qwen 3 4B and 12B). He describes iterating five rounds to improve classification precision, running everything locally in Docker containers due to data sensitivity. Hugo suggests DeepSeek OCR as a potential improvement for PDF processing, noting that frontier models handle PDFs far better than smaller local ones.

Anonymized Student X demonstrates a rapid prototype of a medical scribe application built in Google AI Studio in under 5 minutes using Gemini's new native audio dialogue capabilities, creating a clinical note generation tool with roleplay scenarios. Anonymized Student Y shares an article he wrote about LLM tooling that garnered attention for its accessible explanations of concepts like tool calling versus MCP.

Hugo then delivers an MCP tutorial, explaining the protocol as a unified interface (analogized to USB-C) that lets LLMs access tools and data that others have built. MCP is also explained via the API call mental model in [[ws_8_finetuning_and_production_ai]]. He demonstrates an MCP server he built on Hugging Face for the LLMOps database (15,000+ entries), showing it working in Claude Code. A critical discussion follows about when MCP is actually necessary: Hugo argues you only need to build an MCP server when you want to distribute tools and data to external users, not for personal use. Natalia, Pastor, and Anonymized Student Y push back and forth on this, reaching consensus that MCP is often overhyped and that plain tool calling suffices for most personal or team use cases.

## Key Topics

- PDF document processing challenges with local models
- MCP (Model Context Protocol) explained and demonstrated
- When to build MCP servers versus using plain tool calling
- Google AI Studio for rapid prototyping
- Local model deployment for sensitive data
- The hype cycle around new AI tools and knowing when to use what
- Jira automation as a practical AI application

## Key Insights

- MCP servers are primarily useful for distributing tools and data to external users; for personal or team use, plain tool calling is simpler and sufficient. Tool calling mechanics are covered in depth in [[ws_6_building_ai_agents]] and [[deep_research_agent_ivan_leo]]
- PDF processing with small local models remains a challenging, unsolved problem; frontier models or specialized OCR models (DeepSeek OCR) may be needed for good results. [[thinking_tools_eric_ma]] also addresses PDF ingestion challenges for scientific papers
- The ability to distinguish when to use new tools versus when existing approaches suffice is what separates average from top-tier AI engineers
- Google AI Studio enables rapid prototyping that can produce working demos in minutes
- RAG and MCP are examples of concepts that seem complex to outsiders but straightforward once you understand the basics
- Experimentation with new tools has value even when you don't strictly need them, as it builds intuition for future use cases

## People & Tools Mentioned

- Murat Bilici -- surgeon transitioning to AI, building PDF organization system with Qwen models
- Anonymized Student X -- medical professional building clinical note generation tools
- Anonymized Student Y -- writing accessible LLM tooling articles, DS/ML mentor
- Philip Carter -- Honeycomb/Salesforce, mentioned for MCP server limitations
- Brian Bischoff -- Theory Ventures, podcast on MCP and distribution
- Alex Strick -- ZenML, LLMOps database creator
- Google AI Studio, Gemini 2.5 Pro/Flash, Qwen 3, DeepSeek OCR, Proton Mail, Stitch, FastMCP, Gradio

## Quotable Moments

- "That differentiates, like, an average AI engineer with a top-end AI engineer. It's like knowing when to use what. That's like gold." -- Anonymized Student Y [~50:00]
- "I just built it because I wanted to. Which is a beautiful dog, because I wanted to try." -- Natalia Rodnova on building an MCP server [~30:00]
- "It's a protocol for letting LLMs access tools that other people have built. Now, I just want to be clear, this promise breaks down a lot when you try to build something real." -- Hugo Bowne-Anderson [~25:00]
- "I build a RAG app, and I'm like, what is a big deal? What people are talking about? It's like, you got embeddings, and you calculate similarity, and that's it?" -- Natalia Rodnova [~50:00]

## Highlights

- [~05:00] Murat's detailed account of iterating five rounds on PDF organization with local models, revealing the real-world complexity of document processing at scale
- [~10:00] Anonymized Student X's rapid 5-minute prototype of a medical scribe in Google AI Studio -- a concrete example of how fast prototyping works with new tools
- [~25:00] Hugo's MCP tutorial with USB-C analogy and live demo of querying the LLMOps database through Claude Code
- [~30:00] Natalia's honest admission that she built an MCP server "because I wanted to" even though she could have used plain tool calling, sparking a productive debate
- [~45:00] Rich group discussion on when MCP adds value versus when it is overhead, with Pastor, Anonymized Student Y, and Natalia all offering different perspectives on the hype cycle
- [~50:00] Anonymized Student Y's insight about the distinction between experimenting broadly and knowing when to go deep on specific tools being the hardest and most valuable skill in the field

## Related Sources

- [[ws_6_building_ai_agents]] -- Covers tool calling mechanics in depth, which is the simpler alternative to MCP that the group concluded suffices for most personal use cases
- [[ws_8_finetuning_and_production_ai]] -- Stefan Krawczyk explains MCP via the "it's all just an API call" framework, grounding the protocol in the LLM API structure
- [[deep_research_agent_ivan_leo]] -- Ivan Leo's workshop demonstrates tool calling and tool runtime abstractions, the practical alternative to MCP for custom agent building
- [[thinking_tools_eric_ma]] -- Eric Ma also discusses PDF ingestion challenges; his LiteLLM-based provider-agnostic routing relates to Murat's local model work
- [[demo_day]] -- Natalia's Jira Assistant, which she presents at demo day, uses tool calling rather than MCP, validating the group's conclusion
- [[natalia_ines_guest_workshop]] -- Natalia Rodnova also leads the Prodigy annotation workshop, bringing her practical builder perspective
