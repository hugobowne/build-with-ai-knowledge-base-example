---
type: person
name: "Eric Ma"
role: "Research Data Science Lead / Clinical Development Data Science Lead"
organization: "Moderna"
category: guest_speaker
---

## Appearances

- [[thinking_tools_eric_ma]] — Guest speaker; live-coded Canvas Chat v2 from scratch, demonstrated spec-driven development, LLM Council/committee feature, and refactoring vibecoded slop
- [[ws_6_building_ai_agents]] — Referenced for Moderna audit finding that all production AI was workflows, not agents
- [[ws_7_workflows_multiagent_and_context_engineering]] — Referenced for Moderna audit; LLM Council implementation connected to Karpathy's LLM Council discussed in this session
- [[llm_architecture_rasbt]] — Referenced as co-teacher of Bayesian inference tutorial at SciPy 2017 with [[sebastian_raschka]]

## Key Contributions

- Built Canvas Chat, a nonlinear branching conversation tool implementing Karpathy's LLM Council concept with multiple personas independently researching, cross-reviewing, and synthesizing answers
- Conducted the Moderna audit that found all production AI was workflows (not agents), a finding referenced across multiple workshops as evidence that most teams do not need agents
- Articulated the spec-driven development philosophy: never use strict specs for first prototypes (feel out the problem first), but once the problem/solution space is understood, specs and tests become double constraints that prevent coding agents from going off the rails
- Demonstrated systematic refactoring of "vibecoded slop" from monolithic 8,000+ line files into plugin architecture with small modules

## Notable Quotes

- "You can't know your problem deeply until you've built a wrong solution. So just build and if it's wrong you'll feel it." — [[thinking_tools_eric_ma]]
- "I opusmaxed a lot of Canvas Chat and I didn't check the architecture. I didn't look at how code was organized. I was just like build build build until it became really painful to add new features." — [[thinking_tools_eric_ma]]
- "If Anthropic had to go under and the Claude models were lost forever, I'd be okay switching to other models because I'm not so used to the temperament or the personality." — [[thinking_tools_eric_ma]]
