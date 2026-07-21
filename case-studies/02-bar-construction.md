# Case study 02 — The mis-constructed bar: a 95% false-fail criterion, authored by the arbiter

*Anonymized from a real experiment cycle. Names, data identifiers, and dates are
generalized; the numbers and failure shape are exact.*

## The setup

The successor to case study 01: a repaired null-control suite for the same instrument,
now with a genuine varying null — R = 200 resampled replicates, each asking whether the
instrument falsely detected "existence" in null data, across **three candidate families**,
each controlled at α = 0.05 by the frozen instrument's own per-family error control.

The registered decision bar: **fail the leg if more than 10 of 200 replicates show a
false existence in ANY family.** That bar was proposed by the different-model arbiter
itself, as correction #1 during the pre-execution adjudication, and carried into the
countersigned registration. Director draft → different-model arbiter → human countersign:
all three approved it.

## The defect

The bar applied a **single-family 5% threshold to a three-family UNION count.** Under the
null "the instrument is nominal," each family falsely fires at ≤5% per replicate, so the
union event ("any family fires") occurs at ≈ 1 − (1−0.05)³ ≈ 0.083 per replicate
(observed union rate ≈ 0.083). Then:

> P(Bin(200, 0.083) > 10) ≈ **0.948** — a NOMINAL instrument fails this bar with
> probability ≈ 0.95.

The bar was practically unpassable by construction. The scored run duly failed it —
**15/200** union events vs the bar's **>10/200** — while the per-family rates were
individually **nominal: 9/200 (4.5%), 8/200 (4.0%), 0/200 (0%)**, each within its own
α = 0.05.

A subtlety worth keeping: the director's first recount computed the false-fail against
the wrong reference — a per-family Bin(200, 0.05), giving P(X>10) = 0.417 ("the bar sits
at the null expectation — a coin flip, not a criterion"). Bad enough to flag the defect,
but it **undersold** it: the correct union-rate reference gives 0.95. Even the recount of
a defect needs its reference distribution checked.

## Who caught it, and who didn't

- The chain that approved it: director draft, different-model arbiter (who AUTHORED the
  bar), human countersign — the same three-layer miss as case 01, one cycle later.
- Post-run, the convergent adjudication caught it: the director's raw-record recount
  flagged the bar as uninformative; a fresh-context adversarial pass derived the correct
  union-rate arithmetic (the decisive finding); the different-model arbiter, re-briefed,
  **owned the miss explicitly: "the adjudication chain shares the miss."** It also
  supplied the correct construction: choose the estimand first; if family-wise, Šidák
  sub-bars at α′ = 1 − 0.95^(1/3) ≈ 0.017 per family; then set the critical count for a
  PRE-COMPUTED false-fail (at R = 200, p₀ = 0.05 per family: fail only above k = 17,
  false-fail 0.0121 per bar, ≤ 0.0363 leg-level by Bonferroni) AND pre-computed power
  (0.715 against a 2× defect, 0.996 against 3×).

## The verdict vocabulary

**FAIL-AT-REGISTERED-BAR (BAR-CONSTRUCTION DEFECT)** — with the raw mechanical route
(FAIL at the registered threshold) preserved unedited beside it. Not a refutation of the
instrument: the null construction was valid; the DECISION RULE was inadequate. And not a
pass either — the leg stayed UNRESOLVED pending a bar-only re-registration on fresh data
(see `03-criterion-shopping.md`).

## The rules this created

1. **Every registered empirical decision bar carries, IN the registration, its computed
   false-fail probability under the null it claims to control AND its power against a
   named alternative.** A bar sitting at (or beyond) the null expectation is a coin flip
   (or a guaranteed fail), not a criterion. Make it a fixture: recompute the registered
   constants from scratch at build time and assert they match.
2. **Leg-level error is what must be controlled.** When a criterion spans multiple
   families/sub-bars, compute the false-fail across ALL of them (Bonferroni or exact) —
   a per-bar rate that looks fine can compose into a near-certain leg failure.
3. **The estimand of a multi-family control must be pre-declared** — per-family α or
   family-wise α, with the sub-bars written out — and justified from what downstream
   claims consume.
4. **The arbiter shares the miss — verify rulings.** The defective bar was the arbiter's
   own correction, approved through every layer. A different-model ruling is information,
   not an oracle; corrections get their premises checked like any other claim
   (CHECKLISTS.md §4). Corollary for briefing: when the arbiter reviews an artifact it
   authored, say so and instruct it to be harsher (CHECKLISTS.md §3.3).
