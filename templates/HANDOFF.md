# HANDOFF — <project>

> **Multi-seat setups:** split this into a small CORE (this file: shared ledgers,
> cross-seat law, ONE line per seat) plus one **layer file per seat**
> (`tasks/handoff/<seat>.md`: seat state, first actions, fences) that the seat reads at
> init and writes at save — no write contention on parallel days. The core's per-seat
> lines are awareness, not truth: **the chain log always wins**; a seat about to act on
> a line reads its literal tail. Add a "RISKS TO PROJECT" section to every layer file —
> "NONE identified" is legal but must be written (PROTOCOL.md §G.27).
>
> **Ceilings + rolls (init-cost law, ORCHESTRATION.md §9):** seat rows carry a HARD
> character ceiling (ours: 350 live, 200 retired-stub) — state · blocked-or-not ·
> next event · layer pointer, detail ONLY in the layer file. Each seat trims its OWN
> row. Prose strata roll to an archive file as VERBATIM MOVES with dated roll headers
> — move-or-delete, never re-characterize. Writes to the shared CORE go under an
> advisory lock, assembled in memory and written once; read the staged diff before
> committing so a peer's concurrent edit is unstaged, never swept.

**Date:** <date> (<who is directing / executing / arbitrating>).
**Headline: <one sentence — the biggest thing that changed and where the project now
stands>.**

## FIRST ACTIONS ON RESTART (in order)

1. **Read <the governing protocol section>** before any verdict-bearing work.
2. **<The single next verdict-bearing item>** — with everything a fresh session needs to
   act: which chain log governs, which binding items apply, which data blocks are free,
   what the lean chain for it looks like (draft → arbiter → ONE countersign → build →
   run → D4).
3. **<Parallel threads>**, each with its owner and status-of-record doc — a fresh session
   must know which lines it does NOT own.

## Done this session

- <What landed, with the pass evidence — the numbers, the artifacts, the verdicts of
  record with their exact B1 vocabulary. Point at chain-log sections, don't restate.>

## Current state

- <The experiment ladder: which lines CONFIRMED / OPEN / BLOCKED, in 2–4 lines.>
- **Data blocks (A4 ledger):** consumed: <…>. Free: <…>.
- <Process state: which protocol version governs.>

## Open questions / risks

- <Unresolved items and honest caveats recorded with the last results — including live
  criterion-shopping hazards, carry-forward sensitivity flags, sealed quarantines. Don't
  bury them.>

## Decisions made but not yet in the specs

- <Anything agreed this session not yet written into a governing doc — or "None known".>

## Resume commands
```sh
open "HANDOFF.md"
open "<protocol doc>"          # governing section — read before verdict-bearing work
open "<chain log of record>"   # the line's full record
<the exact shell lines that re-verify the current state: re-run fixtures, print the
verdict fields from the output of record>
```
