---
title: Source playbook for gap-finding
---

# Source playbook for gap-finding

| Source | Endpoint(s) | Good for | Access notes (real runs) |
|---|---|---|---|
| Discourse forums (official product forums, local-language forums) | `/search.json?q=`, `/t/<id>.json` | Feature requests, limits, workarounds, dated replies | Worked reliably, including a Chinese-language Discourse forum (35 topics archived). |
| Competitor GitHub issues | `api.github.com/search/issues?q=repo:<o>/<r>+<terms>`, `/repos/<o>/<r>/issues/<n>` (+ `/comments`) | Concrete failures with numbers (build time, OOM, file counts) | Anonymous API rate-limits quickly; batch small and retry later. |
| Hacker News | `hn.algolia.com/api/v1/search?query=&tags=comment&numericFilters=created_at_i>TS` | Developer opinions, "Show HN" competitors | Few new items once a corpus exists; many already known. |
| Reddit | Arctic Shift `/api/posts/search`, `/api/comments/search` | Fresh complaints | Full-text and title search frequently timed out (4+ minutes); reddit.com JSON returned 403. Do not depend on it. |
| V2EX | `/api/topics/show.json?id=`, `/api/replies/show.json?topic_id=` | Chinese developer community: hosting, blocking, payments | Official API worked. |
| Juejin | search API | Chinese tutorials | Article pages returned an anti-bot page; only search-API summaries were usable, cited as "(summary)". |
| Sspai | site search / web | Chinese power users | Search API returned empty; one tutorial found via web search, no quotable pain. |
| Zhihu | search page | Chinese Q&A | Login wall; no data. |
| Xiaohongshu, Bilibili | — | Non-technical Chinese users | Not attempted in the reference run; a known gap. |
| Personal blogs | direct fetch | Long migration stories | Record the post date from the page. |

## Pain-word query ideas

- Limits: "storage limit", "size limit", "exceed 4gb", "too slow", "build time", "out of memory".
- Trust: "shut down", "discontinued", "is it dead", "export my data", "status page".
- Payments: "PayPal", "WeChat Pay", "Alipay", "renewal", "credit card".
- Compliance: "GDPR", "cookie banner", "analytics without Google", "robots.txt", "llms.txt".
- Links: "404 after rename", "redirect", "permalink", "slug".
- Language-specific: file names and titles in the local script, local hosting/blocking terms (for Chinese: 被墙 "blocked by the firewall", 访问慢 "slow access", 备案 "ICP filing", 图床 "image host", 公众号 "WeChat Official Account").

## Archive discipline

- Archive the full thread text (all replies) at the time you read it; quotes are checked against this copy, not the live page.
- One registry for the whole run; keep file names stable (hash of URL).
- If a source blocks you, write that down in the coverage table instead of substituting another page.
