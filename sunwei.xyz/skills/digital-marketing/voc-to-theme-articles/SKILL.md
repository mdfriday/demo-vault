---
name: voc-to-theme-articles
title: VOC to Theme Articles
description: Turns voice-of-customer research (clustered pain points, YouTube comments, web supplements) into a public set of per-theme articles plus a ranked index. Each article has signal counts, 4–8 verbatim verified quotes without usernames, why it hurts, how people cope today, the product's response with unconfirmed items marked "(unconfirmed)", and open questions. Use when publishing user research to a digital garden or wiki, when asked to "write up the pain points as articles", "make a voice-of-customer section", or when merging several research reports into one theme list.
---

# VOC to Theme Articles

Publish research as one readable page per customer problem, with evidence first and honest product positioning.

## When to use

- After `pain-point-analysis` and/or `web-pain-point-discovery` produced ranked clusters with verified quotes.
- You want a public or team-facing research section that others can link to.
- Not for SEO marketing posts (use `voc-to-blog-post`).

## Goal

A merged, de-duplicated theme list; one article per theme; an index that explains sources, method and ranking. Every quote renders only if it verifies.

## Inputs

- Research reports with clusters, counts and quote sources (URLs, card paths, archived pages, `.info.json`).
- Confirmed capabilities list for the product (see [references/claim-guardrails.md](references/claim-guardrails.md)).
- Target folder, language (quotes stay in the original language), frontmatter keys.

## Steps

1. **Merge themes.** Combine clusters from all reports; merge overlaps (keep the larger count and note the added sources); keep separate tiers for main clusters, new web clusters and language-community themes. Record the merge mapping.
2. **Build a quote bank** (`quotes.json`): `id → {quote, source, url, platform, date}`. Take quotes only from the reports' verified evidence; choose 4–8 per theme covering different sources and years. No usernames.
3. **Draft each article** from [references/theme-article-template.md](references/theme-article-template.md) with `{{Q:id}}` placeholder lines in Voices. Sections: What users are saying (+ Signal callout with approximate counts and rank) → Voices → Why it hurts → How people cope today → Product's response → Open questions → Related.
4. **Product's response.** State confirmed capabilities plainly; mark everything else "(unconfirmed)". Call out conflicts honestly, e.g. a tier that clears content vs. users who say expiring links are unacceptable.
5. **Render quotes:** `python3 scripts/render_quotes.py --src drafts --out articles --quotes quotes.json --registry <pages>/registry.json --base <research-root>`. The run fails without writing if any quote doesn't verify or a placeholder is unknown; it also reports duplicate and unused quotes.
6. **Write the index** from [references/index-template.md](references/index-template.md): hook, research table (sources, scale, notes), method, how to read, the "(unconfirmed)" warning listing confirmed capabilities, and tiered ranked tables. Escape `|` inside table wikilinks as `\|`.
7. **Postcheck:** `python3 scripts/lint_article.py articles/*.md --vault <vault> --vault-prefix <folder> --min-quotes 4 --max-quotes 8 --math` (key order, wikilinks, quote count, `$`, @handles, unsupported blocks). Optionally cross-check with `scripts/verify_quotes.py --markdown articles/*.md --corpus <research-root>`.

## Output

`<folder>/index.md` plus one kebab-case article per theme.

## Checklist

- [ ] Every report cluster is mapped to a theme (merge mapping recorded)
- [ ] 4–8 verified quotes per article, original language, no usernames or emails
- [ ] Signal counts are labelled approximate, with the counting unit stated
- [ ] Every product capability is confirmed or marked "(unconfirmed)"
- [ ] Conflicts between user needs and current product rules are stated
- [ ] Lint passes; index lists all themes with resolving links

## Guardrails

- Privacy: no usernames, emails or customer names. Customer data appears only as aggregates (e.g. "~63% Chinese email domains"), never as lists.
- Counts come from the reports; don't re-estimate or round up for drama.
- Don't turn research pages into sales pages: one "response" section, factual.

## References

- [references/theme-article-template.md](references/theme-article-template.md): article skeleton.
- [references/index-template.md](references/index-template.md): index skeleton with research table and tiers.
- [references/claim-guardrails.md](references/claim-guardrails.md): confirmed-claims list and "(unconfirmed)" rules.
- [references/worked-example.md](references/worked-example.md): excerpt of the "Single-note Sharing" article and run stats.
- `scripts/render_quotes.py`, `scripts/lint_article.py`, `scripts/verify_quotes.py` (`--help` on each).
