---
title: Digital Marketing Skills
date: 2026-09-28
weight: 2
tags:
  - budding
description: Nine reusable agent skills for research-first marketing, covering customer research, pain-point analysis, YouTube research, headlines, blog posts and community leads.
---

# Digital Marketing Skills

← [[skills/index|Skills]]

These are reusable skills distilled from real marketing work: researching what people struggle with, turning that into ranked pain points, and writing content and replies that only claim what is true. Each skill is a folder with a `SKILL.md` (in the Agent Skills format, so an AI agent can load and run it), plus `references/` for templates and worked examples and `scripts/` for deterministic checks.

The method comes from [[knowledge/Digital Marketing/index|Digital Marketing knowledge]]: do the research first, write in the customer's words, and make every claim checkable. The worked examples come from MDFriday.

## How the skills chain

**1. Research: collect what people actually say**
- **VOC Research** and **YouTube Research** gather community posts and video comments into a corpus.
- **Community Lead Discovery** runs continuously. It finds people asking right now, and its research-grade finds feed VOC Research.

**2. Analysis: find and rank the pains**
- **Pain-Point Analysis** clusters and ranks the corpus, with counts and verified quotes.
- **Web Pain-Point Discovery** then looks for pains the analysis missed, including non-English communities.

**3. Content: say it back honestly**
- **VOC to Theme Articles** publishes the research, one page per pain.
- **Headline Swipe File** turns proven titles and search language into keyword-first titles.
- **VOC to Blog Post** writes SEO posts from the pains, the quotes and the titles.
- **Course to Knowledge Articles** is where the copywriting rules (AIDA, headlines, benefits, CTA, risk reversal) came from. Use it to turn any course into usable notes.

Research → Analysis → Content. Each step's output is the next step's input, and quotes are verified at every hop.

## Skills

| Skill | Stage | Purpose |
| --- | --- | --- |
| [[skills/digital-marketing/voc-research/SKILL\|VOC Research]] | Research | Collect community posts into themed, URL-deduplicated evidence cards |
| [[skills/digital-marketing/youtube-research/SKILL\|YouTube Research]] | Research | Top videos for a topic, their comments, pain tags and title patterns |
| [[skills/digital-marketing/community-lead-discovery/SKILL\|Community Lead Discovery]] | Research (ongoing) | Score high-intent posts every 8h, carry or drop leads, draft help-first replies |
| [[skills/digital-marketing/pain-point-analysis/SKILL\|Pain-Point Analysis]] | Analysis | Cluster and rank pains with counts, verified quotes and a product response |
| [[skills/digital-marketing/web-pain-point-discovery/SKILL\|Web Pain-Point Discovery]] | Analysis | Find new pains beyond an existing summary, archived and quote-verified |
| [[skills/digital-marketing/voc-to-theme-articles/SKILL\|VOC to Theme Articles]] | Content | Publish one research article per theme, with unconfirmed items marked |
| [[skills/digital-marketing/headline-swipe-file/SKILL\|Headline Swipe File]] | Content | Evidence-ranked title patterns and keyword-first, 50–60 character titles |
| [[skills/digital-marketing/voc-to-blog-post/SKILL\|VOC to Blog Post]] | Content | AIDA blog posts with real quotes, fair comparisons and confirmed claims only |
| [[skills/digital-marketing/course-to-knowledge-articles/SKILL\|Course to Knowledge Articles]] | Foundation | Turn a course into mastery articles: use it, verify it, improve it |

## Rules every skill shares

- **Verbatim or nothing.** A quote must appear word for word in its saved source (`verify_quotes.py`). A quote that fails is removed, never "fixed".
- **Confirmed claims only.** Product capabilities come from a confirmed list. Anything else is left out of marketing and marked "(unconfirmed)" in research.
- **No personal data.** No usernames or emails in anything published; customer data only as aggregates.
- **Never post for the owner.** Replies and posts are drafts; a human publishes them.
- **Honest numbers.** Counts are approximate and say what they count; views carry a snapshot date.

## Notes

- Some scripts appear in several skills (`verify_quotes.py`, `dedupe_urls.py`, `lint_article.py`, `title_check.py`, `title_patterns.py`) so that each skill folder is self-contained. The copies are identical, so update them together.
- Every script prints its usage with `--help` and uses only the Python 3 standard library. The exception is `yt_collect.py`, which calls `yt-dlp`.
- Worked examples reference MDFriday research from September 2026. Plans and features change, so re-confirm them before reuse.

Related: [[mdfriday/voice-of-custom/index|Voice of the Customer]] · [[mdfriday/blog/index|MDFriday Blog]] · [[skills/user-interview|User Interview]]
