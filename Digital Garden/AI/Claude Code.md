---
title: Claude Code
tags:
  - ai
  - coding
  - tools
---

# Claude Code

Claude Code is leverage for people who already know what “done” looks like. It writes and edits; you still own taste and scope.

## Where it shines

- Boilerplate and refactors you can review in minutes
- Explaining unfamiliar code paths
- Turning a checklist into a first patch

> [!warning]
> Don’t outsource product judgment. If you can’t say what “correct” means, the model will invent one.

## Pair with a garden

Keep architecture notes in Obsidian. Link decisions here so future-you (and future agents) can find them:

- Product wedge → [[Share exactly what you see in Obsidian]]
- Tooling surface → [[MCP]]
- Autonomy boundary → [[AI Agents]]

```ts
// Preference: small diffs, explicit tests, boring names
type ChangeBudget = {
  files: number;
  mustPass: string[];
};
```

## See also

- [[Prompt Engineering]]
- [[AI Agents]]
- [[Build in Public]]
- [[Knowledge Management]]
