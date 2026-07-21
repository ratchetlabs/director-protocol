# ADAPTING — Instantiating the Protocol in a New Project

## What to copy where

| From this repo | To your project | Notes |
|---|---|---|
| `claude/CLAUDE-md-block.md` | append into your `CLAUDE.md` (or agent charter) | Edit the pointer paths if you vendor this repo elsewhere |
| `claude/commands/save.md` | `.claude/commands/save.md` | Adjust the spec-doc names to yours |
| `claude/commands/director.md` | `.claude/commands/director.md` | Session-resume: runs the full initialization sequence (handoff, protocol §G, chain-log tails, thread-ownership check), then acts as director |
| `templates/lessons.md` | `tasks/lessons.md` | **Copy EMPTY** — see below |
| `templates/REGISTRATION.md` | instantiate per experiment | e.g. `experiments/<line>/REGISTRATION-<exp>.md` |
| `templates/BUILD-LOG.md` | instantiate per experiment **line** | `BUILD-<line>.md` — one per line, not per run |
| `templates/C3-BRIEF.md` | instantiate per arbiter call | keep briefs next to the chain log |
| `templates/HANDOFF.md` | `HANDOFF.md` at project root | a living file, overwritten at each checkpoint |
| `PROTOCOL.md`, `DIRECTOR.md`, `CHECKLISTS.md`, `ORCHESTRATION.md` | reference in place (vendor or submodule) | your charter block points at them |
| `tools/gate_check.py` + selftest + `tools/data_ledger.json` | `tools/` (multi-seat setups) | edit `STANDING_LAW_PATHS` in the script; replace the ledger's example rows; run the selftest after any edit. The tool audits INTEGER ranges only — assign every named block a numeric range. No claim script ships: write a small append-only one (append row, recompute frontier, refuse overlaps) — hand-edits of the ledger are the defect the gate's form check catches |
| `templates/ARC-SCOPE.md`, `templates/SEAT-CHARTER.md`, `templates/INBOX-NOTE.md`, `templates/GATE-MANIFEST.json` | instantiate per arc / seat / note / gate (multi-seat setups) | see ORCHESTRATION.md |

## Naming conventions

- **One chain-log doc per experiment line**: `BUILD-<line>.md`. A "line" is a question
  (e.g. "is this instrument's error control real?"), which may take several registrations
  (v1, v1b, v1c…) to answer. Successor registrations append to the SAME chain log — the
  whole lineage (verdict, repair, re-registration) reads in one place.
- Registration docs carry their status in a header block that changes exactly twice:
  DRAFT → (arbiter-adjudicated, corrections applied) → **FROZEN at countersign, with a
  status pointer to the chain log**. After the countersign, all further status lands in
  the chain log only.
- Data/seed blocks get names ("block A", a numbered range — whatever is unambiguous) and
  a project-level ledger of consumed vs free blocks (the handoff doc is a good home).
- Verdict symbols are versioned with the registration (K3′ is a new registration's
  verdict, never a retrofitted K3).

## Where things live (example layout)

One workable layout for a single experiment line — the chain log at the line root, each
registration beside the code/fixtures/manifest it freezes:

```
experiments/<line>/
  BUILD-<line>.md              # the ONE chain log of record for the line
  v1/
    REGISTRATION-<exp>.md      # freezes at countersign; points to the chain log
    code/                      # harness + statistic/router code (ALL decision-bearing)
      harness.py               # applies the router/bar — decision-bearing, hashed
      statistic.py
    fixtures/                  # the §4 construction gates (planted-null, schema, …)
    manifest.md5               # the freeze manifest: hashes of every code/ file + the registration
  v1b/                         # a successor registration appends to the SAME BUILD-<line>.md
    ...
  c3_<exp>_brief.md            # arbiter brief + ruling kept next to the chain log
  c3_<exp>_ruling_raw.md
```

Nothing here is mandatory but the invariants are: the manifest sits beside the code it
pins and lists **every** decision-bearing file (harness included, PROTOCOL A2), and one
chain log spans all `vN` registrations in the line.

