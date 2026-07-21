# DESIGN — Discovery and Design: the Adversarial Front End

The verdict machinery in [PROTOCOL.md](PROTOCOL.md) certifies answers to
well-posed questions. It cannot rescue a badly posed one: a build that freezes the
wrong estimand, bakes in an assumption nobody challenged, or answers a question the
project didn't need will produce impeccably certified junk. In the source project,
the registered-cycle discipline **worked because the same adversarial structure ran
upstream of it** — on discovery (what is true about the problem space?) and on
design (what should we build, and why this and not the rival?). Without that front
end, the rest would have been rigor applied to the wrong object.

The pipeline is three phases with the same shape at different formality:

```
EXPLORE (RESEARCH.md)      →  DESIGN (this doc)              →  REGISTER (PROTOCOL.md §G)
answer-seeking search,        adversarial decision-making,      frozen criteria, fixtures,
no verdicts, cheap kills      frozen design docs                one arbiter round, verdicts
```

Each phase hands the next a committed artifact: exploration graduates a track with a
log line; design freezes a doc the registration cites; nothing crosses a boundary as
a vibe.

## 1. Present the unconstrained best option FIRST

A standing rule from the source project's founder, after a real incident where a
session silently down-ranked the best approach on an assumed budget constraint:

> When evaluating approaches, ALWAYS identify and present the unconstrained best
> option — the right way to accomplish the goal, at the field's frontier — BEFORE
> applying any filter for presumed circumstances (compute, cost, timeline, staffing).
> Present best-then-feasible and let the human make the tradeoff.

LLMs are eager to be helpful about your constraints, and that helpfulness is a
design-time bias: it pre-filters the option space before the decision-maker ever
sees it. The rule makes the filter explicit and moves it to the human. In practice
every design discussion produces two answers — "the right way" and "the feasible
way" — and the gap between them is itself information the project owner needs.

## 2. Every significant decision gets a red-team pass — with NAMED voices

The single highest-value design discipline, and the cheapest (PROTOCOL.md C6 is the
in-cycle form). Before a strategic or architectural decision counts as *made*, the
director voices the positions a real lab would raise, **steelmanned, minimum three,
each with a name**:

- **The skeptic** — why the evidence for this choice is weaker than it looks.
- **The rival approach** — the strongest competing design, argued as its champion
  would argue it, not as a strawman.
- **The won't-scale worry** — where this breaks at 10× the load, data, or team.
- **The wrong-problem worry** — whether this decision serves the actual goal or
  just extends what happened to get built last.

Any canonical voice omitted is NAMED with a one-line reason it doesn't apply. The
pass is written into the decision record ("Red-team:" and then the voices), so both
parties can see the decision survived a challenge — and so a later session can see
*which* challenge it survived, which is what makes revisiting cheap. One-voice
passes and token objections are non-compliant; the observed failure mode is a
model generating three sentences of pro-forma doubt and proceeding. A steelman
that never changes an outcome across many decisions is itself a red flag the
audit watches for.

Two structural notes from production: author names and paper prestige are data
points, not endorsements — the rival approach gets argued on mechanism; and when
the human is new to the field, the director is explicitly instructed to **push
back rather than defer** (see [DIRECTOR.md](DIRECTOR.md)) — deference at design
time is how a project inherits its owner's untested assumptions.

## 3. Arcs open question-first, never capability-first

The goal-gain rule (PROTOCOL.md §G.15) applied at its most important site. A unit
of design work opens by naming the QUESTION it puts to the project's goal — what
the project learns or gains, stated first, before any description of the thing to
be built. "Build the X module" is not a design mandate; "we cannot currently
distinguish A from B, and X would let us — here is what changes if it does" is.
The observed drift this prevents is real and gradual: systems accrete capability
because each next brick is adjacent to the last one, and six weeks later nobody
can say which question the pile answers. If the gain is thin, the director
redesigns the unit; if no one can say why it matters, it doesn't get built.

