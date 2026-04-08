---
type: workshop
title: "Workshop 3: AI Evals and Software Feedback Loops"
date: March 2026
speakers: [Hugo Bowne-Anderson]
topics: [AI evaluation, evals, failure analysis, LLM-as-judge, reference-based metrics, reference-free metrics, annotation, ground truth, confusion matrix, factual inconsistency detection, comparative evaluation, automated eval harnesses, agent demo]
source_file: raw/_cleaned/WS-3.md
word_count: ~21200
---

## Overview

Workshop 3 is devoted entirely to AI evaluation ("evals"), which Hugo frames as the systematic measurement of application quality that guides the entire AI software development lifecycle. This workshop builds on the eval principles from [[ws_1_foundations]] and connects to the deeper eval methodology in [[next_level_evals_stella_eddie]]. The session progresses through three stages of evaluation maturity: vibes (looking at data manually), failure analysis (systematic error categorization), and automated evaluation (code checks and LLM-as-judge). Hugo emphasizes that evals are not a one-time activity but will permeate every remaining workshop in the course.

Before diving into evals, Hugo gives an agentic teaser by live-demoing a 131-line general-purpose coding agent with 4 tools (read, write, edit, bash) that organizes a messy desktop folder. This same agent is demonstrated in [[builders_club_brad]] and built step-by-step in [[ws_6_building_ai_agents]]. He frames coding agents as "general-purpose computer-using agents that are great at writing code" and argues that the bash tool enables anything a computer can do. The demo nearly fails due to exhausted API credits, providing a memorable teaching moment.

The eval content distinguishes reference-based metrics (where ground truth exists, testable with code checks) from reference-free metrics (subjective quality, requiring LLM judges or human annotation). The hands-on portion walks through a factual inconsistency detection dataset from Hugging Face, where Hugo manually annotates 50 summary pairs, achieves 92% accuracy against ground truth, then analyzes his errors to discover that he favored summaries that were "factually accurate but broad" while ground truth favored specific but cryptic summaries. This error analysis drives the creation of two competing prompts (brevity vs. nuance), which split 50/50 in a head-to-head comparison, demonstrating how prompt synthesis emerges from failure analysis. The workshop concludes with building an LLM-as-judge for evaluating personalized outreach emails based on LinkedIn profiles.

## Key Topics

- The three stages of evaluation: vibes, failure analysis, automated evaluation
- Reference-based vs. reference-free metrics
- Manual annotation in spreadsheets
- Confusion matrices for measuring annotator performance
- Error analysis and failure mode categorization
- Building and aligning LLM-as-judge evaluators
- Comparative evaluation vs. single-item evaluation
- Automated eval harnesses (structure and purpose)
- General-purpose coding agents (agentic teaser with live demo)
- The emerging importance of annotation pipelines

## Key Insights

