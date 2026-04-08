---
type: concept
title: "Evaluation-Driven Development"
related_concepts: [llm_as_judge, non_determinism, annotation_and_data_labeling, human_in_the_loop, proof_of_concept_purgatory, observability_and_tracing]
---

## Overview

Evaluation-driven development is the practice of making systematic measurement of application quality the backbone of the AI software development lifecycle. Rather than treating evaluation as a late-stage gate before deployment, this approach positions evals as the continuous compass guiding every design decision -- from the earliest "vibes" check through to automated production monitoring. Hugo Bowne-Anderson introduces evaluation as one of the [[five_first_principles]] for AI software development, and the concept threads through nearly every session in the course.

The practice encompasses a maturity arc. At the most basic level, developers look at their data manually in spreadsheets -- what Hugo and others call "vibes." This is not a pejorative; manual data review can get you surprisingly far before formal eval suites are needed. The next stage is failure analysis, where developers systematically categorize errors to understand why a system fails, not just how often. Hugo demonstrates this concretely in [[ws_3_evals_and_feedback_loops]] by annotating 25 input pairs (yielding 50 individual rows), achieving 92% accuracy against ground truth, then discovering through confusion matrix analysis that his errors had a systematic pattern -- he favored broad, contextual summaries while the ground truth favored specific but cryptic ones. This error analysis directly drove the creation of competing prompts that could be tested head-to-head. The final stage is automated evaluation, encompassing code-based checks (regex, structured output validation, tool-call verification) and [[llm_as_judge]] evaluators for subjective criteria.

William Horton argues that evaluation is the single most important AI engineering skill -- the ability to diagnose agent misbehavior, fix it, and confidently quantify the improvement. Stella Liu and Eddie Wharton frame evals as both a compass for iterative product development and a pass/fail gate for releases. The convergence across these perspectives is striking: evaluation is not a one-time activity but a continuous practice that shapes the entire development process.

## The Three-Stage Maturity Arc

The progression from vibes to failure analysis to automated evaluation is not merely a ladder to climb; each stage remains valuable even as teams mature. Hugo emphasizes in [[ws_3_evals_and_feedback_loops]] that most people make the mistake of trying to change system behavior without first evaluating or debugging, echoing Hamel Hussein's insight that improvement requires observation. The vibes stage -- manually reviewing outputs and building intuition -- is where Stella and Eddie say teams should start but too often skip. Eddie Wharton calls it the highest-impact activity most teams neglect: "Standing up evals without actually looking at your data... hypothesizing what matters without actually looking at the interactions that users are having with your system."

Failure analysis transforms raw observation into actionable categories. In the factual inconsistency detection exercise from [[ws_3_evals_and_feedback_loops]], Hugo's error analysis revealed a systematic bias toward breadth over specificity, which generated two competing prompt strategies. Free-text feedback columns alongside structured labels -- a practice William Horton strongly advocates -- often generate new structured criteria for future annotation rounds. This iterative refinement, where evaluation outputs become inputs for the next development cycle, is the engine of evaluation-driven development.

Automated evaluation scales these practices. Code-based checks should handle everything they can before resorting to LLM judges -- regex for string matching, length checking, and structured output validation are cheaper and more reliable. Stefan Krawczyk demonstrates in [[ws_4_testing_and_observability]] how PyTest Harvest can collect multi-dimensional evaluation data across all assertions, enabling systematic data collection that connects directly to the annotation processes. Per-LLM-call evaluation datasets may be needed for complex pipelines -- you cannot just test the overall system when you have 60+ LLM calls in a DAG, as in Stefan's veterinary transcription case study from [[ws_8_finetuning_and_production_ai]].

## Comparative Evaluation

A key technique within evaluation-driven development is comparative evaluation -- choosing between System A and System B rather than rating individual outputs in isolation. William Horton is the strongest advocate for this approach, arguing in [[ws_3_evals_and_feedback_loops]] that it is more efficient because "people overthink individual ratings but can quickly identify which is better." Even when both options are bad, choosing the better one reveals what you are looking for. Hugo initially pushes back ("What if they're both bad?"), but William's counter is persuasive: the deployment decision is always between options, so the evaluation should mirror that reality.

This approach is operationalized through tools like Prodigy's AB evaluation and ELO tournament workflows, as discussed in [[natalia_ines_guest_workshop]]. Ines Montani and her team built these specifically because comparative judgment aligns with how human cognition works -- relative comparison is cognitively easier and faster than absolute scoring. The statistical foundations for comparative evaluation are explored further in [[next_level_evals_stella_eddie]], where Eddie Wharton's CJ package addresses calibrating cheap LLM judges to expensive human expert labels using causal inference techniques.

