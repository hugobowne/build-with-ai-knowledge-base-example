---
type: concept
title: "LLM-as-Judge"
related_concepts: [evaluation_driven_development, annotation_and_data_labeling, non_determinism, structured_output, human_in_the_loop]
---

## Overview

LLM-as-judge is the practice of using large language models to evaluate the outputs of other LLM systems. It occupies a specific position in the evaluation toolkit: code-based checks (regex, structured output validation, tool-call verification) should handle everything they can first, because they are cheaper and more reliable. LLM judges are reserved for subjective, contextual criteria where deterministic checks cannot suffice -- assessing tone, empathy, clinical accuracy, helpfulness, or whether a fine-tuned model's dialogue sounds sufficiently extraterrestrial.

The concept appears across multiple sources with increasing sophistication. Hugo introduces the basic pattern in [[ws_3_evals_and_feedback_loops]] by building an LLM-as-judge for evaluating personalized outreach emails based on LinkedIn profiles. William Horton applies it in production at Maven Clinic, detailed in [[william_horton_maven_clinic]], where judges assess completeness, clinical accuracy, Maven-specific self-awareness, and appropriate empathy. Eddie Wharton's CJ (Causal Judge) package, discussed in [[next_level_evals_stella_eddie]], brings statistical rigor to the practice by calibrating cheap LLM judges to expensive human expert labels. Ines Montani's team offers AB evaluation and ELO tournament workflows in Prodigy, described in [[natalia_ines_guest_workshop]], as a complementary approach where outputs are compared head-to-head rather than judged individually.

The key insight across all sources is that LLM-as-judge is not a shortcut to avoid human evaluation -- it is a scaling mechanism that must be anchored to human judgment. Without calibration against human labels, LLM judges risk encoding systematic biases that compound silently. The inter-annotator agreement ceiling is perhaps the most important practical constraint: if human labelers only agree 66% of the time on a task, no judge -- human or LLM -- can reliably exceed that ceiling.

## When Code Checks End and LLM Judges Begin

The boundary between code-based evaluation and LLM-as-judge evaluation is a recurring design decision. Hugo frames this clearly in [[ws_3_evals_and_feedback_loops]]: reference-based metrics where ground truth exists are testable with code checks (did the agent call the correct tool? is the output valid JSON? does the response contain required fields?). Reference-free metrics covering subjective quality require LLM judges or human annotation.

William Horton's Maven Assistant demonstrates this division in production. Binary tool-call checks -- did the agent route to the correct sub-agent? did it call the appointment API with the right parameters? -- cover the majority of evaluation needs. LLM-as-judge handles the remainder: was the empathy level appropriate (the agent was over-empathizing on purely informational questions), did the response stay within clinical accuracy bounds without crossing into diagnosis, and did the agent demonstrate proper self-awareness (not telling users to "open the Maven app" when they are already in it). In [[ws_8_finetuning_and_production_ai]], the alien NPC dialogue fine-tuning exercise provides another clear case: when you want to test whether a model speaks "like an extraterrestrial," code checks simply cannot work -- this is a perfect case for an LLM judge with clear evaluation criteria.

Stefan Krawczyk's insight from [[ws_4_testing_and_observability]] adds a systems dimension: in pipelines with many LLM calls, you may need per-call evaluation datasets. The LLM-as-judge pattern must be applied at the right granularity -- judging the final output of a 60-call pipeline may miss failures that are only visible at the individual call level.

## Calibrating Judges Against Human Labels

The most technically demanding aspect of LLM-as-judge is calibration -- ensuring the judge's assessments align with human expert judgment. William Horton's process at Maven Clinic, described in [[william_horton_maven_clinic]], uses two human labelers to establish inter-annotator agreement before comparing the judge against them. He references a prior project where three annotators achieved only 66% unanimous agreement on a 12-class intent classification task. This ceiling is critical: "If your human unanimous result is only 66%, then it's hard to get the LLM to do much better, because you clearly haven't aligned on your criteria."

Eddie Wharton's CJ package, discussed in [[next_level_evals_stella_eddie]], formalizes this calibration. The approach uses causal inference techniques to calibrate cheap LLM judges to expensive human expert labels, quantify uncertainty, and perform power analysis to determine how many human labels are actually needed. This bridges the gap between "run the judge and hope it works" and statistically rigorous measurement.

