---
title: Discovery report template (placeholders are filled by build_report.py)
---

# Discovery report template (placeholders are filled by build_report.py)

```markdown
# <Product> · Web supplement: pain points beyond the existing summary

> Date: YYYY-MM-DD (timezone). Supplements `<existing-summary>.md`; includes only what its N clusters do not cover, plus brief new evidence and <language> community findings.
>
> **Sources searched:** ... **Archived:** P pages (`pages/`, index `registry.json`).
>
> **Result:** K new clusters (+ weak signals), C community-specific pains, a short new-evidence section. **Q quotes from U distinct URLs.**
>
> **Method:** (1) quotes kept in original language and compared verbatim with archived pages (entity-decoded, NFKC, whitespace-collapsed): Q/Q passed. (2) URLs deduped against the existing research's URL list (~X normalized URLs). (3) Signal strength = distinct sources (quoted + corroborating). (4) 「」 = verbatim; plain text = paraphrase or suggestion. (5) Capabilities outside the confirmed list are marked **to be confirmed**.

## 1. New pain clusters
| # | New cluster | Signal (distinct sources) | Latest evidence | Relevance to <Product> |
|---:|---|---:|---|---|
| N1 | ... | 12 | 2025-12 | High |

### N1 <Cluster>
**One line:** ...
- **Signal:** 12 sources ({{N:N1}} quoted, plus 5 corroborating)
- **Quotes:**
{{Q:N1}}
- **Corroborating:** {{X:https://... | https://...}}
- **Related competitors:** ...
- **Difference from existing report:** ...
- **Suggested response:** ... (**to be confirmed** where not a confirmed capability)

## 2. New evidence for existing clusters (brief)
- Cluster 2.x: {{E:S2:0}} ...

## 3. <Language> community pains
**Source situation (honest):** which communities worked, which failed, representativeness.
**Qualitative ranking vs English communities:** ...
### C1 <Pain>
- **One line / Signal / Quotes / Implication**

## 4. Impact on priorities
| Priority | Pain | Why | Must confirm first |
**Impact on existing top messages:** ...

## Appendix: coverage
| Source | Method | Result |
```
