---
type: person
name: "William Horton"
role: "Staff ML Engineer"
organization: "Maven Clinic"
category: builder_in_residence
---

## Appearances

- [[ws_1_foundations]] — Builder in residence; contributed Pets.com/Chewy analogy about being "too early" in AI
- [[ws_2_prompting_and_context]] — Shared experience writing regex to strip Gemini medical disclaimers that system prompting could not override
- [[ws_3_evals_and_feedback_loops]] — Advocated strongly for comparative evaluation over single-item evaluation, and free-text feedback columns
- [[ws_4_testing_and_observability]] — Argued against internal frameworks, advocated OpenAI SDK + LiteLLM gateway pattern
- [[ws_5_context_engineering_and_information_retrieval]] — Contributed to context engineering discussions; noted "Gemini 2.5 Flash is fast but relatively dumb"
- [[ws_6_building_ai_agents]] — Contributed to agent safety discussion, expressed concern about running agents on real filesystems
- [[ws_8_finetuning_and_production_ai]] — Contributed to production patterns discussion including BAAs with providers
- [[builders_club_william_horton]] — Led session on AI engineering careers, eval design, and multi-agent architecture challenges at Maven Clinic
- [[william_horton_maven_clinic]] — Detailed Q&A the day after launching Maven Assistant; covered multi-agent architecture, LLM-as-judge, guardrails, and first-day production discoveries

## Key Contributions

- Built and launched Maven Assistant, a production multi-agent health AI system with lead agent routing to specialized sub-agents, input guardrails (off-topic, prompt hacking, self-harm), and LLM-as-judge evaluation
- Championed comparative evaluation as more efficient than single-item pass/fail labeling: "your choice is always System A or System B"
- Developed judge alignment process using two human labelers to establish inter-annotator agreement before calibrating LLM judges
- Articulated that evaluation is the most important AI engineering skill and described the ideal hire as someone who can diagnose agent misbehavior, fix it, and quantify improvement

## Notable Quotes

- "Making people compare and choose the better one is a more efficient way of labeling... In the end, your choice is always just gonna be, do I deploy System A or System B?" — [[ws_3_evals_and_feedback_loops]]
- "I honestly just want to pick up the OpenAI SDK. I don't want to use your wrapper." — [[ws_4_testing_and_observability]]
- "I practice beat-it-over-the-head prompting. For things that are really important, I put it at the start and the end." — [[william_horton_maven_clinic]]
- "The biggest skill to me is how to get an LLM to do what you want... a combination of prompt engineering and evaluation, with more emphasis on evaluation." — [[builders_club_william_horton]]
