---
type: person
name: "Stefan Krawczyk"
role: "Co-Instructor / Creator of Hamilton and Burr"
organization: "Salesforce"
category: instructor
---

## Appearances

- [[ws_1_foundations]] — Co-instructor; introduced AI SDLC foundations alongside [[hugo_bowne_anderson]]
- [[ws_4_testing_and_observability]] — Primary instructor; taught two-loop model (inner development + outer production), PyTest/PyTest Harvest for LLM testing, OpenTelemetry, framework selection criteria, and guardrails
- [[ws_8_finetuning_and_production_ai]] — Primary instructor for production section; presented veterinary transcription case study (60+ LLM calls) and restaurant voice agent, delivered "it's all just an API call" masterclass

## Key Contributions

- Created the two-loop mental model for AI development (inner development loop for local testing + outer production loop for deployed telemetry feeding back into development)
- Delivered the "it's all just an API call" framework that demystifies every AI buzzword by mapping it to the LLM API structure: RAG populates context, MCP populates tools, guardrails validate inputs/outputs, skills are progressive disclosure of context
- Developed framework selection criteria: evaluate by origin story, 0-to-1 vs. 1-to-N optimization, and whether the framework replaces code you do not care about
- Built Apache Hamilton (DAG framework for LLM workflows) and Apache Burr (agent orchestration), both used in production case studies

## Notable Quotes

- "If you really want to get your performance for your app really good, then you have to think of it on an LLM, per LLM call basis." — [[ws_4_testing_and_observability]]
- "Remember, everything we do in this course is really around an API call... a lot of people forget that fact, and part of it is all the vendors want to sell you something." — [[ws_8_finetuning_and_production_ai]]
- "Agent harness -- to me, is marketing jargon that people use to sell to execs." — [[ws_4_testing_and_observability]]
