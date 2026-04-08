# LLM Knowledge Base — Operations Process

How to add new content to the wiki and maintain it.

---

## Source Types

| Type | Frontmatter `type` | Filename prefix | Example |
|------|-------------------|-----------------|---------|
| Course workshop | `workshop` | `workshop_` | `workshop_1_ai_sdlc_foundations` |
| Guest talk/Q&A | `guest_talk` | `guest_` | `guest_privacy_in_ai_jarmul` |
| Builders club | `builders_club` | `builders_club_` | `builders_club_brad_modal` |
| Demo day | `demo_day` | `demo_day` | `demo_day` |
| Blog post | `blog_post` | `blog_` | `blog_agent_harness_context_engineering` |
| Podcast episode | `podcast` | `vg_ep` | `vg_ep65_agentic_search_jeff_huber` |
| YouTube video | `video` | `vg_` | `vg_lessons_year_building_llms` |

---

## Adding Web Clippings (Blog Posts, Podcast Pages)

1. Use the Obsidian Web Clipper to save the page — it lands in `wiki/Clippings/`
2. Triage: is it worth processing? If not, leave it in Clippings
3. Generate source summary in `wiki/sources/` using the appropriate prefix and `type`
4. Update relevant concept articles — weave in new material, add to Sources sections
5. People pages — link both directions (summary → people, people → summary). Create new people pages if someone appears in 2+ sources
6. Check for new concepts if the content introduces genuinely new cross-cutting ideas
7. Update `_source_registry.md` and `_index.md`
8. QA check — verify summary against original source for fabricated claims, misattributions
9. Run broken link check:
   ```
   python3 -c "import re; from pathlib import Path; wiki=Path('wiki'); all_md=set(f.stem for f in wiki.rglob('*.md')); [print(f'{f.relative_to(wiki)} -> [[{l}]]') for f in wiki.rglob('*.md') for l in re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', f.read_text()) if l not in all_md]"
   ```
10. Commit

---

## Adding YouTube Videos

### Pulling Transcripts

Video IDs are stored in `raw/youtube/video_ids.txt`. To update the list:

```bash
yt-dlp --flat-playlist --print "%(id)s" "https://www.youtube.com/@vanishinggradients/videos" > raw/youtube/video_ids.txt
yt-dlp --flat-playlist --print "%(id)s" "https://www.youtube.com/@vanishinggradients/streams" >> raw/youtube/video_ids.txt
sort -u -o raw/youtube/video_ids.txt raw/youtube/video_ids.txt
```

To pull transcripts:

```bash
uv run python scripts/pull_youtube_transcripts.py raw/youtube/video_ids.txt
```

The script:
- Saves transcripts as timestamped markdown in `raw/youtube/[VIDEO_ID].md`
- Skips videos already downloaded
- Has a 5-second delay between requests to avoid IP blocking
- If blocked, wait and retry later — YouTube blocks typically lift within hours

### Getting Video Titles

```bash
yt-dlp --flat-playlist --print "%(id)s|%(title)s" "https://www.youtube.com/@vanishinggradients/videos"
yt-dlp --flat-playlist --print "%(id)s|%(title)s" "https://www.youtube.com/@vanishinggradients/streams"
```

### Getting Durations

```bash
for f in raw/youtube/*.md; do
  id=$(basename "$f" .md)
  last_ts=$(tail -1 "$f" | grep -oE '\[[0-9:]+\]' | tr -d '[]')
  echo "$id: $last_ts"
done
```

### Processing into Wiki

Same pipeline as web clippings, but:
- Use `type: video` in frontmatter
- Add `podcast: "Vanishing Gradients"` and `source_url: "https://www.youtube.com/watch?v=[ID]"`
- Include `duration` in frontmatter
- Filename prefix: `vg_[descriptive_name]`

Parallelize by batching 7-8 videos per subagent.

---

## Adding Course Transcripts (VTT files)

1. Drop the `.vtt` file in `raw/`
2. Clean: `uv run python scripts/clean_vtt.py`
3. Denoise: `uv run python scripts/denoise.py`
4. Then follow the same pipeline as above (summary, concepts, people, navigation, QA, link check, commit)
5. Use `type: workshop`, `guest_talk`, `builders_club`, or `demo_day` as appropriate
6. Include `duration` from the last timestamp in the VTT

---

## Parallelization

When processing multiple sources, use subagents in parallel — batch 7-8 sources per agent. Don't process sequentially.

---

## QA

After generating summaries, verify them against the original source material:
- Check for fabricated claims (numbers, quotes, examples not in the source)
- Check for misattributions (right fact, wrong person)
- Check for external knowledge injection (true facts not present in the specific source being summarized)
- Fix issues before committing

---

## Related Source Linking

When a blog post is a writeup of a podcast episode (or vice versa), add `related_source:` to both frontmatter files pointing to each other. (To do — not yet implemented.)

---

## Commit Convention

Use `--author="AI legend <ai.legend@smalltech.com>"` for all commits.
