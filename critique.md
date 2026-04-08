# Adversarial Critique of `plan.md`

## Verdict

The plan is well-organized and faithfully translates Karpathy's vision into concrete steps. But it's a **waterfall build plan for what should be an iterative discovery process**, and it avoids the hard questions about information loss, LLM self-evaluation, and how you'll actually know if the result is useful.

---

## Critical Issues

### 1. Garbage in, garbage out — transcription errors are ignored

The VTT cleanup script (step 1a) handles *formatting* — strip timestamps, merge lines, preserve speaker labels. But the raw transcripts are full of ASR errors: "MADNA" for Moderna, "livereamed" for livestreamed, fragmented sentence boundaries. The `.md` files have similar artifacts. The plan produces clean-*looking* markdown from dirty transcripts, and then asks the LLM to synthesize from corrupted input. No denoising step exists.

### 2. The plan is waterfall, but the problem is iterative

Karpathy describes an incremental, evolving process: compile, query, discover gaps, enhance. This plan is a 10-step sequential pipeline: preprocess -> summarize -> extract concepts -> generate articles -> build indices -> lint -> commit. There's no "try querying, discover the concept boundaries are wrong, restructure" loop. You'll build the entire wiki before you learn whether it supports the questions you actually want to ask.

### 3. Information loss is the core risk, and it's unaddressed

You're compressing 410K words of messy transcripts into maybe 20-30K words of wiki. The most interesting insights in transcripts are often offhand remarks, tangential stories, and audience Q&A — exactly the things a "200-400 word structured summary" will drop. The plan has no strategy for managing this loss: no tiered detail levels, no way to flag "this transcript had unusually rich tangents," no mechanism to recover dropped insights later.

### 4. "LLM owns the wiki" is a principle, not a workflow

The plan says the LLM writes everything and humans correct via `compilation-log.md`. But what's the actual invocation pattern? If you add 3 new sources next week, do you re-run concept extraction from scratch? Append to existing concepts? How do you prevent re-compilation from *dropping* insights that were in previous versions? Git diffs will show you *what* changed but not *why* or whether the change lost something valuable.

### 5. LLM self-evaluation is weak evaluation

The linting steps (4a-4f) have the LLM checking its own work. Structural checks (orphans, broken links) are genuinely useful. But "consistency check" (4c) only catches contradictions, not shared errors. "Accuracy spot-check" (4f) is limited by context window — you can't feed a 28K-word VTT and a concept article together. The plan has **no external success criteria**. How do you know the wiki is better than just... searching the raw transcripts?

### 6. 15-25 concepts is a guess with no criteria

Step 1d says "identify 15-25 cross-cutting concepts." Why not 8? Why not 50? The plan provides no criteria for what makes a good concept boundary — granularity, overlap tolerance, minimum source coverage. This is arguably the most important design decision in the whole project, and it's fully delegated to a single LLM pass with no human review gate.

### 7. The concept/theme distinction is blurry

`wiki/concepts/` contains "cross-cutting" articles synthesized across sources. `wiki/themes/` contains "cross-cutting narrative articles spanning multiple concepts." What's the actual difference? If "agentic workflows" is a concept and "the shift from tools to agents" is a theme, the boundary is subjective and will confuse both the LLM and the reader.

---

## Minor Issues

- **People pages are low-value.** You already know who Eric Ma and Ravin Kumar are. Pages with "role, appearances, contributions" are filler that inflate the link graph without adding understanding.
- **No parallelism.** 21 source summaries are embarrassingly parallel, but the plan implies sequential Claude Code sessions. This will be slow.
- **Scale mismatch.** Karpathy cites ~100 articles / ~400K words as where Q&A gets interesting. Your *input* is 410K words, but the compiled wiki will be ~20-30K words — well below that threshold. The infrastructure may be overkill for the current corpus size.
- **The interesting part is deferred.** Q&A and output generation are "Not In Scope Now," but they're where the value lives. Front-loading all compilation before testing queries means you can't course-correct the wiki structure based on actual usage.
- **`_source_registry.md` is metadata the LLM could derive on the fly.** A table of titles, dates, and word counts is trivially re-generable. Maintaining it as a static file adds an update burden with marginal benefit.

---

## What I'd Change

1. **Start with Q&A, not compilation.** Pick 5 questions you want the wiki to answer. Build just enough wiki to answer them. Then expand.
2. **Add a denoising pass** before summarization — have the LLM fix obvious transcription errors in the cleaned VTTs.
3. **Let concepts emerge iteratively.** Don't commit to 15-25 concepts upfront. Start with source summaries, do some Q&A, let the concept structure reveal itself through use.
4. **Define success criteria.** "Can the wiki answer these 10 specific questions better than searching raw transcripts?" gives you something to test against.
5. **Drop themes and people pages** until you actually need them. They can always be added later; removing a bad ontology is harder.
6. **Plan for incremental updates.** What happens when source 22 arrives? The plan should describe the update workflow, not just the initial build.