The companion standing test from the source project generalizes past its origin
domain: anything discovered or tuned by hand for one instance is a *labeled
example* for a general mechanism, not a constant to bake in. The design question
is always "what mechanism would have found this, and would it find the analogue
in the next case?" — a sharp test for whether a design is solving the problem or
memorizing the first instance of it.

## 4. Architecture docs open with a layer map; design docs are state

Every architecture document opens with a **§0 bottom-up layer map**: each layer
one row — what it consumes, what it produces, whether it is frozen, and its
STATUS. This is the five-minute orientation that lets any later session (or any
second seat) load the design without re-deriving it, and it is the surface where
staleness becomes visible — a layer marked live that nothing consumes anymore is
a finding.

Design docs follow the same documentation-as-state rules as everything else
(PROTOCOL.md E-series): decisions made in conversation that no doc records did
not happen; superseded designs get a dated supersession stamp and a pointer, never
a silent edit or deletion. In a multi-session project the design doc IS the
design; the conversation that produced it is scratch.

## 5. Freeze the design, then give it ONE adversarial check

The same freeze-then-arbiter shape the registered cycle uses (§G steps 1–3),
applied one level up. When a design stabilizes: hash-freeze the doc, then ONE
round with a different-model arbiter attacking the *design* — what is
over-constrained, what rival was dismissed too fast, which stated requirement the
architecture doesn't actually meet, what the first build will discover that the
doc assumes away. The director verifies the ruling against the actual problem
(a ruling earns a check), folds what survives, and the frozen design becomes the
document registrations cite. Post-freeze changes are dated amendments, never
edits — the registered cycle downstream depends on the design it cites holding
still.

This is where design connects to build: a registration that cites a frozen design
doc inherits reviewable intent. When implementation surfaces an ambiguity the
design didn't settle, that is a **deviation-log event** (PROTOCOL.md A3) — logged
and resolved explicitly, never silently resolved in code. The worst design
failures in the source project were exactly silent in-code resolutions of
ambiguities the design never noticed it had.

## 6. The kickoff block — the last gate before building

Before the FIRST build action on any line, the builder session writes a 5-line
kickoff block into the line's chain log:

1. The goal in ONE sentence.
2. The governing frozen docs ACTUALLY READ this session — each with a verbatim
   quoted constraint (the quote is proof of contact; a doc "read" without a quote
   wasn't).
3. Two or three ways this build could be WRONG.
4. What it might duplicate — checked by search, not memory (same-team amnesia
   across renamed efforts is the proven failure mode; an inherited "no overlap"
   claim is verified, never trusted).
5. The cheapest probe that would falsify the approach.

No building until the block exists. It costs five minutes and it is the highest
defect-per-line artifact in the whole discipline: item 2 catches designs about to
be violated unread, item 4 catches the second implementation of an existing tool,
item 5 has repeatedly turned a week of building into an afternoon probe that
killed the approach honestly. Trivial mechanical follow-ons inside an
already-kicked-off line are exempt — the block gates lines, not keystrokes.

## Failure modes this front end exists to catch

| Failure | The discipline that catches it |
|---|---|
| Best option silently pre-filtered by assumed constraints | §1 unconstrained-best-first |
| Decision made by momentum, no challenge on record | §2 named-voices red-team |
| Building capability adjacent to capability, goal drifted | §3 question-first arcs |
| Design lives in a conversation; second session re-derives or contradicts it | §4 docs-as-state + layer maps |
| Design assumed sound because it is written down | §5 freeze + one arbiter round |
| Build starts on an unread spec; duplicates existing work; no falsifier named | §6 kickoff block |
| Ambiguity resolved silently in code | §5→A3 deviation log |

None of these require the full registered cycle — they are cheap, they are mostly
writing, and they are where the project's real leverage sits. The registered cycle
guarantees you can trust the answer; the front end is what makes the question
worth answering.
