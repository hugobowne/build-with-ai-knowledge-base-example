---
type: concept
title: "Human-in-the-Loop and Supervised AI"
related_concepts: [evaluation_driven_development, agents_vs_workflows, guardrails, annotation_and_data_labeling, domain_specific_ai, privacy_and_security]
---

## Overview

Human-in-the-loop (HITL) refers to the practice of keeping humans involved in AI system decisions at various stages -- from annotating training data and evaluating outputs to supervising agent execution and approving individual actions before they take effect. Across the course sources, this concept appears not as a temporary concession to immature technology but as a fundamental design principle for responsible AI deployment, particularly in high-stakes domains.

The concept spans a wide range of implementation patterns. At one end sits annotation and evaluation, where humans provide the ground truth that drives system improvement -- covered in [[ws_3_evals_and_feedback_loops]] and [[natalia_ines_guest_workshop]]. At the other end sits supervised agent execution, where a human reviews and approves each action before it fires, as demonstrated by Natalia Rodnova's Jira Assistant at [[demo_day]] and William Horton's Maven Assistant in [[william_horton_maven_clinic]]. Between these sits progressive rollout -- expanding exposure from internal teams to limited external users to broader deployment -- which William describes as essential for discovering what real users actually want.

The course introduces a conceptual framework for reasoning about HITL in agent systems: the agency vs. supervision 2x2, presented in [[ws_6_building_ai_agents]]. High agency combined with low supervision is the danger zone (Simon Willison's lethal trifecta: private data access, external communication capability, and exposure to untrusted content). High agency combined with strong supervision -- exemplified by tools like Cursor, Claude Code, and deep research agents -- represents the productive sweet spot. Hugo's own evolution on agents reflects this: his "Stop Building AI Agents" essay was never about opposing AI autonomy per se, but about opposing AI autonomy without proper human oversight.

## Domain-Specific Requirements

The acceptable level of AI autonomy varies dramatically by domain, and several sources make this concrete. Natalia Rodnova states in [[ws_3_evals_and_feedback_loops]] that in radiology, 95% accuracy is "embarrassing" -- the target is above 99%, always with human-in-the-loop. Hugo adds that he would prefer to receive an incorrect positive diagnosis and then find out otherwise than receive an incorrect negative diagnosis and not find out, illustrating how the cost of different error types shapes HITL requirements.

William Horton's Maven Assistant in [[william_horton_maven_clinic]] implements domain-specific HITL at multiple levels. The self-harm detection guardrail is the only fully automatic human-in-the-loop trigger, immediately transferring the user to a human provider. For other interactions, the progressive rollout strategy served as a form of staged supervision: internal team first, then product and engineering staff, then all Maven employees, then 20% of external users. William emphasizes that testing with the same people eventually yields diminishing returns -- you need to expand your test pool for diverse inputs, but each expansion is a deliberate decision about risk.

Stella Liu argues in [[next_level_evals_stella_eddie]] that if AI evals could be fully automated by AI, "we shouldn't have an AI evals problem in the first place." The fact that we do means human judgment remains essential. This frames HITL not as a temporary crutch but as a structural feature of systems where the quality criteria are themselves ambiguous or contested. Product requirements documents are often missing because teams go straight from prototyping to production -- and defining what the product is designed NOT to do is as important as what it should do.

## Supervised Agent Execution Patterns

Natalia Rodnova's Jira Assistant, presented at [[demo_day]], provides the clearest example of supervised agent execution. The system triages incoming Jira issues, runs LLM calls with tool use to pull database reports, run models, and verify correctness, but every action is presented to Natalia for review before execution. She approves or rejects each step. This supervised mode is practical for high-stakes agent deployments where full automation is premature, and the layered observability built into the system makes each decision point visible.

The annotation workflow described by Ines Montani and Natalia Rodnova in [[natalia_ines_guest_workshop]] represents another form of HITL: model-assisted annotation where even a 50% accurate model pre-annotating data saves 50% of human effort. The human remains in the loop not because the model cannot do the work but because the human's judgment is what creates the ground truth that future models will learn from. Natalia's advice to "annotate alongside your SMEs" even when you are not an expert underscores the value of humans in the loop at the data creation stage, not just the output review stage.

## The Progressive Rollout Strategy

William Horton's account in [[william_horton_maven_clinic]] of Maven Assistant's launch provides a detailed model for progressive rollout as a form of supervised deployment. The phases are distinct: prototyping tools and learning internal APIs, basic tool-calling evaluations, internal user testing with progressive expansion (team, then product/engineering, then all Maven employees, then 20% of external users), and qualitative LLM-as-judge evaluations layered on top. Each phase reveals new information -- the first 24 hours of real user data showed that users frequently want to update profile data (names, addresses), a mundane but high-volume need the team had not prioritized.

This pattern connects to Stella and Eddie's discussion in [[next_level_evals_stella_eddie]] about offline versus online evaluation: offline evals measure against the product owner's expectations, while experiments reveal what real users actually need. Progressive rollout is the mechanism that bridges these two worlds, with human supervision at each stage determining when to expand exposure.

## Where Sources Agree

All sources agree that human-in-the-loop is essential in high-stakes domains and that full automation is premature for most production AI applications. There is strong consensus that progressive rollout is the right deployment strategy, that evaluation requires human judgment at its foundation, and that the agency vs. supervision framework is a useful tool for reasoning about where on the autonomy spectrum a system should sit. The principle that annotation requires human involvement -- even when models assist -- is universally accepted.

## Where Sources Disagree or Add Nuance

The sources differ on how quickly the loop can narrow. Hugo's evolution from "Stop Building AI Agents" to daily agent use suggests the supervision threshold is shifting rapidly as models improve. William Horton's production experience shows that even at Maven Clinic, the system moved from supervised mode to 20% rollout in months, with LLM-as-judge running hourly on 100% of conversations as a form of automated supervision. Stella Liu's argument that human judgment is structurally necessary sits in tension with the practical observation that the amount of human involvement per decision is decreasing. The question is whether HITL converges toward sample-based auditing (humans review a fraction of outputs) or remains at the action-approval level for sensitive domains. The radiology and healthcare examples suggest the latter will persist for regulated industries, while less regulated domains may automate more aggressively.

## Related Concepts

- [[agents_vs_workflows]] -- The agency vs. supervision 2x2 framework determines how much human oversight an agent needs
- [[evaluation_driven_development]] -- Human evaluation is the foundation that automated evaluation builds on; HITL is essential at the eval layer
- [[annotation_and_data_labeling]] -- Annotation is a specific form of HITL that creates the ground truth for training and evaluation
- [[guardrails]] -- Guardrails like self-harm detection can trigger automatic HITL escalation to human operators
- [[domain_specific_ai]] -- Acceptable autonomy levels vary dramatically by domain; healthcare demands far more human oversight than consumer applications
- [[proof_of_concept_purgatory]] -- Skipping HITL to move fast is a common path into purgatory

## Sources

- [[ws_6_building_ai_agents]] -- Introduces the agency vs. supervision 2x2 framework, YOLO mode, and Simon Willison's lethal trifecta for reasoning about agent safety and human oversight
- [[william_horton_maven_clinic]] -- Detailed progressive rollout strategy, supervised mode for health agent, and real-world lessons from expanding exposure to users
- [[ws_3_evals_and_feedback_loops]] -- Natalia's radiology perspective (95% is embarrassing, above 99% with HITL), manual annotation as evaluation foundation
- [[demo_day]] -- Natalia's Jira Assistant in supervised mode: every agent action reviewed before approval
- [[natalia_ines_guest_workshop]] -- Model-assisted annotation as HITL at the data creation stage, annotating alongside SMEs
- [[next_level_evals_stella_eddie]] -- Human judgment as structurally necessary for evaluation; fully automated evals would have solved the problem if they could
