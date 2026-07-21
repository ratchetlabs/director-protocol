# RESEARCH — Goal-Oriented Exploratory Search

The upstream counterpart of the registered cycle: a discipline for **exploratory
research runs** — literature sweeps, design-space reconnaissance, deep dives into an
unfamiliar field — that produces maps and answers a later session can trust, without
the verdict machinery (which would suffocate exploration) and without the opposite
failure (an unbounded wander that burns a week and leaves no reusable record).

The name to hold onto is **goal-oriented exploratory search**. Both halves are
load-bearing and they are in tension by design: *exploratory* means the run spawns
deliberately diverse hypothesis tracks, sweeps distant disciplines for analogous
mechanisms, and protects a tranche of justification-free wandering; *goal-oriented*
means every one of those motions is aimed — a named goal pinned at kickoff, searches
re-aimed each round by what the previous round taught, and the run judged by whether
the question got answered or precisely relocated, never by how interesting the
wander was. The protocol below is the machinery that keeps both halves honest at
once.

In the source project this protocol fed the design phase ([DESIGN.md](DESIGN.md))
and powered standalone deep-dive sessions; several of its runs ended by *finding*
the answer in an existing field rather than inventing one — which is the point.

## The prime directive: the ANSWER, not novelty

> The objective of every run is the ANSWER. A run succeeds when the space is better
> understood and the question is answered or precisely relocated — never by
> defending a novelty claim. If the answer already exists in some field, finding
> and citing it is a **complete success**; an "already known" result is a WIN.

This is the rule that keeps an LLM-driven search honest, because the model's
default gravity is toward the interesting and the generative. Novelty is measured
as a byproduct (a surviving idea can get a literature-priority check: FOUND →
honest interpolation, cite it; NOT-FOUND → logged as candidate-new), but it is
never optimized for. Never assume the human prefers an open question; do not stop
short of a reachable answer out of a supposed preference for elegance. The only
legitimate stops: budget exhaustion (which forces synthesis, never silent
truncation), a genuine re-pose (a new kickoff), or a dead end honestly reached.

**What this protocol does NOT govern:** no verdicts, no frozen criteria, no
pass/fail. A track maturing into scoreable work EXITS into the registered cycle —
the hand-off is one log line ("track X graduates to registration") — and the full
PROTOCOL.md apparatus applies from that moment.

## 1. Kickoff — pin the run before you search (~5 minutes, with the human)

Open a run log (`research/RESEARCH-<slug>.md` or wherever exploration lives in
your layout) whose §0 pins:

- **Goal** — one sentence.
- **Criticality tier** — T1 (an answer here breaks or makes the project) / T2
  (important, alternatives exist) / T3 (learn the space). Set by the HUMAN — it is
  a fact about consequences, not about enthusiasm.
- **Budget** — tier defaults below, adjusted at kickoff. Including the external-
  search allowance up front batch-satisfies any per-search approval convention.
- **Stop/kill conditions** — answered / question dissolved / budget exhausted
  (forces the synthesis step) / a named external event.
- **Seed analogy fields** — around FOUR named disciplines, **related but
  different**: adjacent enough that their mechanisms could transfer, different
  enough that they hold mechanisms your home field doesn't. Named NOW, at kickoff,
  so the close-out can check they were actually swept — and each carries a standing
  obligation (§5): the run must explicitly think through the analogy from that
  field to the current problem, not just read in it.

## 2. Budgets — coarse units, one extension, a split search pool

Meter in coarse units checkable from the log, never tokens. Reference allocation
(the T2 column is production-calibrated; T1/T3 are extrapolations your first run
should treat as a knob under test):

| Unit | T1 | T2 | T3 |
|---|---|---|---|
| Director synthesis sessions | 2 | 1 | ½ |
| Harvest agent-runs (mid-tier, read-against-targets) | 8 | 4 | 2 |
| Fetch agent-runs (cheap tier, enumerate/triage) | 40 | 20 | 8 |
| External searches — planned pool | 20 | 12 | 6 |
| External searches — lead-chase reserve | 8 | 8 | 4 |
| Rounds (§4) | 3 | 2 | 1 |

Rules that earned their place: **one extension per run max**, human-granted,
logged with a reason. The external-search pool is **split** — a planned sub-pool,
plus a lead-chase reserve a mid-run lead can draw from *without* consuming the one
extension (added after a run where every good lead posed an extension dilemma).
The pool is shared and **logged per agent** — the first run overran because
sub-searches inside harvest agents went uncounted. Within a granted budget the
director proceeds autonomously; only an extension or a scope re-pose goes back to
the human.

**A protected explore tranche:** 20% of every non-search budget line is reserved
for justification-free spends — reads and track-spawns with NO stated connection
to the goal. Asking "why is this relevant" at spawn time is banned for tranche
spends; that ban is what makes it a stepping-stone mechanism rather than disguised
exploitation. Tranche spends are tagged `[explore]` so the retro can measure
whether they paid (in production they periodically did, disproportionately).
Unspent tranche EXPIRES — it never rolls into goal-directed spend.

## 3. Model routing — escalate judgment, not execution

Three roles, by tier: **fetch** (cheapest tier — enumerate, triage results, chase
citations, "does X exist"; structured lists out, no interpretation), **harvest**
(mid-tier — read papers/repos/docs against NAMED targets, one topic per run;
report findings plus surprises), **direct + synthesize** (strongest available —
steer, spawn/prune tracks, write checkpoints, decide when a finding changes the
strategy). The director never executes delegable fetches; agents never make prune
decisions. A fourth role, the **adversarial look**, is a different-model arbiter
and touches only the synthesis (§6).