- Evals are "the systematic measurement of application quality" -- not just spreadsheets or gold datasets, as clarified by Shreya, Hamel, and Brian after the 2025 backlash against evals
- Most people focus on changing system behavior without evaluating or debugging first, which prevents improvement (Hamel Hussein's insight)
- Ground truth labels should themselves be interrogated -- Hugo's error analysis showed the "correct" summaries were sometimes cryptic and incomplete
- Comparative evaluation (choosing between two outputs) is more efficient than single-item pass/fail labeling because people overthink individual ratings but can quickly identify which is better (William Horton's key insight)
- Even when both options are bad, choosing the better one reveals what you are looking for
- Free-text feedback columns alongside structured labels become some of the most useful data, often generating new structured criteria for future annotation rounds
- Code-based checks should handle everything they can before resorting to LLM judges -- regex for string matching, length checking, and structured output validation are cheaper and more reliable
- The agent demo's API credit failure illustrates a real production concern: monitoring costs and having fallback strategies
- For acceptable pass rates: Natalia says 95% is "embarrassing" in radiology (aiming above 99% with human-in-the-loop), while Hugo notes coding assistants were accepted well below 80% before November 2025 model improvements

## People & Tools Mentioned

- **Hugo Bowne-Anderson** -- instructor, live-demos both the agent and the eval workflow
- **Charles Pepe-Ranney** -- computational biologist, opens session discussing Karpathy's auto-research loop and agent skills as eval examples
- **William Horton** -- advocates strongly for comparative evaluation, free-text feedback columns
- **Natalia Rodnova** -- shares radiology domain perspective (95% is embarrassing, aiming above 99%)
- **Anonymized Student X** -- discusses precision/recall for reference-based metrics, medical note evaluation
- **Anonymized Student Y** -- asks about trust and verification for agent outputs
- **Joey** -- asks about multi-agent orchestration at Kubernetes-scale, declarative configurations
- **Franklin** -- raises question about evaluating image content in summaries
- **Murat Bilici** -- contributes redundancy as a summary quality criterion
- **Ryan Rodriguez** -- software engineer at Evolution IQ (insurance), discusses LLM determinism and batch-size effects
- **Carol Willing** -- compares eval pass rates to code coverage; parallels to race conditions in distributed systems
- **Michael Powers** -- describes feedback-loop pattern where annotations refine generated FAQ artifacts
- **Hamel Hussein & Shreya Shankar** -- referenced extensively; "Your AI Product Needs Evals" post; eval skills for coding agents; 25% discount for their evals course
- **Eugene Yan** (Amazon) and **Brian Bischoff** (Theory Ventures) -- Hugo's four key evals teachers
- **Karpathy** -- auto-research loop referenced by Charles
- **Stella Liu** (ASU) and **Eddie Landersberg** (CMO Labs) -- upcoming guest talk on next-gen AI evals (see [[next_level_evals_stella_eddie]])
- **Prodigy** -- annotation tool from Explosion AI, used in [[natalia_ines_guest_workshop]]
- **Hugging Face** -- factual inconsistency dataset sourced from

## Quotable Moments

- "We should stop thinking of them as coding agents. We should start thinking of them as general-purpose computer-using agents that are great at writing code." -- Hugo Bowne-Anderson [~15:00]
- "It's about your tolerance for risk... You build trust with these systems, and you figure out what you need to verify and what you don't, just as you do with an intern or a colleague." -- Hugo Bowne-Anderson [~25:00]
- "Making people compare and choose the better one is a more efficient way of labeling... In the end, your choice is always just gonna be, do I deploy System A or System B?" -- William Horton [~105:00]
- "In our business, when we work with people's health, 99% accuracy is great, but it's not awesome. 95% is the lowest -- embarrassing, almost." -- Natalia Rodnova [~125:00]
- "I would prefer to receive an incorrect positive diagnosis and then find out otherwise than receive an incorrect negative diagnosis and not find out." -- Hugo Bowne-Anderson [~130:00]

## Highlights

- [~10:00-25:00] Live demo of 131-line general-purpose coding agent. The demo almost fails due to exhausted API credits, requiring Hugo to add credits in real-time. When it works, the agent organizes a messy desktop from 32 scattered items into 6 organized folders. Anonymized Student Y's follow-up question about verification trust becomes a natural bridge into evals. Hugo's key framing: "With a bash tool, you're able to do absolutely anything that a computer can do."

- [~30:00-40:00] The three-stage eval framework laid out: vibes to failure analysis to automated evaluation. Reference-based vs. reference-free metrics explained with concrete examples (was the correct tool called? vs. did the assistant have a helpful tone?). Anonymized Student X contributes precision/recall discussion for medical note evaluation.

- [~90:00-105:00] Hugo walks through his own annotation errors on the factual inconsistency dataset. His confusion matrix (92% accuracy) reveals he systematically preferred broad, contextual summaries over the ground truth's specific but cryptic ones. This drives creation of two competing prompts (brevity vs. nuance) that split 50/50, demonstrating how error analysis concretely drives prompt iteration.

- [~105:00-115:00] Rich debate on comparative vs. single-item evaluation. William Horton makes a strong case for comparative evaluation as more efficient and more practical ("your choice is always System A or System B"). Hugo's counter: "What if they're both bad?" William: "Even if they're both bad, trying to figure out which one's better can still reveal something of value." The free-text feedback column discussion that follows is a practical gem.

- [~125:00-140:00] Extended discussion on acceptable pass rates across domains. Natalia shares radiology perspective (above 99% target, always human-in-the-loop). Carol Willing draws parallel to code coverage. Ryan Rodriguez raises the fascinating question of whether LLM determinism is achievable by controlling inference batch size, leading to a debate about whether temperature zero truly guarantees determinism. Natalia suggests Monte Carlo-style repeated runs as a practical testing strategy.

## Related Sources

- [[next_level_evals_stella_eddie]] -- Stella Liu and Eddie Wharton take evaluation to the next level with statistical rigor, causal inference, and organizational practices, building on this workshop's foundations
- [[natalia_ines_guest_workshop]] -- Ines Montani and Natalia Rodnova's annotation workshop provides the data labeling best practices that underpin the evaluation methodology taught here
- [[william_horton_maven_clinic]] -- William Horton's LLM-as-judge design and judge alignment process is a production application of the LLM-as-judge techniques introduced here
- [[ws_4_testing_and_observability]] -- Stefan Krawczyk extends evaluation into systematic testing with PyTest/PyTest Harvest and observability with OpenTelemetry
- [[ws_6_building_ai_agents]] -- The 131-line coding agent demoed as a teaser in this workshop is built step-by-step there
- [[search_agents_john_doug]] -- Doug Turnbull's NDCG explanation provides a concrete search-domain application of the evaluation metrics discussed here
