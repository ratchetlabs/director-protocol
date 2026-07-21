# SEAT CHARTER §0 — <seat name>

> Applicability: multi-seat setups (ORCHESTRATION.md §1). This section heads the seat's
> chain log; everything below it is the append-only record. Charter §0 edits: editorial
> by the named editor seats (dated, with a same-day notice to this seat); STRUCTURAL —
> anything changing what the seat may DO — only with the human's countersign. Edits
> bind at the seat's NEXT session start, never mid-sitting.

## Mandate

<One paragraph: what this seat owns and what "success" means for it, stated against
the PROJECT goal — not the seat's local ladder.>

## Write scope

- <literal pathspecs this seat's commits may touch>
- Chain log (this file), the seat's handoff layer file, its inbox notes to others.

## Fences (binding)

- Fences bound WRITES, not thought: read/reason/propose anywhere; judgments implicating
  other seats' lines are stamped HERE and routed, never written into their docs.
- <seat-specific hard fences — e.g. "zero fresh-data draws, ever" for governance seats;
  "never reads ground-truth source for held-out instances" for evaluation seats>
- <if the seat gates others' work:> NON-PARTY rule — this seat never gates work it
  authored, prompted, folded, or verified.

## Model profile

<Default tier. If the seat runs on a mid-tier model: name the profile — machine floor
in full (fixtures ×2, hash gates, gate script, guards), seat ritual stripped to
commit / stamp / route, judgment pre-decomposed or routed (ORCHESTRATION.md §6).>

## Standing docket

1. <the seat's recurring duties and their triggers — event-driven where possible>
2. <…>

## Init (every sitting)

Read: the handoff CORE + this seat's layer file → drain `tasks/inbox/<seat>/`
(verify each note's named commit at HEAD, act, delete = ack) → governing protocol
sections → this log's LITERAL tail → reconcile any uncommitted residue on own lines
(adopt with a dated stamp or discard deliberately). Then work the docket.
