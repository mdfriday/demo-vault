---
name: youtube-research
title: YouTube Research
description: Researches a topic on YouTube by searching many customer-language queries, keeping the most-viewed relevant videos, collecting metadata and top comments with yt-dlp, tagging comment pains, and extracting title patterns, promises and video structures into a content-strategy report. Use when planning video or blog topics, checking what content already wins in a niche, mining YouTube comments for pain points and verbatim quotes, or when asked to analyze or learn from top YouTube videos.
---

# YouTube Research

Find the top videos for a topic, learn what they promise and how they are built, and read their comment sections as a pain-point corpus.

## When to use

- Planning a content calendar or a first batch of videos/posts.
- Collecting a second evidence corpus (comments) next to forum/Reddit VOC cards.
- Building a headline swipe file from titles with real view counts.

## Goal

Know (1) which content layers get views versus which convert, (2) which pains appear in comments and in what words, and (3) which topics and structures to make next, ranked by demand × product fit × competitive openness.

## Inputs

- Topic and product; 10–20 search queries in customer language (see the query set in [references/worked-example.md](references/worked-example.md)).
- Relevance rules: what counts as on-topic, known polluting results to exclude.
- Product facts (confirmed capabilities) to map pains to.
- `yt-dlp` installed (`pip install yt-dlp`).

## Steps

1. **Search broadly.** ~30 results per query, merged and deduped by video id:
   `python3 scripts/yt_collect.py search --queries queries.txt --per-query 30 --out search.tsv`
2. **Filter and pick.** Drop off-topic results by regex, sort by views, keep the top ~50:
   `python3 scripts/yt_collect.py pick search.tsv --exclude "<noise regex>" --top 50 --out ids.txt`
   Review the list by eye: keep philosophy/lifestyle videos (traffic layer) and tutorials (conversion layer); drop pollution.
3. **Fetch metadata and comments** (no video download):
   `python3 scripts/yt_collect.py fetch ids.txt --out comments --max-comments 100`
   Sample comments from the ~30 most relevant videos if time is short; note which were sampled.
4. **Build rows:** `python3 scripts/yt_collect.py rows comments --out rows.json` (views, date, channel size, comment count, chapters).
5. **Tag pains.** First pass with keywords, then read every comment:
   `python3 scripts/yt_collect.py tag comments --taxonomy taxonomy.json --jsonl comments.jsonl`
   Report per-video tags and per-comment counts separately.
6. **Describe each video:** one-line promise and its structure (from chapters, or watch the opening). Group into layers (traffic vs conversion).
7. **Title patterns:** `python3 scripts/title_patterns.py rows.json --pattern "<topic>=<regex>"` for pattern counts, total and median views. Feed these into `headline-swipe-file`.
8. **Pick quotes and verify** them against the info.json files:
   `python3 scripts/verify_quotes.py --quotes yt_quotes.json` (sources are `.info.json` paths; matched per comment).
9. **Recommend.** Topic directions in tiers (P0 conversion now, P1 build the category, P2 brand vision), each with "why" and the high-view structure to model; reusable structure templates with a product-specific rewrite; an execution cadence; method and limitations.

## Output

Report per [references/report-template.md](references/report-template.md), plus raw data kept for audit: `search.tsv`, `ids.txt`, `comments/*.info.json`, `rows.json`, `comments.jsonl`. Add a `.gitignore` for bulky raw files if the folder is versioned.

## Checklist

- [ ] Query list, filters and research date written in the method section
- [ ] Views and subscriber counts labelled as a snapshot on that date
- [ ] Traffic layer and conversion layer distinguished
- [ ] Pain table says whether numbers are per video or per comment
- [ ] Every quoted comment verified verbatim and linked to its video
- [ ] Each recommended topic says why (evidence) and which structure to model
- [ ] Limitations stated (comment sampling, keyword tags are directional)

## Guardrails

- Do not present keyword tags as precise statistics; say "for direction, not exact counts".
- Quote comments exactly; no usernames. Link the video, not the commenter.
- Map pains to confirmed capabilities only; anything else is "to be confirmed".
- Respect platform terms: metadata and public comments only, no downloading of videos.

## References

- [references/report-template.md](references/report-template.md): report skeleton and table columns.
- [references/worked-example.md](references/worked-example.md): MDFriday Top 50 study (layers, pain table, P0 topics, structure templates, query set).
- `scripts/yt_collect.py` (search, pick, fetch, rows, tag; `--dry-run` prints yt-dlp commands), `scripts/title_patterns.py`, `scripts/verify_quotes.py`.
