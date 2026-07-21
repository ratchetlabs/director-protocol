# Case study 05 — The tier transition: moving seats to a cheaper model without losing the floor

*Anonymized from a real project's records. Numbers are exact. The transition was
user-directed ("that will help with the strongest-model tokens immediately") and executed
in one day across three seats; the profile it ran under is ORCHESTRATION.md §6.*

## The situation

The project ran roughly ten parallel director seats — build lines, a gatekeeper (scribe),
a machine-executor seat, a supply/producer seat, a registrar, an auditor — all on the
strongest available model tier. Cost forced the question: which seats actually need
frontier-tier judgment *per sitting*, and which are running pre-structured work under
mechanical controls?

The candidates chosen were the three most mechanized seats: the **gatekeeper** (runs the
conformance gate and writes the shared ledgers), the **machine executor** (a build seat that
drains a pre-adjudicated adoption backlog — units already ruled on by the registrar —
against a human-signed component manifest and an acceptance bench), and the
**producer** (mints corpora to an enumerated consumer schema behind certification
fixtures). The registrar and the judgment-heavy build seats stayed on the strong tier.

## The profile (decided BEFORE the move, not improvised during it)

**KEEP — everything a machine runs, cut nothing:** the conformance-gate script, fixture
suites run twice byte-identical, hash freeze/re-hash tooling, the data-ledger claim tool,
command guards, the named human gates.

**STRIP — the seat ritual**, replaced by three duties: commit own-scoped paths at event
boundaries; stamp what you did, dated, any format; when in doubt, route to the registrar
and continue what is not in doubt.

**Judgment pre-decomposed or routed, never attempted solo:** each transitioning seat's
charter gained a banner naming the profile, and its queued work was pre-structured into
closed-ended steps ("run Y, expect Z, else route") at a strong-model sitting before the
flip. The gate's three mechanical legs were extracted into a script (`tools/gate_check.py`
here is its generalized form) whose contract is: PASS / FAIL / **NEEDS-JUDGMENT routes to
the registrar** — the tool never judges.

## What happened on day one

**The gatekeeper's first cheap-model gate** ran the script (17/17 hashes exact, data
audit pass, 11 boundary rows PASS + 3 NEEDS-JUDGMENT) and **routed all three judgment
rows** instead of ruling on them. The registrar answered with a standing ruling; the
gate closed CONFORMS the same day. The seat's own-error register (the "errors found in own thinking" line,
DIRECTOR.md §4a) from that sitting records it catching itself mid-draft re-acquiring removed judgment ("CONFORMS with a
separate caveat" — a judgment shape) and routing instead — the profile's intended
behavior, self-enforced.

**The same sitting, the gatekeeper self-caught two real errors:** (1) it first parsed a
shared queue structure as a list and nearly recorded a false "claimed row is missing"
finding — caught because two other seats' committed numbers contradicted its count, and
the contradiction triggered a re-derivation at the bytes; (2) its first ledger write
re-encoded the whole file (63 spurious line changes for a one-row edit); it reverted and
rewrote to the claim tool's own serialization convention (final diff: 2 lines).

**The machine executor's first cheap-model sitting** opened by re-reading its queue at
the bytes and **refuting its own line's predecessor — a committed claim by an earlier
session of the SAME seat** (correcting your own line's record is in scope; another
seat's record is routed, never edited — ORCHESTRATION.md §1) — a strong-tier sitting
had written "executable queue EMPTY" the previous day, and the count was false at write
time (a row had landed 14 hours before the claim; the predecessor had carried a derived
count into a checkpoint without re-reading the source). The cheap-model seat corrected
the record, ratcheted the lesson, and **routed the judgment-shaped question** (how to
adopt the newly-found unit) to the registrar rather than inventing structure solo.

**The registrar's watch converged to sampling.** It spot-verified the transitioned
seats' first commits at the bytes: both passed, the second "above the floor" (the seat
re-derived a near-miss judgment own-hands where the profile required only mechanical
legs). After two clean passes the watch dropped from every-commit to sampling, with
NEEDS-JUDGMENT arrivals as the tripwire.

## What this shows

1. **Ritual is calibrated to the model; floors are calibrated to the claims.** The
   cheaper model got *less* ceremony and *more* mechanical checking — and the floor
   (script + fixtures + hash gates + routing) carried the safety, not the model tier.
2. **"Route, don't rule" is teachable as a mechanical contract.** The gate script's
   NEEDS-JUDGMENT verdict gives a weaker model a *legal move* that is always correct —
   the day-one behavior showed the seats taking it under real ambiguity.
3. **The most notable single event was a cheap-model seat correcting a strong-model
   seat's committed error** — because the discipline ("counted state is re-read from
   source at every boundary; bytes before statements") is model-independent, and the
   cheaper seat ran it faithfully.
4. **The watch is cheap because routing is structural.** Supervision cost collapsed to
   spot-checks precisely because anything judgment-shaped arrives at the registrar by
   construction rather than needing to be hunted for.

## The rules this created or confirmed

- The **tier profile** itself (ORCHESTRATION.md §6): keep the machine floor, strip the
  ritual, pre-decompose or route judgment.
- **Counted state is re-read from its source at every checkpoint boundary** — never
  carry a derived count forward; never write a prohibition on top of one.
- **A gate tool must be field-validated the same day it ships** — the script's first
  live gate doubled as its acceptance test, with the registrar verifying the routes.
- **Watch new transitions at every commit, then sample.** Two clean spot-verifies at
  the bytes license the drop; a NEEDS-JUDGMENT anomaly re-raises the cadence.
