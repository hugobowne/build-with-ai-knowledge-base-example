---
type: concept
title: "Prompt Engineering"
related_concepts: [context_engineering, evaluation_driven_development, the_api_call_mental_model, model_selection_and_tradeoffs, non_determinism]
---

## Overview

Prompt engineering is the art and practice of writing effective instructions for LLMs -- crafting the text that tells a model what to do, how to do it, and what constraints to respect. Despite recurring claims that "prompt engineering is dead," the course treats it as a foundational skill that remains one of the most impactful levers in the AI development lifecycle, especially in early stages. Hugo Bowne-Anderson addresses this directly in [[ws_2_prompting_and_context]]: "Prompt engineering is dead -- that's just so far from the truth."

The practice spans a wide range of sophistication. At one end, it is a developer carefully choosing words and structuring instructions. At the other, it involves systematic iteration through hundreds of prompt versions, A/B testing alternatives, and understanding how prompts interact with model training (what Drew Brunig's research calls "fighting the weights"). The iteration count varies enormously by use case: Thomas Vicky from PiMC Labs achieved production-quality synthetic surveys for Colgate in just 8 iterations, while Nathan from Carvana spent 600+ iterations on Fortune 500 public-facing car descriptions. Most course participants report iterating about 3 times on a prompt before shipping, which Hugo considers about right for most cases.

Prompt engineering exists in tension with two related concepts. First, with [[context_engineering]] -- as systems mature, the machine that assembles the prompt becomes more important than the prompt itself. Second, with model training -- system prompts can conflict with deeply trained model behaviors, a phenomenon William Horton experienced at Maven Clinic when he had to write regex to strip Gemini's persistent medical disclaimers because "this stuff's probably trained very deeply into the model, so it's very hard to override that with the instructions sometimes." This tension between instruction and training is what Drew Brunig's research identifies as coding harnesses having "thousands to tens of thousands of tokens that are essentially fighting the weights."

## The 10 Principles of Effective Prompting

Hugo presents 10 principles in [[ws_2_prompting_and_context]] that structure the practice:

Defining roles gives the model a persona and behavioral anchor. Giving instructions specifies the task clearly. Output constraints (format, length, structure) reduce variance and increase usefulness. Providing context supplements the model's knowledge with relevant information. Using delimiters prevents prompt injection by clearly separating instructions from user-provided content. Few-shot examples demonstrate desired behavior through concrete instances. Explicit rules set boundaries the model should not cross. Handling ambiguity instructions tell the model what to do when the input is unclear. Saying what not to do (negative constraints) is often as important as saying what to do. And chain-of-thought prompting encourages step-by-step reasoning.

Hugo nearly removed chain-of-thought from the list, given that modern reasoning models have adjustable reasoning effort built in. But Caleb Tutty pushed back with evidence from legal transcription work: explicit step-by-step instructions still produce "quite dramatically" different results even with high-effort reasoning enabled for sequential tasks. This suggests that chain-of-thought as a prompting technique and chain-of-thought as a trained behavior operate at different levels, with the prompting technique still adding value on top of the model's native reasoning capabilities.

## Prompt Engineering in Production

In production systems, prompt engineering becomes more demanding. William Horton describes his approach in [[william_horton_maven_clinic]] as "beat-it-over-the-head prompting" -- for critical instructions, he places them at both the start and the end of the prompt. He explicitly told the Maven health agent that "you don't know what date it is" and gave it a dedicated tool for date reasoning, because the model "thinks it does, and it doesn't." This level of explicitness -- redundancy for critical constraints, tool-based workarounds for known model failures -- characterizes production prompt engineering.

Tool descriptions represent another dimension of prompt engineering that practitioners underestimate. John Berryman and Doug Turnbull discuss in [[search_agents_john_doug]] how tool descriptions require per-provider iteration. Hugo demonstrates in [[ws_6_building_ai_agents]] that the same tool description works on GPT-5 but fails on Gemini 2.5 Flash, requiring prompt-level adjustments. This provider-specific tuning of tool descriptions is prompt engineering applied to the agent's capability surface rather than its instruction set.

Ivan Leo introduces meta-prompting in [[deep_research_agent_ivan_leo]] -- asking models to improve their own prompts and tool descriptions. This technique "wouldn't have been possible a year or two ago" and represents a shift where prompt engineering partially automates itself. The model reviews its own tool descriptions and suggests improvements, which the developer evaluates and incorporates.

## The Iteration Spectrum

The enormous range of iteration counts -- from 8 to 600+ -- reflects real differences in risk profile and use case. Nathan's 600+ iterations at Carvana were warranted because the output was public-facing at a Fortune 500 company, where each word carries brand risk. Thomas Vicky's 8 iterations for synthetic surveys worked because the output was internal and the task was well-constrained. Natalia Rodnova offers a pragmatic ceiling: "after 50 iterations I'm just gonna give up and try something else," suggesting that when prompt engineering alone cannot solve the problem, the answer lies in different approaches -- better context, different tools, or fine-tuning.

Stefan Krawczyk frames the iteration process in [[ws_4_testing_and_observability]] through his two-loop model: the inner development loop involves local prompt tuning with test cases, while the outer production loop feeds deployed telemetry back into prompt refinement. This systematic framing elevates prompt engineering from an art to an engineering practice with feedback loops.

## Where Sources Agree

All sources agree that prompt engineering is not dead and remains a foundational skill. They agree that iteration is essential -- the first prompt is rarely the final prompt. They agree that different models respond differently to identical prompts, making model-specific prompt tuning necessary. And they agree that as systems mature, the focus shifts from hand-crafted prompts to automated context engineering, but this does not eliminate the need for prompt engineering skill.

## Where Sources Disagree or Add Nuance

The main tension is between prompt engineering and model training. William Horton's experience at Maven Clinic shows that post-training behaviors (Gemini's medical disclaimers) can be so deeply embedded that no system prompt can override them, requiring "more heavy-handed tactics" like regex stripping. Drew Brunig's research, shared by Brad Morris in [[ws_2_prompting_and_context]], quantifies this: system prompts in coding agents contain thousands of tokens fighting the model's weights. This raises the question of whether prompt engineering has fundamental limits imposed by model training.

