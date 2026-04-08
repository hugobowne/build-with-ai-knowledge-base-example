# LLM Knowledge Base — Build Plan

Based on [Karpathy's post](karpathy_tweet.md) on using LLMs to build personal knowledge bases. Each section below quotes the relevant part of his post, then describes what we're building.

---

## Project Setup

**Dependencies:** managed with `uv`

```
uv init
uv add webvtt-py   # parsing VTT subtitle files
uv add matplotlib   # visualizations (for Output phase)
```

The VTT cleanup script is the only code we write upfront. Everything else is LLM compilation done through Claude Code sessions. We keep dependencies minimal and add as needed.

**Obsidian:** set vault root to `llm-kb/` so both `raw/` and `wiki/` are visible.

---

## In Scope Now

### 1. Data Ingest → Karpathy: "Data ingest"

> "I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally 'compile' a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all."

- [ ] **1a. VTT preprocessing script** — Python script using `webvtt-py` to convert `.vtt` files in `raw/` to clean markdown in `raw/_cleaned/`. Strips cue numbers and timestamp lines, merges consecutive speaker lines into paragraphs, preserves speaker labels as `**Speaker:**`, inserts periodic timestamp markers (`[~05:00]`). Already-clean `.md` files in `raw/` need no preprocessing.

- [ ] **1b. Source summaries** — For each raw source (cleaned VTTs + existing `.md` files), use the LLM to generate a structured summary in `wiki/sources/`. Each summary includes: YAML frontmatter (type, date, speakers, topics), 200-400 word overview, key topics, key insights, people/tools mentioned, quotable moments, and connections to other sources. All references use `[[wiki-link-syntax]]`. Process one source at a time (context window constraint).

- [ ] **1c. Source registry** — Build `wiki/_source_registry.md`: a table of all raw sources with title, date, speakers, word count, and link to each summary. This is one of Karpathy's "auto-maintained index files."

- [ ] **1d. Concept extraction** — Feed all source summaries (~15-20K words total) to the LLM in one pass. Identify 15-25 cross-cutting concepts, map which sources discuss each, propose filenames.

- [ ] **1e. Concept articles** — Generate one article per concept in `wiki/concepts/`. Each synthesizes across sources: overview, key points with source links, where sources agree/disagree, related concepts, and a sources section. These are the heart of the wiki — Karpathy's "categorizes data into concepts, writes articles for them, and links them all."

- [ ] **1f. People pages** — Lightweight pages in `wiki/people/` for key speakers: role, appearances, contributions, notable quotes. Exist mainly for Obsidian backlink navigation.

- [ ] **1g. Theme pages** — Cross-cutting narrative articles in `wiki/themes/` that tell a story spanning multiple concepts and sources.

- [ ] **1h. Backlinks and cross-linking** — Ensure all wiki pages use `[[wiki-link-syntax]]` consistently. Source summaries link to concepts, concept articles link to sources and other concepts, people pages link to appearances. Obsidian handles reverse backlinks automatically.

### 2. Index and Navigation → Karpathy: "Data ingest" + "Q&A"

> "The LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale."

- [ ] **2a. `_index.md`** — Master landing page linking to everything, grouped logically.
- [ ] **2b. `_map_of_content.md`** — Concepts grouped by theme (Obsidian MOC pattern).
- [ ] **2c. `_glossary.md`** — Key terms with definitions and links to concept articles.

These index files are how the LLM navigates the wiki for Q&A — progressive disclosure from index → concept → source summary → raw transcript. No RAG needed at this scale.

### 3. IDE Setup → Karpathy: "IDE"

> "I use Obsidian as the IDE 'frontend' where I can view the raw data, the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly."

- [ ] **3a. Obsidian vault** — Open `llm-kb/` as vault. Enable Graph View. Verify wikilinks resolve, backlinks work, graph shows link structure.
- [ ] **3b. The LLM owns the wiki** — Human corrections go through `wiki/_logs/compilation-log.md` and the next enhancement pass. You don't edit wiki files directly.

### 4. Linting → Karpathy: "Linting"

> "I've run some LLM 'health checks' over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity."

- [ ] **4a. Orphan detection** — Find files with no incoming or outgoing links.
- [ ] **4b. Broken link detection** — Verify all `[[link]]` targets exist.
- [ ] **4c. Consistency check** — LLM compares concept articles for contradictory claims.
- [ ] **4d. Coverage gaps** — LLM checks if important source insights are missing from concept articles.
- [ ] **4e. Connection discovery** — LLM identifies non-obvious relationships between concepts ("find interesting connections for new article candidates").
- [ ] **4f. Accuracy spot-check** — LLM verifies sample summaries against raw transcripts.

Results go to `wiki/_logs/lint-report.md`.

---

## Directory Structure

```
llm-kb/
  karpathy_tweet.md
  plan.md
  pyproject.toml
  raw/
    _cleaned/              # VTTs converted to clean markdown
    *.md                   # already-clean source transcripts
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

> "Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. Often, I end up 'filing' the outputs back into the wiki to enhance it for further queries."

- Marp slideshows (needs Marp Obsidian plugin or `marp-cli`)
- matplotlib visualizations
- Filing outputs back into `wiki/outputs/` with links from concept articles
- Explorations and queries "always add up" in the knowledge base

### Extra Tools → Karpathy: "Extra tools"

> "I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries."

- Search engine over the wiki (web UI + CLI)
- Batch update scripts for when new sources are added
- Tools grow organically from use

### Synthetic Data & Finetuning → Karpathy: "Further explorations"

> "As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM 'know' the data in its weights instead of just context windows."

- Generate training data from the wiki's clean markdown + metadata
- Finetune a model to "know" the knowledge base

---

## Execution Order

| Step | What | Depends on |
|------|------|-----------|
| 0 | `uv init`, add dependencies | — |
| 1 | Write + run VTT cleanup script | 0 |
| 2 | Source summaries for `.md` talk transcripts | — |
| 3 | Source summaries for cleaned VTTs | 1 |
| 4 | Build `_source_registry.md` | 2, 3 |
| 5 | Concept extraction + concept articles | 2, 3 |
| 6 | People pages + theme pages | 5 |
| 7 | Index files (`_index`, `_map_of_content`, `_glossary`) | 5, 6 |
| 8 | Set up Obsidian vault, verify links | 7 |
| 9 | Lint checks, fix issues | 7 |
| 10 | Git commit | 9 |