The annotation disagreement problem surfaces here as well. Stella Liu notes in [[next_level_evals_stella_eddie]] that co-founder disagreements sometimes surface in evaluation labels, revealing misalignment that is fundamentally an organizational problem, not an evaluation problem. The "benevolent dictator" model -- where decisions need to be made but disagreeing annotators should prompt reflection -- offers a practical resolution. This connects directly to the annotation best practices covered in [[natalia_ines_guest_workshop]], where Ines Montani emphasizes iterating on annotation guidelines until inter-annotator agreement stabilizes.

## The Paired Classifier Pattern

A subtle but high-impact pattern emerges from William Horton's production experience: pairing the LLM judge with a classifier that determines whether the judge should even apply. At Maven Clinic, evaluating clinical accuracy on non-clinical questions (like "how do I cancel my appointment?") inflated failure rates meaninglessly. The solution is a routing step that classifies each conversation by type, then applies the appropriate judge only to relevant conversations.

This pattern generalizes beyond healthcare. Any production system with heterogeneous query types risks misleading evaluation metrics if judges are applied indiscriminately. The paired classifier ensures that each judge is evaluated against the distribution it was designed for, producing actionable rather than noisy metrics.

## Where Sources Agree

All sources agree that LLM-as-judge is a scaling mechanism, not a replacement for human evaluation. Code-based checks should be exhausted first. Calibration against human labels is essential. The quality of human labels -- including the degree of inter-annotator agreement -- sets the ceiling for judge performance. And comparative evaluation (choosing between outputs A and B) is often more effective than asking a judge to rate a single output in isolation, because people and LLMs both struggle with absolute scoring but can more reliably rank alternatives.

## Where Sources Disagree or Add Nuance

The sources reveal different levels of sophistication in how they approach LLM-as-judge. Hugo's [[ws_3_evals_and_feedback_loops]] workshop treats it as a practical technique to build and iterate on. William Horton's [[william_horton_maven_clinic]] account adds production realism -- the paired classifier pattern, the judge alignment process with two labelers, the danger of saturated metrics. Stella and Eddie's [[next_level_evals_stella_eddie]] pushes toward statistical rigor with causal inference and power analysis, while acknowledging most teams are not even doing error analysis properly.

There is also an implicit tension about when LLM judges are sufficient versus when human evaluation remains necessary. Stella's observation that "if AI evals can be fully automated by AI then we shouldn't have an AI evals problem in the first place" suggests a fundamental limit. Eddie is more pragmatic about using LLM judges as a cheap measurement primitive that can be calibrated. William occupies the middle ground in production: LLM-as-judge runs hourly on 100% of conversations, with human labels sampled for ongoing calibration.

The stylistic evaluation use case from [[ws_8_finetuning_and_production_ai]] -- judging whether alien dialogue sounds alien enough -- raises the question of whether some evaluation criteria are better suited to LLM judges than humans, inverting the usual assumption that humans are the gold standard.

## Related Concepts

- [[evaluation_driven_development]] -- LLM-as-judge is a key technique within the broader evaluation-driven development practice
- [[annotation_and_data_labeling]] -- Human labels are the foundation for calibrating LLM judges; inter-annotator agreement is the performance ceiling
- [[non_determinism]] -- LLM judges are themselves non-deterministic, adding a layer of variance to the evaluation process
- [[structured_output]] -- Judges and guardrails both use structured output to produce consistent, parseable evaluation results
- [[human_in_the_loop]] -- Human evaluation remains essential for calibration and for catching failure modes that LLM judges miss

## Sources

- [[ws_3_evals_and_feedback_loops]] -- Building an LLM-as-judge for personalized outreach emails; the three-stage eval framework positioning judges as the automated layer
- [[next_level_evals_stella_eddie]] -- CJ package for calibrating LLM judges to human experts; statistical rigor and power analysis for judge evaluation
- [[william_horton_maven_clinic]] -- Production judge alignment with two human labelers; 66% agreement ceiling; paired classifier pattern; judge criteria for empathy, clinical accuracy, and self-awareness
- [[ws_8_finetuning_and_production_ai]] -- LLM-as-judge for evaluating alien NPC dialogue fine-tuning, where code checks cannot assess stylistic quality
- [[natalia_ines_guest_workshop]] -- AB evaluation and ELO tournament workflows as a complementary comparative evaluation approach
