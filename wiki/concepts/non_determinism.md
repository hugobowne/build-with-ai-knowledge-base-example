---
type: concept
title: "Non-Determinism in AI Systems"
related_concepts: [evaluation_driven_development, five_first_principles, llm_as_judge, observability_and_tracing, llm_architecture_and_inference]
---

## Overview

Non-determinism is the fundamental property that LLM outputs vary across runs, even with identical inputs. Hugo Bowne-Anderson frames this as the "double entropy problem" in [[ws_1_foundations]] -- there is non-determinism in both the outputs (the model may produce different responses to the same prompt) and the inputs (users phrase requests differently each time). This dual source of variance makes AI systems fundamentally different from traditional software, where the same input reliably produces the same output.

The course treats non-determinism not as a bug to fix but as a property to build systems around. Hugo states explicitly: "You don't solve nondeterminism, you build systems around it that minimize risk." This reframing is essential because the traditional software engineering instinct -- to eliminate variance -- leads teams astray. Temperature settings, seed values, and "deterministic" modes offer the illusion of control but do not eliminate the fundamental property. Ryan Rodriguez raises in [[ws_3_evals_and_feedback_loops]] whether controlling inference batch size could achieve true determinism, sparking a debate about whether temperature zero truly guarantees identical outputs. The consensus is that it does not, at least not reliably across all providers and hardware configurations.

Yet the framing goes further. Stella Liu argues in [[next_level_evals_stella_eddie]] that non-determinism is a superpower in certain contexts. Deep research agents benefit from diverse outputs -- running the same query multiple times and getting different results means the agent explores more of the solution space. Writing tools may benefit from some degree of what is conventionally called "hallucination." Sebastian Raschka's discussion in [[llm_architecture_rasbt]] of inference scaling techniques -- parallel sampling, sequential refinement -- reveals that non-determinism is not just tolerated but deliberately exploited at the architectural level, where multiple diverse reasoning chains are generated and the best is selected.

## The Double Entropy Problem

The "double entropy" framing is one of the course's most distinctive contributions. Traditional software testing assumes deterministic mapping from input to output: given the same input, you can assert a specific output. LLMs break this assumption on both sides. The output side is well understood -- temperature, sampling, and the stochastic nature of autoregressive generation mean outputs vary. But the input side is equally important and less discussed: real users do not send the same prompt twice. They phrase questions differently, provide varying amounts of context, make typos, and bring different conversational histories.

This double variance has profound implications for evaluation. As discussed in [[ws_3_evals_and_feedback_loops]], traditional unit testing (assert output equals expected) fails for LLM systems. Natalia Rodnova suggests Monte Carlo-style repeated runs as a practical testing strategy -- running the same test multiple times and analyzing the distribution of outputs rather than checking for exact matches. Stefan Krawczyk extends this in [[ws_4_testing_and_observability]] with PyTest Harvest, which collects results across multiple dimensions simultaneously, accommodating the reality that a single test run tells you very little about system behavior.

William Horton references the double entropy problem by name in [[william_horton_maven_clinic]], applying it to the practical challenge of launching Maven Assistant. When real users started interacting with the health agent, the input entropy was immediately visible: users wanted to update profile data (names, addresses) -- a mundane but high-volume need the team had not prioritized. No amount of synthetic testing could have captured the full distribution of real-world inputs.

## Non-Determinism in Architecture and Inference

Sebastian Raschka's discussion in [[llm_architecture_rasbt]] grounds non-determinism in the architecture. Temperature and sampling parameters control the degree of randomness in token selection, but the deeper story involves inference scaling. Modern reasoning models use techniques that deliberately exploit variance: parallel sampling generates multiple reasoning chains and selects the best, sequential refinement iterates on outputs, and external judges evaluate different candidate answers. Adjustable reasoning effort, which Hugo discusses in [[ws_2_prompting_and_context]] (noting GPT-5.4's implementation), lets developers choose how much compute -- and implicitly how much variance exploration -- to spend on each query.

