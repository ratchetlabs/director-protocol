# Case study 04 — The lean audit: which process layers actually catch defects

*Anonymized from a real project's process audit. The audit was user-directed ("the
process is too complicated and bound by formality; get what is actually required while
removing unneeded steps") and produced the lean protocol that is now PROTOCOL.md §G.*

## The question

After weeks of verdict-bearing cycles, the project's process had accreted layers: a
director pre-review, a pre-freeze review, a mandatory different-model adjudication at
registration, a separate user go/no-go gate after the countersign, a build-complete
review, a mandatory post-run different-model adjudication, sometimes parallel
fresh-context AND different-model post-run passes, plus status mirroring of every
decision into four documents (registration, project registry, handoff, memory).

The audit walked the full history of caught defects and asked one question per layer:
**what did this layer catch that nothing cheaper had already caught?**

## What actually caught defects

| Layer | Record |
|---|---|
| **Construction fixtures** (schema assertions, exhaustive routers, byte-level differ-checks) | Caught defects continuously, at build time, for free — including aggregation bugs that per-component tests were blind to |
| **Planted nulls / vacuity probes** | Caught the project's worst miss (case 01) in one step, post-run, after three review layers passed it |
| **Static conformance checks** (registered inputs vs every layer's allowlist, by inspection) | Caught a mid-run construction stop; as a fixture, caught the same class at *registration* in the next cycle |
| **Pre-computed arithmetic** (false-fail/power recomputed from scratch) | Caught constant-transcription and reference-distribution errors; made case 02's class impossible to re-register |
| **Directed post-hoc adversarial review of SURPRISING outcomes** (a fresh-context pass or a different-model arbiter, briefed with named suspects and required to recount from raw records) | Caught case 02's union-bar arithmetic; caught a comparator that couldn't move its scored channel; overturned a false "line exhausted" conclusion |
| **The ONE pre-execution different-model check, when briefed with directed attack lines** | Extracted real corrections at registration (including a genuine pin-mismatch defect) — earning its single slot |

## What caught nothing

- **Duplicate pre-approvals** (director pre-review + pre-freeze review + build review as
  separate ceremonies): never caught anything the fixtures and the single build-complete
  pass didn't. Collapsed into ONE director pass at build-complete.
- **The separate go/no-go gate** after the countersign: the hash-freeze/re-hash machinery
  already guaranteed nothing drifted between signature and run — the gate was a second
  signature guarding against a drift that was mechanically impossible. Retired; the one
  countersign now explicitly consumes the data blocks.
- **Parallel same-verdict arbiters** (running fresh-context AND different-model post-run
  reviews by default): when they agreed, the second added cost, not information;
  disagreement was the only informative outcome. Replaced by escalate-one,
  second-only-on-disagreement.
- **Status mirroring** into four documents at decision time: pure transcription load and
  a source of inconsistency defects. Replaced by one chain-log doc per line, mirrors at
  checkpoint only.

## The decisive fact

**Both of the project's two worst misses sailed through the maximum-ceremony
configuration.** The vacuous null (case 01) and the mis-constructed bar (case 02) were
each authored, adversarially adjudicated by a different model family, and human-
countersigned — three layers, two model families, and a human — and both were caught only
by mechanical post-run checks and directed adversarial recounts. In case 02 the arbiter
had *authored* the defect it approved. Ceremony density did not correlate with catch
rate; check mechanization did.

## The rules this created (the lean protocol, PROTOCOL.md §G)

1. **Fixtures over review steps.** A new failure mode becomes a FIXTURE first; a review
   step only if no fixture can express it.
2. **One honest adversary over three charitable ones.** ONE directed different-model
   check at registration; post-run, director recount by default, escalation to ONE
   arbiter only for disputed / line-closing / favorable-and-load-bearing verdicts; a
   second arbiter only on disagreement.
3. **One user gate per cycle**, explicitly consuming the data blocks; the freeze
   machinery replaces the second signature.
4. **One chain-log doc per line**; mirrors at checkpoint only.
5. **Ratchet hygiene**: every new lesson must answer "which existing step does this
   retire?" — the ratchet may tighten checks while thinning ceremony.

What lean did **not** relax: pre-registration and freezes, verdict vocabulary, dual
reporting, "same-model agreement ≠ confirmation," the lessons ratchet, and the mandatory
different-model refutation attempt before any line-closing conclusion.
