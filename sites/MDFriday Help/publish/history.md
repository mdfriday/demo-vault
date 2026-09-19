---
title: Publish history and rollback
weight: 39
tags: [history, Personal]
date: 2026-09-19
---

# Publish history and rollback

## Goal

Browse past **publish** versions for a project and roll back when needed (site stays public).

## Prerequisites

- **Personal** plan for actionable history
- Guest / Free: History tab is a locked empty state (🔒) + upgrade prompt
- Only **Publish** writes history; **Preview never enters history**

## Steps (Personal)

1. Right panel → **History** tab
2. Browse version entries (time, mode, theme, URL, Live or not)
3. **View**: open that version’s page
4. **Rollback**: after confirm, overwrite the current published content with that historical version (site stays public)
5. On the current Live entry you can also **Unpublish** (see [[unpublish|Unpublish]])

<!-- MEDIA: screenshot — Personal history list -->
![Placeholder: publish history](../images/placeholder-history.png)

## Confirm success

- After rollback, the public URL shows the older content
- Project status stays **Published** (unlike Unpublish)

## Related

- [[unpublish|Unpublish]]
- [[../plans/guest-free-personal|Plans]]

## Common failures

| Symptom | What to do |
| --- | --- |
| History is a locked empty state | Upgrade to Personal, or confirm you only previewed and never published |
| Rollback failed | Network / quota; check Notice; report on Discord |
