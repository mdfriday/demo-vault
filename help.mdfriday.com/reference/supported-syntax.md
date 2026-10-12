---
title: Supported syntax in MDFriday
weight: 55
tags: [reference, syntax]
date: 2026-10-11
lastmod: 2026-10-11
description: What MDFriday Publish renders in Faithful mode and in a theme, and what it does not render today.
---

# Supported syntax in MDFriday

Applies to plugin **v26.10.2**.

This is the support list as implemented in the plugin, the theme packs, and the page engine. Items not yet checked on a production site are marked. A locked or missing block is a product limit, not a failed publish.

## Faithful (one note)

Obsidian renders the note, then MDFriday saves that HTML. What you see in reading view is what visitors get, including output from community plugins such as Dataview, **as a still picture of that moment**.

- Filters, sorts, and other clicks do not keep working
- The snapshot can change the next time those plugins render. It is not a guarantee
- A folder cannot use Faithful. The panel disables it

## Theme mode (one note, or a whole folder)

The engine renders the Markdown itself. These work:

- Wikilinks and embeds that point at notes **inside** the published note or folder
- Callouts
- Mermaid
- Math (KaTeX)
- Footnotes
- Fenced code with highlighting

These do not:

| You wrote | What happens |
| --- | --- |
| Dataview or Bases in a themed note or in a folder | The query is not executed. Publish that page as a single note in **Faithful** if you need the table |
| Canvas, Excalidraw | Not published |
| A wikilink to a note outside the selection | That note is not on the site. Check the preview. Do not assume the graph hides the title; that edge has not been measured on production |
| RSS, comments, or a second language switch in the plugin | Not available |

## Check your own notes

1. [[../publish/local-preview|Preview]] the real note, not a sample
2. If a block is missing, switch **Faithful** and **Single-page theme** once each
3. For a folder, stay on a wiki theme. Faithful will not appear

Guest publish is enough for this check. You do not need Personal to see whether a block survives.

## Related

- [[../themes/index|Themes]]
- [[../publish/modes|Publish modes]]
- [[../faq|FAQ]]
- <https://mdfriday.com/solutions/digital-garden/>
