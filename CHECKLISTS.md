# CHECKLISTS — The Director's Judgment Moves, Made Mechanical

> **Why this file exists.** The discipline in PROTOCOL.md was developed by a strong
> director model whose judgment moves were largely implicit. A director running on a
> smaller model — or any director under time pressure — compensates with **explicit
> checklists, not more review layers.** Every checklist below was observed, as an implicit
> move, in real verdict-bearing cycles; each has a real defect it caught or would have
> caught. Run the matching checklist at the matching moment. Each ends with a **DO NOT
> PROCEED UNTIL** gate — treat it literally.
>
> When in doubt, run the checklist. When a genuine judgment call remains after the
> checklist, escalate it to the user as a framed decision — do not improvise.

---

## 1. SESSION START

Before any verdict-bearing act in a session:

1. Read the governing protocol section (PROTOCOL.md §G) — not from memory, from the file.
2. Read the **tail of the chain log** (`BUILD-<line>.md`) for the line you think you're
   working on: last countersign, last deviation, current "NEXT" pointer.
3. Identify which experiment line / thread THIS session owns. If the project runs parallel
   sessions or agents, check file mtimes / `git log --since` for activity by another
   session since the chain log's last entry. **Never touch another thread's line** — its
   chain log, its data blocks, its frozen files.
4. Confirm the "NEXT" pointer is actually runnable: enumerate the next step's inputs from
   its registered definition and check each exists (an unbuilt prerequisite means NEXT =
   build, not run).
5. Check the data-block ledger: which blocks are consumed, which are free, which are
   consumed-but-untouchable.

**DO NOT PROCEED UNTIL** you can state, in one sentence each: the line this session owns,
its current cycle stage, and the one next action the chain log licenses.

---

## 2. REGISTRATION REVIEW (before spending the arbiter)

The arbiter check (§G.3) is one per registration — don't waste it on defects you can catch
mechanically. Before briefing the arbiter, the director independently:

1. **Recomputes EVERY registered number with your own code** — bar constants, false-fail
   probabilities, power values, sub-bar thresholds, rejected-alternative rates. Write a
   few lines of scratch code; do not re-read the draft's arithmetic. (In the source
   record: the director reproduced a draft's four bar constants to 4+ decimals AND the
   rejected alternative's rates before the arbiter saw it — so the arbiter's attack budget
   went to the estimand, where the live hazard actually was.)
2. **Verifies every code-line citation by opening the file.** If the draft says "the
   instrument reads per-family booleans at lines L1–L2," open the file and read those
   lines. If it says "the fence excludes block B," read the actual allowlist.
3. **Verifies every fence/allowlist claim by reading the actual list** — by inspection,
   never by running. Every registered data block × every layer's allowlist (generator,
   harness, driver): is each registered block admitted by EVERY layer? Are never-run
   blocks absent from every runnable allowlist? A missing allowlist entry found at
   registration is a named build deliverable; found mid-run it is a deviation.
4. **Confirms the estimand is argued from what downstream consumes** — never from what
   passes on already-seen data. If the registration follows a failed run, the
   criterion-shopping hazard is LIVE: the draft must disclose numerically which choices
   would pass/fail on the consumed data, argue the choice only from registered downstream
   consumers, and test on fresh blocks (see `case-studies/03`).
5. **Checks pre-freeze satisfiability**: for every mechanical pass criterion, is its
   satisfiability decidable RIGHT NOW from frozen constants + frozen machinery, without
   running? If yes, COMPUTE it and record the answer. A criterion provably unsatisfiable
   (or provably trivial) is a construction defect to fix pre-freeze, not a result to
   discover post-run.
6. **Checks every pin (hash) against the live file.** An archival hash that differs from
   the live file's current hash is a defect to resolve now (which one does the freeze
   pin?).

**DO NOT PROCEED UNTIL** every registered number has been reproduced by independent
computation, every cited line has been read, and every fence claim checked against the
actual list.

---

## 3. ARBITER BRIEFING

When writing the brief for the different-model check (template: `templates/C3-BRIEF.md`):

1. **Directed attack lines, not open questions.** "Try to REFUTE the estimand argument:
   (a) is there ANY registered consumer of the union event? (b) is the rider enforceable
   or does it leak? (c) would this argument have been equally available BEFORE the failed
   run?" — not "please review the estimand section."
2. **Tell the arbiter which section to attack FIRST**, and why it is the highest-risk
   section (usually: the disclosed hazard).
