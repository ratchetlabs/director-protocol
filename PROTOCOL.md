# PROTOCOL — Process Rules for Verdict-Bearing Work

> **Who this is for.** These rules codify a working discipline for LLM-directed empirical
> and research work so that ANY model running a session applies the same discipline. They
> are written as **triggers → required actions → artifacts**, not as virtues, because the
> failure mode they guard against is not ignorance but *not noticing in the moment*. If a
> trigger fires, the action is mandatory; "I judged it unnecessary" is not an exemption —
> the whole point of a pre-commitment is that in-the-moment judgment is the thing being
> distrusted.
>
> **Scope.** Rules bind on **verdict-bearing work**: anything that will produce a claim, a
> pass/fail, a design decision, or a doc another session will trust. Free reading,
> brainstorming, and note-taking are exempt — do not proceduralize exploration.
>
> **How each rule is written.** TRIGGER (when it fires) / RULE (what you must do) /
> ARTIFACT (what must exist afterward). Worked examples live in `case-studies/`.

---

## §G. THE LEAN CYCLE (the default shape — read this first)

Rules A–F below are the underlying laws. §G is how they compose into ONE default cycle
shape for every verdict-bearing experiment. (§G is the BACK half of a pipeline: the
question it certifies arrives from the adversarial front end — `RESEARCH.md` for the
exploration that maps the space, `DESIGN.md` for the design step that decides what to
build and freezes why. A cycle registered against an unchallenged design is rigor
applied to the wrong object.) It exists because a full process audit of the
source project (see `case-studies/04-lean-audit.md`) found that the layers that actually
caught defects were **mechanical checks** (fixtures, planted nulls, static conformance) and
**directed post-hoc adversarial review of surprising outcomes** — while redundant
pre-approval layers and status mirroring caught nothing the fixtures didn't, and the
heaviest process failed to prevent either of the two worst misses on record
(`case-studies/01` and `02`), both authored-and-approved through every ceremonial layer.
**Prefer fixtures over review steps; prefer one honest adversary over three charitable
ones.**

**The lean verdict-bearing cycle:**

1. **Pre-register + freeze (A1/A2/A4/A6, unchanged):** criterion, fresh data blocks,
   constants, estimand. Every registered decision bar carries **pre-computed false-fail
   probability AND power**; multi-family controls pre-declare per-family vs family-wise
   error control (`case-studies/02` and `03`). Hash-freeze every decision-bearing file and
   gate the scored run on a re-hash — automated, near-free, keep all of it.
2. **Construction fixtures (the PREFERRED home for every new lesson):** planted-null /
   vacuity checks (B5), extractor isolation, static fence/allowlist conformance,
   output-schema assertions (per-item records AND magnitudes, not aggregates), exhaustive
   verdict routing. A new failure mode becomes a **FIXTURE first**; a review step only if
   no fixture can express it.
