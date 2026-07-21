# <EXP-ID> — <one-line description of what this registers> (DRAFT)

> **STATUS:** DRAFT → (after arbiter ruling + corrections applied) → **FROZEN at user
> countersign.** Status semantics: while DRAFT, anything may change; after the arbiter
> ruling, corrections are applied verbatim and marked "(arbiter correction N)" in place;
> at the countersign this document FREEZES — its hash goes into the freeze manifest, and
> **all further status lands in the chain log `BUILD-<line>.md` only** (a status pointer
> here, nothing else). The ONE countersign authorizes build + freeze + scored run AND
> consumes the §5 data blocks — no separate go/no-go.
>
> **What this registers.** <Exactly which criterion/instrument/design is new here. If this
> is a successor registration, state what is re-adopted by pin (§1) and name the ONE thing
> replaced.>
>
> **Governing ruling this draft transcribes (binding)** — `[successor/multi-family only]`:
> <chain-log §, the verdict of record, and the numbered binding items (i)–(n) this draft
> must discharge — with a pointer to where each is discharged below. Omit this block for a
> first, single-family registration.>
>
> **Applicability legend.** Sections and sub-parts are tagged `[always]` or
> `[successor/multi-family only]`. The always parts (§1 pins/A2, §2.2 bar/B2, §3 router,
> §4 gates, §5 blocks/A4) are the minimum any registration carries. The
> `[successor/multi-family only]` parts — the governing-ruling block above, the
> criterion-shopping disclosure (§2.1), union/leg-level sub-bars and Šidák-style
> corrections (§2.2), NOT-ROUTED dual reports (§2.2/§2.4) — apply ONLY when a prior run has
> seen relevant data (successor) or the bar spans multiple families. A first, single-family
> registration deletes them rather than filling them with N/A.

---

## 1. Pins — what is re-adopted BYTE-UNCHANGED (A2/A6) `[always]`

Every decision-bearing file, hashed. The scored driver re-hashes at run time and refuses
to run on mismatch. Pin the LIVE file's current hash and verify it now; if an archival
hash differs from the live file, resolve which one the freeze pins before the arbiter
sees this draft (CHECKLISTS.md §2.6).

| File | Role (re-adopted by pin) | Hash |
|---|---|---|
| `<file>` | <role — "VERBATIM, no constant changed (A6)"> | `<md5>` |

**Design re-adopted by reference:** <pointers to the parent registration's sections that
carry unchanged — do not restate them. Then: "The ONE thing replaced is <parent §
sentence>, superseded by §2 below.">

---

## 2. The registered decision rule (the new criterion)

### 2.1 Estimand — pre-declared, argued from what downstream consumes `[always; the criterion-shopping disclosure box below is successor/multi-family only]`

> **CRITERION-SHOPPING HAZARD DISCLOSURE (mandatory if any relevant data has been seen).**
> <If a prior run revealed which estimand/criterion choice would pass, SAY SO NUMERICALLY:
> "on the consumed block, choice X passes (counts …) while choice Y fails (…)". Then:
> the choice below is argued ONLY from what downstream claims consume, never from which
> choice passes; and it is tested on the FRESH §5 blocks. Direct the arbiter to attack
> this subsection FIRST (§7 brief).>

**What downstream actually consumes.** <Enumerate every registered downstream consumer of
this verdict and what quantity each reads. The estimand must be the quantity they consume.>

**The honest case FOR the alternative (steelmanned).** <Write the strongest argument for
the estimand you are NOT choosing, with its correct construction spelled out.>

