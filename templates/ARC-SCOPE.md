# ARC SCOPE — <ARC-NAME> (for signature)

> Applicability: multi-seat setups running arc-level signatures (ORCHESTRATION.md §5).
> The human signs SCOPES, not cycles; inside a signed arc, cycle closes go through the
> non-party mechanical gate (CHECKLISTS.md §11). A request without the purpose summary
> is returned unsigned.

## Purpose summary (plain language, FIRST)

<What question does this arc put to the project goal? Why now? What does the project
gain if it succeeds — stated as INFORMATION ACQUIRED, skeptic-checkable later — and
what does it lose if skipped? 3–6 sentences, no jargon. This must agree with the
`goal_gain` row below.>

## Scope table (every row enumerated — no TBD cells)

| Field | Value |
|---|---|
| `goal_gain` | <if this succeeds the project learns ___; if skipped it loses ___> |
| Claim class | <the ONE class of claim this arc may produce — name it and keep the vocabulary stable across arcs, e.g. "instrument-tier certification" (a tool works as specced) vs "evidence-tier result" (a claim about the world)> |
| Venues | <environments / datasets / corpora the arc touches> |
| Interface surfaces | <each surface, tagged read / write / freeze> |
| Pathspecs (write scope) | <the literal path prefixes the arc's commits may touch> |
| Data-budget ceiling | <max fresh data blocks this arc may draw, e.g. "≤ 6 blocks"> |
| Gate-count bound | <max mechanical-gate closes before the arc must re-pose, e.g. "8"> |
| Expiry | NONE BY DATE — closure, exhaustion, or suspension only |

## Compensating controls (what keeps scope-level signing honest)

- **Same-day digest** to the human with required fields <list them>; a missed digest
  AUTO-SUSPENDS the arc.
- **Suspension at will**: the human may suspend any time; suspension blocks new gates
  and cancels unstarted runs.
- **Planted-error audits** (auditor seat, <weekly> cadence): deliberately defective
  packets through the real gate; a missed audit reverts all arcs to per-decision
  scope cards until the human rules.

## Out-of-scope triggers (what forces a scope card back to the human)

- Any write outside the pathspecs that is not standing-law machinery in mandated form.
- Any claim outside the claim class; any data draw beyond the ceiling.
- Any semantic-interpretation question at a gate (the gate is set-membership only).

**Signature line:** signing this arc authorizes every in-scope cycle through the
gate-count bound, data draws to the ceiling via your ledger's claim script (ADAPTING.md,
tools row), and DELEGATES per-cycle countersigns to the mechanical gate. <date, signer>