3. **ONE independent adversarial check per registration — and ONE ROUND, period:** a
   different-model arbiter (C3) attacks the freeze candidate along directed attack lines
   (see `templates/C3-BRIEF.md`). The director then verifies the ruling against real code
   and data — **a ruling earns a check** — folds what survives, and moves on.
   **Arbitration ladders are retired:** no delta re-check after folding cures (post-fold
   verification is the director's own diff pass), no send-back rounds, no re-dispatch.
   Residual doubt routes IN-HOUSE — to the registrar seat (ORCHESTRATION.md §4) or the
   human — never to another arbiter round. The one-round law is per SLOT: a cycle has
   at most two arbiter slots — this registration check, and the post-run escalation of
   step 5 (which may add a second arbiter ONLY on first-arbiter-vs-director
   disagreement). There is no
   separate director pre-review + pre-freeze review + build review stack; those collapse
   into ONE director pass at build-complete.
4. **ONE user gate per cycle — and routine gates eventually self-clear:** the countersign
   authorizes build + freeze + scored run. There is no separate go/no-go — the
   freeze/re-hash machinery already guarantees nothing drifts between signature and run.
   The data blocks are thereby **consumed at the user's one signature; say so explicitly
   in the countersign item.** Expect this gate to evolve: once the human observes their
   per-cycle signature has become a rubber stamp and says so, the seat **self-clears**
   routine gates (dated stamp at the gate moment + disclosure in the next checkpoint
   briefing) and the human's attention moves up a level — to signing scopes and reviewing
   verdicts (ORCHESTRATION.md §5). Self-clearance is authorization bookkeeping, not
   verdict strength: a self-cleared gate carries every evidentiary duty the countersign
   carried. Named high-stakes gates (scored capstone runs, fresh-data draws) keep their
   teeth longest.
5. **Post-run: the director's forced-fresh-look (D4) only, by default.** ESCALATE to ONE
   arbiter (fresh-context adversarial pass or different-model, pick the one fitting the
   dispute) ONLY when the verdict is (i) disputed by the director, (ii) line-closing /
   terminal, or (iii) favorable AND load-bearing. Run a SECOND arbiter only if the first
   disagrees with the director. **Run solo (no different-model arbiter available):** a
   favorable AND load-bearing verdict remains **PROVISIONAL** — it carries an open C5 debt
   until a genuine different-model check runs, and must NOT be ratified as
   citable-without-qualifier. Same-model fresh-context review removes anchoring, not shared
   priors; it holds the verdict, it does not discharge the debt (ADAPTING, degrading
   gracefully).
6. **ONE chain-log doc per experiment line** (`BUILD-<line>.md`, see
   `templates/BUILD-LOG.md`) holds registration status, rulings, deviations, countersigns,
   and the run record. Registration docs freeze at countersign with a status POINTER to
   the chain log — no mirroring every stamp into multiple docs at decision time; handoff
   and memory update at checkpoint only.

**What lean does NOT relax:** A1/A2/A4/A6 pre-commitment; B1 verdict vocabulary; B4 dual
reporting; the C-header (same-model agreement ≠ confirmation); D3 lessons ratchet; C3 for
LINE-CLOSING conclusions (still mandatory before acting on any impossibility / terminal
STOP).

**Ratchet hygiene:** when a lesson is added, ask which existing review step is now
redundant with it and retire that step in the same edit. The ratchet may tighten checks
while thinning ceremony.

---

## §G+. Amendments from the scaling period

The lean cycle above is the v0.1 extraction. Running it for another two weeks — at
up to a dozen concurrent sessions across a hundred-plus registered arcs — added the rules
below. They are ordered by how often they fired. (The multi-session structure itself —
seats, inboxes, arcs, mechanical gates, the model-tier economy — is
[ORCHESTRATION.md](ORCHESTRATION.md).)

**Numbering legend:** "§G.1"–"§G.6" cite the lean cycle's numbered STEPS above;
"§G.8"+ cite the rule headings below. The numbering is sparse on purpose — it
preserves the source project's rule numbers so its records stay citable; nothing is
missing from this repo at the gaps.

### §G.8 Proportionality + collaborative pushback
- **RULE:** size the verification stack to the artifact's blast radius BEFORE running it,
  and state the sizing where the work is registered. Doc-only / reversible / no-fresh-data
  artifacts: ONE adversarial pass + ONE hash-freeze at signature-ready bytes. The full
  stack is reserved for data-consuming, frozen-interface, or line-closing work.
  Red-team output is **"here is the risk, and here is how we make your idea work"** —
  yes-with-fences, never a bare veto; ONE stated disagreement round, then execute the
  human's call without re-litigation. A requirement found blocking the goal gets "this
  requirement now blocks the goal; here is the amendment" in the same breath — stalling
  on an unamended requirement is goal abandonment, not discipline.
- **Cure gate (the anti-hardening rule):** before adopting any new check or cure, name
  the REAL need in one line — "what failure, observed or plausible HERE, does this
  prevent?" Hardening that models your own tools and teammates as attackers is
  disproportionate by default; when in doubt, the cheaper change wins, including "no
  change."

### §G.9 Arbiter economy — adjudication stays in-house
- **RULE:** verdict authority sits with the director and the human's gates — never with
  the arbiter model. A ruling is an independent-prior *instrument*, input to judgment.
  Before any non-mandatory dispatch, walk the in-house ladder: (1) the bytes — frozen
  docs, stamps, fixtures, grep; (2) the owner of the fact — read their log, ask them;
  (3) your own judgment — make the call, stamp it dated, own it; (4) the arbiter, only
  for genuine independence. At dispatch, one log line names: the question, why steps 1–3
  cannot answer it, and what independent prior the arbiter adds. If the middle clause
  cannot be filled honestly, do not dispatch. Dispatching to avoid making a call
  (approval-seeking, arbiter-as-cover) is as non-compliant as rubber-stamping a ruling.
- **The three-leg test for discretionary dispatches** — fire only when ALL hold: (1) it
  is a JUDGMENT, not a check (no byte/fixture/recompute settles it); (2) it is EXPENSIVE
  TO BE WRONG (consumes fresh data, freezes an interface others build on, closes a line,
  or licenses an external claim); (3) SHARED PRIORS are the specific risk (you authored
  it, the verdict favors you, or you conclude impossibility).
- **STRUCTURAL vs EDITORIAL, defined once:** a change is STRUCTURAL iff it changes what
  may PASS/FAIL, what is measured, what data is drawn, what is fenced, or what is
  claimed. Everything else is EDITORIAL and never re-triggers review, whatever a local
  fence says. The gatekeeping move is a one-line **semantic-diff claim** written before
  deciding: "this edit changes / does not change what the doc licenses, because …".

### §G.15 Goal-gain — activity is never gain
- **RULE:** before verdict-bearing work starts, state the expected gain toward the
  PROJECT goal as **information the project acquires** — skeptic-checkable later.
  "Exercises the harness" is the named anti-pattern. Thin gain is a design defect the
  seat fixes by redesigning the unit; and "if you can't say why it matters, don't do it
  and move on" — dropping low-gain work is compliant and complete. Work scopes open
  QUESTION-FIRST ("what is the highest-gain question this line can put to the project
  next?") — units are derived from the question, never enumerated from what the seat
  happens to be able to run.

### §G.16 Bytes before statements
- **RULE:** the truth bar inside the verdict machinery extends to ALL writing. Every
  factual claim is exactly one of: **VERIFIED** own-hands against committed bytes this
  session (file + line, hash, or commit — a verbatim quote is the proof of contact);
  **ASKED** — attributed to a named answer from the owner; or **LABELED** — marked as
  assumption/unverified in the output itself. Never a fourth state. Current-state claims
  ("we use X", "Y is live", "Z doesn't exist") are the highest-risk class: read the
  owning doc's literal tail, never infer from activity or memory; negative-existence
  claims additionally require a positive-control search (prove the search finds a thing
  you KNOW exists before trusting its empty result).
- **Counts name their derivation command (§G.16a):** any count in a verdict-adjacent
  stamp names the one-liner that reproduces it (`grep -c …`, `wc -l …`). No command
  nameable → label the count UNVERIFIED.

### §G.24 A review names the judgment it re-derived
- **RULE:** a pass counts as a REVIEW only if its output names the specific judgment(s)
  it re-derived and SHOWS the re-derivation (the recomputed number, the attempted
  counter-construction, the premise it tried to break). A pass that only attests
  conformance (hashes match, fixtures green) is an **ACK** and must be labeled as one.

### §G.25 Stamps carry a grade; rulings mark what binds
- **RULE:** every verification stamp carries ONE grade: **REVIEWED** (judgment re-derived, shown) ·
  **TESTED** (ran the artifact own-hands without re-deriving a judgment) · **ACKED**
  (read-and-agree). An ungraded stamp reads as ACKED. Rulings additionally mark what
  **binds** — the holding successors must honor — versus commentary, which stays freely
  re-litigable.

### §G.21 Orphan-step census at every close
- **RULE:** every cycle/arc close lists every follow-on step the work surfaced that no
  registered unit owns; each gets exactly ONE disposition: (a) execute it in-cycle (the
  strong default — finishing small related tasks is a success needing disclosure, not
  approval); (b) route to a named owner with a named trigger; (c) kill explicitly with a
  dated reason. "Mentioned in the close prose" is a non-state. Mechanical test: grep your
  own close for "future"/"deferred"/"not done here" — every hit has a disposition line or
  the close is not done.

### §G.26 Critical-path register — UNOWNED links are reported first
- **RULE:** when presenting any path to a capability spanning more than one unit of
  work, classify EVERY dependency: **BUILT** (name the artifact) · **OWNED** (name the
  seat AND the queued work that ripens it) · **UNOWNED** (no ripening mechanism
  anywhere). An "X → Y → Z" chain is not licensed prose while a link is UNOWNED —
  report the UNOWNED link first and route it the same session. "Ripens naturally,"
  "sequenced behind," and "future work" are not states.

### §G.27 Every checkpoint carries a risk section
- **RULE:** every checkpoint briefing carries "RISKS TO PROJECT" unconditionally —
  "NONE identified" is legal but must be written. A named risk is never briefing-only:
  before the checkpoint completes, the seat has either cured it (if trivially in-scope)
  or routed it to the correct owner, and the briefing reports the *disposition*, never a
  bare worry.

### §G.23 Rule-supersession — the rulebook must trend down
- **RULE:** the active instruction set gets a periodic stewardship sweep testing every
  rule against three retirement conditions: (a) condition-gone, (b) better-method (a
  fixture or tool now enforces it), (c) never-fires. Candidates are SUPERSEDED — compact
  pointer stays, full text archives with a dated reason — never silently deleted.
  **Net active rule mass trends DOWN while coverage holds; a growing rulebook is a
  finding.** The mature form is a rule-card register: each card is the binding rule;
  origin stories and worked examples live in an archive doc the cards point to.

---

## A. Pre-commitment and freezes

### A1. Pre-register before the first scored run
- **TRIGGER:** any experiment that will produce a verdict.
- **RULE:** before the first scored run, write and freeze: operational definitions, a
  per-condition prediction table, decision rules (thresholds, bars — each with
  pre-computed false-fail and power, see B2), and the data blocks. Constants marked
  `(proposed)` may be tuned ONLY to satisfy the environment's own construction checks —
  **never against any experimental arm's performance** — and freeze the moment the first
  scored run starts. Predictions are **never edited post-hoc**; misses are logged honestly
  against the frozen table.
- **ARTIFACT:** a registration doc with a freeze declaration (`templates/REGISTRATION.md`).

### A2. Hash-register frozen sources; gate the scored run on the hashes
- **TRIGGER:** a freeze declaration exists and code files implement it.
- **RULE:** list every decision-bearing file with its content hash in the freeze. The
  scored harness re-hashes at run time, records the match in the results file's metadata,
  and refuses to run on mismatch. A **decision-bearing file** is any file whose content
  can change a verdict — this EXPLICITLY includes the scored harness that applies the
  router/bar, not only the statistic-producing code; the fence/allowlist definitions; and
  any fixed inputs the verdict reads. If in doubt whether a file can move a verdict, it is
  decision-bearing and goes in the manifest. Any content hash is acceptable, but **the
  freeze manifest and the harness re-hash must use the SAME algorithm** (the templates use
  md5).
- **ARTIFACT:** hash table in the registration; `frozen_source_hash` metadata in results.

### A3. Deviation log — never silently resolve an ambiguity in code
- **TRIGGER:** implementation surfaces an ambiguity (pre-freeze), or anything changes
  after the freeze (post-freeze).
- **RULE:** pre-freeze ambiguities become numbered, ratified items in the registration —
  each stating exactly which frozen sections it touches. Post-freeze changes become
  append-only deviation entries (date, what, why, which prediction/decision cells
  affected). A post-freeze deviation is NEVER fixed by editing the frozen experiment — it
  becomes the mandate for a **new** registration with **new data blocks and new verdict
  symbols** (a primed successor, not a retrofit).
- **ARTIFACT:** numbered ambiguity items + append-only DEV entries in the chain log.

### A4. Data discipline — named, disjoint, never-before-observed blocks
- **TRIGGER:** any stochastic run whose result will be scored.
- **RULE:** every phase (shakedown, calibration, null, scored) gets its own named data /
  seed block, mutually disjoint, declared before the run; the scored block must never have
  been observed in any prior run. Fresh nulls get deliberately fresh blocks so a fix
  cannot be backfit to them. State explicitly which act consumes each block (under §G,
  the user's one countersign).
- **ARTIFACT:** block table in the registration.

**Boundary with A2:** a fixed, already-observed dataset that a DETERMINISTIC claim is
*about* is an A2 pinned input (hash it into the freeze manifest), not an A4 block; A4
governs never-before-observed draws feeding scored estimates. When a claim mixes both,
the stochastic part draws fresh blocks and the fixed part gets pinned.

### A5. Pre-commit downstream decisions to verdicts (make the pick mechanical)
- **TRIGGER:** an experiment's outcome will drive a later design choice.
- **RULE:** before the run, map **every possible verdict** to exactly one named
  downstream option, so the pick is mechanical rather than post-run judgment.
- **ARTIFACT:** a verdict→disposition table in the registration.

### A6. Construction-check firewall (the retune rule)
- **TRIGGER:** a constant needs tuning during implementation.
- **RULE:** tuning is legal only against a **construction check** (a property of the world
  or the instrument, not of any arm's score). Any retune re-runs the FULL construction
  gate — no partial re-check — and is logged as an ambiguity item. Inherited constants are
  re-adopted by copy (hash-pinned) and re-verified, never carried informally from an old
  freeze.

---

## B. Verdicts and reporting honesty

### B1. Controlled verdict vocabulary — untestable ≠ null ≠ refuted ≠ fail-at-bar
- **TRIGGER:** writing up any experimental outcome.
- **RULE:** use the fixed verbs and nothing looser:
  - **HOLDS** — the falsifier didn't fire.
  - **NULL** — fired-where-it-might-have failed to fire; distinguish a **WEAK NULL**
    caused by an estimator artifact from a clean refutation.
  - **VACUOUS** — the test never existed in the data.
  - **UNTESTABLE-BY-CONSTRUCTION** — a precondition or gate failed; an honest non-result,
    distinct from a null (`case-studies/01`).
  - **FAIL-AT-REGISTERED-BAR (defect class named)** — the run failed a bar that was
    itself mis-constructed; not a refutation of the subject (`case-studies/02`).
  - **HALF-CONFIRMED / HALF-UNTESTED** — for split conjunctions.
  - **RESIDUAL** — leftovers owed to future work.
  Compound claims use separate booleans per capability, never conflated — conflation makes
  the underlying question unfalsifiable. Every verdict write-up states **what it licenses
  and what it does NOT license.**

### B2. Calibrated bars — false-fail and power, computed before the run
- **TRIGGER:** registering any empirical decision rule (a count-over-R, a
  threshold-over-N, a majority bar), or any method that could succeed "by luck."
- **RULE:** the registration must state (a) the bar's computed **false-fail probability**
  under the null it claims to control *(false-fail: the probability the bar returns FAIL
  by sampling luck alone, under the declared null — a worked bar with both numbers is in
  `case-studies/03`)*, and (b) its **power** against a named alternative — the
  probability the bar fires when a real effect/defect of the named size is present.
  A bar sitting at the null expectation is a coin flip, not a criterion. When the bar
  spans multiple families, the **leg-level** error (across all sub-bars) is what must be
  controlled — pre-declare per-family vs family-wise and write the sub-bars out
  (`case-studies/02`). Where luck is possible, measure the empirical chance rate with a
  matched null run through the SAME downstream machinery.
- **DETERMINISTIC / LOGICAL claims are the exception:** for a claim about code
  correctness, an invariant, or a proof — where the answer is not stochastic — the
  statistical bar is replaced by **exhaustive and boundary-case fixtures** (every case, or
  every equivalence class plus its edges). False-fail probability, power, and data-block
  consumption are then N/A, and the registration must **say so explicitly** rather than
  leave the B2 cells blank: state "deterministic claim — no statistical bar; verified by
  exhaustive/boundary fixtures §<n>" so a reader sees the omission was reasoned, not
  forgotten.

### B3. Two-sided checks — prove the effect AND the counterfactual
- **TRIGGER:** a construction claims "X costs Y" or "X causes Y".
- **RULE:** verify both sides: the manipulated condition FAILS (effect present) and the
  matched counterfactual MEETS (effect absent when the cause is absent). One-sided checks
  pass for the wrong reason. Corollary: write the one-line accounting identity for any
  bound FIRST — algebra before prescription.

### B4. Dual reporting — a superseded bar must never look "met"
- **TRIGGER:** a criterion is re-anchored or weakened after ratification.
- **RULE:** every artifact forever reports the OLD anchor's (failing) result beside the
  new one. Report diagnostic readings beside binding ones as fragility flags; serialize
  non-routed reference statistics so the road not taken stays on the record.

### B5. Vacuity check at shakedown
- **TRIGGER:** before any scored run, for every arm / detector / control.
- **RULE:** verify the arm's watched input stream actually DIFFERS across the conditions
  it is meant to discriminate — traced to the channels the instrument **consumes**, not
  the surface the arm manipulates. Byte-identical consumed streams = a vacuous test you
  will only discover after burning the freeze (`case-studies/01`). Every statistical
  instrument additionally gets a **planted-true-null probe** as a construction fixture:
  feed it input that is null BY CONSTRUCTION; it must return zero detections.

### B6. Evidence-channel rule — primary sources for verdict-bearing claims
- **TRIGGER:** a claim a verdict rests on, or ANY absence claim ("the source never says
  X"), sourced from an extraction / summary pass.
- **RULE:** verify against the primary source directly and record the evidence channel.
  Paraphrase chains are fine for orientation, never for verdicts.

---

## C. Anti-single-model bias

**The standing fact:** every fresh-context subagent you spawn is the same base model as
you. Fresh context removes conversational contamination, **not shared priors**. Same-model
agreement is weak evidence; structure must supply the independence the model can't.

### C1. Blind review by redaction
- **TRIGGER:** comparing designs/rivals, or scoring anything where knowing the author's
  hypothesis would contaminate the judge.
- **RULE:** judges are fresh-context agents given a neutral scenario suite + a scrubbed
  packet (author predictions and "our build" comparisons redacted; halo-bearing claims
  rewritten to plain design claims). Fixed canonical order for every judge. Silence scores
  UNSPECIFIED — inventing mechanisms on the author's behalf is the judge's named failure
  mode. Author predictions re-enter only at synthesis, as a separate column.

### C2. Adversarial second pass on every favorable verdict
- **TRIGGER:** any judge/reviewer pass produced verdicts (especially favorable ones) that
  §G escalation criteria reach (disputed / line-closing / favorable-and-load-bearing).
- **RULE:** a second fresh agent gets the same packet + the first pass's output, with the
  explicit job of ATTACKING the most favorable verdicts and any verdict resting on
  mechanisms the source doesn't license. Assume your first pass was charitable — in the
  source project's record, the charitable-judge failure mode appeared in every first pass
  ever audited.

### C3. Different-model adjudication for pass-criterion changes AND line-closing conclusions
- **TRIGGER:** an amendment changes a PASS CRITERION (not merely an instrument); a dispute
  needs an arbiter and same-model bias matters; **OR you have reached a NEGATIVE /
  IMPOSSIBILITY conclusion that would CLOSE a line of work** — an "exhaustion" proof, a
  "no X can satisfy Y" claim, a terminal STOP, a wrong-problem pivot. A negative-existence
  verdict derived from a handful of failed constructions is a HYPOTHESIS, not a result; it
  is at exactly these moments that a director's confidence is most dangerous, because it
  abandons work.
- **RULE:** send it to a **different model family** for adversarial adjudication BEFORE
  executing, with an exhibits package, and file the ruling. For a line-closing conclusion,
  task the arbiter to REFUTE it (produce the construction you claim can't exist); one
  cheap arbiter call is trivial against abandoning a satisfiable design. Instrument-only
  changes are exempt. Pre-commit a hard stop on amendment chains.
- **THE RULING EARNS A CHECK — it does not end the matter.** A different-model verdict is
  information, not an oracle: verify it against primary artifacts (real code, real data,
  the frozen text) whether it AGREES with you or REFUTES you. An unverified ruling is just
  a more expensive rubber stamp — the arbiter can be confidently wrong, and can even share
  the miss (in `case-studies/02`, the defective bar was the arbiter's own correction).
  Cross-model *disagreement* is the signal worth most — do not explain it away.

### C4. Forcing checks — independent re-derivation, function-matched
- **TRIGGER:** you believe a design is "forced by the demands" (vs. merely the path you
  happened to take).
- **RULE:** give several fresh agents ONLY the goal + scenarios (all project vocabulary
  scrubbed — keep a scrub log), vary framing but never content, and have SEPARATE blind
  judges score each design against a functional-match table (match by function, not
  vocabulary). Gate on a pre-declared threshold. Same-model newcomers are correlated
  draws — the result carries a same-model scope qualifier until a different family
  replicates it.

### C5. Same-model caveat + dormant replication debt with named tripwires
- **TRIGGER:** any same-model convergence result gets used or upgraded.
- **RULE:** record the caveat in the doc itself. The different-model replication debt is
  DORMANT, not owed — until a named tripwire fires (external citation; using the claim to
  decline a rival design; publication-grade language; a build commitment). List the
  tripwires next to the claim. A same-lineage rerun does NOT discharge the debt.

### C6. Red-team pass on every significant decision
- **TRIGGER:** any strategic/architectural decision, including additions to a
  registration.
- **RULE:** voice the named positions (the skeptic, the rival approach, the won't-scale
  worry, the wrong-problem worry, the RIGGING worry — in both directions: could this fix
  hand us a positive? a negative?), steelman each, then give a director verdict with an
  explicit disposition ("ACCEPTED with [named guards] binding"). Mark it "Red-team:" in
  the doc so the decision visibly survived a challenge. Kill-first for new abstractions:
  steelman every reduction to something already present; a candidate earns a seat only by
  forcing a demand nothing existing produces. See DIRECTOR.md.

---

## D. Second-look passes (error catching)

### D1. Load-bearing audit when a claim's strength changes
- **TRIGGER:** a result upgrades/downgrades a claim that other docs cite.
- **RULE:** enumerate EVERY citation site (docs, status lines, memory), confirm each
  carries the required scope qualifier, and state explicitly what does and does not
  structurally rest on the claim.

### D2. Re-run settled verdicts as honesty controls
- **TRIGGER:** the environment changes under an experiment whose earlier verdicts are
  treated as settled.
- **RULE:** re-run the settled arms as controls in the new environment. If a control
  fires, HALT and retune (logged as a deviation) — the change reopened what you thought
  was closed.

### D3. The lessons ratchet
- **TRIGGER:** ANY correction — by the user, by an adjudicator, or by your own second
  look.
- **RULE:** append to the lessons file (newest first) in the fixed shape Context / What
  happened / Fix / **Rules** — where Rules is a generalized trigger-shaped rule that would
  have prevented the mistake, not a description of the fix. If the rule is process-level,
  also add it to THIS document. Then apply ratchet hygiene (§G): a new failure mode
  becomes a FIXTURE first, and adding a lesson should retire whatever review step it makes
  redundant.

### D4. Second look before "done" — the forced-fresh-look protocol
- **TRIGGER:** about to mark verdict-bearing work complete, or about to assert a result.
- **WHY THE OBVIOUS VERSION FAILS:** re-reading your own work in the same context is
  anchored — the reasoning that produced an error is in context, and agreeing with it is
  cheaper than re-deriving it. Errors survive re-reading almost perfectly. Every step
  below converts "review this" into a question you weren't already anchored on. Do the
  steps mechanically; do not substitute a general "looks right" pass.
- **RULE — run these in order:**
  1. **Re-derive, don't re-read.** For each load-bearing number/claim, compute it a
     SECOND way (an identity that must sum; recompute a summary from the raw records —
     never from leg-level summaries).
  2. **Predict-then-check.** BEFORE opening any result (test output, JSON, grep), write
     the expected value and what would be suspicious. Surprise is the only reliable
     in-context error signal, and it exists only if the prediction came first. For scored
     runs, register the predictions in the chain log BEFORE the output file exists
     (CHECKLISTS.md §6).
  3. **Pointed questions** (answer each, don't skim):
     - Is every number in my prose present in, or derivable from, the artifact I cite?
     - Does this test's input actually differ across the conditions it discriminates?
     - Any ABSENCE claim — verified against the primary source, or a paraphrase?
     - Is the verdict verb right — could this "null" be "untestable"? this "fail" a
       "fail-at-bar"? this "holds" "vacuous"?
     - If the result had come out the OTHER way, would I have scrutinized it this hard?
  4. **Assume it's wrong; name the mechanism.** "Suppose this result is wrong — what
     mechanism would produce this exact output anyway?" Then check that mechanism.
     Generating failure hypotheses is not anchored the way evaluating correctness is.
  5. **Escalate per §G.5** when the verdict is disputed, line-closing, or favorable and
     load-bearing: one arbiter, given ONLY the artifacts — never the transcript; the
     transcript carries the anchoring.
- **SCOPE LIMIT (honest):** this protocol catches SLIPS (wrong numbers, vacuous tests,
  wrong verbs, unverified absences). It does NOT reliably catch FRAMING errors — a frame
  error lives in the premises the self-reviewer inherits and falls only to an external
  party holding a different frame. Frames need C2/C3; do not let D4 substitute for them.

---

## E. Documentation-as-state

### E1. Docs are the state
- **TRIGGER:** always.
- **RULE:** the design docs ARE the project state. Fix stale documentation (broken
  pointers, completed "next steps", outdated status lines) on sight. Keep spec status
  lines current when work lands.

### E2. Checkpoint discipline
- **TRIGGER:** the user asks for a checkpoint, or a session ends after substantive work.
- **RULE:** run the checkpoint routine (`claude/commands/save.md`): reconcile specs,
  overwrite the living handoff doc (`templates/HANDOFF.md`), refresh project memory,
  print a restart briefing.

### E3. Decisions land in docs, not in chat
- **TRIGGER:** a decision is made mid-session (ratification, verdict, pick).
- **RULE:** it isn't made until it's written into the governing doc. Under §G the chain
  log IS that doc — one write at decision time, mirrors at checkpoint only.

---

## F. Model economy — what to escalate

The director model executes everything above; the rules are designed so discipline comes
from structure, not from the model's spontaneous judgment. Reserve **escalation** (a
stronger session, or a different-model arbiter) for the few places where judgment itself
is the product:

1. **Pass-criterion adjudication** (C3) — mandatory different-model.
2. **The one registration check** (§G.3) — the arbiter's directed attack on the draft.
3. **Different-model replication when a C5 tripwire fires.**
4. **Phase-boundary design reviews** — before committing to a build phase, not during.
5. **Line-closing / impossibility conclusions** (C3) — a different-model attempt to
   REFUTE the conclusion BEFORE acting on it; escalate the *judgment*, keep the *labor*
   (verifying the arbiter's answer) on the default model.
6. NOT for: routine implementation, doc sync, running pre-registered experiments,
   first-pass reviews. The line is judgment-vs-labor: escalate where being wrong is
   expensive and same-model priors might capture you; never escalate something you can
   just check yourself.

Delegate all delegable **execution** (builds, harvests, drafting, paper reading) to
cheaper executor agents; the director writes the brief and verifies the product. When
escalating, prepare an **exhibits package**: the question, the frozen text, the evidence,
the proposed change — so the expensive call spends tokens judging, not reconstructing
context.

---

## Session-start check (10 seconds)

Am I doing verdict-bearing work this session? If yes: is there a governing registration or
spec, and is it frozen? Which experiment line does THIS session own (CHECKLISTS.md §1)?
Am I about to tune anything (→ A6)? Will anything I produce be scored (→ A1/A4/B2)? Am I
judging my own or a same-model output favorably (→ C2)?

## Red flags — stop and check the rules if you catch yourself…

- editing a prediction, threshold, or verdict symbol after seeing results (→ A3, the
  freeze attack)
- tuning a constant because an arm scored badly (→ A6)
- registering a bar without computing its false-fail probability and power (→ B2)
- reporting "null" for something that was never actually testable (→ B1)
- choosing an estimand after the data has revealed which choice passes (→ B2,
  `case-studies/03`)
- taking a fresh subagent's agreement as independent confirmation (→ C header)
- summarizing a favorable, load-bearing review pass without an adversarial second pass
  (→ C2 / §G.5)
- declaring something impossible / exhausted / a terminal STOP and acting on it without a
  different-model attempt to refute it first (→ C3)
- accepting a different-model ruling — even one that refutes you — without verifying it
  against the real code/data (→ C3, "the ruling earns a check")
- treating a check that passed a PROXY (geometry, a precondition, a subset) as proof the
  full pipeline works (→ B5; run the same code path the scored run will run)
- resolving an ambiguity "the obvious way" in code without logging it (→ A3)
- marking done without the forced fresh look (→ D4)
- making a decision in conversation that no doc records (→ E3)
- adding a review step where a fixture would do (→ §G.2)
