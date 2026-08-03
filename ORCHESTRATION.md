# ORCHESTRATION — Running Multiple Director Seats in Parallel

This document describes the multi-seat structure the source project converged on after
roughly two weeks of running the [lean cycle](PROTOCOL.md) at increasing scale: several
concurrent LLM sessions, each a **full director**, each owning a distinct line of work,
coordinating through committed files rather than shared context. It documents what
worked in production — not a speculative architecture.

Read [PROTOCOL.md](PROTOCOL.md) first. Orchestration does not replace the lean cycle;
it is the answer to "what happens when one session is no longer enough" — because
lines of work outnumber hours, because independence between builder and reviewer must
be real, and because context windows end but projects don't.

---

## 1. Seats, not subagents

A **seat** is a persistent role — a mandate, a write scope, and a chain log — that
successive LLM sessions occupy. The session dies; the seat persists in files. This is
the load-bearing inversion: you are not orchestrating *processes*, you are
orchestrating *state that any process can resume*.

Every seat is a **primary, full-strength director**. There is no "main" session that
sub-delegates to lesser ones: a seat holding a build line has the same judgment
duties — red-teaming, pushing back, verifying rulings against real artifacts — as any
other. (Subagents still exist *within* a seat for delegated labor; see DIRECTOR.md.
The seat itself is never a subagent.)

**Fences bound writes, not thought.** Each seat's charter names the paths it may
write. Everything else it may read, reason about, red-team, and propose on freely —
"not my area" is never a licensed posture for a judgment call. A judgment implicating
another seat's line goes in *your* chain log and is **routed** to the owner, with a
close-out line recording where it went. Silence and unrouted drops are the
non-compliance, not the cross-line thought.

A minimal seat charter fits in one section (see `templates/SEAT-CHARTER.md`):
mandate · write scope (pathspecs) · fences (what it must never do) · chain-log path ·
standing docket. Charters are maintained by named editor seats only; **editorial**
charter edits are free (dated, with a notice to the seat), **structural** edits —
anything changing what the seat may *do* — require the human's countersign.

## 1a. Who launches a seat (the dispatch law)

**Seat instantiation is human-only, with exactly one carved exception.** No seat
launches, proposes launching, or builds launch machinery for another seat — cross-seat
latency is note routing plus the peer's queue, never waiting-for-launch.

The exception: **the scheduler seat (the architect, in our roster) dispatches the two
mechanized execution lanes — the machine executor and the supply seat** — as bounded
mid-tier sittings (§6 profile). The trigger is DEMAND, mechanically defined: an
unacknowledged act-grade or blocking note sits in the lane's inbox with no launch
residue, or scheduler-constituted work stands ready with no live sitting. A ripe-work
sentence in ANY inbound note is an act-grade demand in the scheduler's queue. A
covering monitor never counts as a live sitting — check for the lane's own recent
commits or live processes before deciding it is running.

**The scheduler is the scheduler of record.** It may wait only behind a clean, cited
run of the lab-pulse tool (§3) with every flag opened and disposed. Idle-with-demand —
or the human having to nudge the sequencing — is a scheduler defect *by definition*,
not a judgment call.

## 2. State: files win, context loses

Three rules make parallel seats safe to kill at any moment:

1. **Docs are the state.** Every decision lands in a committed file (the chain log,
   a registration, a ledger row) the same day it is made. A decision that lives only
   in a conversation does not exist.
2. **Chain logs win.** Each line of work has ONE append-only chain log. Summaries of
   it (handoff files, memory, status tables) are conveniences that decay within hours
   on a busy day. A seat about to act on a line reads the **literal tail** of the
   owning chain log — never a summary, never a header grep (mixed section styles can
   hide hundreds of lines below the last heading you matched).
