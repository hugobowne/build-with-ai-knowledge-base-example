# LLM Knowledge Base

This knowledge base comes from the fifth and final quarter of our [Building AI Applications for Data Scientists and Software Engineers -- from First Principles](https://maven.com/hugo-stefan/building-ai-apps-ds-and-swe-from-first-principles) course on Maven.

A structured knowledge base compiled from ~36 hours of AI/ML content: course workshops, guest talks, builders club sessions, and a demo day. Speakers include Sebastian Raschka, Ines Montani, Katharine Jarmul, Ravin Kumar (Google DeepMind), Ivan Leo (Google DeepMind), Eric Ma (Moderna), William Horton (Maven Clinic), Stella Liu, Eddie Landesberg, John Berryman, Doug Turnbull, and many others.

The wiki is ready to use. Clone the repo, open `wiki/` as an [Obsidian](https://obsidian.md/) vault, and start exploring.

## Quick start

1. Install [Obsidian](https://obsidian.md/) (free)
2. Clone this repo
3. In Obsidian: "Open folder as vault" and select the `wiki/` directory
4. Open the graph view (Ctrl/Cmd+G) to see how everything connects, then dive into `_index.md` for a guided overview

## What's in the wiki

- **21 sources** (~341K words): 8 course workshops, 8 guest talks, 3 builders club sessions, 1 demo day
- **29 concept articles**: cross-cutting topics like context engineering, eval-driven development, RAG, prompt engineering, agents vs workflows
- **21 people pages**: speakers and contributors
- **6 theme essays**: narrative threads spanning multiple concepts and sources
- **Navigation**: index, map of content, glossary, source registry, all interlinked with `[[wiki-links]]`

## How this was built

Andrej Karpathy [tweeted about using LLMs to build personal knowledge bases](karpathy_tweet.md): compiling raw sources into interlinked Obsidian wikis. He hadn't yet shared his code or process, so I decided to reverse-engineer it with Claude.

I took his tweet, had Claude draft a [plan](plan.md), wrote an [adversarial critique](critique.md) of that plan, then generated an [updated plan](plan_updated.md) incorporating the critique. From there, Claude and I executed it step by step: cleaning transcripts, generating summaries, extracting concepts, cross-linking everything, and running multi-agent review swarms for accuracy.

The pipeline:

1. **Ingest**: raw transcripts (VTT) are cleaned and denoised into markdown
2. **Summarize**: an LLM generates structured source summaries with highlights and cross-references
3. **Extract**: concepts are identified across all sources; articles, people pages, and themes are generated
4. **Link**: everything is cross-linked with wiki-links; navigation files are built
5. **Lint**: broken links, contradictions, coverage gaps, and accuracy are checked

New content follows the same pipeline. See [process.md](process.md) for operational details and [plan_updated.md](plan_updated.md) for the full build plan.

## Project structure

```
wiki/                       # The Obsidian vault: open this in Obsidian
  sources/                  # One summary per raw source
  concepts/                 # Cross-cutting concept articles
  people/                   # Speaker/contributor pages
  themes/                   # Narrative essays spanning concepts
  outputs/                  # Q&A results, visualizations
  _index.md                 # Master landing page: start here
  _source_registry.md       # Table of all sources
  _map_of_content.md        # Concepts grouped by theme
  _glossary.md              # Key terms and definitions
  _logs/                    # Compilation and lint logs
raw/                        # Source material (transcripts, blog posts), not committed
scripts/                    # Python utilities for ingesting new content
```

## Key principles

- **The LLM owns the wiki**: human corrections go through the compilation log, not direct edits
- **Parallelization**: independent tasks (summaries, concept articles) are processed in parallel batches
- **Iterative refinement**: multi-agent review swarms check accuracy, attribution, and consistency
- **Preserve the raw**: summaries include highlights pointing back to the richest parts of source material

## What's next

Karpathy later published a more detailed writeup of his pattern: [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), covering the three-layer architecture (raw sources, wiki, schema), operations (ingest, query, lint), and indexing strategies. Planning to try that out and see how it compares to what we built here.

---

If you find this helpful, please star the repository and share it with a friend. For more independent AI education like this, [subscribe to our Substack](https://hugobowne.substack.com/).

We're planning to expand this material and run more workshops on local LLMs and building AI products with them. If you want to be first to hear about it, [let us know what you're interested in here](https://tally.so/r/EkLjyA).
