---
title: Access password
weight: 37
tags: [security, password]
date: 2026-10-09
lastmod: 2026-10-09
description: Add an access password so the page body is encrypted before upload and decrypted in the visitor's browser. Works on every plan.
---

# Access password

## Goal

Require a password before a visitor can read the page body. Useful for a brief or an internal note that still needs a link.

This is content encryption, not a login. The page body is encrypted on your computer with AES-256-GCM (PBKDF2-SHA256, 100,000 iterations) and decrypted in the visitor's browser. MDFriday's servers never receive the password or the plaintext.

## What stays public

- The page title
- The URL
- Image and attachment files (only the HTML body is encrypted)

Do not publish an attachment that cannot be public. There is one password, not several, and you cannot revoke a single reader. If you forget the password, set a new one and publish again — it cannot be recovered.

## Prerequisites

- Any plan can use it: Guest, Free, and Personal. A Guest site still clears at the next UTC 00:00. Claim Free to keep the same URL
- The sidebar path config records that a password is set. It does not store the password text there. The password is not uploaded; the published page body is ciphertext
- A per-page `password:` in frontmatter works in **theme mode** only. Child pages inherit the parent section's password. Faithful (single-note) mode uses the site password from Advanced, not frontmatter

## Steps

1. Right panel → **Advanced**
2. Enable **Access password** and enter it (leave it empty for a public page)
3. [[local-preview|Preview]], then **Publish**
4. Send the link and the password on separate channels

<!-- MEDIA: screenshot — Advanced access password -->
![Placeholder: access password](../images/placeholder-password.png)

To encrypt one page inside a themed site, add this to that note's frontmatter and publish again:

```yaml
password: your-password
```

## Confirm success

- An incognito visitor sees the password gate before the body
- View source or the network panel: the body is ciphertext, not the note text
- The title, URL, and image files are still reachable without the password
- To remove the password: clear it and publish again

## Related

- [[unpublish|Unpublish]] (takes the site offline; stronger than changing the password)
- <https://mdfriday.com/security/>
- <https://mdfriday.com/solutions/share-a-note/>

## Common failures

| Symptom | What to do |
| --- | --- |
| Set a password but the page is still public | **Publish again.** Changing the panel without publishing does nothing |
| You cannot get in either | Check spaces and full-width characters, then set a new password and publish again. The old password cannot be recovered |
| A single page is not encrypted | `password:` in frontmatter applies in theme mode only. Faithful mode uses the site password from Advanced |
| Images are visible without the password | Expected. Attachments are not encrypted |
