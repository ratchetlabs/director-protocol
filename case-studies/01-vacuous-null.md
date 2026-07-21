# Case study 01 — The vacuous null: a control leg that could not fail

*Anonymized from a real experiment cycle. Names, data identifiers, and dates are
generalized; the numbers and failure shape are exact.*

## The setup

An experiment line needed to validate a statistical instrument — a detector claiming to
separate real structure from artifacts in a simulated environment. The registration
included the standard control: a **null leg**, an arm where the effect was absent by
construction, on which the instrument was required to detect nothing. The registered null
arm used the environment's "constant mode," which froze the environment's rendered output.

The registration went through the full ceremony of the time: a director draft, a
**different-model arbiter adjudication** (approved with corrections, applied), and a
**human countersign**. The build passed its fixtures. The scored run executed on a fresh
data block.

## The defect

The "constant mode" froze only the **rendered surface** (the pixels). But the instrument
never consumed the rendered surface — it consumed **live trace channels** computed
upstream of rendering. Those channels were **byte-identical across the null arm and the
real arm: 480/480 identical records on both consumed channels.**

So the null hypothesis was never instantiated. The "null" arm fed the instrument exactly
the same data as the real arm — the leg **could not fail by construction**. It duly
"detected" three genuine effects it had promised would be absent, which initially read as
"the instrument invents structure" — a false line-closing conclusion one adjudication
away from killing a healthy instrument.

## Who caught it, and who didn't

- The director's draft missed it.
- The different-model arbiter's pre-execution adjudication missed it.
- The human countersign missed it.
- The build fixtures missed it (they tested the harness, not the arm's effect on the
  *consumed* channels).
- **A post-run probe caught it in one step:** feed the instrument a channel that is null
  BY CONSTRUCTION and check it returns zero detections; then diff the null arm's consumed
  channels against the real arm's. The diff came back byte-identical — the arm froze the
  wrong quantity. The probe simultaneously **exonerated the instrument** (it behaved
  correctly on a genuine planted null) and localized the defect to the registration.

Cost: one consumed data block plus a full adjudication cycle — spent to avoid filing a
false "instrument is dead" verdict.

## The verdict vocabulary

The honest verdict was **UNTESTABLE-BY-CONSTRUCTION (null-leg vacuous)** — not NULL, not
REFUTED. The instrument was neither validated nor invalidated; the test never existed in
the data. Conflating "the control failed" with "the control never ran" is exactly what
the controlled vocabulary (PROTOCOL B1) prevents: it kept the line open for an honest
successor instead of closing it on a phantom result.

## The rules this created

1. **Trace every registered null/control arm to the instrument's CONSUMED inputs,
   end-to-end** — not to the surface the arm manipulates. "The arm freezes X" is only a
   control if the instrument reads X.
2. **Every new statistical instrument gets a planted-true-null probe as a mandatory
   construction FIXTURE** (not a post-run afterthought): input that is null by
   construction must yield zero detections, next to a negative control proving the check
   can fire.
3. **The vacuity/differ-check (B5) belongs in every registration's construction-gate
   list** — assert, at byte level, that the watched input streams actually DIFFER across
   the conditions the test discriminates.
4. Vocabulary: **UNTESTABLE ≠ NULL ≠ REFUTED.** The wrong verb here closes lines that
   deserve successors.

The deeper lesson fed the lean-protocol audit (`04-lean-audit.md`): three review layers
including a different-model arbiter and a human signature all missed what one mechanical
probe found immediately.
