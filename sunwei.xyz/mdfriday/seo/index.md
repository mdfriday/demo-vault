---
title: MDFriday SEO strategy
tags:
  - seo
  - mdfriday
---

# MDFriday SEO strategy

← [[mdfriday/index|MDFriday]] · [[voc-db/README|VOC database]] · [[voice-of-custom/index|Voice of the Customer]]

How MDFriday plans to be found, from October 2026 to September 2027. This is a public summary: the pages we plan to write, why, and how we'll know whether they work. Every SEO page below has its own short note in `briefs/`, and every user voice in the [[voc-db/README|VOC database]] can point to the page it supports through its `seo_brief` field. Research, pages and results reference each other.

## Goal

Someone who has an Obsidian or Markdown folder and wants it to be a website should meet MDFriday the first time they look — in Google, in AI search, on Reddit, on YouTube — publish their first site quickly, trust it, and be willing to pay for their own domain.

- **North star:** new sites successfully published for the first time, per week.
- **Money metric:** paying Personal users / monthly recurring revenue.

## Positioning, in three steps

| Stage | One-liner | Homepage targets |
|---|---|---|
| 1. Obsidian publishing (Q1–Q2) | *Right-click a folder in Obsidian. See your website. No account, no Git.* | obsidian to website |
| 2. Markdown publishing (Q3) | *Turn any Markdown folder into a website — from Obsidian or your browser.* | markdown to website |
| 3. Knowledge as an asset (Q4) | *Publish what you know. Grow readers. Get paid.* | markdown publishing platform |

Each step builds on the last; the Obsidian pages stay. Stages 2 and 3 only start once the product features they describe are live.

## Four quarters

| Quarter | Focus | Main pages |
|---|---|---|
| Q1 · Oct–Dec 2026 | Trust foundations + high-intent Obsidian pages | Publishing guides, digital garden, single-note sharing, Obsidian Publish and Quartz comparisons, showcase |
| Q2 · Jan–Mar 2027 | Go deeper on Obsidian publishing, migration, launch moments | Flowershow and Digital Garden comparisons, migration guide, wiki / knowledge base, themes, Chinese pages |
| Q3 · Apr–Jun 2027 | Expand to Markdown (depends on Studio) | Markdown website, docs, blog, Hugo alternative, Mermaid / LaTeX |
| Q4 · Jul–Sep 2027 | Knowledge as an asset | Newsletter, monetizing notes, user stories, an original research report |

