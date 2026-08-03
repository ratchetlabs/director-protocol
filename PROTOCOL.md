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
   vacuity checks (the watched input stream must actually DIFFER across the conditions
   it discriminates), **two-sided construction** (the manipulated world FAILS **and**
   the matched counterfactual MEETS — one-sided checks pass for the wrong reason),
   extractor isolation, static fence/allowlist conformance, output-schema assertions
   (per-item records AND magnitudes, not aggregates), exhaustive verdict routing.
   A new failure mode becomes a **FIXTURE first**; a review step only if no fixture can
   express it. *(The former B3/B5 rules live HERE now — folded, not weakened.)*
   **Mutation-battery floor:** any battery that edits source in a tight loop runs the
   interpreter with bytecode caching disabled and caches cleared (same-second same-size
   mutants can reuse stale bytecode), and every NEW fail-closed duty gets its mutation
   arm at the moment it is written.
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
- **The register diet — this rule proved out at scale (2026-08-03, source project):**
  one sitting cut the live register **−20.3%** in two moves. (1) **Law-only rewrite:**
  provenance parentheticals, worked-instance retellings, and rationale essays deleted
  in place under a deletion-only bar — version history is the archive; a card keeps
  only its operative clauses. Measured surprise: provenance was ~18% of card mass,
  not the estimated 60–70% — the rest was live law, so (2) further shrink came from
  **retirement, not compression**: thirteen legacy rules retired in ONE human-ratified
  batch. That batch is why this file's A5, B3, B5, B6, C1, C4, C6, D2, E, and the F
  ladder are gone (numbering keeps its gaps — never renumber): B3/B5 folded into cycle
  step 2's fixture list, B6 into §G.16, C6's red-team into `DESIGN.md`, D2 retired
  outright (the honesty-control PATTERN survives as fixture practice), E folded per
  its stub, F reduced to the seat rule. Two rules were promoted out of the legacy
  sections into first-class cards instead of dying — retirement sweeps also surface
  what deserves promotion.

---

## §G++. Maturity amendments (source-state 2026-07-21 → 2026-08-03)

The scaling period's amendments (§G+) were about verdict economy. This second wave is
about **seat mechanics at sustained scale** — what a lab of parallel seats needs so
that idle time, waits, context budgets, and cross-seat dependencies are governed by
grammar rather than vigilance.

### §G.29 No bare waits — a wait is EARNED, and every stop is labeled
- A bare "waiting on X" is never a legal seat state. Before ANY wait, descend the
  ladder: **tier 0** own signed work → **1** interface audit on surfaces you share →
  **2** demand walk (a TOOL RUN over the lab's live state — see `tools/` pulse
  pattern — every line naming your seat gets an explicit opened-and-disposed line)
  → **3** cross-project clearinghouse sweep → **4** wayfinding/primer drafting →
  **5** written closure: "ladder walked, tiers 1–4 one line each" + an ACTIONS TAKEN
  line (or explicitly "actions: NONE").
- **Every turn end is a held-unit check.** Ending a stroke while holding a unit whose
  inputs are in hand IS a wait entry. The closing line states exactly ONE, verbatim
  enum so tooling can parse it: `STOP-LABEL: CONTINUE | ARMED-WAIT |
  CHECKPOINT-HOLDS-UNIT(<reason>) | HANDOFF(<queue>)`.
- **Dead-man wake:** detection alone cannot actuate — a stalled lab is SILENT. A
  `CHECKPOINT-HOLDS-UNIT` stop accepts only two reasons (checkpoint-now, or a NAMED
  human gate), and the named-gate form ARMS a one-shot timer before stopping; on wake
  the held-unit check re-runs. A held stop with neither wake nor exemption is a stall
  by construction.
- **Pre-wait push-assertion (research-line seats):** before any wait, assert (a)
  nothing remains that could push the line — no arc to open, no note owed; (b) you
  are NOT waiting on the human — where a human question existed, take your
  recommended path, record it, raise it at the next checkpoint (a queue, never a
  block).

