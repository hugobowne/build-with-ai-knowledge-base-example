# LLM Knowledge Base — Updated Build Plan

Based on [Karpathy's post](karpathy_tweet.md), the [original plan](plan.md), and its [adversarial critique](critique.md). Key changes: iterative over waterfall, denoising added, information-loss mitigation via highlights, parallelization, incremental update workflow defined upfront.

---

## Project Setup

**Dependencies:** managed with `uv`

```
uv init
uv add webvtt-py   # parsing VTT subtitle files
uv add matplotlib   # visualizations (for Output phase)
uv add seaborn      # visualizations
```

The VTT cleanup script is the only code we write upfront. Everything else is LLM compilation done through Claude Code sessions. We keep dependencies minimal and add as needed.

**Obsidian:** set vault root to `llm-kb/` so both `raw/` and `wiki/` are visible.

---

## In Scope Now

### 1. VTT Cleanup + Denoising → Karpathy: "Data ingest"

> "I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally 'compile' a wiki..."

- [x] **1a. VTT preprocessing script** — Python script using `webvtt-py` to convert `.vtt` files in `raw/` to clean markdown in `raw/_cleaned/`. Strips cue numbers and timestamp lines, merges consecutive speaker lines into paragraphs, preserves speaker labels as `**Speaker:**`, inserts periodic timestamp markers (`[~05:00]`). Already-clean `.md` files in `raw/` need no preprocessing. ✅ `scripts/clean_vtt.py` — 15 VTTs cleaned.
- [x] **1b. LLM denoising pass** — Run over each cleaned VTT and each existing `.md` file. Fix ASR errors (e.g. "MADNA" → "Moderna", "livereamed" → "livestreamed"), fix fragmented sentence boundaries. Preserve meaning — correct transcription artifacts, don't rewrite. All 21 denoising passes are independent and can run in parallel. ✅ `scripts/denoise.py` — 18/21 files modified. Key fixes: speaker name capitalization (981 instances), Crouchik→Krawczyk, Carpathy→Karpathy, Yugo/Hugh→Hugo, Robeita→RoBERTa.

### 2. Source Summaries (parallel, then link) → Karpathy: "Data ingest"

> "The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all."

- [x] **2a. Generate source summaries** — For each raw source (cleaned VTTs + existing `.md` files), generate a structured summary in `wiki/sources/`. Each includes: YAML frontmatter (type, date, speakers, topics), 200-400 word overview, key topics, key insights, people/tools mentioned, quotable moments. All 21 summaries generated **in parallel**. ✅ 21/21 summaries in `wiki/sources/`. Generated in 4 parallel batches.
- [x] **2b. Highlights section** — Each summary includes a highlights section flagging specific timestamps/sections worth returning to in the raw transcript: surprising claims, disagreements between speakers, concrete examples, deep audience Q&A. These are pointers back to the richest parts, preserving what the summary compresses away. ✅ Included in each summary. Timestamps are approximate (~5min markers from VTT cleanup).
- [x] **2c. Linking pass** — Feed all 21 summaries to the LLM, add cross-references and `[[wiki-links]]` between related sources. ✅ 215 wiki-links added across all 21 files (9-12 per file). Each file has inline links + a Related Sources section.
- [ ] **2d. Review pass** — For each summary, check whether the highlights caught anything the summary missed. Flag gaps. ⏳ Not yet done (deferred — doing concept review first).

### 3. Source Registry + Concept Extraction → Karpathy: "Data ingest" + "Q&A"

> "The LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents..."

- [x] **3a. Source registry** — Build `wiki/_source_registry.md`: table of all raw sources with title, date, speakers, word count, and link to each summary. ✅ 21 sources, ~341K words total.
- [x] **3b. Concept extraction** — Feed all source summaries to the LLM in one pass. Identify cross-cutting concepts, map which sources discuss each, propose filenames. No fixed target for number of concepts — let it emerge from the content. ✅ 27 concepts extracted → `wiki/_concept_list.md`. Each maps to 3-6 sources.
- [x] **3c. Concept review** — Three parallel reviews of the concept list: (1) coverage gaps — topics in transcripts not captured by any concept, (2) boundary review — overlaps, blurry distinctions, granularity issues, (3) accuracy spot-check — verify concept descriptions against raw transcripts. ✅ Added 3 concepts (Five First Principles, Structured Output, Synthetic Data), merged Comparative Evaluation into Eval-Driven Development, fixed attributions (Moderna audit source, Kirby analogy, dark patterns), corrected boundaries (skills → Context Engineering, workflow primitives → Agents vs Workflows). Final count: 29 active concepts.

### 4. Wiki Content Generation → Karpathy: "Data ingest"

> "...it categorizes data into concepts, writes articles for them, and links them all."

- [x] **4a. Concept articles** — One per concept in `wiki/concepts/`. Each synthesizes across sources: overview, key points with source links, where sources agree/disagree, related concepts, sources section. ✅ 29 concept articles generated in 4 parallel batches. 11-agent review swarm checked: articles vs source summaries, cross-concept consistency, quote accuracy, disagreement section integrity, claims against raw transcripts, dropped content. Fixes applied: attribution corrections (Kirby→Doug, "rip out harness"→Nicholas Moy, Jarmul quote, Eddie Landesberg policy eval framing), fabricated disagreement sections rewritten (ai_sdlc, five_first_principles), fine-tuning caveats added, line counts corrected, Pi/OpenClaw distinction clarified.
- [x] **4b. People pages** — Lightweight pages in `wiki/people/` for key speakers: role, appearances, contributions, notable quotes. ✅ 21 people pages. Category tags added (instructor, guest_speaker, builder_in_residence, student).
- [x] **4c. Theme pages** — Cross-cutting narrative articles in `wiki/themes/` spanning multiple concepts and sources. ✅ 6 themes: From Demo to Production, Cutting Through the Hype, Trust/Safety/Human Oversight, Building Blocks of Intelligent Systems, The Data Flywheel, The Shifting Boundary.
- [x] **4d. Backlinks and cross-linking** — Ensure all wiki pages use `[[wiki-link-syntax]]` consistently. ✅ 1,584 wiki-links across all files, 0 broken. Source filenames renamed with workshop_/guest_/builders_club_ prefixes for graph readability.

### 5. Index Files + Obsidian Setup → Karpathy: "IDE"

> "I use Obsidian as the IDE 'frontend' where I can view the raw data, the compiled wiki, and the derived visualizations."

- [x] **5a. `_index.md`** — Master landing page linking to everything, grouped logically. ✅ Concepts grouped into 7 thematic clusters, sources by type.
- [x] **5b. `_map_of_content.md`** — Concepts grouped by theme (Obsidian MOC pattern). ✅ 7 clusters with one-line descriptions per concept.
- [x] **5c. `_glossary.md`** — Key terms with definitions and links to concept articles. ✅ 70+ terms defined alphabetically.
- [x] **5d. Obsidian vault** — Open `wiki/` as vault. Graph view with color-coded groups by type (concept, workshop, guest_talk, person, theme etc.) configured in `.obsidian/graph.json`. ✅
- [ ] **5e. The LLM owns the wiki** — Human corrections go through `wiki/_logs/compilation-log.md` and the next enhancement pass. You don't edit wiki files directly.

### 6. Linting → Karpathy: "Linting"

> "I've run some LLM 'health checks' over the wiki to e.g. find inconsistent data, impute missing data, find interesting connections for new article candidates..."

- [ ] **6a. Orphan detection** — Find files with no incoming or outgoing links.
- [x] **6b. Broken link detection** — Verify all `[[link]]` targets exist. ✅ 0 broken links across 1,584 total. Checked after every rename/edit pass.
- [x] **6c. Consistency check** — LLM compares concept articles for contradictory claims. ✅ Cross-concept review found 5 contradictions (Kirby attribution, "rip out harness" attribution, Moderna audit source, coding agent line count, Eric Ma file size). All fixed.
- [x] **6d. Coverage gaps** — LLM checks if important source insights are missing from concept articles. ✅ 16 dropped insights identified; most are career/organizational content outside concept scope. A few practical tips worth folding in later.
- [ ] **6e. Connection discovery** — LLM identifies non-obvious relationships between concepts.
- [x] **6f. Accuracy spot-check** — LLM verifies sample summaries against raw transcripts. ✅ 11-agent review swarm verified claims against WS-1–8, guest talks, and source summaries. Issues found were cosmetic (attribution, quote precision). Substantive content held up.

Results go to `wiki/_logs/lint-report.md`.

### 7. Incremental Update Workflow

When new source content is added to `raw/`:

- [ ] **7a.** Clean + denoise new files (Phase 1)
- [ ] **7b.** Generate source summaries for new files
- [ ] **7c.** Run linking pass across **all** summaries (old + new)
- [ ] **7d.** Re-run concept extraction across **all** summaries — diff against existing concept list
- [ ] **7e.** Update existing concept articles that the new content touches
- [ ] **7f.** Create new concept articles if new concepts emerged
- [ ] **7g.** Update people/theme pages as needed
- [ ] **7h.** Regenerate index files
- [ ] **7i.** Run linting

Key principle: concepts are always derived from the full set of summaries, never patched incrementally.

---

## Directory Structure

```
llm-kb/
  karpathy_tweet.md
  plan.md
  plan_updated.md
  critique.md
  pyproject.toml
  raw/
    _cleaned/              # VTTs converted + denoised to clean markdown
    *.md                   # source transcripts (denoised in place)
    *.vtt                  # raw subtitle files
  wiki/
    _index.md
    _source_registry.md
    _map_of_content.md
    _glossary.md
    _logs/
      compilation-log.md
      lint-report.md
    sources/
    concepts/
    people/
    themes/
    outputs/
```

---

## Not In Scope Now (Later)

### Q&A → Karpathy: "Q&A"

> "Once your wiki is big enough (~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc."

We can start doing Q&A as soon as the wiki is compiled — just ask questions in Claude Code sessions. But formalizing a Q&A workflow (e.g., always filing answers back, maintaining an output index) comes after the wiki exists.

### Output Formats → Karpathy: "Output"

> "Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images..."

- Marp slideshows (needs Marp Obsidian plugin or `marp-cli`)
- matplotlib visualizations
- Filing outputs back into `wiki/outputs/` with links from concept articles
- Explorations and queries "always add up" in the knowledge base

### Extra Tools → Karpathy: "Extra tools"

> "I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki..."

- Search engine over the wiki (web UI + CLI)
- Batch update scripts for when new sources are added
- Tools grow organically from use

### Synthetic Data & Finetuning → Karpathy: "Further explorations"

> "As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM 'know' the data in its weights instead of just context windows."

- Generate training data from the wiki's clean markdown + metadata
- Finetune a model to "know" the knowledge base

---

## Web Clipping Protocol

When new content is clipped via the Obsidian Web Clipper:

1. **Clip lands in `wiki/Clippings/`** — the clipper saves it as markdown with frontmatter (title, source URL, author, date, tags). No action needed.

2. **Triage** — decide if it's worth processing into the wiki:
   - Is it related to course content or topics the wiki covers?
   - Does it add something the wiki doesn't already have?
   - If no to both, leave it in Clippings as a reference. Done.

3. **Generate source summary** — if worth processing:
   - Read the clipped article
   - Write a source summary to `wiki/sources/` following the same format as existing summaries (frontmatter, overview, key topics, key insights, highlights)
   - Use `type: blog_post` (or `podcast`, `repo`, `slides` etc.) in frontmatter
   - Add `[[wiki-links]]` to existing concepts and sources

4. **Update existing concept articles** — if the clipped content adds to existing concepts:
   - Add references and insights to relevant concept articles
   - Update "Sources" sections
   - Don't rewrite articles — just weave in the new material

5. **People pages** — link source summaries to existing people pages with `[[wiki-links]]`. Update people pages with new appearances. If a person appears in 2+ sources but has no people page, create one with the standard format and category tag.

6. **New concepts** — if the clipped content introduces a genuinely new cross-cutting idea not covered by existing concepts, add it to `_concept_list.md` and generate a new concept article.

7. **Update navigation** — add the new source to `_source_registry.md`. Update `_index.md` if needed.

8. **QA check** — verify source summaries against their original source material. Check for fabricated claims, misattributions, and accuracy of key insights. Fix any issues found.

9. **Run broken link check** — verify 0 broken links after changes.

Key principle: clipping is cheap, processing is selective. Not everything clipped needs a source summary. The Clippings folder is a staging area, not a backlog.

### To Do

- [ ] Add `related_source:` field to frontmatter linking blog posts to their corresponding podcast episodes (and vice versa) where one is a writeup of the other.

---

## Execution Order

| Step | What | Depends on | Parallelizable |
|------|------|-----------|----------------|
| 0 | `uv init`, add dependencies | — | — |
| 1a | Write + run VTT cleanup script | 0 | — |
| 1b | LLM denoising pass (all 21 files) | 1a (VTTs), — (MDs) | Yes, all 21 independent |
| 2a | Source summaries (all 21) | 1b | Yes, all 21 independent |
| 2b | Highlights sections | with 2a | — |
| 2c | Linking pass | 2a | — |
| 2d | Review pass | 2a, 2b | — |
| 3a | Source registry | 2c | — |
| 3b | Concept extraction | 2c | — |
| 4a | Concept articles | 3b | Yes, per concept |
| 4b | People pages | 2c | Yes, per person |
| 4c | Theme pages | 4a | — |
| 4d | Cross-linking pass | 4a, 4b, 4c | — |
| 5 | Index files + Obsidian setup | 4d | — |
| 6 | Linting | 5 | — |
