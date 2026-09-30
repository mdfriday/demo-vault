---
title: Access password
weight: 37
tags: [security, password]
date: 2026-09-19
---

# Access password

## Goal

Require visitors to enter a password before opening the link — useful for briefs and internal materials that still need a link but a gate.

## Prerequisites

- Any plan (Guest / Free / Personal) can use access password (per Advanced options in the panel)
- Password is submitted **at publish time**; the plugin only keeps enablement-style flags locally and **does not persist the plaintext password in pathConfigs long-term**

## Steps

1. Right panel → **Advanced**
2. Enable **Access password** and enter it (placeholder: **leave empty for public access**)
3. [[local-preview|Preview]] (if the gate is on, preview may also show the gate page), then **Publish**
4. Send the link and password on separate channels

<!-- MEDIA: screenshot — Advanced access password -->
![Placeholder: access password](../images/placeholder-password.png)

## Confirm success

- Incognito / signed-out visitors hit the password gate on the public URL first
- Remove password: clear it and publish again

## Related

- [[unpublish|Unpublish]] (a more thorough offline than changing the password)
- <https://mdfriday.com/solutions/share-a-note/>

## Common failures

| Symptom | What to do |
| --- | --- |
| Set a password but still public | Confirm a successful **Publish again**; do not only change the panel without publishing |
| You cannot get in either | Check spaces / full-width characters; unpublish then republish |