**Not our fight (we may write helpful content, but don't target it):** team docs with SSO, paragraph-level hiding, pure developer static-site tinkering, throwaway single-note sharing tools.

## Keyword clusters

- **Publish Obsidian:** publish obsidian notes · publish obsidian without github · publish obsidian folder · share obsidian note · update / fix published notes
- **Digital garden:** obsidian digital garden · digital garden without github · what is a digital garden
- **Compare:** obsidian publish alternative · quartz alternative · flowershow alternative · digital garden plugin alternative · quartz vs obsidian publish
- **Cost and setup:** obsidian publish free · custom domain · hosting · self-hosted · obsidian to html
- **Markdown (from Q3):** markdown website · markdown wiki / docs / blog · hugo alternative

One page = one main keyword. New domains have little authority, so we start with long-tail questions and link them up to parent pages.

## Page types

| Type | What it is | Length |
|---|---|---|
| Guide | Answers one search question end to end, with steps | 1,800+ words |
| Compare | Helps a reader decide between tools; every number has a source and a "last verified" date | 900–1,400 words |
| Solution | A use case (digital garden, wiki, sharing) | 600–1,000 words |
| Product / Homepage / Pricing | Conversion pages | — |
| Trust | Security, changelog, migration | — |
| Story | Real sites, including our own (always labelled as ours) | — |

## How we write a page

Every guide follows the same skeleton: answer first → how to choose (comparison table with a check date) → steps with MDFriday → boundaries and limits → common failures → FAQ → related guides.

- **Answer first.** The H1 is the search question; the first 50–150 words answer it.
- **Write the limits.** Every guide says what MDFriday can't do. Anything not verified in production is labelled as such.
- **Reproducible steps.** One action per step, with the expected result and a screenshot.
- **Fair to competitors.** We name other tools, don't disparage them, and recommend them where they fit better.
- **Real voices.** Each page uses at least one verbatim quote from the [[voc-db/README|VOC database]].

## Fact guardrails

- Only write capabilities that are confirmed in the product. Unconfirmed items are written as "planned" or "not possible today".
- No "the only", no "cheapest" — show the scenario prices and let readers compare.
- No promised timings ("in 60 seconds") until we have measured them.
- Every competitor price has a source link and a check date; numbers older than 31 days aren't used on new pages.
- "Free" always comes with its limits (Guest: 5 MB, cleared at the next 00:00 UTC unless claimed; Free: 200 MB).
- We don't use download counts or user counts as selling points.

## Metrics and the minimum loop

The SEO loop counts as working only when all four have happened once:

1. A page is live in production.
2. Google Search Console shows it indexed and getting impressions.
3. Install clicks from that page are recorded.
4. The page has gone through one 8-week review (index status, impressions, average position, install click rate).

M01 (October 2026) covers step 1 only, so the full loop can first complete around M03. Until then we only ship new pages, add evidence (screenshots, short videos), and build outside signals (Reddit replies, videos). We don't change titles or keywords of live pages without data.

Rhythm: weekly report → monthly review → quarterly gate → annual review. After each milestone we write down what we learned and update the playbooks.

## Playbooks

- **Writing a guide:** the skeleton above, 1,800+ words of practical detail, 5–7 FAQs, six internal links (product, two solutions, a guide, a comparison, a call to action).
- **Fact checking:** a claim goes on a page only if it's confirmed by the source code, by the founder, or by the help center.
- **Shipping a page:** draft → checklist → pre-release review → production → submit to Search Console → reply-link it in community answers.
- **Comparison pages:** facts only, sources and dates on every number, say when the other tool is the better choice.

## Roadmap

| Month | Highlights |
|---|---|
| M01 · Oct 2026 | Consistent facts across the site, measurement set up, first four guides, single-note sharing, security and migration pages |
| M02 · Nov 2026 | Obsidian Publish alternative, product page, homepage, pricing, custom domain, "is Obsidian Publish free" |
| M03 · Dec 2026 | Quartz and Digital Garden comparisons, migration guide, showcase, digital garden without GitHub |
| M04–M06 · Jan–Mar 2027 | Update / broken-after-publishing guides, Flowershow, themes, wiki and knowledge base, hosting, multilingual, Product Hunt |
| M07–M09 · Apr–Jun 2027 | Markdown pages (with Studio) |
| M10–M12 · Jul–Sep 2027 | Newsletter, monetization, user stories, research report, year-one review |

## Page list

Status: `in-progress` = being written for the current month; `planned` = scheduled; `live` = published.

| Brief                                                     | Page                                                            | Type             | Target keyword                         | Month   | Status      |
| --------------------------------------------------------- | --------------------------------------------------------------- | ---------------- | -------------------------------------- | ------- | ----------- |
| [[B00-guides-and-compare-hubs\|B00]]                      | Guides and Compare hub pages                                    | Hub              | (none — navigation page)               | M01     | in-progress |
| [[B01-publish-obsidian-notes\|B01]]                       | How to Publish Obsidian Notes                                   | Guide (pillar)   | publish obsidian notes                 | M01     | in-progress |
| [[B02-publish-obsidian-without-github\|B02]]              | Publish Obsidian Without GitHub                                 | Guide            | publish obsidian without github        | M01     | in-progress |
| [[B03-publish-obsidian-folder\|B03]]                      | Publish an Obsidian Folder as a Website                         | Guide            | publish obsidian folder                | M01     | in-progress |
| [[B04-obsidian-digital-garden\|B04]]                      | Obsidian Digital Garden (solution page)                         | Solution         | obsidian digital garden                | M01     | in-progress |
| [[B05-share-obsidian-notes-solution\|B05]]                | Share Obsidian Notes (solution page)                            | Solution         | share obsidian notes                   | M01     | in-progress |
| [[B06-share-obsidian-note\|B06]]                          | Share a Single Obsidian Note as a Web Page                      | Guide            | share obsidian note                    | M01     | in-progress |
| [[B07-obsidian-publish-alternative\|B07]]                 | Obsidian Publish Alternative                                    | Compare          | obsidian publish alternative           | M02     | planned     |
| [[B08-obsidian-website-builder\|B08]]                     | Obsidian Website Builder (product page)                         | Product          | obsidian website builder               | M02     | planned     |
| [[B09-obsidian-to-website-homepage\|B09]]                 | Obsidian to Website (homepage)                                  | Homepage         | obsidian to website                    | M02     | planned     |
| [[B10-pricing-page\|B10]]                                 | Pricing page                                                    | Pricing          | mdfriday pricing                       | M02     | planned     |
| [[B11-obsidian-publish-custom-domain\|B11]]               | Obsidian Publish Custom Domain                                  | Guide            | obsidian publish custom domain         | M02     | planned     |
| [[B12-obsidian-publish-free\|B12]]                        | Is Obsidian Publish Free? Cost and Free Ways to Publish         | Guide            | obsidian publish free                  | M02     | planned     |
| [[B13-quartz-alternative\|B13]]                           | Quartz Alternative                                              | Compare          | quartz alternative                     | M03     | planned     |
| [[B14-digital-garden-plugin-alternative\|B14]]            | Digital Garden Plugin Alternative                               | Compare          | digital garden plugin alternative      | M03     | planned     |
| [[B15-move-from-obsidian-publish\|B15]]                   | Move from Obsidian Publish to MDFriday                          | Guide            | migrate from obsidian publish          | M03     | planned     |
| [[B16-digital-garden-without-github\|B16]]                | Digital Garden Without GitHub                                   | Guide            | digital garden without github          | M03     | planned     |
| [[B17-obsidian-website-examples\|B17]]                    | Obsidian Website Examples (showcase)                            | Showcase         | obsidian website examples              | M01–M12 | in-progress |
| [[B18-friday-plugin-migration\|B18]]                      | Friday Plugin Migration Guide                                   | Trust            | (existing users)                       | M01     | in-progress |
| [[B19-security-page\|B19]]                                | Security page                                                   | Trust            | (trust page)                           | M01     | in-progress |
| [[B20-changelog\|B20]]                                    | Changelog                                                       | Trust            | (trust page)                           | M01     | in-progress |
| [[B21-friday-plugin-end-of-support\|B21]]                 | Friday Plugin End of Support (announcement)                     | Blog             | (announcement)                         | M04     | planned     |
| [[B22-start-a-digital-garden-2027\|B22]]                  | Start a Digital Garden in 2027                                  | Blog (seasonal)  | start a digital garden                 | M04     | planned     |
| [[B23-flowershow-alternative\|B23]]                       | Flowershow Alternative                                          | Compare          | flowershow alternative                 | M04     | planned     |
| [[B24-obsidian-website-without-coding\|B24]]              | Obsidian Website Without Coding                                 | Guide            | obsidian website without coding        | M04     | planned     |
| [[B25-obsidian-publish-themes\|B25]]                      | Obsidian Publish Themes                                         | Themes           | obsidian publish themes                | M04     | planned     |
| [[B26-obsidian-to-html\|B26]]                             | Obsidian to HTML                                                | Guide            | obsidian to html                       | M04     | planned     |
| [[B27-markdown-wiki\|B27]]                                | Markdown Wiki (solution page)                                   | Solution         | markdown wiki                          | M05     | planned     |
| [[B28-obsidian-knowledge-base\|B28]]                      | Obsidian Knowledge Base (solution page)                         | Solution         | obsidian knowledge base                | M05     | planned     |
| [[B29-how-to-host-obsidian-website\|B29]]                 | How to Host an Obsidian Website                                 | Guide            | how to host obsidian website           | M05     | planned     |
| [[B30-obsidian-wikilinks-website\|B30]]                   | Obsidian Wikilinks on a Website                                 | Guide            | obsidian wikilinks website             | M05     | planned     |
| [[B31-obsidian-publish-self-hosted\|B31]]                 | Obsidian Publish Self-Hosted                                    | Guide            | obsidian publish self hosted           | M05     | planned     |
| [[B32-obsidian-multilingual-website\|B32]]                | Obsidian Multilingual Website                                   | Guide            | obsidian multilingual website          | M06     | planned     |
| [[B33-foundry-hugo-in-typescript\|B33]]                   | Foundry: Hugo Reimplemented in TypeScript                       | Blog (technical) | (developer audience)                   | M06     | planned     |
| [[B34-mdfriday-on-product-hunt\|B34]]                     | MDFriday on Product Hunt                                        | Blog (launch)    | (launch)                               | M06     | planned     |
| [[B35-chinese-localization\|B35]]                         | Chinese localization (6 pages)                                  | Localization     | (Chinese core pages)                   | M06     | planned     |
| [[B36-markdown-website\|B36]]                             | Markdown Website (category page)                                | Solution         | markdown website                       | M07     | planned     |
| [[B37-markdown-website-builder\|B37]]                     | Markdown Website Builder (Studio product page)                  | Product          | markdown website builder               | M07     | planned     |
| [[B38-publish-markdown-without-github\|B38]]              | Publish Markdown Without GitHub                                 | Guide            | publish markdown without github        | M07     | planned     |
| [[B39-markdown-docs\|B39]]                                | Markdown Docs (solution page)                                   | Solution         | markdown docs                          | M08     | planned     |
| [[B40-markdown-blog\|B40]]                                | Markdown Blog (solution page)                                   | Solution         | markdown blog                          | M08     | planned     |
| [[B41-hugo-alternative\|B41]]                             | Hugo Alternative                                                | Compare          | hugo alternative                       | M08     | planned     |
| [[B42-markdown-mermaid-website\|B42]]                     | Markdown Mermaid Website                                        | Guide            | markdown mermaid website               | M09     | planned     |
| [[B43-markdown-latex-website\|B43]]                       | Markdown LaTeX Website                                          | Guide            | markdown latex website                 | M09     | planned     |
| [[B44-homepage-markdown-positioning\|B44]]                | Homepage positioning: markdown to website                       | Homepage         | markdown to website                    | M07     | planned     |
| [[B45-obsidian-newsletter\|B45]]                          | Obsidian Newsletter (solution page)                             | Solution         | obsidian newsletter                    | M10     | planned     |
| [[B46-monetize-your-notes\|B46]]                          | Monetize Your Notes                                             | Guide            | monetize obsidian notes                | M11     | planned     |
| [[B47-user-stories\|B47]]                                 | User stories series (5 posts)                                   | Story            | (case studies)                         | M10–M12 | planned     |
| [[B48-state-of-obsidian-publishing-2027\|B48]]            | State of Obsidian Publishing 2027                               | Report           | (original research)                    | M11     | planned     |
| [[B49-what-is-a-digital-garden\|B49]]                     | What Is a Digital Garden                                        | Guide            | what is a digital garden               | M11     | planned     |
| [[B50-obsidian-course-notes-website\|B50]]                | Obsidian Course Notes Website                                   | Guide (seasonal) | obsidian for students publish notes    | M11     | planned     |
| [[B51-homepage-platform-positioning\|B51]]                | Homepage positioning: publishing platform                       | Homepage         | markdown publishing platform           | M12     | planned     |
| [[B52-year-one-review\|B52]]                              | MDFriday Year One review                                        | Blog             | (annual review)                        | M12     | planned     |
| [[B53-update-published-obsidian-notes\|B53]]              | Update Published Obsidian Notes                                 | Guide            | update obsidian publish site           | M04     | planned     |
| [[B54-obsidian-notes-broken-after-publishing\|B54]]       | Obsidian Notes Broken After Publishing? What to Check First     | Guide            | obsidian notes broken after publishing | M05     | planned     |
| [[B55-obsidian-publishing-mistakes\|B55]]                 | Obsidian Publishing Mistakes                                    | Blog             | obsidian publishing mistakes           | M06     | planned     |
| [[B56-quartz-vs-obsidian-publish-vs-digital-garden\|B56]] | Quartz vs Obsidian Publish vs Digital Garden                    | Compare          | quartz vs obsidian publish             | M04     | planned     |
| [[B57-obsidian-seo\|B57]]                                 | SEO for Published Obsidian Notes                                | Guide            | obsidian seo                           | M05     | planned     |
| [[B58-story-sunwei-xyz\|B58]]                             | Case study: Publishing a 255-Note Obsidian Garden with MDFriday | Story            | (case study)                           | M03     | planned     |
| [[B59-story-help-center\|B59]]                            | Case study: How We Run MDFriday's Help Center on MDFriday       | Story            | (case study)                           | M02     | planned     |

## Voice of the customer by page

```base
filters:
  and:
    - type == "voc"
    - "!seo_brief.isEmpty()"
views:
  - type: table
    name: VOC by SEO page
    groupBy:
      property: seo_brief
      direction: ASC
    order:
      - file.name
      - title
      - decision
      - reply
      - date
```
