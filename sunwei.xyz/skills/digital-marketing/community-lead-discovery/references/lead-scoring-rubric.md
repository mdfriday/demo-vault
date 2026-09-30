---
title: Lead scoring rubric
---

# Lead scoring rubric

## Bands (as used in the reference digests)

| Band | Score | Meaning | Action |
|---|---|---|---|
| URGENT | ~90+ | Fresh, very clear intent for exactly what the product does, thin or unsatisfying replies so far | Draft a reply now; top of digest |
| HIGH | 80–89 | Clear intent and strong fit; thread may already have decent answers | Draft a reply if still open |
| MEDIUM | 50–79 | Related need, partial fit, or intent implied rather than stated | Listen; reply only if the OP asks the fitting question |
| Weak signal | <50 | Adjacent topic, off-lens, promotional, locked | "Noise / weak signals" list only |

## Calibration examples (reference run, publishing niche)

- **~92:** "Best way to publish pages without using git": a sync-plugin user asks for self-hosted publishing without git as the CMS. Exact pain, fresh, few answers.
- **~54:** A genealogy / local-history vault post whose goals include publishing finished outputs, but publishing isn't discussed yet → soft listen.
- **~40:** "What would you use today for a simple static business site": generic static hosting, no notes vault → archive-listen.
- **~34:** Obsidian longevity / wikilinks discussion with many comments but no publishing need → weak.
- A competitor's own launch or "bump" post: watch for organic follow-up questions; don't advertise in it.

## Carry / cool / drop (defaults in `lead_tracker.py`)

- Quiet window = no change in the activity metric and no newer activity. Score decays a few points per quiet window.
- URGENT/HIGH: demote one band on the 3rd consecutive quiet window, DROP on the 4th. Example: 92 → decays → 3rd quiet demoted (84→82) → 4th quiet DROP (46).
- MEDIUM: 1st quiet = cooling, 2nd = soft-DROP, 3rd = DROP.
- Activity resumes on a soft-DROP → cancel it and rescore (it may land below 50 → archive-listen).
- DROP + new activity + rescore ≥50 → REVIVE.
- Brand already mentioned in the thread → LISTEN-ONLY, whatever the score.

## Suggested factor weights (a calibration aid, NOT the original method)

The reference digests scored holistically. If you need consistency across runs, decompose and then sanity-check against the examples above:

| Factor | Points | High end looks like |
|---|---:|---|
| Intent clarity | 0–30 | Explicitly asks for a tool or approach the product provides |
| Fit | 0–25 | Their constraints match confirmed capabilities (no unconfirmed features) |
| Freshness | 0–15 | Posted or active within the window |
| Reply gap | 0–15 | Few or unsatisfying answers; question still open |
| Reach / audience | 0–10 | Active sub or forum, thread visible |
| Engagement risk | −15–0 | Brand already present, promo-hostile sub, locked, or mod-removed |
