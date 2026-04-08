---
type: person
name: "Caleb Tutty"
role: "Consultant"
organization: "Independent (based in Jakarta)"
category: student
---

## Appearances

- [[ws_2_prompting_and_context]] — Shared experience from legal transcription ASR work showing chain-of-thought still helps even with reasoning models
- [[ws_4_testing_and_observability]] — Discussed model upgrade testing processes; noted still on GPT-5.1 in production
- [[ws_6_building_ai_agents]] — Expressed concern about running agents on real filesystems; raised key open question about guardrails and unexpected tool access
- [[ws_7_workflows_multiagent_and_context_engineering]] — Raised practical concerns about evaluator-optimizer pattern needing very good exit conditions to avoid infinite loops
- [[ws_8_finetuning_and_production_ai]] — Contributed to production patterns discussion
- [[demo_day]] — Presented 3D printing agent extending [[deep_research_agent_ivan_leo]] with OpenSCAD as a tool in Docker, generating iterative 3D-printable objects with automated validation

## Key Contributions

- Built a 3D printing agent that extends the deep research workshop to include OpenSCAD in Docker containers, enabling iterative generation of 3D-printable objects (vases, chess sets, drone assemblies) with automated validation scripts
- Pushed back on the claim that chain-of-thought is obsolete with reasoning models, reporting from production experience that explicit step-by-step instructions still change outputs "quite dramatically"
- Raised important safety and guardrail questions about agent autonomy, including the key open question: "Is there a compromise where guardrails let something have access to tools in maybe an unexpected way?"

## Notable Quotes

- "When I saw the workshop with Hugo and Ivan, I thought, this is a runtime and a harness that could be used for pretty much anything that needs to use tools." — [[demo_day]]