3. **Expect the kill.** Sessions routinely die mid-flight (usage limits, crashes) —
   a NORMAL terminal state, not an anomaly. A kill loses context, never files, so:
   commit own-scoped durable state at **every event boundary** (ruling folded, build
   accepted, fixtures green), not just at session end. The successor's first duty on
   finding uncommitted residue on its own line: read the diff, verify its claims
   against real artifacts (an interrupted sitting can be stamped-but-not-executed OR
   executed-but-not-stamped), then **adopt with a dated stamp or discard
   deliberately**. Never silently continue a half-written stamp.

**The handoff file** is the shared map: a small CORE (state every seat needs — shared
ledgers, cross-seat law, one line per seat) plus a **per-seat layer file** each seat
reads at init and writes at save. Splitting layers by seat eliminates write contention
on parallel days. The core's per-seat lines are awareness, not truth — the chain log
always wins. `templates/HANDOFF.md` shows the shape.

## 3. Communication: committed facts, not messages

Seats coordinate through **inbox notes** — small files in `tasks/inbox/<seat>/` —
under four rules that turned out to carry all the weight:

1. **Commit first, note second.** Every note names the commit hash of the committed
   fact it reports. A note whose hash does not resolve at HEAD is a *non-state*: the
   receiver treats it as not-yet-sent. This single rule closes the entire
   acted-on-uncommitted-work class of race conditions.
2. **Delete is the ack.** The receiver verifies the pointed-at fact at the bytes (a
   note is a claim, not a fact), acts or files it, then deletes the note. Anything
   present in the inbox IS the unprocessed set — no separate read-receipts.
3. **Blocking requests carry a timestamp and a timeout.** A note that blocks its
   sender carries date AND time-of-day; no response within a stated window (ours: 30
   minutes) → the sender raises to the human in its own conversation. The raise is
   *diagnostic only* — it licenses nothing; silence is never consent.
4. **Waiting seats arm an emitting monitor.** A seat expecting a response arms a
   filesystem monitor on its inbox that **emits an event on arrival and is silent
   when empty** — a log-only polling loop is deaf by construction (nothing re-invokes
   an idle session that merely wrote to its own log). Concrete recipes per harness, and
   the honest fallback where no re-invocation primitive exists: ADAPTING.md, "Wiring
   the inbox monitor". Monitors die with the session; the successor's init inbox read
   is the kill-safe backstop.

**No bare waits — and every stop is labeled.** "Waiting, nothing to do" is never a
legal seat state; a wait is *earned* by descending the ladder (PROTOCOL.md §G.29):
own signed work → interface audits → the demand walk → clearinghouse sweep →
wayfinding → written closure with an ACTIONS TAKEN line. Two mechanics matured after
the ladder itself:

- **The demand walk is a TOOL RUN, not a memory exercise.** A small **lab-pulse**
  script derives, live from the committed state, a one-screen view: every seat's
  last-stamp age and declared stop-label, inbox counts, held-unit stops gone stale.
  The wait closure CITES its output and disposes every line naming your seat. The
  pulse is a DOORBELL, never a disposition — judgment stays at the seat.
- **Every turn end is a held-unit check**, closed with a parseable enum the pulse
  can act on: `STOP-LABEL: CONTINUE | ARMED-WAIT | CHECKPOINT-HOLDS-UNIT(<reason>) |
  HANDOFF(<queue>)` — plus the dead-man wake on held human gates (PROTOCOL.md §G.29:
  a stalled lab is silent; the only self-actuation a seat has is a timer it arms
  before stopping).
- **Arming carries a self-proof.** The monitor arm plants a probe file in the watched
  inbox, sees its own emission, removes it — exactly ONE "ARMED + self-proof PASS"
  event. An arm without the proof is a promise, not a monitor.

In the same spirit, **unblocking another seat outranks your own queue**: when
a seat learns it holds the input another thread is blocked on, servicing the unblock
comes first, with a one-line cost/benefit stamp either way.

**Route judgment calls the moment they fire.** With the registrar always available
(see §4), batching questions to "save a round trip" just serializes latency into your
own line. Ask when the question exists.

## 4. Specialized seats: the four roles that earned their keep