### §G.30 Model profile — discipline never scales with the model
- A seat's laws bind identically on every model tier. Running a cheaper model, ADD
  vigilance (self-caught errors are reported by name at checkpoint), never subtract
  duties. Companion to the F stub and ORCHESTRATION.md §6.

### §G.31 Seat instantiation is human-only
- No seat launches, proposes launching, or builds launch machinery for another seat.
  ONE narrow exception, held by the scheduler seat alone (ORCHESTRATION.md §1a).

### §G.32 An indicting check earns a second, differently-built check
- When a check INDICTS prior work, do not act on one instrument's word: build a
  second check on a DIFFERENT mechanism before executing the indictment. Symmetric
  honesty: the same skepticism you give favorable results, given to damning ones.

### §G.33 / §G.42 Seal and coverage claims bind their whole surface
- "sealed / clean / all-green" binds the WHOLE tracked surface, not the part you
  looked at; any scan result carries what it did NOT sweep, declared by the
  instrument itself. Silent truncation reads as "covered everything" — the class of
  miss these two cards exist to kill.

### §G.35 / §G.35a Rulings and commit subjects are evidence
- Every arbiter ruling's raw output is a COMMITTED artifact under the arc it ruled.
- A commit subject naming a stamp IS a stamp claim (subjects are read as state by
  every later reader) — and subjects cap at **≤120 chars**: the stamp's text lives in
  the chain log, never the subject line. Long subjects re-inflate every future
  init read that walks the log.

### §G.36 The hand-authored register (prime-directive lens)
- Every hand-authored constant, menu, or per-case fact in machinery is a LABELED
  example for a general mechanism, or it is a violation shape. Closed menus are the
  named failure. This is the generalization test applied to your own apparatus.

### §G.37 Fence claims are behavioral
- A claimed fence ("tool X can't touch Y") is verified by BEHAVIOR — a probe that
  tries — never by reading configuration. Config describes intent; the probe
  measures the fence.

### §G.39 Pinning append-managed docs
- A hash pin on a doc that legitimately grows binds a LINE-PREFIX (first N lines +
  their hash), never the whole file — otherwise every lawful append breaks the pin
  and truth-decays into "expected failures."

### §G.40 Tiered close gates + the self-serve checker
- Gate requests carry tiers (blocking vs advisory); the checker RUNS before the gate
  is requested — a gate opened on unchecked work spends the gatekeeper's attention
  on what a script catches. Gate legs prove their own derivations before indicting
  (§G.13h kin); "exit nonzero" and "no judgment formed" are DIFFERENT verdicts and
  the report says which.

### §G.43 "Unseen" is a fenced claim
- Any transfer/hold-out claim names its fence: what the system could NOT have
  observed, enforced by construction (leave-one-out drops, served-only construction)
  — never "it wasn't in the store," which is a grain error.

### §G.44 Staged contact — cheap probes first, certification is not progress
- First fire of any new/amended surface: answer-side check at unit open · no maiden
  flight on unspent material · probe-loop as the default iteration mode,
  seat-autonomous (asking permission to run a cheap probe is itself the violation) ·
  a delivery witness on anything handed across seats. Apparatus checks alone never
  satisfy — at least one probe is answer-side/behavioral.

### §G.45 / §G.46 Registration-time honesty for serving units
- A unit registered to SERVE pairs its serving mode with a live witness at
  registration, and its CHANNEL is registered too. Event-triggers gate SPEND, never
  BUILD — build what you can verify now; spend (data, fresh material, external calls)
  waits on the trigger.

### §G.47 The reconciled answer
- Before ANY recommendation/options answer leaves the seat: one step-back row — does
  the answer actually reconcile with everything this seat already knows? The cheap
  cure for locally-correct globally-wrong replies.

### §G.48 Dependency asks are act-grade
- Routing a cross-seat dependency is an ACT, not an fyi: it names what is owed, lands
  in the owing seat's queue, and dual-routes to the scheduler when the owing seat is
  a dispatched lane. Entering a dependency wait without the routed ask is a bare wait
  (§G.29).

### §G.49 / §G.50 Composition and power constants
- At every registration boundary: REUSE-OR-FORK against the signed component
  manifest — a `composes:` block naming what is reused; forks earn their existence.
