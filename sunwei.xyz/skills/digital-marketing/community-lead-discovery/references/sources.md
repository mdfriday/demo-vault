---
title: Sources and fallbacks
---

# Sources and fallbacks

Parameterize the lists; the reference run used the ones shown.

## Tier 1: Reddit (subs, e.g. ObsidianMD, selfhosted, webdev, SideProject, indiehackers, staticSiteGenerators, productivity, statichosting)

| Method | Endpoint | Notes |
|---|---|---|
| Arctic Shift posts | `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=<sub>&after=<epoch>&before=<epoch>&limit=100` | Primary; per sub; watch for the 100 cap |
| Arctic Shift by id | `.../api/posts/ids?ids=<id,id>` | Re-check carried leads |
| Arctic Shift comments | `.../api/comments/search?link_id=<id>&limit=100` | Comment counts and last activity; can lag |
| Reddit RSS | `https://www.reddit.com/r/<sub>/new/.rss`, thread `https://www.reddit.com/comments/<id>/.rss` | Fallback and freshness check; 429s are common, so retry from a second network |
| Reddit JSON | `/r/<sub>/new.json` | Often 403 from servers; don't rely on it |
| Pullpush | `api.pullpush.io` | Often 429; optional |

## Tier 2

| Source | Endpoint | Notes |
|---|---|---|
| Discourse forum | `/latest.json`, `/search.json?q=<kw>`, `/tag/<tag>.json`, `/t/<id>.json` | Views and posts_count as metrics; search can 429 |
| Hacker News | `https://hn.algolia.com/api/v1/search_by_date?query=<kw>&numericFilters=created_at_i><epoch>`; item `https://hacker-news.firebaseio.com/v0/item/<id>.json` | Filter false positives (e.g. "hugo" matching other products) |
| Dev.to | `https://dev.to/api/articles?tag=<tag>&per_page=30` (+ `&top=7`), `https://dev.to/feed/tag/<tag>` | Tags used: obsidian, markdown, digitalgarden, staticsite, hugo, astro, quartz, docusaurus, mkdocs, notes |
| Medium | `https://medium.com/feed/tag/<tag>` | Article HTML (claps) is often behind Cloudflare, so reuse the last confirmed value and mark it |
| Product Hunt | `https://www.producthunt.com/feed` (Atom) | Launches only; rarely intent posts |

## Practices

- Save every raw response under `raw/<source>/` with a status file (`name:http_status:bytes`).
- Use the owner's machine as a second network when the box is rate-limited, and say so in Coverage.
- Never log in, and never use session cookies or private APIs to get around limits.