**Freeze-manifest format + the re-hash gate (A2's enforcement half).** Any format
works; the simplest is `md5sum`-style lines, generated with
`md5sum code/* REGISTRATION-<exp>.md > manifest.md5` at freeze and verified with
`md5sum -c manifest.md5`. The gate itself is ~5 lines at the top of the scored
harness: recompute each manifest entry, write the match into the results metadata
(`frozen_source_hash: OK`), and `sys.exit` with a refusal message on any mismatch —
the run must REFUSE to start, not warn. Keep the manifest itself out of the manifest.

## Wiring a different-model arbiter CLI

The arbiter must be a **different model family** from the director — that is the entire
point (PROTOCOL, C header). Any CLI-drivable model works (e.g. OpenAI's codex CLI when the
director is Claude, or vice versa).

- Drive it from the director session via shell: write the brief to a file, run the CLI
  with the brief + read access to the exhibits, capture the ruling to a file
  (`c3_<exp>_ruling_raw.md`) so it enters the record unedited.
- Practical trap: a CLI executed from a background shell may block forever reading an
  inherited stdin pipe — redirect stdin from `/dev/null` for background invocations, and
  if a call seems slow, check CPU time first (near-zero CPU after minutes = blocked on
  I/O, not thinking).
- Give the arbiter file access to the real code and data named in the brief; a
  paraphrased exhibit defeats the purpose.
- Budget: ONE arbiter call per registration + escalations per §G.5. This is cheap
  against what it protects (a consumed data block, an abandoned line).

## Wiring the inbox monitor (multi-seat setups)

ORCHESTRATION §3 requires a waiting seat's monitor to EMIT — meaning: produce the kind
of event your harness re-invokes an idle session on. What that is depends on the
harness:

- **Harness with a native monitor primitive** (e.g. Claude Code's `Monitor` tool with
  a persistent watch command): use it — per-arrival emission, silent when empty. A
  watch loop that diffs the inbox listing and prints ONLY on new files satisfies the
  contract; add a blank-line guard so empty listings don't false-wake.
- **Harness that re-invokes on background-process EXIT:** run a watcher that exits on
  first arrival (`fswatch -1 tasks/inbox/<seat>/` or an `inotifywait -e create` /
  polling loop that exits when the listing grows). Exit = the emission; re-arm on wake.
- **No re-invocation primitive at all:** monitors are impossible — say so and lean on
  the two backstops, which exist for exactly this: the successor's init inbox read
  (every note is processed at next session start) and the sender's 30-minute raise to
  the human. Do NOT fake a monitor with a log-only loop; it reads as armed and hears
  nothing.

## What starts EMPTY

- **`tasks/lessons.md` — the ratchet is the engine; our lessons are not your lessons.**
  The source project's lessons file is deliberately not included: its entries are rules
  distilled from *its* corrections, and importing them would give you the prose without
  the fixtures or the scar tissue. Your ratchet earns its authority by recording YOUR
  corrections. The generalizable lessons that survived contact with reality are already
  folded into PROTOCOL.md and CHECKLISTS.md.
- **The case-study list.** `case-studies/` here documents the source project's defects as
  teaching material. Your project will accumulate its own; write them when a lesson is
  big enough to deserve narrative.
- **The fixture library.** Fixtures are project-specific by nature. What transfers is the
  fixture *classes*: planted-true-null, vacuity/differ-check on consumed channels, static
  fence/allowlist conformance, output-schema (per-item records + magnitudes), exhaustive
  verdict routing, end-to-end aggregate-verdict fixtures with known answers, bar-arithmetic
  recomputation, estimand-lock. Build each class the first time its trigger fires.

## Growing into orchestration (when one session stops being enough)

Do NOT start with the full multi-seat structure — every governance seat below earned
its existence at a specific pain point, and adopting it before the pain exists is
ceremony. The observed order (ORCHESTRATION.md §4):

1. **Solo director** — everything above, one session at a time. Stay here as long as
   one session can hold the project.
2. **Second concurrent line → add the gatekeeper discipline.** The moment two seats run
   concurrently you need: per-seat write fences, the inbox protocol (commit-first,
   delete-is-ack), and a NON-PARTY gate on cycle closes — `tools/gate_check.py` is the
   mechanical half. One of the seats can hold the gatekeeper hat for the other at
   first; a dedicated scribe seat comes when gate volume justifies it.
3. **First real disagreement → add the registrar.** A standing consult seat that
   constitutes arcs, rules on scope questions, and receives every routed
   NEEDS-JUDGMENT. Your strongest model belongs here.
4. **Rulebook outgrows memory → add the auditor.** Rule-register stewardship, guard
   tooling, planted-error audits on a weekly cadence.
5. **Two lines consume the same corpus → add the producer contract** (the consumer's
   exact reader schema + the MATES line), with or without a dedicated supply seat.
6. **Signature fatigue → move to arcs.** When the human's per-cycle countersigns become
   rubber stamps, switch to arc-level signatures (`templates/ARC-SCOPE.md`) with the
   mechanical gate + compensating controls, and let routine gates self-clear.

The tier economy (ORCHESTRATION.md §6) comes LAST: only move a seat to a cheaper model
after its work is pre-structured and its floor (gate script, fixtures, hash gates) has
run clean for a while at the strong tier — the floor is what you are trusting, so it
must exist and be field-validated first.

## Mid-tier director notes (running the protocol on a smaller model)

- **When in doubt, run the checklist.** CHECKLISTS.md exists to replace the implicit
  judgment a stronger director supplied with explicit steps. Do them mechanically; the
  "do not proceed until" gates are literal.
- **Escalate judgment calls to the user rather than improvising.** If a checklist leaves
  a genuine open decision (which estimand, whether a deviation is a criterion change),
  present it as a framed decision — the tradeoff, your recommendation, what each choice
  consumes — and wait. An improvised resolution of an ambiguity is exactly the A3
  violation the protocol exists to prevent.
- Quote binding rules from the governing docs; never restate them from memory (see
  DIRECTOR.md §6). Include "the registration governs on conflict" in every executor
  brief.
- Prefer arithmetic to argument: if a disagreement can be settled by a 10-line script
  (recompute the bar, recount the raw records, hash the file), run the script.

## Degrading gracefully (solo use, no arbiter CLI)

Without a different-model arbiter you lose the protocol's only source of genuinely
independent judgment. The fallback ladder, weakest last:

1. **Mechanical checks lose nothing** — fixtures, planted nulls, hash freezes, recomputed
   arithmetic, static conformance are model-independent and remain the layer that catches
   most defects anyway. Invest here first.
2. **The human as arbiter**: for pass-criterion changes and line-closing conclusions,
   present the user the exhibits package and the refutation task. Slower, but genuinely
   independent.
2a. **The one REGISTRATION check, when solo, maps onto this ladder too:** rung 2 (the
   human as arbiter) when the registration sets or changes a pass criterion; otherwise
   rung 3, labeled as same-model. It is never skipped silently — a registration that
   got no independent attack says so in its freeze block.
2b. **No countersigning human at all** (fully autonomous use): the gates self-clear by
   construction — keep their ARTIFACTS anyway (each countersign item becomes a dated
   self-clearance stamp stating what it consumed), so the process stays auditable
   after the fact. What you lose is real: no genuinely independent party ever sees a
   line-closing conclusion — treat every one as PROVISIONAL, per the C5 debt above.
3. **Fresh-context self-review is the weak fallback, and must be labeled as such.** A
   fresh instance of the same model, given only the artifacts (never the transcript),
   attacking the favorable verdicts — this removes conversational anchoring but NOT
   shared priors. **Same-model agreement ≠ confirmation**, ever. Any verdict that passed
   only same-model review carries a written scope qualifier ("same-model review only;
   different-model check owed if [named tripwire]") next to the claim, per PROTOCOL C5.
4. What you must NOT do: skip the check entirely for line-closing conclusions. If no
   independent party is available, the line-closing conclusion stays a HYPOTHESIS in the
   record (B1) until one is.
