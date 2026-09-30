---
title: Pain point report template
---

# Pain point report template

```markdown
# <Product> · Customer pain points (based on <corpus>)

> Date: YYYY-MM-DD (timezone) · Scope: <folders/files> · Language: <narrative language>; quotes kept in original language

## 1. Overview
### 1.1 Sources
| Source | Files | How it was used |
|---|---:|---|
| VOC cards | 567 (7 themes) | Read every card, hand-tagged. Main evidence. |
| Comment corpus | 592 comments / 35 videos | Read every comment, counted explicit pains only. |
| Own marketing drafts | 6 | Not counted. Used only to check product claims. |
| Customer list | 1 | Aggregate only (e.g. domain distribution). No personal data quoted. |

Time span, platform distribution.

### 1.2 Method
1. Hand multi-label tagging with N tags; X items background-only (excluded); Y items with ≥1 tag.
2. Comments: counted only comments that clearly express a pain.
3. Quote verification: every quote compared verbatim with its source file (whitespace-normalized): A/A and B/B passed.
4. Caveats: single annotator (±10%); card text may be the collector's paraphrase; per-video tags ≠ per-comment counts.

## 2. Ranked pain clusters
| # | Cluster | Corpus items | Since <year> | Comments | Intensity |
|---:|---|---:|---:|---:|---|
Other small signals: ...

### 2.1 <Cluster name>
**Description:** what people are trying to do, where exactly they get stuck, in their terms.
- **Evidence:** N items (P% of corpus, M since <year>); K comments.
- **Representative quotes:**
  - "verbatim quote" — `path/to/source` · https://source-url (context)
- **Related competitors:** ...
- **Opportunity / matching capability:** confirmed capabilities only; otherwise "to be confirmed".

## 3. By audience (rough keyword counts, magnitude only)
| Audience | Evidence (rough) | Top 3 pains | Typical scenario / signal |

## 4. Competitor view
| Competitor | Items mentioning | Main complaints | What users praise (the bar to meet) |

## 5. Implications
### 5.1 Top 5 marketing messages (by evidence strength)
1. **"Message in customer language."** Cluster(s), evidence, hook quotes, demo idea, pre-conditions to confirm.
### 5.2 Product gaps the data points to (status to be confirmed internally)
| Priority | Gap | Evidence | Note |
Data gaps: ...

## 6. Appendix: source inventory and counts
```
