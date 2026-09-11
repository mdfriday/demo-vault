---
title: Prompt Engineering
tags:
  - ai
  - prompts
---

# Prompt Engineering

Prompting is product design in text form. The goal is not clever wording — it is **reliable behavior**.

## A simple pattern

1. **Role** — who the model is for this task
2. **Context** — only what changes the answer
3. **Constraints** — format, length, must / must-not
4. **Example** — one good output beats three adjectives

> [!example]
> Bad: “Write a better landing page.”
> Better: “Rewrite this hero for solo founders. Max 12 words. Emphasize one-click publish. Keep brand voice calm.”

## When prompts become systems

Once a prompt is reused daily, promote it:

- Save it next to the workflow in your [[Second Brain]]
- Wire it into [[Claude Code]] or an [[AI Agents|agent]]
- Expose tools through [[MCP]] instead of stuffing everything into the prompt

| Level | What you maintain | Failure mode |
|-------|-------------------|--------------|
| One-off chat | Nothing | Drift |
| Saved prompt | Text | Stale examples |
| Tool-using agent | Tools + policy | Silent wrong tool |

## See also

- [[Claude Code]]
- [[AI Agents]]
- [[MCP]]
- [[AI Product Development]]