Build seats do the object-level work. Four *governance* roles emerged as worth their
overhead — each exists because it holds an independence or a consistency that a build
seat structurally cannot hold about itself:

**The registrar (the standing consult seat; some projects call it the architect).**
Constitutes new arcs, rules on scope and
interface questions, maintains the dependency board and the capability ledger, and
serves as the standing consult surface every other seat routes judgment calls to.
Registrar rulings mark what **binds** (the holding successors must honor) versus
commentary — future seats re-litigate commentary freely, holdings only via amendment.
The registrar is the natural seat for your strongest model: it absorbs the judgment
the other seats route out.

**The scribe (non-party gatekeeper).** Runs the mechanical conformance gate (§5) on
other seats' close packets, and is the **sole writer** of shared ledgers (data-block
consumption, integration queues). The scribe must be NON-PARTY to anything it gates —
it did not author, prompt, fold, or verify the work under review. This is the seat
that makes "the builder never grades their own work" real at zero marginal human cost.

**The auditor (process steward).** Owns the rulebook's hygiene: folds amendments,
archives superseded text, sweeps for rules that never fire (**net rule mass must
trend down** — a growing rulebook is a finding), builds and maintains the guard
tooling, and runs **planted-error audits**: deliberately defective packets submitted
through the real gate on a fixed cadence to prove the gate still catches what it
claims to catch. A gate nobody has ever seen fail is an unmeasured gate.

**The supply seat (producer).** Builds corpora, environments, and fixtures that other
seats consume. Its governing law is the **consumer's exact reader schema**: the
receiving side enumerates, at request time, the exact artifact set and key-level
schema its frozen consuming code reads — derived by grepping the reader, quoted
verbatim — and the producer ships to THAT, never to its own reading of the domain.
Every delivery carries a `MATES:` line — YES/NO/UNCERTAIN, verified at the
*counterparty's* bytes — answering "when they consume this into a verdict, what could
make it lie or go silently dead?" A satisfied spec feeding a dead metric is the named
failure mode.

Start with zero of these. The order they earned their existence in the source
project: scribe (the moment two seats ran concurrently), architect (the moment two
seats disagreed), auditor (the moment the rulebook outgrew memory), supply (the
moment two lines consumed the same corpus). See [ADAPTING.md](ADAPTING.md).

## 5. Arcs: sign scopes, gate cycles mechanically

Per-cycle human countersigns do not scale past a few concurrent seats — and audited
against defects caught, they were ceremony. What replaced them:

**The human signs ARCS** — scope containers, not cycles. An arc's scope table
enumerates: the claim class it may produce, venues, interface surfaces touched
(read/write/freeze), pathspecs, a data-budget ceiling, and a **gate-count bound**
(never a calendar expiry — a date becomes a floor everyone waits for; arcs run to
closure or exhaustion). Every arc opens with a plain-language **purpose summary**:
what question this puts to the project goal, why now, what the project gains — a
`goal_gain` row is mandatory, and "exercises the harness" does not qualify.
`templates/ARC-SCOPE.md` is the form. Where arcs COME FROM is the design front end
([DESIGN.md](DESIGN.md)): the question-first framing, the red-teamed approach choice,
and the frozen design doc the arc's registrations cite all precede the signature —
an arc request without that lineage is the "capability-first" drift the front end
exists to catch. Exploration feeding the design runs under [RESEARCH.md](RESEARCH.md).

**Inside an arc, cycles close through the mechanical gate** run by the non-party
gatekeeper: re-hash every claimed artifact from its canonical path at committed HEAD;
audit data-block consumption against the shared ledger (full output, not a summary
line); check every touched path by **set-membership** against the arc's pathspecs.
The three legs are a script, not a judgment — ours ships here as
[`tools/gate_check.py`](tools/gate_check.py). Anything requiring interpretation
(partial ledger overlaps, paths outside the declared scope, packet-vs-registration
conflicts) emits **NEEDS-JUDGMENT and routes to the registrar** — the tool never
judges. One standing carve-out: paths written by lab-wide standing machinery (the
shared ledger a claim tool maintains, the lessons file) sit outside per-arc scope *by
construction*, but only in the machinery's **mandated form** — the gate form-checks
them, and a hand-edit of an exempted file is still a defect.