Machine-load discipline, learned the hard way (a fan-out crashed the host
mid-run): cap concurrent agents (the source project ran ≤2, dispatched in
staggered waves), offload heavy compute to cloud rather than pegging the local
machine, and write run-log entries incrementally at dispatch and at each agent
return — never held in memory for a checkpoint write — so a crash loses no state.

## 4. The round loop — generate, walk, prune, with evolutionary pressure

Each round (count set by tier):

1. **GENERATE, diversity-forced.** Spawn hypothesis TRACKS — ≥5 for T1/T2,
   spanning ≥3 distinct mechanism families. A track = one-line hypothesis +
   evidence that would advance it + a **named kill condition at spawn**.
   Unrelated-looking tracks are welcome; relatedness is not a spawn criterion.
2. **WALK.** Route fetches and harvests across tracks per budget. The director
   re-reads the accumulating log BEFORE routing each batch — the walk is informed
   by the search so far, not by the plan from an hour ago. **This is where the
   goal-orientation bites: the next round's searches are RE-AIMED by what this
   round taught.** A finding that reframes the problem redirects queries, kills
   tracks, and spawns new ones at the next GENERATE — the plan pivots on learning,
   it is never executed as written. (A run whose round-3 queries could have been
   written at kickoff wasn't listening.)
3. **SYNTHESIS CHECKPOINT.** The director writes 5–15 lines: how the findings
   fit, what surprised, the current best map — surfaced to the human each round
   (the human steers between rounds, never mid-walk). The checkpoint MUST ask:
   **"if this finding is right, what question does it now make askable that
   wasn't before?"** A surfaced successor question is a first-class outcome — the
   best runs converge AND relocate the problem, and the continue-vs-re-pose call
   is made explicitly (a re-pose is a NEW kickoff, never a stretched budget).
4. **PRUNE, with a protected niche.** Score tracks coarsely — evidence accrued,
   goal connection, diversity contribution — and prune the bottom, EXCEPT the
   **wildcard slot**: the highest-novelty track survives one round regardless of
   goal connection. A track killed by its own spawn-time kill condition is an
   HONEST KILL — the system working, not a failure. Pruned ≠ deleted: prunes stay
   in the log with reasons, and the retro audits pruning quality.
5. **RECOMBINE.** Before the next GENERATE, one explicit pass ("track A's
   mechanism under track B's constraint") — and sweep the stepping-stones file
   (below). Recombination is where stepping stones pay.

## 5. Analogy sweeps — explicit, audited, and thought through

The four related-but-different disciplines from kickoff are not background
reading — they are a standing obligation the run must discharge. At kickoff and at
each synthesis checkpoint, for each seed field (plus any accrued mid-run), the
director asks the question EXPLICITLY: **"what is this field's analogous mechanism
for our problem?"** — and logs every attempt as one line:

```
field → mechanism considered → BITE / NO-BITE / DEFERRED
```

Failures included; the audit record is the point. The thinking is the required
part — a field marked swept because an agent read three papers in it, with no
logged attempt to map its mechanism onto the problem, is an unswept field. The
one-line format is what makes the obligation checkable at close-out: the retro
reads the sweep lines and reports which fields bit. In production, analogy hits
were among the highest-value findings per unit spend — the mechanism your field
is missing usually already exists somewhere, under a different name, and the
sweep is how "already known, found and cited" wins actually happen.

Mechanics: choosing a distant field is a DIRECTOR act, never an agent act —
agents receive named fields, they do not pick new ones. Keep sweeps and tranche
wanders clear of restricted/safeguarded domains your model's safety layer will
refuse — a blocked spend buys nothing and can stall an agent; log the slot
`FENCED` and pick another field.

## 6. One adversarial look — at the synthesis, at the end

The final synthesis gets ONE different-model adversarial pass: always for T1;
for T2/T3 only when the synthesis will feed a registration, a design decision, or
a human decision. The prompt shape: *attack this synthesis — what is
over-weighted, which pruned track was killed wrongly, which named field went
unswept, what would a hostile reviewer say the map misses.* The ruling earns a
check (PROTOCOL.md C3 discipline unchanged — verify it against the actual
sources; a ruling is information, not an oracle).

## 7. The retro — the protocol tunes itself

At close, a retro block answered from the log's own lines: where value actually
came from (which tier, which round, exploit vs `[explore]`, which analogy fields
bit) · did a convergence relocate the problem, and was the successor question
followed or at least logged? · did the run reach an answer or stop short on a
novelty preference? · was anything pruned that later mattered? · which budget
lines bound first? — and **ONE knob change** proposed for the next run. One at a
time, so runs stay comparable. A newly added, not-yet-exercised mechanism carries
a first-exercising obligation: the first run that uses it must report on it
explicitly, and a mechanism that sits unexercised across runs gets retired rather
than accreting (that retirement rule has fired in production).

## 8. Cross-run retention: the stepping-stones file

One standing file (`research/STEPPING-STONES.md`) holds pruned-but-interesting
tracks, NO-BITE analogies, and orphan fragments; every RECOMBINE step sweeps it.
It exists because per-run memory systematically discards stepping stones — they
don't resemble destinations — and it is the one organ that survives across runs.

## Where this connects

- **Feeding design:** a run whose synthesis stabilizes an approach hands
  [DESIGN.md](DESIGN.md) its raw material — the red-team's rival-approach voice
  argues from the tracks this protocol kept honest records of.
- **Deep dives:** a T3 run with a ½-session synthesis budget is the shape for
  "spend an afternoon actually understanding X" — cheap, logged, and it leaves a
  map the next session can load instead of re-deriving.
- **Exiting:** anything scoreable graduates to a registration
  ([PROTOCOL.md](PROTOCOL.md) §G) and the full verdict discipline takes over.
