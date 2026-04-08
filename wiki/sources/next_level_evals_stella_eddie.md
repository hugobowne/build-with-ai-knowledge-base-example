---
type: guest_talk
title: "Next Level Evals in 2026: From Vibes to Statistical Rigor"
date: 2026-03-17
speakers: [Stella Liu (ASU), Eddie Wharton (Simo Labs), Hugo Bowne-Anderson]
topics: [AI evaluation, offline evals, online evals, AB testing, LLM judges, causal inference, error analysis, team sports, product development, statistics, non-determinism, hallucination, test set design, annotation disagreement]
source_file: raw/next_level_evals_2026_stella_eddie.md
word_count: ~12000
---

## Overview

A guest Q&A session with Stella Liu (Head of AI Applied Science at Arizona State University, Maven course instructor on AI evals) and Eddie Wharton (founder of Simo Labs, focused on causal inference in evaluation, formerly StitchFix). This session extends the eval foundations from [[ws_3_evals_and_feedback_loops]] into statistical rigor and organizational practice. The conversation covers the full landscape of AI evaluation: why evals matter, who should do them, the relationship between offline and online evaluation, what statistics you need, the biggest mistakes teams make, and how causal inference is emerging as the next frontier.

Stella frames evals as both a compass for product development and a pass/fail gate for releases, emphasizing the regulated industry perspective (education) where compliance adds another dimension. Eddie focuses on two motivations: making quantitative progress toward objectives, and "not embarrassing yourself" by catching low-effort failure modes. Both agree evals are a team sport involving PMs, data scientists, UX designers, and subject matter experts -- not a one-person job.

The discussion of offline vs. online evaluation is particularly rich. Eddie reframes the relationship: both are fundamentally "policy evaluation" -- the same problem whether you're testing a drug in an RCT, a red vs. green button, or prompt A vs. prompt B. Stella adds that offline evals measure against the product owner's expectations, while experiments reveal what real users actually need -- these can diverge significantly. The Amazon Rufus chatbot is cited as a cautionary example of missing product constraints.

Eddie's work on causal inference in evaluation (CJ - causal judge evaluation package, recently past 10K PyPI downloads) addresses a critical gap: calibrating cheap LLM judges to expensive human expert labels, quantifying uncertainty, and power analysis for how many human labels you actually need. Hugo provokes a lively exchange on whether data science has ever done causal inference well (his assertion: outside a handful of two-sided marketplace companies, no), leading to a memorable back-and-forth on counterfactuals, Bayesian vs. frequentist approaches, and sample size problems in biology research.

## Key Topics

- Why AI evals matter: compass for product development, pass/fail gate for releases, compliance in regulated industries
- AI evals as team sport: PMs, data scientists, UX designers, subject matter experts
- Offline vs. online evaluation: both are policy evaluation; offline measures against product owner expectations, online reveals real user needs
- Error analysis as the highest-impact early activity: looking at your data before automating anything
- LLM judges: cheap measurement primitive, but must be calibrated to human experts
- Causal inference in evaluation: calibrating judges, quantifying uncertainty, power analysis
- Statistics needed for evals: understanding non-determinism, confidence levels, distributions
- Building good test sets: mapping real user interaction distributions to offline test suites
- Hallucination as a spectrum: possibly desirable in writing tools, definitely bad in factual retrieval
- The biggest mistake: standing up evals without looking at your data

## Key Insights

- "If AI evals can be fully automated by AI then we shouldn't have an AI evals problem in the first place" -- fully self-optimizing systems would have solved this; the fact that we haven't means human judgment remains essential
- Error analysis is the highest-impact activity most teams skip -- hypothesizing what matters without looking at interactions is the most common failure mode
- Offline evals measure against product owner expectations; experiments reveal what real users need -- these often diverge, especially for qualitative dimensions like tone and helpfulness
- Non-determinism is a superpower in some contexts: deep research benefits from diverse agent outputs; writing tools may benefit from some "hallucination"
- Product requirements documents are often missing because teams go straight from prototyping to production -- defining what the product is designed NOT to do is as important as what it should do
- The annotation disagreement problem is often upstream of evaluation: co-founder disagreements surfacing in eval labels reveal misalignment that is fundamentally an organizational problem, not an eval problem -- [[natalia_ines_guest_workshop]] covers annotation best practices for managing this
- Causal inference in AI evaluation is still early days: most teams aren't even doing error analysis properly, but at scale and maturity it converges to a statistics/causal inference problem
- Benevolent dictator model for evals: decisions need to be made, but disagreeing annotators should prompt reflection, not automatic override