**Compensating controls** (what keeps arc-level signing honest): a same-day digest to
the human — required fields: gates run with their verdicts, data drawn vs the ceiling,
judgment rows routed and their answers, the next expected gate — where a missed digest
auto-suspends the arc; human suspension at will; and the auditor's planted-error
audits on a weekly cadence. When an arc's fence is hit (a write outside scope, a
claim outside class), the question returns to the human as a **scope card** — a
one-decision mini-scope naming exactly what changed and what signing it would
license.

**Routine gates self-clear.** Once the human has said, in effect, "these per-cycle
signatures are rubber stamps — you are always authorized," the seat stamps a dated
self-clearance and discloses it in the save briefing rather than blocking on a
signature. Named exceptions stay real gates (for us: scored capstone runs and
fresh-data-block draws kept their teeth the longest, and even those eventually
reduced to machine-checkable preconditions plus disclosure). The principle: **a gate
whose answer is always yes is a latency tax, not a control** — replace it with the
mechanical precondition it was standing in for, and spend the human's attention on
arc constitution and verdict review, where it changes outcomes.

## 6. The model-tier economy

The most consequential discovery of the orchestration period: **most seats do not
need your strongest model most of the time — if and only if the mechanical floor is
real.** The source project ran its strongest-tier model on all seats until cost
forced the question, then moved its most mechanized seats (gatekeeper, machine
executor, supply) to a mid-tier model under an explicit profile.

**The roster that stuck (still running as of 2026-08-03):** director seats holding
research judgment — architect, research lines, auditor — stay on the frontier tier;
the **scribe/gatekeeper seat and the two dispatched execution lanes (machine
executor, supply) run mid-tier (Opus-class) permanently**, the lanes launched by the
scheduler per §1a. The tier assignment follows the WORK SHAPE — mechanized floors and
pre-decomposed judgment go mid-tier; open-ended judgment stays top-tier — never
seniority of the seat. The profile:

**KEEP — everything a machine runs, cut nothing:** conformance-gate script · fixture
suites run twice, byte-identical · hash freeze/re-hash tooling · data-ledger tooling ·
command guards · the named human gates.

**STRIP — the seat ritual**, replaced by three duties: (1) commit own-scoped paths at
event boundaries; (2) stamp what you did in the chain log, dated — any format;
(3) when in doubt, route to the registrar and continue what is not in doubt.
Retired for these sittings: kickoff ceremonies, verbatim quote-proofs, multi-voice
red-teams (state the one biggest risk in one line), stamp grammar.

**Judgment is pre-decomposed or routed, never attempted solo.** New estimands,
adjudications, and line-closing calls are either pre-drafted at a strong-model
sitting into closed-ended steps ("run Y, expect Z, else route") or sent to the
registrar. Executing a pre-drafted decision structure is in scope; inventing one
is not. Verdict vocabulary survives in one sentence: never report a null or
untestable result as a refutation, or a superseded bar as met.

Two findings made this credible rather than hopeful (worked example:
[case-studies/05-tier-transition.md](case-studies/05-tier-transition.md)):

- The mid-tier seats' first sittings **self-caught real errors** — including a
  predecessor's false "queue is empty" claim, caught by re-reading the queue at the
  bytes at init — and correctly *routed* the judgment-shaped questions instead of
  answering them. The profile's intended behavior, self-enforced on day one.
- The strong-model seats' **watch duty converged to sampling**: spot-verify the first
  few gates a newly-transitioned seat runs, then drop to occasional checks unless a
  NEEDS-JUDGMENT anomaly fires. The gate script's routing discipline is what makes
  the watch cheap.

The general shape: **ritual is calibrated to the model; floors are calibrated to the
claims.** A weaker model gets *less* ceremony and *more* mechanical checking — never
the reverse.