3. **Disclose authorship conflicts.** If the arbiter authored any prior artifact now under
   review (a correction, a bar, a design it previously approved), SAY SO in the brief and
   instruct it to be HARSHER for that reason, not gentler. (Source record: the arbiter's
   own prior correction was the defective bar; the successor brief opened by telling it
   so.)
4. **List the exact materials** — documents, code files with the specific line ranges that
   matter, the raw output JSONs — so the arbiter judges rather than reconstructs.
5. **Require a fixed ruling format**: per-question APPROVE / APPROVE-WITH-CORRECTIONS
   (numbered, verbatim-appliable) / REJECT (with the refutation), ending in one `OVERALL:`
   line. Corrections must be concrete edits, not advice. Require "if you find nothing
   wrong, say what you TRIED and failed to break" — a section the arbiter didn't attack is
   unreviewed, not clean.
6. For post-run favorable verdicts: frame the whole brief as a **refutation attempt**
   ("assume the PASS is an artifact until the evidence forces you to concede") and require
   recounts from RAW records, never summaries.

**DO NOT PROCEED UNTIL** the brief names its attack-first section, discloses any arbiter
authorship conflict, and specifies the ruling format.

**ONE ROUND, period (§G.3 as amended).** This brief is the slot's only dispatch: no
delta re-check after you fold the cures (your own diff pass is the post-fold
verification), no send-back rounds. Residual doubt routes IN-HOUSE (your registrar
seat, or the human), never to another arbiter round — so make this brief count.

---

## 4. RULING VERIFICATION ("a ruling earns a check")

When ANY arbiter ruling comes back — agreeing with you OR refuting you — before applying
anything:

1. **List the ruling's factual claims** (about code, data, documents, arithmetic).
2. **Verify each against the primary artifact**: recompute claimed hashes; open cited
   docs at the cited sections; execute claimed behaviors against real code; re-derive
   claimed arithmetic. (Source record, both directions: a director-verified ruling caught
   that a registration had pinned an ARCHIVAL hash where the live file differed — real
   defect, confirmed by hashing the live file; and a director once verified an arbiter's
   overturning table against the real refit before accepting that its own "exhausted"
   conclusion was wrong.)
3. **Apply corrections verbatim and mark each in place** ("(arbiter correction N)") so a
   later reader can diff what the arbiter changed.
4. For each applied correction, **verify the correction's own premise** — a correction
   asserting a document fact gets that fact checked before the edit lands. Corrections
   can be wrong; the arbiter shares your fallibility, not your blind spots.
5. **Do not silently drop any part of a ruling.** Declined corrections get a written
   reason in the chain log.

This applies with equal force when the ruling AGREES with you — an unverified agreeable
ruling is a rubber stamp, and the most expensive kind.

**DO NOT PROCEED UNTIL** every factual claim you are about to act on has been checked
against real code, data, or documents — not against the ruling's own prose.

---

## 5. BUILD-COMPLETE PASS (the ONE director pass, §G.3)

When an executor reports the build green:

1. **Re-run all fixtures YOURSELF.** Never trust the builder's report of its own success;
   the pass evidence is your re-execution, not their message.
2. **Re-verify the freeze manifest**: every pin present, every hash matching, no
   decision-bearing file unpinned, no pinned file edited.
3. **For any transcribed or re-implemented law** (a driver rewritten "thin," a resampling
   law copied into a new harness): run a **BEHAVIORAL equivalence probe** — identical
   inputs AND identical RNG streams into old and new implementations; deep-compare outputs
   on the **pinned keyset**, comparing outcomes AND provenance/draw-order (the RNG call
   sequence), across enough replicates to exercise the paths. **Beware trivially-true
   comparisons**: a deep-compare over keys that are missing from both sides passes
   vacuously — pin the keyset explicitly and assert the keys exist before comparing.
   (Source record: a 20-replicate probe deep-compared per-family booleans + the FULL
   sampled-provenance index sequences → 0 mismatches; that probe, not the builder's word,
   licensed the transcription.)
4. **Rule explicitly on every surfaced ambiguity** (A3 candidates). The executor's job was
   to surface them; yours is to rule ACCEPTED/REJECTED with a reason, in the chain log,
   one by one — including the "minor items." **Accepting silently is deciding silently.**
5. **Static conformance re-check**: registered blocks vs every layer's allowlist, by
   inspection (checklist 2.3 again, now against built code).