On the necessity of chain-of-thought, the course shows a productive disagreement. Hugo's instinct to remove it from his principles reflects the reality that reasoning models have absorbed this technique. Caleb's pushback reflects the empirical reality that explicit chain-of-thought still changes results. The resolution may be that chain-of-thought prompting and trained reasoning are complementary rather than redundant.

The relationship between prompt engineering and context engineering also generates debate. William Horton questions in [[ws_4_testing_and_observability]] whether context engineering is really different from prompt engineering. The resolution offered across sources is one of scale and automation: prompt engineering is what a human writes; context engineering is building the system that writes it. But in practice, the boundary is porous -- a developer writing a system prompt template with retrieval placeholders is doing both simultaneously.

## Related Concepts

- [[context_engineering]] -- The automated counterpart; building the machine that populates what prompt engineering crafts by hand
- [[evaluation_driven_development]] -- Prompt iteration is guided by evaluation; error analysis drives prompt changes
- [[the_api_call_mental_model]] -- Prompts map to specific parts of the API call (system prompt, user messages, tool descriptions)
- [[model_selection_and_tradeoffs]] -- Different models respond differently to identical prompts; model choice and prompt design are intertwined
- [[non_determinism]] -- Prompts interact with stochastic generation, making prompt effects probabilistic rather than deterministic

## Sources

- [[ws_2_prompting_and_context]] -- The 10 principles, iteration counts (8 to 600+), system vs. user prompts, chain-of-thought debate, "fighting the weights"
- [[william_horton_maven_clinic]] -- "Beat-it-over-the-head prompting," regex stripping of model safety behaviors, date awareness workarounds
- [[ws_4_testing_and_observability]] -- Prompt tuning in the two-loop development model; system prompts fighting the weights
- [[deep_research_agent_ivan_leo]] -- Meta-prompting: models improving their own prompts and tool descriptions
- [[search_agents_john_doug]] -- Tool descriptions requiring per-provider iteration; prompt engineering applied to agent capability surfaces
