# <sender> → <receiver>: <one-line headline>

> File name convention: `tasks/inbox/<receiver>/<date>-<sender>-<slug>.md`.
> Rules (ORCHESTRATION.md §3): COMMIT FIRST, note second — the note names the commit
> hash of the committed fact it reports; a hash that does not resolve at HEAD means the
> note is not-yet-sent. Receiver verifies the fact at the bytes, acts, then DELETES the
> note (delete = ack). Anything present in an inbox IS the unprocessed set.

**Committed fact:** `<commit hash>` (<what it is: artifact commit or chain-log stamp,
with the doc + section>).

<2–6 sentences: what happened, what the receiver is expected to do with it — or
explicitly "no action expected; FYI".>

**Blocking?** <NO — informational, no response expected. | YES — this blocks
<sender>'s <what>; posted <date, time-of-day>; if no response in <30 minutes>,
sender raises to the human (diagnostic only — silence is never consent).>

**MATES:** <YES/NO/UNCERTAIN — for deliveries the receiver consumes into a verdict:
walked at THEIR consuming bytes; one clause on what could make it lie or go silently
dead. Omit for pure FYIs.>
