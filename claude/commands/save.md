---
description: Prepare a clean session checkpoint for restart (reconcile docs, write HANDOFF, save memory, print briefing).
---

The user is about to restart the session. Produce a **full checkpoint** so a fresh
session continues seamlessly. Do exactly these four steps, in order, then stop.

The authoritative specs are the project's design docs and the per-line chain logs
(`BUILD-<line>.md`); decisions live in docs, not in chat (PROTOCOL E3). Honour those
conventions throughout. If the project uses git, commit the checkpoint when done (never
commit secrets or raw experiment recordings); do not push unless asked.

**1. Reconcile the docs with reality.** Look at what this session actually changed. If a
component landed, a decision was locked, a verdict was filed, or status moved, make sure
the authoritative doc reflects it — status lines, DONE markers *with the measured
numbers*, chain-log entries. Only edit what is genuinely stale; do not restate things
already written. If nothing is stale, say so and move on.

**2. Write/refresh `HANDOFF.md`** at the project root (overwrite it — it is a living
checkpoint, not an append log; template: `templates/HANDOFF.md`). Keep it scannable.
Include:
   - **Date** and a one-line session headline.
   - **First actions on restart** — in order, starting with "read the governing protocol
     section before any verdict-bearing work."
   - **Done this session** — what landed, with the pass evidence (numbers, artifacts,
     verdicts with their exact vocabulary).
   - **Current state** — where each experiment line stands, plus the data-block ledger
     (consumed vs free).
   - **Open questions / risks** — anything unresolved, including honest caveats recorded
     with the last result (live hazards, carry-forward flags — don't bury them).
   - **Decisions made but not yet in the specs** — anything agreed this session that
     hasn't been written into a governing doc yet.
   - **RISKS TO PROJECT** — unconditional (PROTOCOL §G.27); "NONE identified" is legal
     but must be written; every named risk reports its disposition (cured or routed),
     never a bare worry.
   - **Resume commands** — the exact shell lines to re-verify the current state.
   *(Multi-seat setups: write YOUR seat's layer file `tasks/handoff/<seat>.md`, not the
   shared core — see `templates/HANDOFF.md`.)*

**3. Save/refresh the project memory** (whatever persistent-memory mechanism the harness
provides): ONE entry capturing the *non-obvious* "where we are / what's next" hook — the
orientation that lets the next session start fast. Convert relative dates to absolute. Do
not duplicate what HANDOFF already records verbatim. Update the existing entry rather
than creating a duplicate.

**4. Print a tight restart briefing** to the chat (not a file): one short paragraph of
current state, the single next action, the open threads, and an **"errors found in my
own thinking this session"** line — self-caught errors are successes and are reported
by name (DIRECTOR.md §4a), never buried. End by pointing to `HANDOFF.md` for the
detail.

Do not start the next task — just checkpoint.
