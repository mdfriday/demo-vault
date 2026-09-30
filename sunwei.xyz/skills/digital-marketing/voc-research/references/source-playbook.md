---
title: 'Source playbook (public, read-only)'
---

# Source playbook (public, read-only)

Prefer official JSON APIs and feeds over scraping HTML. Log every source's status (OK, 403, 429, timeout, empty) so coverage is honest.

| Source | How to search | Notes from real runs |
|---|---|---|
| Discourse forums (e.g. forum.obsidian.md) | `GET /search.json?q=<terms>&page=N`, `GET /latest.json`, `GET /tag/<tag>.json`, full topic `GET /t/<id>.json` | Reliable. Topic JSON gives every post with dates. Occasional 429 on search. |
| Reddit (by subreddit) | Arctic Shift: `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>&title=<terms>&after=<date>&limit=100`; comments: `/api/comments/search?link_id=<id>`; by id: `/api/posts/ids?ids=<id,...>` | Best archive for Reddit, but keyword search times out or returns 429 under load; retry later. Reddit's own JSON often returns 403. |
| Reddit (fresh) | RSS: `https://www.reddit.com/r/<sub>/new/.rss`, thread: `/r/<sub>/comments/<id>/.rss` | Works from some networks and gets 429 from others; try a second machine before giving up. |
| Hacker News | Algolia: `https://hn.algolia.com/api/v1/search?query=<terms>&tags=story` (or `tags=comment`, `numericFilters=created_at_i>TS`); item: `/api/v1/items/<id>`; Firebase `https://hacker-news.firebaseio.com/v0/item/<id>.json` | Filter false positives by hand (a "hugo" search returns Victor Hugo). |
| Dev.to | `https://dev.to/api/articles?tag=<tag>&per_page=30` (add `&top=7` for top) | Clean JSON; many posts are tutorials, which are still evidence of the setup the author had to do. |
| Medium | Tag RSS `https://medium.com/feed/tag/<tag>`, author RSS `https://medium.com/feed/@<name>` | HTML pages are often behind Cloudflare; use RSS. |
| GitHub issues (competitors) | `https://api.github.com/search/issues?q=repo:<owner>/<repo>+<terms>`; issue + comments via REST | Great for concrete failure reports and feature requests. |
| Personal blogs | Web search with customer phrases ("how I published my ... for free") | Record the post date from the page, not today's date. |
| YouTube | See the `youtube-research` skill. | Comments are a separate corpus; keep them apart from cards. |

## Query patterns

Search in customer language, not product language. Combine:

- the job: "publish notes", "share one note", "turn vault into website"
- the tools people compare: official option, popular free options, "alternative"
- friction words: "without git", "too complicated", "broken after publishing", "free", "self-host"

Worked example (MDFriday, the YouTube query set that also worked for forums): share obsidian notes · publish obsidian notes · obsidian publish alternative · free alternative to obsidian publish · obsidian digital garden · obsidian quartz · obsidian website · obsidian blog · obsidian github pages · obsidian netlify · obsidian hugo publish · obsidian wiki publish · obsidian knowledge base website.

## Batch discipline

- One batch file per source and window, e.g. `batch-forum-2026w38.json`, `batch-reddit-older.json`.
- Dedupe every batch against all earlier cards and the exclusion list before writing.
- Keep a short coverage note per batch: sources tried, status, items found, items written, duplicates skipped.
