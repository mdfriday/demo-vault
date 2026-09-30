---
title: Tagging guide
---

# Tagging guide

## Build the taxonomy

1. Read a sample (50–100 items) across themes and platforms.
2. Write ~20 tags, each a pain in customer terms ("setup and deploy barrier", "rendering fidelity lost", "price and lock-in"). Avoid feature names.
3. For each tag, write a keyword regex for the first pass (see `taxonomy.example.json`). Include the words people actually use, in every language present.

## Keyword first pass (triage, not counts)

`tag_counts.py` shows rough volumes and produces `review.csv` (item, date, keyword tags, empty `manual_tags`, `background_only`). Use it to:

- spot tags that are too broad (a tag matching almost everything is a bad regex, e.g. matching a metadata key),
- find items that match nothing (possible new tags or background-only),
- order your manual reading.

Real calibration (MDFriday): the keyword "setup-and-deploy" regex matched 194 of 567 cards; after reading them, 150 carried that pain. On YouTube, keyword tagging put "themes/appearance" on 29 of 30 sampled videos, but reading the comments found only 11 comments that expressed a theme pain; most were "What theme is that?" curiosity.

## Manual pass (the numbers you publish)

- Read every item. Assign all tags that apply.
- `background_only` = no concrete pain (philosophy essays, launch posts, showcases). Exclude from every count.
- Comments: count one per comment that clearly expresses the pain. Thanks, questions about the video's theme or general chat do not count.
- Keep per-video (or per-thread) tallies and per-comment tallies in separate columns.

## Clustering and ranking

- Merge tags into ~15 clusters. Keep very small, distinct signals as "other small signals" instead of forcing them in.
- Rank by corpus items plus comment count, then sanity-check the order by reading the top quotes.
- Add a recent-period column (e.g. since 2025) to separate growing pains from old ones.
- Intensity labels (one line, evidence-based): "most frequent, directly causes abandonment" · "growing fast, causes refunds" · "long-standing, main migration motive" · "medium frequency but often called the only blocker" · "low frequency, high willingness to pay".