6. Confirm nothing rendered/observed a scored block during the build (fixtures must be
   synthetic or consumed-data only).

**DO NOT PROCEED UNTIL** the fixtures have passed under YOUR execution, every ambiguity
has an explicit ruling, and any transcribed law has a passing equivalence probe on a
pinned keyset.

---

## 6. PRE-RUN (predictions registered before the output exists)

Immediately before (or while) the scored run executes, and strictly BEFORE the output file
exists or is opened:

1. **Write the predictions into the chain log** — dated, numbered, with numeric bands, one
   per verdict-relevant quantity: gate outcomes, each leg's expected result, expected
   count ranges (with the statistical band stated: "counts in ≈4–16 of 200, binomial 95%
   band at p=.05"), the predicted verdict with its probability under the null, dual-report
   agreement bands, even wall-clock time.
2. **Pre-arm the escalation condition in the same entry**: "if ANY prediction misses —
   especially [the named worst cases] — §G.5 escalation is pre-armed; a PASS here is
   favorable+load-bearing ⇒ one-arbiter check regardless."
3. State which priors the bands come from (calibration runs, the predecessor's run of
   record) so a later reader can audit the prediction quality.

The point: surprise is the only reliable in-context error signal, and it exists only if
the prediction came first. Predictions written after peeking are worthless and forbidden
(A1: never edited post-hoc; misses logged honestly).

**DO NOT PROCEED UNTIL** the numbered prediction list is committed to the chain log and
the escalation condition is pre-armed in writing.

---

## 7. POST-RUN D4 (the forced fresh look)

When the scored output exists:

1. **Recount every verdict-bearing number from RAW records** — per-item/per-replicate
   records, never leg-level summaries. Re-derive the verdict label from the raw counts +
   the registered rule; compare with the harness's reported label. (Source record: a
   director recount from raw per-family records exposed that the failed bar sat AT the
   null expectation — the beginning of the bar-defect finding.)
2. **Check each pre-registered prediction, one by one**, and report misses honestly — even
   misses that are not verdict-bearing (a wall-time miss, a band miss on a dual report).
   Prediction misses are your cheapest anomaly detector.
