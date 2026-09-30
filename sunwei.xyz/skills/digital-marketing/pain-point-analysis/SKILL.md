---
name: pain-point-analysis
title: Pain Point Analysis
description: Clusters and ranks customer pain points across a VOC corpus (cards, forum threads, YouTube comments) into a sourced report with per-cluster counts, verbatim-verified quotes, audience and competitor views, top marketing messages and product gaps. Use when you have collected customer evidence and need to answer "what hurts most, for whom, and what should we say or build?", when asked to summarize, rank, cluster or prioritize pain points, or before writing positioning, VOC articles or blog posts.
---

# Pain Point Analysis

Turn a pile of customer evidence into a ranked, trustworthy list of pains, each backed by counts and exact quotes, and translate it into messages and product gaps.

## When to use

- After `voc-research` and/or `youtube-research` produced a corpus.
- Before messaging, landing pages, VOC articles or blog posts.
- Not for discovering pains outside the corpus (use `web-pain-point-discovery` afterwards).

## Goal

Answer, with evidence: which pains are biggest and growing, who has them, how competitors fail or succeed on them, what the top messages are, and which product gaps the data points to.

## Inputs

- Corpus paths (VOC cards, comment files, research notes) and an inventory of what each contains.
- Product facts: the list of capabilities that are confirmed (everything else is "to be confirmed").
- Optional: customer list for aggregate-only stats (never quote personal data).

## Steps

1. **Inventory every source.** Table of source, file count and how it will be used (main evidence, cross-check only, excluded). Exclude your own marketing drafts from pain counts; use them only to check product claims.
2. **Draft a tag taxonomy** of ~20 pain tags from a first read. Run the keyword first pass to see volumes and find candidate items:
   `python3 scripts/tag_counts.py --cards cards/ --taxonomy taxonomy.json --since-year 2025 --csv review.csv`
   Keyword counts over-count (in the MDFriday run, "setup" keywords hit 194 cards; hand-tagging confirmed 150). See [references/tagging-guide.md](references/tagging-guide.md).
3. **Hand-tag every item.** Multi-label. Mark items with no concrete pain as background-only and exclude them from all counts. For comments, count only comments that clearly express a pain (curiosity like "what theme is that?" is not pain).
4. **Merge tags into ~15 clusters** and rank by corpus count plus comment count. Add a "since <recent year>" column to show growth and a one-line intensity judgment (e.g. "directly causes abandonment").
5. **Write each cluster:** description in customers' terms, evidence counts, 3–4 representative quotes with file path and URL, related competitors, product opportunity (confirmed capabilities only).
6. **Verify every quote verbatim** before publishing:
   `python3 scripts/verify_quotes.py --quotes quotes.json --base <corpus root>` (JSON list of `{quote, source}`; yt-dlp `.info.json` files are searched per comment). Target: all quotes pass. Fix or drop failures, never "adjust" the source.
7. **Cross-cut views:** by audience (rough keyword counts, magnitude only), by competitor (mention counts, main complaints, what users praise).
8. **Implications:** top 5 marketing messages ranked by evidence strength, and a product-gap table (P0–P3) where every capability claim not on the confirmed list says "to be confirmed". Note data gaps (e.g. customers are mostly one language community but evidence came from another).
9. **Method and caveats section** (see Guardrails) and an appendix with the source inventory and counts.

## Output

A single report, structure in [references/report-template.md](references/report-template.md): overview (sources, method, caveats), ranked cluster table, one section per cluster, audiences, competitors, implications, appendix.

## Checklist

- [ ] Every source listed with how it was used; excluded sources say why
- [ ] Background-only items excluded from counts
- [ ] Ranked table has counts, recent-year column and intensity
- [ ] Every quote verified verbatim (script output recorded, e.g. "55/55 and 45/45")
- [ ] Card quotes that may be paraphrases are labelled as such
- [ ] Product claims limited to confirmed capabilities; the rest marked "to be confirmed"
- [ ] No emails, usernames or other personal data anywhere

## Guardrails

- Counts are hand labels: state the tolerance (the MDFriday report used "treat as ±10%; read magnitude and order, not exact values").
- Keep units straight: per-video tags and per-comment counts are different numbers; say which one each table uses.
- A quote is only a quote if it is copied exactly from the source. Paraphrase in your own voice and mark it as such.
- Aggregate personal data only (e.g. email-domain distribution), never individual records.

## References

- [references/report-template.md](references/report-template.md): report skeleton with section-by-section instructions.
- [references/tagging-guide.md](references/tagging-guide.md): building the taxonomy, keyword first pass versus manual tagging, intensity labels.
- [references/taxonomy.example.json](references/taxonomy.example.json): example keyword taxonomy (publishing-tool market).
- [references/worked-example.md](references/worked-example.md): excerpts from the MDFriday report (ranking table, one cluster, messages, gaps).
- `scripts/tag_counts.py`, `scripts/verify_quotes.py` (`--help` for usage).