## 7. Cross-seat honesty laws

Four laws bind every seat's writing, and they are what keeps a many-author record
trustworthy:

- **Bytes before statements.** Every factual claim outside the verdict machinery is
  (a) VERIFIED own-hands against committed bytes — quote the file and line; a fact
  you cannot quote is a fact you have not checked; (b) ASKED — attributed to a named
  answer from the owner; or (c) LABELED an assumption in the output itself. Never a
  fourth state. Current-state claims ("we use X", "line Y is live") are the
  highest-risk class: read the owning chain-log tail, never infer from titles or
  memory.
- **Counts name their derivation command.** Any count in a verdict-adjacent stamp
  ("17/17 hashes match", "812 records") names the one-liner that reproduces it
  (`grep -c …`, `wc -l …`). No command nameable → the count is labeled UNVERIFIED.
- **Stamps carry a grade.** REVIEWED (a named judgment re-derived, shown) · TESTED
  (ran the artifact own-hands: fixtures, reruns, recomputed hashes) · ACKED
  (read-and-agree). An ungraded stamp reads as ACKED. A review that only attests
  "hashes match, fixtures green" is an ACK wearing a review's name — a real review
  **names the judgment it re-derived** and shows the re-derivation.
- **Errors found in your own thinking are successes.** Every save briefing carries an
  "errors found in own thinking" line, by name. The posture is to verify everything
  at the bytes *including your own prior conclusions* (predict-then-check on re-entry,
  never a plain re-read). A seat that reports its own catch is the process working;
  shame-hiding is the defect.

## 8. What we deliberately did NOT build

- **A message bus or framework.** Files + git + one monitor primitive carried the
  entire coordination load. Every abstraction we considered adding would have hidden
  the state that makes kills survivable.
- **A central dispatcher.** The seats self-schedule against their charters and the
  human routes new work. What DID earn its keep since this section was first written
  is the narrow form in §1a: one scheduler seat dispatching two mechanized lanes on
  mechanically-defined demand. The general dispatcher — anything deciding what
  arbitrary seats work on — remains unbuilt on purpose.
- **Calendar-based anything.** Date-driven reviews and expiries repeatedly decayed
  into floors people waited on. Everything cadence-shaped either became event-driven
  (gates, notes, monitors) or got an explicit weekly slot owned by a named seat (the
  planted-error audit).

## 9. The context budget — init cost is governed, not endured

Every session re-reads its way into the lab, so **bytes on the always-read path are a
tax on every future sitting**. The source project ran an explicit diet program
(measured, 2026-08-02/03) once init cost was observed to dominate short sittings.
What generalizes:

- **The shared handoff is CORE + layers.** CORE holds shared ledgers (live facts
  only) and ONE ROW per seat — state · blocked-or-not · next event · layer pointer —
  under a HARD character ceiling (ours: 350 live, 200 retired-stub). Everything else
  lives in the seat's own layer file, read only by that seat at init. Prose strata
  roll to an archive file with verbatim moves (MOVE-OR-DELETE, never re-characterize;
  the archive's roll headers are the provenance).
- **Rule register and lessons are read as index + delta** (PROTOCOL.md §G++ init
  diet): one-line doorbells at init, full cards/entries only when a trigger fires,
  `register-read:`/`lessons-read:` commit pointers making the delta mechanical.
- **Commit subjects cap at ≤120 chars** (PROTOCOL.md §G.35a) — the init freshness
  beacon is `git log <checkpoint>..HEAD`, so every oversized subject is read forever.
- **Seat memory outside the repo gets pruned on the same law:** standing human
  rulings + current-work context stay; anything duplicating the charter, the
  register, or the repo's own history is deleted, not summarized. Auto-recalled
  memory is invisible preload — its budget is as real as the files you read on
  purpose.
- **Know your floor.** Measure a bare session (no task) before optimizing: the
  harness's own system prompt and tool schemas set a floor no repo diet can cross.
  Optimize the delta above the floor; report the split honestly.
