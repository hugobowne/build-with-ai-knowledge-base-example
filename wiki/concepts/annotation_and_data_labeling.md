---
type: concept
title: "Annotation and Data Labeling"
related_concepts: [evaluation_driven_development, llm_as_judge, human_in_the_loop, retrieval_augmented_generation, fine_tuning_and_distillation, domain_specific_ai]
---

## Overview

Annotation and data labeling is the foundational practice of creating labeled datasets for training, evaluation, and system improvement. Across the course sources, annotation emerges not as a tedious prerequisite but as a core engineering practice that shapes every downstream decision -- from what your models can learn to how rigorously you can evaluate them. The sources converge on several principles that challenge common assumptions: label scheme design decisions have outsized impact, single-label annotation passes are counterintuitively faster than multi-label ones, model-assisted annotation dramatically reduces human effort even at low accuracy, and annotating alongside subject matter experts is essential even if you lack domain expertise.

Ines Montani provides the most systematic treatment in [[natalia_ines_guest_workshop]], drawing on years of experience building spaCy and Prodigy at Explosion AI. Her core principle -- factor business logic out of classification logic -- reshapes how annotation tasks should be designed. Rather than teaching a model to recognize "minor date of birth" (a concept that changes daily as people age), you separate the classification task (finding dates) from the business logic (computing whether someone is a minor). This principle applies broadly: fine-grained labels that encode domain rules require far more training data than generic labels combined with downstream logic.

Hugo's hands-on evaluation workshop in [[ws_3_evals_and_feedback_loops]] demonstrates annotation as the entry point to evaluation, walking through manual annotation of 25 input pairs (yielding 50 individual rows), building confusion matrices, and discovering through error analysis that ground truth labels themselves can be questioned. William Horton's work at Maven Clinic in [[william_horton_maven_clinic]] shows annotation in production: using two human labelers to calibrate LLM-as-judge systems, with the critical finding that inter-annotator agreement is the ceiling for automated judge performance. Stella Liu and Eddie Wharton in [[next_level_evals_stella_eddie]] elevate this further, framing annotation disagreement as an organizational problem rather than a technical one -- when co-founders disagree on labels, the issue is misalignment in the organization, not in the evaluation system.

## Label Scheme Design

The single most impactful annotation decision is label scheme design, and Ines Montani's examples in [[natalia_ines_guest_workshop]] make this vividly concrete. Her crime report extraction case study shows that fine-grained labels (stabber/stabbee, crime location) require far more training data than generic labels (person, location) combined with follow-up business logic. The custody document anonymization case demonstrates a common and costly mistake: trying to teach a model temporal concepts (who is a minor) that change daily. The solution is to separate what the model classifies from what code computes.

The S&P Global commodities trading case study quantifies the impact of good design: breaking multi-label annotation into single-label passes was 10x faster overall, with individual models requiring just 15 hours of single-annotator time to reach production quality. Ines frames this as reducing cognitive load -- iterating over annotation types first (one label at a time) then over examples is dramatically faster than considering all labels simultaneously for each example. The principle echoes in Hugo's [[ws_3_evals_and_feedback_loops]], where he separates reference-based metrics (code-checkable) from reference-free metrics (requiring human judgment), effectively factoring the evaluation task into simpler sub-tasks.

## Model-Assisted Annotation and the LLM Role

Model-assisted annotation -- pre-populating annotations with model predictions -- emerges as a practical accelerator across multiple sources. Ines states in [[natalia_ines_guest_workshop]] that even a 50% accurate model pre-annotating data saves 50% of human effort, because correcting wrong labels is faster than creating labels from scratch. Prodigy's token boundary snapping (automatically aligning selections to valid token boundaries) and train curve feature (knowing when more data will improve models) are specific tooling innovations that reduce annotation friction.

The role of LLMs in annotation is nuanced. Ines argues in [[natalia_ines_guest_workshop]] that LLMs should be used to build the system -- writing spaCy rules, generating training data, creating hypothesis sentences for annotators to verify -- rather than being the production system. When you need speed, privacy, cost-effectiveness, or accuracy at scale, investing in smaller trained models pays off. This connects to the broader [[fine_tuning_and_distillation]] discussion: annotation creates the data that trains smaller, faster, cheaper models to replace expensive LLM calls.