## People & Tools Mentioned

- Stella Liu -- Head of AI Applied Science at ASU, Maven course instructor (AI Evals and Analytics Playbook)
- Eddie Wharton -- founder of Simo Labs, focused on causal inference in AI evaluation, formerly StitchFix
- CJ (Causal Judge) -- Eddie's open-source package for calibrating LLM judges to human experts (10K+ PyPI downloads)
- Amazon Rufus -- cited as example of AI chatbot without proper product constraints (users using it as free GPT)
- Shreya Hamill -- referenced for "benevolent dictator" concept in evals
- Andrej Karpathy -- referenced for the take that every LLM hallucinates 100% of the time without retrieval grounding
- Bill Campbell (Trillion Dollar Coach) -- Hugo references his approach to getting the best idea from everyone then disagree-and-commit
- Carol Willing -- active participant in Discord, CPython core developer
- Natalia, Matt, Magda (spaCy/Explosion AI) -- ran data annotation workshop (see [[natalia_ines_guest_workshop]])

## Quotable Moments

- "AI evals is a team sport. It's not just a PM but also data scientists, UX designers, and subject matter experts." -- Stella Liu [~07:55]
- "Standing up evals without actually looking at your data... hypothesizing what matters without actually looking at the interactions that users are having with your system." -- Eddie Wharton [~31:02]
- "If AI evals can be fully automated by AI then we shouldn't have an AI evals problem in the first place." -- Stella Liu [~33:30]
- "The person who's best suited to thinking about evaluation... someone who has really good intuition for the product and has really strong empathy for the user." -- Eddie Wharton [~11:14]
- "Is hallucination good or bad for writing tools? It's actually hard to tell... I assume users of an AI-powered writing tool wanted it to hallucinate to some degree. I don't want the writing to be deterministic." -- Stella Liu [~28:52]

## Highlights

- [~05:00] Evals as compass and gate: Stella's dual framing of evals for product iteration guidance and release decisions, plus the compliance dimension from regulated industries (education)
- [~06:00] Eddie's two motivations: making quantitative progress toward objectives, and "the motivation not to embarrass yourself" -- catching low-effort failure modes before users see them
- [~14:00] Hugo's provocative framing: someone who has the right incentives should be responsible for evals -- "if it doesn't work enough times you should lose your job" -- plus the annotation disagreement story revealing co-founder tension
- [~22:00] Offline vs. online evaluation: Eddie reframes both as "policy evaluation" -- same fundamental problem as RCTs, AB tests, and prompt comparison. Stella adds the gap between product owner expectations and real user needs
- [~28:00] Hallucination as spectrum: potentially desirable in creative writing tools, definitely harmful in factual systems -- Karpathy's framing that LLMs hallucinate 100% of the time without grounding
- [~31:00] Biggest eval mistakes: using vendor tools with built-in metrics without looking at data (Stella), standing up evals without examining user interactions (Eddie), not having a PRD or specification (Hugo)
- [~36:00] Statistics for evals: understanding non-determinism is foundational; at maturity it's fundamentally a data science problem with distributions and confidence levels
- [~42:00] Spicy statistics exchange: Hugo claims data science has never done causal inference well outside a handful of companies; Eddie pushes back on counterfactual framing; they arrive at unexpected agreement through biology research examples with n=3
- [~45:00] Eddie on causal judge evaluation: calibrating cheap LLM judges to expensive human experts, power analysis for label budgets, and why this field will mature toward established statistical practices

## Related Sources

- [[ws_3_evals_and_feedback_loops]] -- Hugo's hands-on eval workshop covers the practical foundations (vibes, failure analysis, automated evaluation) that Stella and Eddie build upon with statistical rigor
- [[william_horton_maven_clinic]] -- William Horton's LLM-as-judge design for Maven Assistant is a production application of the judge calibration and human label alignment that Eddie discusses
- [[builders_club_william_horton]] -- William argues evaluation is the most important AI engineering skill, directly aligned with Stella and Eddie's emphasis on eval as a team sport
- [[natalia_ines_guest_workshop]] -- Ines Montani and Natalia Rodnova's annotation workshop covers the data labeling practices that underpin the evaluation methodology discussed here
- [[search_agents_john_doug]] -- Doug Turnbull's NDCG explanation provides a concrete example of the evaluation metrics Stella and Eddie discuss at a higher level
- [[ws_4_testing_and_observability]] -- Stefan Krawczyk's testing and observability workshop connects to the systematic evaluation infrastructure Stella and Eddie advocate for
