# BUILD-<line> — chain log of record for the <line> experiment line

> **Scope.** ONE chain-log doc per experiment line (§G.6). Every registration in this
> line (v1, v1b, v1c…) appends its entries HERE: registration status, arbiter rulings +
> verifications, countersigns, build reports, deviations, pre-run predictions, the run of
> record, adjudication, and the verdict. Registration docs freeze at countersign and
> point here. Entries are append-only and dated; nothing is rewritten.

## §1. Registration — <EXP-ID>

- **Draft:** `<REGISTRATION doc filename>` (drafter: <who>, <date>). <One line: what it
  registers; if a successor, which binding items of the prior ruling it discharges.>
- **Director pre-arbiter verification (CHECKLISTS.md §2):** <what was independently
  recomputed (each registered number, to how many decimals); which code lines were opened
  and confirmed; which fences/allowlists were read; the estimand-consumption check.>
- **Arbiter ruling (the ONE §G registration check):** brief `c3_<exp>_brief.md`
  (attack-first section named; authorship conflicts disclosed), ruling
  `c3_<exp>_ruling_raw.md`. **OVERALL: <APPROVE / APPROVE-WITH-CORRECTIONS / REJECT>**,
  per-question summary. <For each attack line: what the arbiter tried and found.> (If no
  different-model arbiter is available: same-model fresh-context fallback, labeled per
  ADAPTING's degrading-gracefully ladder; the verdict carries the C5 tripwire.)
- **Ruling verification ("a ruling earns a check"):** <each factual claim in the ruling
  checked against real code/data — hashes recomputed, cited docs opened, arithmetic
  re-derived. Corrections applied verbatim, each marked in the registration; declined
  corrections with written reasons.>

## §2. Countersign (the ONE user gate)

**USER COUNTERSIGN <date>: `<registration filename>` is RATIFIED as corrected.** The
signature authorizes build + freeze + scored run; **data blocks <A> + <B> are hereby
CONSUMED (A4/§G.4).** <Any rider text the ruling required, copied verbatim.> Next: build →
gates green → freeze manifest → scored run → director D4 (+ escalation per §G.5).

## §3. Build + director pass at build-complete

- **Build (executor):** <N/N gates PASS (fixture output artifact named), freeze manifest
  = <n> pins. Surfaced ambiguities listed as A3-<EXP>-N candidates. No scored block
  observed.>
- **Director verification (re-derived, not re-read — CHECKLISTS.md §5):** fixtures re-run
  BY THE DIRECTOR — <N/N> reproduced. Manifest re-verified. **Equivalence probe** (for
  any transcribed law): <old vs new implementation, identical inputs + identical RNG,
  <n> replicates deep-compared on the pinned keyset (outcomes AND provenance/draw-order)
  → <0> mismatches.>
- **A3 rulings (director, one per surfaced ambiguity — accepting silently is deciding
  silently):** A3-<EXP>-1 <ACCEPTED/REJECTED: reason>. A3-<EXP>-2 <…>. Minor items
  (a)–(n) <ruled individually>.

## §4. Deviations (append-only)

**A3-<EXP>-RUN-1 — <title> (<date>).** What happened / why it is not a criterion change
(or: why it IS, and the new-registration mandate it creates) / the fix (no frozen file
touched; new fixture added; manifest re-pinned) / disclosure to the user before
proceeding.

## §5. Pre-run predictions (REGISTERED BEFORE THE OUTPUT EXISTS — CHECKLISTS.md §6)

Director predictions (<date>, run in flight / not yet started; output file not on disk;
priors: <named calibration/predecessor runs>):
1. <gate/re-hash outcome>
2. <each leg's expected result>
3. <count bands with the statistical band stated>
4. <PREDICTED VERDICT + its probability under the null>
5. <dual-report agreement band>
6. <wall time ± band>

If ANY prediction misses — especially <named worst cases> — §G.5 escalation is pre-armed
<state which trigger applies; note if a PASS is favorable+load-bearing ⇒ one-arbiter
check regardless>.

## §6. Run of record

**Run of record** (<date>; re-hash <n/n> PASS; wall <t>; output `<artifact>`; blocks
<A>+<B> now CONSUMED): <per-leg results with raw numbers>. **Mechanical router verdict:
<VERDICT (route)>** — the routing itself is <disputed/undisputed>.

## §7. Adjudication

- **Director D4 (CHECKLISTS.md §7):** <every verdict-bearing number recounted from RAW
  records; label re-derived; each §5 prediction checked, misses reported honestly;
  non-routed reference statistics computed.>
- **Escalation decision (per the §G.5 table):** <none needed / ONE arbiter because
  disputed | line-closing | favorable-and-load-bearing>. <If escalated: brief + ruling
  artifacts; the arbiter's findings; director verification of each factual claim.>
- <Second arbiter ONLY if the first disagreed with the director: record the disagreement
  and both rulings.>

## §8. VERDICT OF RECORD

**Verdict of record: `<B1-vocabulary verdict>`** — raw mechanical route `<route>`
preserved in the output artifact, never rewritten.

- **What stands:** <list>.
- **What is NOT licensed:** <list — claims that may not be cited, re-poses that stay
  blocked, quarantines that stay sealed>.
- **Disposition (from the registration's §6 table — mechanical):** <named option>.
  <Binding items (i)–(n) on any successor registration.>
- **Lessons ratcheted:** <pointer to lessons entries + which fixtures they became +
  which review steps they retired (CHECKLISTS.md §10)>.

**USER COUNTERSIGN <date>: the verdict of record is RATIFIED.** <Any held dispositions
and their conditions.>

---

*(Successor registrations in this line append as §9, §10, … following the same shape.)*
