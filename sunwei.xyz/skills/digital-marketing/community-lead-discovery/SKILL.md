---
name: community-lead-discovery
title: Community Lead Discovery
description: Runs a recurring (e.g. every 8 hours) scan of communities such as Reddit, Discourse forums, Hacker News, Dev.to, Medium and Product Hunt for high-intent posts where a product genuinely helps. It scores each post 0–100 (URGENT / HIGH / MEDIUM ≥50, weak signals below), carries, cools and drops leads across windows, writes a digest with per-source coverage, and drafts help-first replies with founder disclosure for the human to post. Use when asked for a lead digest, community monitoring, "find people asking for X", social listening for buying intent, or drafting a reply to a community thread.
---

# Community Lead Discovery

Find the few threads where someone is actively asking for what the product does, and help them first. Report honestly when there is nothing.

## When to use

- A standing monitor on a schedule (e.g. 00:00 / 08:00 / 16:00 in the owner's time zone).
- A one-off "who is asking for this right now?" sweep.
- Drafting a reply to a specific thread.
- Not for bulk research (use `voc-research`); lead posts that look like research signal can be handed to it.

## Goal

A digest per window: urgent, HIGH and MEDIUM leads with evidence, new leads ≥50, carry/drop changes, weak signals, competitor notes and a coverage table, plus draft replies the owner can post themselves.

## Inputs

- Product one-liner, confirmed capabilities, and the pains it fits (the "lens").
- Sources: subreddits, forum categories/tags, HN keywords, Dev.to tags, Medium tags, Product Hunt; see [references/sources.md](references/sources.md).
- Previous digest end time and the lead state file (`leads.json`).
- Owner's own post IDs (tracked, never treated as leads).

## Steps

1. **Window.** `python3 scripts/lead_tracker.py window --prev-end <prev-end-UTC> --tz <tz>` gives AFTER/BEFORE epochs and the label. Start from the previous digest end, not "now minus 8h", so nothing falls in a gap.
2. **Fetch per source** with the fallbacks in [references/sources.md](references/sources.md). Record HTTP status and caps per source; a failed source is reported, not silently skipped.
3. **Dedupe:** `python3 scripts/dedupe_urls.py check --known seen.txt new_urls.txt` (reddit, HN, Discourse, YouTube IDs normalized).
4. **Screen with the lens:** drop off-topic, removed or mod-locked posts and keyword false positives. Keep evidence (title, body gist, comment count, last activity).
5. **Score** each survivor 0–100 with [references/lead-scoring-rubric.md](references/lead-scoring-rubric.md). Fields: id, source, title, url, score, comments_prev/now, last_activity, status, brief, intent, pain, competitors, fit, angle.
6. **Update carry/drop:** write this window's observations to `obs.json`, then run `python3 scripts/lead_tracker.py update --state leads.json --obs obs.json --md changes.md`. Review every proposal. Brand already in thread → LISTEN-ONLY; own posts → OWN.
7. **Draft replies** only for URGENT/HIGH leads that are still open and have no brand mention, following [references/reply-guidelines.md](references/reply-guidelines.md).
8. **Write the digest** with [references/digest-template.md](references/digest-template.md) and save the raw responses, candidates JSON and coverage next to it.

## Output

`<digest-dir>/DIGEST.md`, `candidates-*.json`, `coverage.json`, `raw/`, updated `leads.json`.

## Checklist

- [ ] Window starts at the previous digest end; label in the owner's time zone
- [ ] Every listed post has a real URL fetched this run (or marked "NOT CHECKED" with the reason)
- [ ] Scores have a one-line reason; weak signals (<50) listed separately, not in tables
- [ ] Carry/drop decisions state the metric change (e.g. "comments 19 flat, 1st quiet")
- [ ] No reply drafted where the brand already appeared or the thread is locked or stale
- [ ] Coverage lists every source with status (200 / 403 / 429 / blocked) and caps

## Guardrails

- **Never post, vote, DM or sign up on the owner's behalf.** Drafts only.
- **Never invent posts, URLs, counts or quotes.** "Nothing urgent this window" is a valid digest.
- **Help first:** the reply must be useful even if the product line is deleted.
- **Founder disclosure** whenever the product is mentioned; one soft mention at most.
- **Never double-post** in a thread where the brand already appeared; listen only.
- Don't suggest bypassing employer IT or platform rules; skip mod-removed threads.
- Keep usernames out of anything shared beyond the owner.

## References

- [references/lead-scoring-rubric.md](references/lead-scoring-rubric.md): bands, calibration examples, suggested factor weights.
- [references/digest-template.md](references/digest-template.md): digest layout and carry/drop wording.
- [references/sources.md](references/sources.md): endpoints, fallbacks and known failure modes.
- [references/reply-guidelines.md](references/reply-guidelines.md): help-first reply structure with an example.
- `scripts/lead_tracker.py` (`window`, `update`; `--help`), `scripts/dedupe_urls.py` (`--help`).