This connects to a subtle point about chain-of-thought prompting. Hugo nearly removed chain-of-thought from his 10 principles of effective prompting, given that modern reasoning models have adjustable effort built in. But Caleb Tutty pushes back in [[ws_2_prompting_and_context]], reporting that explicit step-by-step instructions still produce "quite dramatically" different results even with high-effort reasoning enabled. The implication is that non-determinism operates at multiple levels: the model's inherent stochasticity, the effect of prompting strategies on output distributions, and the reasoning architecture's own exploration of solution paths.

## Building Systems Around Non-Determinism

The practical response to non-determinism spans evaluation, observability, and system design. From [[ws_1_foundations]], the prescription is to log everything from day zero -- you cannot characterize a distribution you cannot observe. From [[ws_3_evals_and_feedback_loops]], the prescription is to evaluate statistically: look at distributions, not individual outputs; use confusion matrices, not spot checks; run tests multiple times, not once.

System design patterns that accommodate non-determinism include structured output constraints (forcing responses into schemas reduces output variance), guardrails (catching outputs that fall outside acceptable bounds), and the evaluator-optimizer pattern from [[ws_7_workflows_multiagent_and_context_engineering]] (generating multiple candidates and selecting the best). Carol Willing's practice of having three different LLMs audit code files in parallel, connected to Karpathy's LLM Council concept, explicitly leverages non-determinism as a diversity mechanism -- different models are more likely to catch different issues.

## Where Sources Agree

All sources agree that non-determinism is a fundamental property of LLM systems, not a bug to be fixed. They agree that building systems around it -- through evaluation, logging, structured constraints, and statistical thinking -- is the correct response. They agree that the double entropy problem (variance in both inputs and outputs) makes LLM systems qualitatively different from traditional software.

## Where Sources Disagree or Add Nuance

The most interesting divergence is on whether non-determinism is merely tolerable or actively beneficial. Hugo's framing in [[ws_1_foundations]] emphasizes building systems that "minimize risk" from non-determinism, treating it as a challenge to manage. Stella Liu's framing in [[next_level_evals_stella_eddie]] reframes it as a superpower for deep research and creative applications. Sebastian Raschka's architectural perspective in [[llm_architecture_rasbt]] shows that modern inference scaling deliberately exploits non-determinism for better results.

There is also a practical disagreement about whether temperature zero provides meaningful determinism. Ryan Rodriguez raises the question in [[ws_3_evals_and_feedback_loops]], and the discussion reveals that while temperature zero reduces variance, it does not eliminate it -- hardware differences, batching, and provider implementation details introduce variation. The safe stance is that LLMs are non-deterministic by nature, and any apparent determinism is fragile.

The hallucination framing adds further nuance. Stella notes that "hallucination" is a spectrum, potentially desirable in writing tools but definitely harmful in factual retrieval systems. Karpathy's assertion that LLMs hallucinate 100% of the time without retrieval grounding positions non-determinism as inseparable from the generative mechanism itself. Whether you call it hallucination, creativity, or variance depends on the application context.

## Related Concepts

- [[evaluation_driven_development]] -- Non-determinism makes evaluation necessary and demands statistical approaches rather than exact-match testing
- [[five_first_principles]] -- Non-determinism is the second of Hugo's five first principles for AI software development
- [[llm_as_judge]] -- LLM judges are themselves non-deterministic, adding variance to the evaluation layer
- [[observability_and_tracing]] -- Logging from day zero is the precondition for understanding non-deterministic system behavior
- [[llm_architecture_and_inference]] -- Inference scaling techniques deliberately exploit non-determinism through parallel sampling and sequential refinement

## Sources

- [[ws_1_foundations]] -- The "double entropy problem" framing; non-determinism as one of five first principles; building systems around it rather than solving it
- [[ws_3_evals_and_feedback_loops]] -- Monte Carlo-style repeated runs as testing strategy; debate about temperature zero determinism; statistical evaluation approaches
- [[next_level_evals_stella_eddie]] -- Non-determinism as superpower for deep research; hallucination as a spectrum; non-determinism requiring statistical rigor in evaluation
- [[llm_architecture_rasbt]] -- Inference scaling techniques (parallel sampling, sequential refinement) that exploit non-determinism; temperature, sampling, and reasoning effort at the architectural level
- [[ws_2_prompting_and_context]] -- Adjustable reasoning effort in GPT-5.4; chain-of-thought still producing different results even with reasoning models; model behavioral differences on identical prompts
