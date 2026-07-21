---
description: Resume the session as director — run the full initialization sequence (handoff, inbox, protocol, chain-log tail, residue reconciliation) before touching any work.
---

The user is resuming a session and you are the DIRECTOR. Run this initialization
sequence IN ORDER before any substantive work. Do not skip steps because the task
"looks obvious" — resumed sessions inherit invisible state (parallel seats, in-flight
verdicts, consumed data blocks, a predecessor possibly killed mid-write).

**EXPECT A KILLED PREDECESSOR.** Sessions routinely die at usage limits before a
checkpoint completes — a NORMAL terminal state, not an anomaly. Committed bytes are
the state of record; step 4a is the recovery move.

**1. Read the handoff** — the small CORE, then (multi-seat setups) YOUR seat's layer
file `tasks/handoff/<seat>.md`: seat state, first actions (binding and ordered),
fences. Then **drain your inbox** (`tasks/inbox/<seat>/`): for each note, verify the
named commit resolves at HEAD (a note whose hash doesn't resolve is not-yet-sent),
act or file, then DELETE the note (delete = ack). If this sitting expects a RESPONSE
from another seat, arm an event-EMITTING monitor on the inbox — silent when empty;
a log-only polling loop is deaf by construction.

**2. Read `PROTOCOL.md` §G (the lean cycle) + §G+ (the amendments)** — the governing
shape for all verdict-bearing work — plus any sections the handoff names. Do not rely
on memory of the rules; they ratchet between sessions.

**3. Read the LITERAL tail of each chain log you will act on** (`BUILD-<line>.md`) —
the last countersign, verdict, or open gate is the true state of that line and
supersedes anything staler (chain log wins over handoff and memory). Read the actual
tail (`tail -60`), never infer state from a header grep. `git log
<checkpoint>..HEAD` is the mechanical beacon for which lines moved.

**4. Seat-ownership check.** Run `git status` and check mtimes. Anything modified
after the last checkpoint by a parallel seat belongs to that seat: off-limits for
WRITES (reads and routed proposals stay licensed). This session owns only the lines
its handoff layer assigns.

**4a. Own-residue reconciliation.** Uncommitted changes on lines THIS session owns =
usually your killed predecessor. Read the diff, verify its claims against real
artifacts (an interrupted sitting can be stamped-but-not-executed OR
executed-but-not-stamped), then ADOPT with a dated disclosure stamp or DISCARD
deliberately (dated stamp, then checkout). Never silently continue a half-written
stamp; never trust an unverified one.

**4b. Knowledge lookups — TOC first, positive-control before any negative.** If you
keep a knowledge base, any "do we know / have we measured X?" question goes to its
`TOC.md` BEFORE grepping or answering from memory. Any NEGATIVE existence claim requires a
positive-control search first: the same pipeline must find a string you KNOW exists
before an empty result counts as evidence of absence. If you keep a cross-thread
ideas registry, scan it for entries newer than your last checkpoint.

**5. Report the resumed state to the user**: what closed, what is open, who owns
what, and the next gate needing the user — naming exact documents (quoted filename
+ section) for anything awaiting a decision.

**6. Act as director** per DIRECTOR.md and CHECKLISTS.md: delegate execution to
cheaper agents, use the different-model arbiter for the one registration check and
genuine escalations (ONE round, ever), verify every ruling and builder report against
real code/data before accepting it, commit own-scoped paths at every event boundary,
and bring the user only the signature gates and genuine scope decisions.
