# Director Protocol

A working discipline for LLM-directed empirical and research work — any project where an
LLM session produces **claims that must survive adversarial scrutiny**: experiment
verdicts, pass/fail results, design decisions other sessions will trust.

It was extracted from a working research project at [Ratchet Labs](https://ratchetlabs.ai)
that ran this discipline for weeks across a hundred-plus registered experiment arcs — first as a single director
session, then as a fleet of parallel director seats — and audited itself along the way
to find out **which process layers actually caught defects**. Two findings shaped
everything here:

> **1. Defects are caught by MECHANICAL checks — fixtures, planted nulls, static
> conformance checks, pre-computed arithmetic — and by DIRECTED adversarial review of
> surprising outcomes. They are not caught by ceremony density.** The two worst defects
> in the source project's history each sailed through the *maximum* ceremony
> configuration (multiple pre-approvals, a different-model arbiter, a human countersign)
> and were caught only by mechanical post-run probes. Prefer a fixture over a review
> step; prefer one honest adversary over three charitable ones.
>
> **2. Ritual is calibrated to the model; floors are calibrated to the claims.** With
> the mechanical floor real — a conformance-gate script, fixture suites, hash gates,
> and a structural "route judgment, don't rule on it" contract — the most mechanized
> seats ran on a mid-tier model with supervision collapsing to spot-checks. On day one
> of that transition, a cheap-model seat caught and corrected a strong-model seat's
> committed error ([case study 05](case-studies/05-tier-transition.md)).

## What it actually does

"Survives adversarial scrutiny" is the outcome. The mechanism is four functions,
all answers to the same three facts about LLM sessions: they are amnesiac, they
are credulous, and several of them running in parallel have no natural way to
share a world.

**It keeps memory intact — by never letting memory live in the model.** Sessions
die at usage limits mid-thought; summaries of summaries drift. The protocol treats
session death as the normal case and relocates all load-bearing state into
committed bytes: append-only chain logs per line, hash-pinned registrations, a
handoff layer. What makes that *memory* rather than just files is the re-entry
discipline — a successor session doesn't resume, it **reconstructs**: read the
literal tail of the log, treat the dead predecessor's uncommitted work as an
unverified draft to adopt or discard deliberately, verify claimed facts against
artifacts before continuing them. The conversation is scratch; the repo is the
mind.

**It keeps claims grounded — by refusing to let a statement exist without a
pointer.** Every factual claim has exactly three legal states: verified own-hands
against a named artifact, attributed to a named source, or explicitly labeled
unverified — no fourth state, and a "verification" that cites no byte (path,
hash, line, rerun output) doesn't count. Around that: a controlled verdict
vocabulary (untestable ≠ null ≠ refuted) and freezes, because claims can only be
grounded against things that hold still.

**It keeps the research arc grounded across sessions — continuity of INTENT, not
just of facts.** A session can inherit every fact its predecessor knew and still
lose the plot. So the arc is pinned at both ends: pre-registration up front
(question, criterion, decision bar committed before the run — no later session,
including your own future self after seeing results, can quietly move the
goalposts), and a lessons ratchet at the back (every correction becomes a written
rule or a fixture, so the arc stops re-fighting settled battles).

**It keeps multiple agents in shared context — where shared means independently
verifiable, not shared belief.** Coordination happens through the repository,
never through conversation: cross-seat facts travel as committed notes naming the
commit hash of the fact they report; a note from another agent is a *claim* the
receiver verifies at bytes before acting. Because parallel seats are usually the
same model family, agreement is not confirmation — independence is bought
structurally: a different-model arbiter, a non-party gatekeeper, an auditor
outside every line.

All four are one move applied four times: **externalize everything load-bearing
into committed, hash-citable artifacts, and make every re-entry — a new session,
another agent, your own later self — a verification event rather than a trust
event.** Scrutiny-survival then comes almost for free: claims built this way were
constructed the way a skeptic would audit them.

## The lean cycle in 60 seconds

One verdict-bearing experiment cycle ([PROTOCOL.md](PROTOCOL.md) §G):

1. **Register + freeze.** Criterion, estimand, constants, fresh data blocks — BEFORE
   running. Every decision bar carries **pre-computed false-fail probability AND
   power**. Hash-freeze every decision-bearing file; the run refuses to start on a
   mismatch.
2. **Construction fixtures.** Planted nulls, vacuity checks, schema assertions, static
   fence conformance. Every new failure mode becomes a **fixture first**.
3. **ONE adversarial check at registration — ONE round, ever:** a different-model
   arbiter attacks the freeze candidate; the director verifies the ruling against real
   code and data (**a ruling earns a check**), folds what survives, and moves on. No
   arbitration ladders.
4. **Human signature at the *scope* level.** Early on this was one user gate per cycle,
   consuming the data blocks explicitly; the human soon ruled those routine gates rubber
   stamps, and since then they **self-clear** with a dated disclosure stamp — the human
   signs arc scopes, ceiling raises, and routed doubts instead
   ([ORCHESTRATION.md](ORCHESTRATION.md) §5).
5. **Post-run: the director's forced-fresh-look only, by default.** Escalate to ONE
   arbiter only for disputed / line-closing / favorable-AND-load-bearing verdicts.
6. **ONE chain-log doc per experiment line** holds the whole record.

## Scaling it: seats, arcs, and the tier economy

When one session stops being enough, [ORCHESTRATION.md](ORCHESTRATION.md) documents the
multi-seat structure that ran in production: persistent **seats** occupied by
successive sessions (fences bound writes, not thought) · coordination through
**committed facts** (commit-first inbox notes, delete-is-ack, event-emitting monitors) ·
four governance roles that earned their keep (registrar, non-party gatekeeper, auditor,
producer) · **arc-level human signatures** with a mechanical conformance gate per cycle
close (shipped here as [`tools/gate_check.py`](tools/gate_check.py) — PASS / FAIL /
NEEDS-JUDGMENT-routes, the tool never judges) · and the **model-tier economy**: strongest
model on judgment-heavy seats, mid-tier on mechanized seats with the floor kept at full
strength. Grow into it stepwise — [ADAPTING.md](ADAPTING.md) gives the observed order.

## Quick start

**Hands-on path (copy commands, run the tool, first cycle): [GETTING-STARTED.md](GETTING-STARTED.md).** The conceptual order:

1. Copy `claude/CLAUDE-md-block.md` into your project's `CLAUDE.md` (or equivalent
   charter), and the `claude/commands/` files into your commands directory: `save.md`
   (checkpoint) and `director.md` (session-resume initialization + act as director).