William Horton's approach in [[william_horton_maven_clinic]] uses annotation for a different purpose: calibrating LLM judges. Two human labelers annotate samples, their agreement is measured, and the LLM judge is then calibrated against this human baseline. This flips the traditional annotation flow -- instead of annotating data to train a model, you annotate data to evaluate whether an automated evaluator is trustworthy.

## Annotation Disagreement as Signal

A recurring theme across sources is that annotation disagreement is informative, not just a problem to resolve. William Horton shares in [[william_horton_maven_clinic]] that at a previous job, human annotators achieved only 66% unanimous agreement on a 12-class intent classification task. This ceiling limits automated judge performance -- if humans cannot agree, expecting an LLM to do better is unreasonable. The practical implication is that you need at least two labelers to distinguish task ambiguity from judge failure.

Stella Liu and Eddie Wharton take this further in [[next_level_evals_stella_eddie]], framing annotation disagreement as often an upstream organizational problem. When disagreements surface in eval labels, they frequently reveal misalignment between stakeholders about what the product should do. The "benevolent dictator" model for evals -- someone must make decisions, but disagreements should prompt reflection rather than automatic override -- provides a governance pattern. Natalia Rodnova's advice in [[natalia_ines_guest_workshop]] to annotate alongside SMEs connects to this: the disagreements between model-like logical thinking and expert domain reasoning are where the most valuable insights emerge.

## Where Sources Agree

All sources agree that annotation is foundational to both training and evaluation, and that label scheme design has outsized impact on efficiency and quality. There is consensus that model-assisted annotation saves significant effort, that inter-annotator agreement is the performance ceiling for automated systems, and that annotation should be iterative (design schema, annotate, compare, discover inconsistencies, revise, repeat). The practical advice to start annotating yourself rather than delegating entirely to SMEs is shared across Ines Montani, Natalia Rodnova, and Hugo's own hands-on annotation exercises.

## Where Sources Disagree or Add Nuance

The sources differ on the appropriate response to annotation disagreement. Stella and Eddie's "benevolent dictator" model assumes someone should decide; William Horton's approach accepts the disagreement ceiling and designs systems around it (the paired classifier pattern that determines whether the judge should even apply). Ines Montani's focus is on making the disagreement less likely by simplifying the task through better label scheme design. These are complementary but distinct strategies, and the right approach depends on whether the disagreement stems from task complexity, ambiguous guidelines, or genuine domain controversy.

There is also a tension between Ines's strong position that LLMs should build the system rather than be the system and the broader course trend toward using LLMs directly in production. The annotation-trained smaller models she advocates require significant upfront investment in data labeling, which may not be justified for all use cases -- a tension William navigates by using LLM judges directly in production while calibrating them against human annotations.

## Related Concepts

- [[evaluation_driven_development]] -- Annotation creates the ground truth that evaluation depends on; error analysis on annotations drives prompt iteration
- [[llm_as_judge]] -- LLM judges must be calibrated against human annotations; inter-annotator agreement sets the ceiling for judge performance
- [[human_in_the_loop]] -- Annotation is a specific form of HITL that creates training and evaluation data
- [[fine_tuning_and_distillation]] -- Annotation data is what makes fine-tuning and distillation possible; label quality determines model quality
- [[domain_specific_ai]] -- Domain-specific annotation requirements (radiology, legal, healthcare) shape label scheme design and acceptable accuracy thresholds

## Sources

- [[natalia_ines_guest_workshop]] -- The definitive annotation source: Prodigy, label scheme design principles, S&P Global case study, cognitive load reduction, model-assisted annotation, structured RAG, and when to use LLMs versus smaller trained models
- [[ws_3_evals_and_feedback_loops]] -- Manual annotation as the entry point to evaluation, confusion matrices, error analysis revealing ground truth limitations, and free-text feedback columns as annotation innovation
- [[next_level_evals_stella_eddie]] -- Annotation disagreement framed as an organizational problem, the benevolent dictator model for resolving disagreements, and why human judgment remains essential
- [[william_horton_maven_clinic]] -- Two human labelers for judge calibration, the 66% inter-annotator agreement ceiling, and the paired classifier pattern for determining when judges should apply
