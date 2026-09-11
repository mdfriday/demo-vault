---
title: AI Agents
tags:
  - ai
  - agents
---

# AI Agents

An agent is a loop with tools: observe → decide → act → check. The hard part is not the loop — it’s **stopping conditions**.

## Keep agents narrow

| Agent type | Good at | Bad at |
|------------|---------|--------|
| Research | Gathering + summarizing | Final taste |
| Coding | Local edits with tests | Ambiguous product scope |
| Ops | Repetitive checklists | Novel judgment calls |

> [!danger]
> Unbounded agents burn tokens and trust. Give them a finish line.

## Connect the dots

- Better instructions → [[Prompt Engineering]]
- Better tools → [[MCP]]
- Better coding partner → [[Claude Code]]
- Why ship thin → [[AI Product Development]]

$$
\text{Useful autonomy} \approx \frac{\text{clear goal} \times \text{safe tools}}{\text{open-endedness}}
$$

## See also

- [[MCP]]
- [[Build in Public]]
- [[Second Brain]]
