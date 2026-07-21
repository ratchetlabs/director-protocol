# Case study 03 — Criterion shopping: repairing a bar after the data has shown its hand

*Anonymized from a real experiment cycle. Names, data identifiers, and dates are
generalized; the numbers and failure shape are exact. Continues case study 02.*

## The hazard

After the mis-constructed bar failed (case 02), the consumed run's data was on the table —
and it **revealed which estimand would pass**:

- **Per-family reading (α = 0.05 per family):** observed counts 9/200, 8/200, 0/200 —
  all nominal → PASSES.
- **Family-wise reading (Šidák α′ ≈ 0.017 per family, expectation 3.4):** observed 9 and
  8 both far above the sub-bar → FAILS.

Whoever writes the repair registration now *knows the answer key*. Choosing "per-family"
because it passes is criterion shopping — the freeze attack in slow motion. But refusing
to repair at all would leave a healthy instrument dead at a defective bar. The protocol's
answer was to make the hazard itself a registered, attackable object.

## How the repair was made honest

The bar-only re-registration (day 2, one day after the failed run) did four things:

1. **Argued the estimand from what downstream consumes — never from what passes.** Every
   registered downstream consumer of the verdict was enumerated and shown to read
   **per-family** quantities: the verdict router consumed per-family booleans on separate
   limbs; the follow-on experiment's registered criterion was conjunctive across
   families; the frozen instrument's own error-control claim was per-family by
   construction (no cross-family correction existed in the frozen code). No registered
   consumer of the union event existed. The family-wise case was **steelmanned in the
   registration anyway** (with its correct Šidák construction written out), and
   union-shaped claims were BANNED by an explicit rider absent separate validation — so
   choosing per-family did not quietly license the family-wise reading.
2. **Disclosed the hazard numerically, in a box, in the registration**: "the consumed
   block's counts (9/8/0) pass per-family while family-wise would fail; the choice below
   is therefore argued ONLY from consumption; the consumed block proves NOTHING here —
   the bars were chosen after seeing it."
3. **Directed the arbiter to attack the estimand FIRST.** The brief's first question:
   try to REFUTE the consumption argument — (a) find ANY registered consumer of the union
   event; (b) test whether the rider is enforceable or leaks; (c) **ask whether the same
   argument would have been available and equally strong BEFORE the failed run — if not,
   name the leak.** The arbiter's refutation attempt failed on (a) and, decisively,
   ruled on (c) that the argument was available pre-run (no leak), while still extracting
   corrections (a verbatim rider text; an i.i.d.-wording fix on the binomial null; a
   fixture for the escalation trigger).
4. **Decided only on FRESH data.** New, never-observed blocks for both the environment
   draws and the resampling RNG stream — with the pre-commitment stated in the
   registration: *"if the fresh counts land above the bar, the experiment fails at a bar
   we pre-committed to, knowing the old data passed it."* The consumed block appears in
   the successor only as design-justification material, never as verdict evidence.

The corrected bar itself carried the case-02 lessons: fail iff any family exceeds
k = 17 of 200 (per-bar false-fail 0.0121, leg-level ≤ 0.0363 Bonferroni, power 0.715 at a
2× defect and 0.996 at 3×) — plus an **estimand-lock fixture** asserting that no routed
code path compares the union count to any bar (the union count is serialized under an
explicit `NOT_ROUTED` field, dual-reported forever).

## The rules this created

1. **Estimand pre-declaration is mandatory** for any multi-family decision rule — argued
   from registered downstream consumers, with the rejected reading steelmanned and its
   claim forms explicitly banned or separately validated.
2. **When a repair follows a failed run, the criterion-shopping hazard is LIVE and must
   be disclosed numerically in the registration itself** — which choices pass/fail on the
   consumed data — then attacked first by the arbiter, with the "would this argument have
   been available before the run?" test applied explicitly.
3. **Fresh-data separation discharges the hazard**: the choice may be *informed* by
   consumed data's diagnostics (e.g. a sensitivity flag), but the verdict comes only from
   never-observed blocks, with the uncomfortable outcome pre-committed in writing.
4. **Lock the estimand mechanically**: a fixture asserting the routed predicate reads
   exactly the registered quantity and that the rejected estimand appears only under a
   NOT-ROUTED field.