2. Read [PROTOCOL.md](PROTOCOL.md) once, end to end. Starting from a blank problem
   rather than a ready-to-register experiment? [RESEARCH.md](RESEARCH.md) and
   [DESIGN.md](DESIGN.md) are the front end — explore, then design adversarially,
   then register. Read [DIRECTOR.md](DIRECTOR.md) if
   you are configuring the director role.
3. Start your first experiment line by instantiating `templates/REGISTRATION.md` and
   `templates/BUILD-LOG.md`. Copy `templates/lessons.md` (empty — the ratchet is the
   engine; our lessons are not your lessons).
4. Wire a different-model arbiter CLI if you have one ([ADAPTING.md](ADAPTING.md) shows
   how, and how to degrade gracefully without one).
5. When in doubt mid-cycle, run the matching checklist in [CHECKLISTS.md](CHECKLISTS.md).
6. When you outgrow one session, read [ORCHESTRATION.md](ORCHESTRATION.md) and grow into
   seats stepwise (ADAPTING.md, "Growing into orchestration").

## Repo map

| Path | What it is |
|---|---|
| `GETTING-STARTED.md` | The ~10-minute working setup: vendor, wire commands, smoke-test the gate tool, first cycle |
| `PROTOCOL.md` | The rules (A–F), the lean cycle (§G), and the scaling-period amendments (§G+) — triggers → required actions → artifacts |
| `DESIGN.md` | The adversarial front end: unconstrained-best-first, named-voices red-team, question-first arcs, design freezes, the kickoff block |
| `RESEARCH.md` | The exploratory-search protocol: answer-not-novelty, tiered budgets, the round loop, explore tranche, stepping stones |
| `ORCHESTRATION.md` | Multi-seat structure: seats, fences, state, inbox protocol, arcs + the mechanical gate, the model-tier economy |
| `DIRECTOR.md` | The director role: red-teaming, pushing back, own-error posture, model economy |
| `CHECKLISTS.md` | Twelve mechanical checklists with "do not proceed until" gates — the director's judgment moves made explicit |
| `ADAPTING.md` | Instantiating in a new project; arbiter wiring; the stepwise path into orchestration; solo fallback |
| `tools/` | `gate_check.py` — the conformance gate as a runnable script — with selftest and a starter data ledger |
| `templates/` | Registration, chain log, arbiter brief, handoff, arc scope, seat charter, inbox note, gate manifest, empty lessons ratchet |
| `case-studies/` | Five anonymized real defects/transitions and the rules they created |
| `claude/` | Paste-in charter block + commands (`save`, `director`) for Claude Code projects |

## What this is not

Not a prompt library, not an eval harness, and not an agent framework — there is no
runtime here to adopt or be locked into. It is the connective discipline that decides *when* a number is trustworthy, *who* checks it, and *what a
verdict is allowed to claim* — plus the coordination layer that kept those guarantees
intact across many concurrent sessions using nothing but files, git, and one monitor
primitive. It binds only on verdict-bearing work — free exploration, reading, and
brainstorming are deliberately exempt.

## License

MIT — see [LICENSE](LICENSE).
