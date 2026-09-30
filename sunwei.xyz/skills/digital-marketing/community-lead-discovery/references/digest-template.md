---
title: Digest template
---

# Digest template

```markdown
# <Product> 8h Lead Digest — YYYY-MM-DD HH:00 <TZ>

Window: <AFTER ISO> → <BEFORE ISO> (previous run <label>) + CARRY/DROP review. No invented posts/URLs. **URGENT: <n or none>. HIGH: <n>. NEW ≥50 this window: <n>.** <One line on the most important change.>

## URGENT
### 1. <Source> — <short title> ~<score> (<NEW / CARRY / REVIVE>)
- **Source:** <url> · <posted UTC>
- **Summary:** what they asked; comments prev→now (Δ); last activity; what the replies say.
- **Intent:** what they want to do.
- **Pain:** why current tools fail them.
- **Match %:** ~NN% (which confirmed capabilities fit; why not higher)
- **Suggested Response:** draft reply or "listen only" with reason (see reply-guidelines).
- **Opportunity:** open / half-open / closed, and why.
- **Status:** CARRY 90→88 (Δ comments +1).

## HIGH
<same block, or **None.**>

## MEDIUM
| Source | Summary | Score |
|---|---|---|
| <Source id> **CARRY** | gist; "comments 19 flat (Δ0), 1st quiet"; action | ~54 |

## NEW this window (≥50)
- <Source>: <title> ~NN, or **none**.

## DROP / cooling
- <id> <topic>: soft-DROP cancelled (activity resumed) → rescored ~40 → archive-listen only.
- <id>: brand already in thread → stay DROP / archive; do not engage.

## Noise / weak signals (not in tables)
- <id> <topic> ~34 (reason)
- Own post <id>: comments 21 flat (not a lead)

## Competitors / trends / insights (evidence only)
- <observation with the thread IDs that show it>

## Coverage
<Source>: status (200 / 403 / 429 / Cloudflare-blocked), caps, fallbacks used. E.g. "Box Reddit RSS 6/8 OK (2 × 429) · Arctic OK (cap 100) · Pullpush 429 · Reddit JSON 403 · Forum/HN/Dev.to/Medium RSS/PH OK".

Saved: <digest-dir>/
```

Wording rules: state the metric that drove each status change; say "flat" not "no news"; use "NOT CHECKED (reason)" when a thread could not be re-fetched instead of carrying stale numbers as new.