## Evaluation in Production

Production evaluation introduces new dimensions. William Horton's experience launching Maven Assistant, detailed in [[william_horton_maven_clinic]], illustrates the full production evaluation lifecycle: binary tool-call checks cover most cases, LLM-as-judge handles subjective criteria (appropriate empathy, clinical accuracy, "Maven accuracy"), and the judge should be paired with a classifier that determines whether it should even apply -- evaluating clinical accuracy on non-clinical questions inflates failure rates meaninglessly. His progressive rollout strategy -- from team to company to 20% of external users -- creates expanding evaluation pools that surface diverse inputs impossible to anticipate in advance.

Eddie Wharton frames production evaluation through the lens of offline versus online evaluation. Both are fundamentally "policy evaluation" -- the same problem whether you are testing a drug in an RCT or comparing prompt A versus prompt B. But offline evals measure against the product owner's expectations, while experiments with real users reveal what people actually need -- and these can diverge significantly. The Amazon Rufus chatbot serves as a cautionary example of missing product constraints.

Student projects at [[demo_day]] demonstrate evaluation-driven development in practice, from Natalia Rodnova's Jira Assistant (with layered observability showing each LLM call) to Michael Powers' Q&A distillation pipeline (four rounds of generate-annotate-revise).

## Where Sources Agree

All sources converge on several points. First, evaluation must begin early and continue throughout the development lifecycle -- it is not a late-stage activity. Second, looking at your data before automating anything is the highest-impact and most frequently skipped step. Third, code-based checks should be exhausted before resorting to LLM judges. Fourth, evaluation is a team sport involving PMs, data scientists, UX designers, and subject matter experts -- not a one-person job. Fifth, the evaluation practice itself is iterative: evaluation outputs feed back into development as new annotations, refined prompts, and updated criteria.

## Where Sources Disagree or Add Nuance

The sources reveal productive tensions around several dimensions. On acceptable pass rates, Natalia Rodnova states that 95% is "embarrassing" in radiology (aiming above 99% with human-in-the-loop), while Hugo notes coding assistants were accepted well below 80% before November 2025 model improvements. This domain-dependent threshold is one of the most consequential design decisions teams face.

On how much statistical rigor is needed, Stella and Eddie push for confidence intervals, power analysis, and causal inference methods, while the workshop emphasis is on getting started with vibes and spreadsheets. These positions are not contradictory but represent different points on the maturity arc. Eddie acknowledges that most teams are not even doing error analysis properly, so causal inference is aspirational for most.

Carol Willing draws a provocative parallel between eval pass rates and code coverage -- suggesting that like code coverage, eval pass rates may give false confidence if not thoughtfully designed. The question of whether fully automated evaluation is even possible remains open: Stella's observation that "if AI evals can be fully automated by AI then we shouldn't have an AI evals problem in the first place" is a sharp reminder that human judgment remains essential.

## Related Concepts

- [[llm_as_judge]] -- The primary technique for automating evaluation of subjective criteria, requiring careful calibration against human labels
- [[non_determinism]] -- The fundamental property that makes evaluation necessary and challenging; Monte Carlo-style repeated runs as a testing strategy
- [[annotation_and_data_labeling]] -- The data creation practice that feeds evaluation; label scheme design directly impacts eval quality
- [[human_in_the_loop]] -- Evaluation-driven development requires human judgment at every stage, from initial vibes through production monitoring
- [[proof_of_concept_purgatory]] -- Evaluation is the primary escape route from purgatory; without it, teams cannot improve their systems
- [[observability_and_tracing]] -- You cannot evaluate what you cannot observe; logging from day zero enables evaluation-driven development

## Sources

- [[ws_1_foundations]] -- Establishes evaluation as one of five first principles for AI software development
- [[ws_3_evals_and_feedback_loops]] -- The definitive eval workshop: three-stage framework, hands-on annotation, failure analysis driving prompt iteration, LLM-as-judge construction
- [[ws_4_testing_and_observability]] -- Extends evaluation into systematic testing with PyTest/PyTest Harvest and per-LLM-call evaluation datasets
- [[next_level_evals_stella_eddie]] -- Statistical rigor, causal inference, offline vs. online evaluation, and evals as a team sport
- [[builders_club_william_horton]] -- Evaluation as the most important AI engineering skill; comparative evaluation advocacy
- [[william_horton_maven_clinic]] -- Production LLM-as-judge design, judge alignment with human labelers, progressive rollout as expanding evaluation
- [[natalia_ines_guest_workshop]] -- Annotation pipelines feeding evaluation; AB evaluation and ELO tournament workflows
- [[demo_day]] -- Students applying evaluation techniques in working projects
