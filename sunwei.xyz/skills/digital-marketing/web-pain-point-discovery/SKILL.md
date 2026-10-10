---
date: 2026-10-02
name: web-pain-point-discovery
title: Web Pain Point Discovery
description: Searches the open web for NEW customer pain points that an existing pain-point summary does not cover, archives every source page, verifies each quote verbatim against the archive, dedupes against all previously used URLs, scores signal strength by distinct sources, and adds a dedicated section for non-English communities (e.g. Chinese forums, V2EX). Use when a first pain-point report already exists and you need a gap-filling supplement, fresh 2025+ evidence, competitor GitHub-issue mining, or when your customers speak a language your evidence does not.
---

# Web Pain Point Discovery

Find what the existing research missed. Everything cited is archived, verified and new.

## When to use

- A pain-point summary exists and you suspect blind spots (new platforms, newer complaints, other languages).
- Customer base and evidence base differ (e.g. customers mostly Chinese-speaking, evidence mostly English).
- Not for the first pass over a corpus (use `pain-point-analysis`).

## Goal

A supplement that lists only (1) new pain clusters, (2) brief new evidence for existing clusters, and (3) community-specific pains for under-covered languages, each with signal strength and sourced, verified quotes.

## Inputs

- The existing summary: its cluster list (what counts as "already covered").
- A known-URL list: every URL the existing research used (collect with `scripts/dedupe_urls.py collect`).
- Confirmed product capabilities (anything else will be marked "to be confirmed").
- Target communities and languages.

## Steps

1. **Define "covered".** List existing clusters and small signals. New clusters must be outside them.
2. **Search sources** in [references/source-playbook.md](references/source-playbook.md): Discourse forums (JSON), competitor GitHub issues, HN Algolia, Reddit via Arctic Shift, V2EX API, local-language forums and blogs. Search with pain words ("limit", "slow", "404", "can't pay", "blocked", local-language equivalents).
3. **Archive every page you might cite** (API text, all replies):
   `python3 scripts/archive_page.py <url> ... --out pages --print 600`
   Then find exact wording: `python3 scripts/grep_archive.py "<regex>" --registry pages/registry.json`.
4. **Record evidence** as JSON entries `{cluster, url, quote, platform, date}`; the quote is copied from the archived text in its original language. Keep corroborating (archived but not quoted) URLs per cluster.
5. **Dedupe** against the known list: `python3 scripts/dedupe_urls.py check --known known_urls.txt new_urls.txt`. New-cluster and community sections must use only NEW URLs; a "new evidence for existing clusters" section may reuse known ones (allow it explicitly).
6. **Score signal strength** = number of distinct sources (quoted URLs + corroborating archived pages). A thread with many replies still counts once.
7. **Write the report from a template** with placeholders (`{{Q:N1}}` quotes, `{{N:N1}}` source count, `{{X:url | url}}` corroborating sources, `{{E:S2:0}}` inline quote), then build and verify in one step:
   `python3 scripts/build_report.py --template report_template.md --evidence evidence.json --registry pages/registry.json --known known_urls.txt --allow-known S2 --out REPORT.md`
   The build fails if any quote is not verbatim, any URL is not archived, or a new-section URL is already known.
8. **Priority impact:** table of P0–P3 with "why" and "what must be confirmed first", and how the findings change the existing top messages.
9. **Coverage appendix:** every source, method and result, including failures (rate limits, anti-bot pages, login walls) and sources not tried.

## Output

`REPORT.md` per [references/report-template.md](references/report-template.md), `pages/` archive + `registry.json`, `evidence.json`, and the template, so the report can be rebuilt and re-verified.

## Checklist

- [ ] Every new cluster is outside the existing summary's clusters
- [ ] All quotes verified verbatim against archived pages (e.g. "92/92")
- [ ] No new-section URL appears in the known list
- [ ] Signal strength = distinct sources, stated per cluster
- [ ] Non-English section states which communities were covered and how representative they are
- [ ] Capabilities outside the confirmed list are marked "to be confirmed"
- [ ] Coverage table lists failures and untried sources honestly

## Guardrails

- Convention: 「…」 (or quotation marks) only for verbatim, verified text; paraphrase and proposed copy in plain text or “…” clearly labelled as yours. Summaries from search snippets are labelled "(summary)".
- Never cite a page you did not archive; never "fix" a quote to read better.
- No usernames in the report. Quote the words, link the thread.
- Be polite to sources: sequential requests, backoff on 429, stop when blocked, and record it.

## References

- [references/report-template.md](references/report-template.md): report skeleton with placeholders.
- [references/source-playbook.md](references/source-playbook.md): endpoints, pain-word queries, local-language communities and their access notes.
- [references/worked-example.md](references/worked-example.md): MDFriday supplement excerpts (new-cluster table, one cluster, Chinese community, priorities).
- `scripts/archive_page.py`, `scripts/grep_archive.py`, `scripts/build_report.py`, `scripts/dedupe_urls.py`, `scripts/verify_quotes.py` (`--help` on each).