3. Run the D4 pointed questions (PROTOCOL D4.3), mechanically.
4. **Compute the reference statistics the verdict does NOT route on** (the dual reports,
   the not-chosen estimand's counts) and check they tell a consistent story; a
   contradiction between routed and non-routed readings is a finding to report, not to
   suppress.
5. **Escalate per the §G.5 triggers**:
   - verdict **disputed** by the director's recount → ONE arbiter;
   - verdict **line-closing / terminal** → ONE different-model arbiter, tasked to REFUTE;
   - verdict **favorable AND load-bearing** → ONE arbiter, briefed as a refutation
     attempt (checklist 3.6);
   - otherwise → D4 alone suffices; write it up.
   Run a SECOND arbiter only if the first disagrees with the director. Verify whatever
   comes back (checklist 4).

**DO NOT PROCEED UNTIL** every verdict-bearing number has been recounted from raw records
and the escalation decision has been made against the table (not against your mood about
the result).

---

## 8. USER GATES (countersign items)

When presenting anything for the user's signature:

1. **Name the exact document** — quoted filename, plus the section — for every item.
   "Countersign the registration" is not an item; "countersign
   `REGISTRATION-<line>.md` §5 seed table + §2 decision rule" is.
2. **State what the signature consumes and authorizes, in one sentence**, in the item
   itself: e.g. "this ONE signature authorizes build + freeze + scored run AND consumes
   data blocks A and B — there is no later go/no-go." The user must never discover
   after the fact what their signature spent.
3. One gate per cycle (§G.4). If you find yourself queuing a second signature for the
   same cycle, either the cycle design is wrong or the item belongs in the next cycle.
4. Record the countersign verbatim in the chain log, dated, including any rider text the
   ruling requires to be copied verbatim.

**DO NOT PROCEED UNTIL** every pending signature item names its document and states its
consumption sentence.

**Self-clearing (once the human has ruled routine gates are rubber stamps):** the
checklist above still runs in full — the change is only WHO clears it. Stamp a dated
self-clearance at the gate moment, disclose it in the next checkpoint briefing, and
keep the named high-stakes exceptions (scored capstone runs, fresh-data draws) as real
signatures until the human retires those too. A self-cleared gate carries every
evidentiary duty the countersign carried (PROTOCOL.md §G.4).

---

## 9. VERDICT WRITE-UP

When writing the verdict of record:

1. **Use the B1 vocabulary exactly**: HOLDS / NULL (distinguishing a WEAK NULL
   estimator artifact from a clean refutation) / VACUOUS / UNTESTABLE-BY-CONSTRUCTION /
   FAIL-AT-REGISTERED-BAR (defect class named) / HALF-CONFIRMED / HALF-UNTESTED /
   RESIDUAL. The distinctions are load-bearing: an instrument that
   failed a mis-constructed bar is not refuted (`case-studies/02`); a control that could
   not fire is not a null (`case-studies/01`).
2. **Preserve the raw mechanical route beside the verdict of record** — if the harness's
   registered router said FAIL(reason) and adjudication reclassified it, both live in the
   record forever; the raw route is never rewritten.
3. **Dual-report** (B4): superseded bars' results beside current ones; routed beside
   non-routed readings; the predecessor's results cited (never re-scored).
4. **State what the verdict licenses AND what it does NOT license**, as explicit lists:
   what may now be cited, what stays blocked, which claims are BANNED absent further
   validation (copy any required rider verbatim).
5. State the disposition from the pre-registered verdict→disposition table (A5) — the
   pick is mechanical.
6. Land it in the chain log (E3); mirrors wait for checkpoint.

**DO NOT PROCEED UNTIL** the write-up contains the exact vocabulary verb, the preserved
raw route, and both license lists.

---

## 10. LESSONS RATCHET (after any correction)

When corrected — by the user, an arbiter, or your own second look:

1. **Write the lesson** (`tasks/lessons.md`, newest first): Context / What happened /
   Fix / **Rules** — where Rules is a generalized, trigger-shaped rule that would have
   prevented the mistake, not a description of the fix.
2. **A new failure mode becomes a FIXTURE first.** Ask: can a construction fixture, a
   static check, or a schema assertion express this lesson mechanically? If yes, the
   fixture is the primary artifact and the prose is its pointer. Prose-only lessons are
   the fallback, not the default. (Source record: a mid-run allowlist gap became a
   static fence-conformance fixture in the same fix; the successor registration then
   caught the same defect class at registration time, pre-declared, instead of mid-run.)
3. **Ratchet hygiene — retire in the same edit.** Ask: which existing review step does
   this lesson (or its fixture) make redundant? Retire that step in the same edit. The
   ratchet may tighten checks while thinning ceremony; a ratchet that only ever adds
   process reproduces the ceremony-density failure the lean protocol exists to prevent.
4. If the rule is process-level (project-independent), also add it to PROTOCOL.md's
   relevant rule.

**DO NOT PROCEED UNTIL** the lesson entry exists AND you have answered — in writing,
even if the answer is "none" — which step it retires and whether a fixture can express it.

---

## 11. CONFORMANCE GATE (the non-party gatekeeper's checklist — multi-seat setups)

When gating another seat's cycle-close packet (ORCHESTRATION.md §5). Precondition:
you are NON-PARTY — you did not author, prompt, fold, or verify anything in the packet.

1. **Fill the gate manifest from the packet** (`templates/GATE-MANIFEST.json`). A CLOSE
   PACKET is the closing seat's chain-log stamp that must name: the verdict + its B1
   verb · every decision-bearing artifact with claimed hash at its canonical repo path ·
   the data-block claim (ranges + "zero drawn, frontier untouched" as the zero-case) ·
   the paths the cycle's commits touched · the arbiter-check pointer (brief + ruling
   files) · the goal-gain line's location. A packet missing any of these is returned
   INCOMPLETE — that is a packet defect, not a judgment call. Fill the manifest from
   the chain-log-named canonical paths, never from the submitting seat's summary.
2. **Run the mechanical legs** (`tools/gate_check.py`): re-hash · data audit (full
   output, never a summary line) · boundary set-membership. The script's counts go in
   your stamp with their derivation named (§G.16a).
3. **Route every NEEDS-JUDGMENT row** to the registrar/human BEFORE any CONFORMS —
   partial ledger overlaps, un-covered paths, packet-vs-registration conflicts. Ruling
   on them yourself is the exact judgment the non-party gate exists to remove. A
   standing-law path's form-check failure routes too: the exemption covers
   mandated-form writes only.
