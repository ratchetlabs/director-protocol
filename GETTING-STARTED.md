# GETTING STARTED — a working setup in ~10 minutes

This is the hands-on path: copy the files, wire the commands, run the one shipped tool,
and walk your first cycle. The concepts live in [README.md](README.md) and
[PROTOCOL.md](PROTOCOL.md); this file is just "make it work."

**Prerequisites:** `git`, `python3` (any recent 3.x, no packages needed), and an LLM
coding harness that can read your project files (the `claude/` commands assume Claude
Code; any harness with custom commands works — see ADAPTING.md).

## 1. Vendor the protocol into your project

From your project root:

```sh
git clone https://github.com/ratchetlabs/director-protocol.git docs/director-protocol
# or: git submodule add <url> docs/director-protocol
```

Copy the pieces your project instantiates (the rest is referenced in place):

```sh
mkdir -p .claude/commands tasks
cp docs/director-protocol/claude/commands/*.md .claude/commands/
cp docs/director-protocol/templates/lessons.md tasks/lessons.md   # EMPTY on purpose
cat docs/director-protocol/claude/CLAUDE-md-block.md >> CLAUDE.md
```

Then edit the pasted block in `CLAUDE.md`: point its `PROTOCOL.md` / `CHECKLISTS.md`
references at `docs/director-protocol/`.

## 2. Smoke-test the one shipped tool (60 seconds)

The conformance gate ships ready to run against its starter ledger:

```sh
cd docs/director-protocol
python3 tools/gate_check_selftest.py        # expect: selftest: 11/11 pass
```

Now run it on a toy manifest to see the three verdicts:

```sh
cat > /tmp/demo_manifest.json <<'EOF'
{
  "packet": "demo",
  "files": [{"path": "README.md", "md5": "00000000000000000000000000000000"}],
  "data_ranges": [[1000, 1004], [5000, 5001]],
  "scope_pathspecs": ["src/"],
  "touched_paths": ["src/x.py", "tasks/lessons.md", "docs/notes.md"]
}
EOF
python3 tools/gate_check.py /tmp/demo_manifest.json
```

Read the output: the bogus hash **FAILs** (re-hash leg) · `[1000,1004]` **PASSes**
(exact starter-ledger claim) while `[5000,5001]` is **NEEDS-JUDGMENT** (unclaimed —
the tool routes, it never guesses) · `src/x.py` passes the boundary, `docs/notes.md`
is NEEDS-JUDGMENT (outside scope), and `tasks/lessons.md` is
**EXEMPT-PENDING-FORM-CHECK** (standing-law path — exempt from arc scope, but the
gatekeeper still owes one manual form-look; hand-edits remain defects). The tool
exits **nonzero** while any FAIL remains — deliberate, so a wrapping script refuses
too. That refusal-to-guess contract is the whole design (ORCHESTRATION.md §5).

You will not need this tool until you run multiple seats — but now you know it works
and what its output means.

## 3. Start your first experiment line

```sh
mkdir -p experiments/<line>/v1/{code,fixtures}
cp docs/director-protocol/templates/BUILD-LOG.md      experiments/<line>/BUILD-<line>.md
cp docs/director-protocol/templates/REGISTRATION.md   experiments/<line>/v1/REGISTRATION-<exp>.md
```

Fill the registration BEFORE writing experiment code: the claim, the decision bar
(with computed false-fail + power, or the deterministic exception), the data blocks,
the prediction table. Freeze it with a manifest:

```sh
cd experiments/<line>/v1
md5sum code/* REGISTRATION-<exp>.md > manifest.md5    # macOS: md5 -r
```

and add the ~5-line re-hash gate at the top of your scored harness (recipe: ADAPTING.md,
"Freeze-manifest format + the re-hash gate") so the run **refuses** on any mismatch.

## 4. Run the cycle

In your harness, invoke the `director` command (or paste `claude/commands/director.md`
as the session's first instruction). The session initializes from your handoff + chain
log, then follows the lean cycle: registration review (CHECKLISTS §2) → the ONE
arbiter check (§3–4; no arbiter CLI? see ADAPTING "Degrading gracefully") → your ONE
countersign → build + fixtures → predictions into the chain log BEFORE the output
exists (§6) → run → forced fresh look (§7) → verdict write-up (§9). End every session
with the `save` command; resume every session with `director`.

## 5. When you outgrow one session

Read [ORCHESTRATION.md](ORCHESTRATION.md), then ADAPTING.md "Growing into
orchestration" — add seats stepwise at the pain points, not all at once. The
templates (`SEAT-CHARTER`, `ARC-SCOPE`, `INBOX-NOTE`, `GATE-MANIFEST`) and the gate
tool from step 2 are waiting for that moment.

**Stuck?** Every mid-cycle "what now?" has a matching checklist in
[CHECKLISTS.md](CHECKLISTS.md) — find the moment you're in, run its list literally.
