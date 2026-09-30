---
title: Claim guardrails
---

# Claim guardrails

Public content may only state product facts the owner has confirmed. Keep the list next to the drafts and check every product sentence against it.

## Confirmed-claims list format

```markdown
| Claim | Status | Source / date confirmed | Allowed wording |
|---|---|---|---|
| Right-click a note or folder to publish | confirmed | owner, YYYY-MM-DD | "Right-click a note or folder, and publish." |
| Build runs locally; only chosen notes upload | confirmed | owner | … |
| Supports <plugin X> rendering | unconfirmed | — | do not claim; say "test those pages first" |
```

MDFriday example (confirmed at the time of the reference run): right-click publish of a note or folder; local build; Cloudflare CDN hosting; AS mode (pages look like the Obsidian notes); multiple switchable themes; selective publish; plans: Guest (no account, 1 site, 5 MB, cleared at the next UTC midnight), Free (3 sites, 50 MB, cleared on the 1st of each month), Personal (about \$5–6/month, 1 GB, permanent). Re-confirm before reuse; plans change.

## Rules

1. **Unconfirmed = absent** in blog posts. In research articles, mark unconfirmed items "(unconfirmed)" instead.
2. **Conflicts are stated, not hidden.** If users ask for "links that never expire" and a tier clears content, say so next to the pitch.
3. **Temporary tiers are called temporary** wherever "free" appears.
4. **Competitor facts** (prices, features) are dated, stated as "roughly" if they vary, and verified from their public pages at writing time.
5. **No invented numbers:** user counts, conversion rates, benchmarks, testimonials.
6. **Quotes are verbatim** and pass `verify_quotes.py`; attribution is platform + year (+ link), never a username.

## Red-flag phrases to grep before publishing

"supports all", "every plugin", "fully compatible", "forever free", "unlimited", "never expires", "guaranteed", "#1", "best", "thousands of users", "trusted by", "secure" (without specifics), "instant".