4. **Verify the judgment-adjacent legs**: the closed registration's one arbiter check
   happened and was verified (one per REGISTRATION — an arc may close several);
   the chain-log opening stamp's goal-gain line exists (§G.15); the seed/data row uses
   the ledger's frontier field verbatim at write (never a stale last-consumed literal).
5. **Stamp with a grade** (REVIEWED/TESTED/ACKED — this gate is normally TESTED), the
   gate count against the arc's bound, and your own data draw (normally "ZERO drawn,
   frontier ≥N untouched").

**DO NOT PROCEED UNTIL** every claimed hash re-derived from its canonical path at
committed HEAD, every judgment row is routed-and-answered, and the stamp's every count
names its derivation command.

---

## 12. ARC REGISTRATION (signing scopes instead of cycles — multi-seat setups)

When drafting an arc for the human's signature (`templates/ARC-SCOPE.md`):

1. **Open with the purpose summary, in plain language, ABOVE the scope table**: what
   question this arc puts to the project goal, why now, what the project gains — the
   `goal_gain` row as prose. A request without the summary is returned unsigned.
2. **Enumerate the scope table completely**: claim-class the arc may produce · venues ·
   interface surfaces tagged read/write/freeze · pathspecs · data-budget ceiling ·
   gate-count bound. No calendar expiry — arcs run to closure, exhaustion, or human
   suspension; a date becomes a floor everyone waits for.
3. **State the compensating controls** that make scope-level signing honest: the
   same-day digest (missed digest auto-suspends), suspension-at-will, and the planted-
   error audit cadence.
4. **Check the question is question-first**: the units inside the arc are DERIVED from
   the arc's question. Enumerating what the seat can run and calling it the arc is the
   named anti-pattern (§G.15).

**DO NOT PROCEED UNTIL** the purpose summary exists, every scope-table row is
enumerated (no "TBD" cells), and the goal-gain row states information the project
acquires — not activity.

## 13. WAIT ENTRY / TURN END (every seat, every stop — PROTOCOL.md §G.29)

Before entering ANY wait, or ending a turn while holding a unit whose inputs are in
hand:

- [ ] Tier 0 — own signed work remaining? Do it instead.
- [ ] Tier 1 — interface audit owed on any surface you share?
- [ ] Tier 2 — demand walk RUN AS A TOOL (lab pulse over committed state); every line
      naming your seat gets an explicit opened-and-disposed line. Pulse output CITED
      in the closure — a walk with neither citation nor a disclosed tool-failure
      fallback is non-compliant.
- [ ] Tier 3 — cross-project clearinghouse swept?
- [ ] Tier 4 — wayfinding/primer debt you could pay?
- [ ] Tier 5 — written closure: "ladder walked, tiers 1–4: one line each" + ACTIONS
      TAKEN line (routes with note+hash, drafts, alarms — or explicitly "actions:
      NONE").
- [ ] Closing line carries exactly ONE verbatim label:
      `STOP-LABEL: CONTINUE | ARMED-WAIT | CHECKPOINT-HOLDS-UNIT(<reason>) |
      HANDOFF(<queue>)`.
- [ ] `CHECKPOINT-HOLDS-UNIT` reason is checkpoint-now or a NAMED human gate — and
      the named-gate form ARMS the one-shot dead-man wake before stopping.
- [ ] Research-line seats: push-assertion — (a) nothing remains that could push the
      line; (b) NOT waiting on the human (take your recommended path, record it,
      raise at next checkpoint).
- [ ] The wait is DECLARED to the waited-on seat (a note in their inbox), and the
      inbox monitor's ARMED + self-proof emission has fired.

## 14. TIERED CLOSE GATE (requesting or receiving — PROTOCOL.md §G.40)

Requester, before the gate opens:

- [ ] The self-serve checker RAN and its report is committed under the arc — a gate
      opened on unchecked work spends the gatekeeper on what a script catches.
- [ ] Tier declared: blocking vs advisory.
- [ ] The request opens with its PURPOSE and names the exact artifacts (paths +
      hashes), not "the usual".

Gatekeeper, before any verdict:

- [ ] Every red leg PROVES ITS OWN DERIVATION before indicting (a failing gate leg is
      a claim like any other).
- [ ] "Checker exited nonzero" vs "no judgment formed" are reported as DIFFERENT
      states, never merged.
- [ ] The verdict names what was NOT swept (coverage is a claim).
- [ ] An indicting verdict earns a second, differently-built check before anyone acts
      on it (§G.32).