**Recommendation (director's verdict):** <the choice, with numbered reasons; plus how the
rejected reading is kept on the record without being routed (dual report, §2.4) and any
claim forms that are BANNED absent separate validation (rider, §6).>

### 2.2 The bar — statistic, constants, false-fail, power (ALL PRE-COMPUTED — mandatory) `[always; union/leg-level sub-bars, Šidák-style corrections, and NOT-ROUTED reference bars are successor/multi-family only]`

**Statistic.** <Exact definition, per family/arm, over R items, from named serialized
fields.>

**Decision rule (the registered bar):**

> **FAILS if and only if <exact predicate, exact inequality form (> vs ≥), exact
> constants>.** Otherwise PASSES. <Dual readings computed against the same bars are
> reported, flagged on disagreement, and never change the routed verdict.>

**Null model and false-fail arithmetic (shown, not asserted — recompute for this draft):**
- State the null model and why it applies to this construction (independence /
  exchangeability argument; disclose what the bar does NOT claim, e.g. cluster-robustness).
- Per-bar false-fail: P(<statistic> breaches | null) = <computed value>.
- **Leg-level false-fail across ALL sub-bars** (the number that must be controlled):
  Bonferroni bound = <n × per-bar> (valid under any dependence); independence value for
  reference = <value>. A bar sitting at the null expectation is a coin flip, not a
  criterion.
- Rejected alternatives: show the constants you did NOT choose and their (unacceptable)
  leg-level rates, so the choice is visibly reasoned.

**Power arithmetic (the bar must discriminate, not merely be survivable):**

| Alternative (named) | E[statistic] | Power to fail the bar |
|---|---|---|
| null | <> | <= false-fail, above> |
| <named defect at k× floor> | <> | <computed> |
| <named defect at m× floor> | <> | <computed> |

Disclosed limitations: <e.g. power against a single-family defect at the small alternative,
and why raising it is out of scope>.

**Honest disclosure (if prior data exists):** on the consumed block the observed values
<would PASS / would FAIL> these bars. That block proves NOTHING here — the bars were
chosen after seeing it. The verdict comes only from the fresh §5 blocks; pre-commit now
to accepting a fresh-block failure at these bars.

**Non-routed reference bars:** <the rejected estimand's construction, serialized for the
dual report, marked NOT-ROUTED.>

### 2.3 Known sensitivity flags — each addressed mechanically

<For every carry-forward flag from prior runs (a confound, an imbalance): the chosen
instrument (stratified dual report / matched sampling / …), the justification, and a
MECHANICAL pre-declared escalation trigger with its exact formula, tie-handling, and
serialized fields — never a discretionary "we'll look at it".>

### 2.4 Mandatory dual reports (B4) `[always for superseded bars; NOT-ROUTED alternative-estimand reports are successor/multi-family only]`

<Everything reported beside routed quantities, never consumed: predecessor results
(cited, never re-scored); superseded bars' readings; alternative-estimand counts;
sensitivity strata.>

### 2.5 Serialization (BINDING)

The scored output must contain, with EXACT field names, **per-item decision evidence** —
per-replicate, per-family records (statistics, p-values, admit booleans, AND
**magnitudes**), never aggregate-only. Echo the registered constants (bar, false-fail,
power) into the artifact so the output is self-describing. A construction fixture (§4)
asserts every field and refuses aggregate-only output. The run of record must be
auditable without re-execution.

---

## 3. Verdict router `[always]`

<The exhaustive mapping from leg outcomes to verdicts: every combination of pass/fail
booleans routes to exactly one named verdict; any missing boolean → CONSTRUCTION-STOP.
An exhaustive-router fixture (§4) asserts this.>

---

## 4. Construction gates (fixtures — all must pass before freeze) `[always]`

- **Vacuity / differ-check (B5):** the consumed input channels actually differ across
  discriminated conditions; byte-level assertion.
- **Planted-true-null:** input null BY CONSTRUCTION → zero detections; plus a negative
  control proving the check can fire.
- **Schema fixture:** every §2.5 field present, per-item, magnitudes included.
- **Bar-arithmetic fixture:** recompute the §2.2 false-fail and power values from scratch;
  assert they match the registered constants to 1e-6.
- **Estimand-lock fixture:** the routed predicate reads exactly the registered quantity;
  NO routed code path consumes the rejected estimand (it appears only under a NOT-ROUTED
  field).
- **Static fence conformance:** every registered data block admitted by EVERY layer's
  allowlist BY LIST INSPECTION (never by running); never-run blocks in no runnable
  allowlist. If a needed allowlist extension is known now, it is a NAMED build
  deliverable and this gate is declared red until it lands.
- **Exhaustive router fixture** (§3).
- **Escalation-trigger fixture** (§2.3): synthetic cases where the trigger must fire,
  must not fire, and the boundary case.
- **Hash freeze (A2):** the freeze manifest = §1 pins + the new files + this document;
  re-hash HARD-FAIL before any scored data is touched.

---

## 5. Data blocks (A4) — fresh, disjoint, consumption rule stated `[always]`

| Block | Role | Observed by run? | Rationale |
|---|---|---|---|
| block A (<range/name>) | <role> | <yes/no> | <> |
| block B (<range/name>) | <role> | <> | <> |

**Consumption rule (state explicitly):** both blocks are CONSUMED at the user's ONE
countersign of this document — the countersign authorizes build + freeze + scored run
with no separate go/no-go; the hash re-check is what guarantees nothing drifts between
signature and run. Blocks are disjoint from every consumed block and never before
observed; no build step may render or observe them before the scored run.

<If any allowlist/fence does not yet admit a registered block, pre-declare the finding
HERE, with the code lines read, and name the extension module as a build deliverable —
so it is a registered step, not a mid-run deviation.>

---

## 6. Named dispositions (A5) — every verdict mapped before the run

| Verdict | Disposition (mechanical) |
|---|---|
| <PASS> | <what it licenses — plus any RIDER banning claim forms not validated here, to be copied verbatim into the countersign entry> |
| <FAIL(reason)> | <named repair-or-close path> |
| <UNTESTABLE / STOP> | <> |

---

## 7. Cycle plan + countersign checklist (§G)

- [ ] (1) **Arbiter adjudication of THIS draft** (the ONE independent check at
  registration). Brief directs attack at: <the disclosed hazard first; then arithmetic;
  then scope>. Ruling gets director verification against real code/data. (If no
  different-model arbiter is available: same-model fresh-context fallback, labeled per
  ADAPTING's degrading-gracefully ladder; the verdict carries the C5 tripwire.) Artifacts:
  `c3_<exp>_brief.md`, `c3_<exp>_ruling_raw.md`; disposition recorded in the chain log.
- [ ] (2) **ONE user countersign** of this doc — the item names this file + the §5 block
  rows and states: the signature authorizes build + freeze + scored run AND consumes the
  §5 blocks. Status stamps land in the chain log only.
- [ ] (3) **Build:** <named deliverables> → all §4 gates PASS → freeze manifest. ONE
  director pass at build-complete (CHECKLISTS.md §5).
- [ ] (4) **Scored run** (re-hash gate first) → quarantined output.
- [ ] (5) **Post-run: director D4** (predictions registered in the chain log BEFORE the
  output exists — CHECKLISTS.md §6). Escalate ONE arbiter only per §G.5 (note: a PASS
  that is favorable and load-bearing DOES get the one-arbiter check). Verdict write-up
  appended to the chain log.

---

## 8. What this does NOT re-open (scope fence)

<Enumerate: predecessor verdicts that stand regardless of this run; designs ruled valid
and re-adopted untouched; quarantined outputs that stay sealed; questions this
registration deliberately does not answer. Anything not listed as open is closed.>

---

## 9. Deviation log (A3 — placeholder; surfaced, never silently resolved)

New deviations, if any surface during build or run, are logged here as **A3-<EXP>-N**
entries and in the chain log BEFORE any resolution lands in code. *(None yet.)*

**Pre-flagged for the arbiter (not deviations — disclosed choices):** <numbered list of
every judgment call in this draft: the estimand recommendation + hazard, declined
alternatives with grounds, constants chosen for leg-level (not per-bar) control, accepted
power limitations.>