- A power constant ("bar met at N") is STAGE-SCOPED: cite it only at the stage whose
  false-fail arithmetic produced it.

### The init diet — context cost is a governed budget
- The rule register is read as **INDEX + anchors + DELTA, never in full**: init reads
  the one-line card index (a DOORBELL, never the door), 2–3 always-read cards in
  full, and every card changed since the seat's recorded `register-read: <commit>`
  pointer. Every other card is read IN FULL the moment its trigger fires.
- Card extraction is a TOOL (`exact card bytes by section name`), not ad-hoc
  text-slicing — overshoot reads double the cost silently.
- Seat memory outside the repo obeys the same law as the rulebook: an INDEX of
  one-line hooks, files pruned to standing human rulings + current-work context —
  everything derivable from the repo or duplicating the charter is deleted, not
  summarized. (Measured at the source project: memory 73→22 files, register −20.3%,
  CORE handoff rows hard-capped — the floor that remains is the harness itself.)

---


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

### B4. Dual reporting — a superseded bar must never look "met"
- **TRIGGER:** a criterion is re-anchored or weakened after ratification.
- **RULE:** every artifact forever reports the OLD anchor's (failing) result beside the
  new one. Report diagnostic readings beside binding ones as fragility flags; serialize
  non-routed reference statistics so the road not taken stays on the record.

## C. Anti-single-model bias

**The standing fact:** every fresh-context subagent you spawn is the same base model as
you. Fresh context removes conversational contamination, **not shared priors**. Same-model
agreement is weak evidence; structure must supply the independence the model can't.

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

### C5. Same-model caveat + dormant replication debt with named tripwires
- **TRIGGER:** any same-model convergence result gets used or upgraded.
- **RULE:** record the caveat in the doc itself. The different-model replication debt is
  DORMANT, not owed — until a named tripwire fires (external citation; using the claim to
  decline a rival design; publication-grade language; a build commitment). List the
  tripwires next to the claim. A same-lineage rerun does NOT discharge the debt.

## D. Second-look passes (error catching)

### D1. Load-bearing audit when a claim's strength changes
- **TRIGGER:** a result upgrades/downgrades a claim that other docs cite.
- **RULE:** enumerate EVERY citation site (docs, status lines, memory), confirm each
  carries the required scope qualifier, and state explicitly what does and does not
  structurally rest on the claim.

### D3. The lessons ratchet
- **TRIGGER:** ANY correction — by the user, by an adjudicator, or by your own second
  look.
- **RULE:** append to the lessons file (newest first) in the fixed shape Context / What
  happened / Fix / **Rules** — where Rules is a generalized trigger-shaped rule that would
  have prevented the mistake, not a description of the fix. If the rule is process-level,
  also add it to THIS document. Then apply ratchet hygiene (§G): a new failure mode
  becomes a FIXTURE first, and adding a lesson should retire whatever review step it makes
  redundant.
- **At scale, SHARD:** one router file + a per-seat shard (`lessons/<seat>.md`). Each
  shard opens with a DISTILLED section — one RULE line per entry, the only part read
  at init; the full entry is opened the moment its family fires (same doorbell law as
  the card index). A correction writes the full entry + its distilled line in the
  same commit, and the seat's layer records `lessons-read: <commit>` so successors
  read only what's new.

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

## E. (retired at maturity — folded)

Documentation-as-state earned graduation into the working laws themselves: docs-are-
the-state and checkpoint discipline live in §G cycle step 6 and ORCHESTRATION.md §2;
decisions-land-in-docs is §G.16's bytes-before-statements applied to decisions. The
E-section ceremony rows added nothing the folds don't.

## F. Seat rule (the stub that survived)

The escalation ladder is retired — arbiter economy lives in §G.9 and the tier economy
in ORCHESTRATION.md §6. What survives is one invariant: **model identity never scales
discipline.** A seat holds its FULL duties whatever model runs it — red-team passes,
forced fresh looks, push-back. A cheaper model changes the error rate you watch for,
never the laws that bind the seat (§G++ model profile).

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
