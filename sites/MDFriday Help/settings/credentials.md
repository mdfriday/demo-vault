---
title: Credential (mdf key)
weight: 71
tags: [settings, credentials]
date: 2026-09-19
---

# Credential (mdf key)

## Goal

Understand the auto-issued publish credential and copy it to the account site or another device when needed.

## Where

**Settings → MDFriday Publish** (or the MDFriday item in Settings) → **Credentials**

## Fields

| Item | Meaning |
| --- | --- |
| Credential (mdf key) | Unified key; kind is guest or user (product does not encode kind into the displayed string) |
| Not created yet | Copy: *Not created yet — issued automatically on first publish.* |
| Created | Truncated preview; click to copy (*Mdf key copied*) |

> [!warning] Keep it private
> The mdf key is your publish identity. Do not commit it to a public repo or screenshot it for strangers. If lost/leaked, rotate via the official account-site flow (whatever that site currently supports).

## Related

- [[../plans/claim-and-upgrade|Claim and upgrade]]
- [[../get-started|First publish]]
