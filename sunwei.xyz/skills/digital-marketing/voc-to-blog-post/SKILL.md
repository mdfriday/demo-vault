---
name: voc-to-blog-post
title: VOC to Blog Post
description: Writes SEO blog posts driven by real customer demand, using voice-of-customer research. It produces keyword-first titles, 140–160 character meta descriptions, AIDA structure opened with verbatim, verified customer quotes, honest competitor comparisons, features turned into benefits, a small no-risk call to action with truthful plan limits, and a confirmed-claims-only guardrail, then lints and verifies every quote. Use when turning pain-point research into blog content, writing "alternatives", "vs", "how to without X" or "is X worth it" posts, building a product blog index, or reviewing a draft for fabricated claims.
---

# VOC to Blog Post

Write posts that help the reader whichever tool they pick and mention the product honestly, so the post earns trust and search traffic.

## When to use

- You have verified customer quotes and ranked pains (from `pain-point-analysis`, `voc-to-theme-articles` or `web-pain-point-discovery`).
- You have a target keyword per post (from `headline-swipe-file`).
- Not for internal research reports or community replies (use `community-lead-discovery`).

## Goal

A set of posts plus an index, where every quote is verbatim and sourced, every product claim is confirmed, and every title and description fits search limits.

## Inputs

- Product name and a **confirmed capabilities list** (features and plan limits the owner has confirmed). See [references/claim-guardrails.md](references/claim-guardrails.md).
- Research corpus with verbatim quotes and source URLs (the quote corpus).
- Title log with a keyword and the chosen title per post.
- Target folder, frontmatter keys, wikilink style, whether the site renders LaTeX (then escape `$` as `\$`).
- Founder story facts (optional; only real ones).

## Steps

1. **Map posts to pains.** One post per reader job (e.g. "publish without Git", "choose a tool", "keep private notes private"). Each post targets one keyword and one or two research themes.
2. **Draft with the template** in [references/blog-template.md](references/blog-template.md):
   - **Attention:** title (keyword first, 50–60 chars) and a description of 140–160 chars. Open in second person with the reader's situation.
   - **Interest:** 2–5 verbatim quotes as blockquotes, `> “quote” — [Platform, year](url)`. Explain honestly why the problem exists.
   - **Desire:** an honest options comparison ("describe every option the way its happiest users would"; the official or paid option is the benchmark, with its real trade-offs), the founder story, then features → benefits bullets ("**Feature.** So you …"), then a "What it doesn't remove" limits paragraph.
   - **Action:** a small, specific test (about 5 minutes, exact steps) plus the true plan facts and risk reversal ("if it isn't for you, you've lost ten minutes").
   - **Further reading:** path-qualified wikilinks to sibling posts and the research pages.
3. **Apply the copywriting checklist:** [references/copywriting-checklist.md](references/copywriting-checklist.md).
4. **Claim pass.** Every product sentence maps to the confirmed list; anything else is removed or phrased as a limit ("I'm not going to claim support for every community plugin; test those pages first").
5. **Verify quotes:** `python3 scripts/verify_quotes.py --markdown posts/*.md --corpus <research-dir>`. Any MISS gets fixed or the quote is deleted, never "adjusted".
6. **Lint:** `python3 scripts/lint_article.py posts/*.md --vault <vault> --vault-prefix <blog-folder> --title-range 50,60 --desc-range 140,160 --min-quotes 2 --max-quotes 6 --math`.
7. **Check titles:** `python3 scripts/title_check.py --keyword "<kw>" "<title>"`.
8. **Write the index,** grouped by reader job, with a one-line promise per post, a short "Try" section with the true plan facts, and a link to the research.

## Output

`<blog-folder>/<kebab-slug>.md` per post plus `index.md`; frontmatter `title`, `date`, `tags`, `description`.

## Checklist

- [ ] Title keyword-first, 50–60 chars; description 140–160 chars
- [ ] 2–5 quotes per post, all verified verbatim with a source link and year
- [ ] Competitors described fairly, including where they are better
- [ ] Every product claim is on the confirmed list; temporary tiers are called temporary
- [ ] One clear CTA with a low-risk first step; no fake urgency or scarcity
- [ ] Lint passes: wikilinks resolve, `$` escaped, no @handles or usernames, no unsupported blocks

## Guardrails

- Never invent quotes, statistics, testimonials, user counts or URLs.
- No usernames in attributions: platform and year only.
- Don't disparage competitors; the comparison must be something their fans would accept.
- Urgency only if it is real (e.g. a real price change date). Otherwise, reduce risk instead.
- Publishing is the owner's call: deliver files, don't post to external platforms.

## References

- [references/blog-template.md](references/blog-template.md): post and index skeletons.
- [references/copywriting-checklist.md](references/copywriting-checklist.md): AIDA, headline, benefits, CTA, urgency, risk reversal and customer-language checks.
- [references/claim-guardrails.md](references/claim-guardrails.md): the confirmed-claims list format and red-flag phrases.
- [references/worked-example.md](references/worked-example.md): excerpt from "Publish Obsidian Notes Without GitHub".
- `scripts/verify_quotes.py`, `scripts/lint_article.py`, `scripts/title_check.py` (`--help` on each).
