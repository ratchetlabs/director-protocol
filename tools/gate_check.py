#!/usr/bin/env python3
"""gate_check.py — the non-party conformance gate as an executable checklist.

The mechanical half of the cycle-close gate (ORCHESTRATION.md §5). It NEVER
judges: every check emits PASS / FAIL / NEEDS-JUDGMENT, and NEEDS-JUDGMENT
routes to your registrar (or the human) — the tool refusing to guess is the
design, not a limitation.

Three legs:
  REHASH      — re-hash every claimed artifact from its canonical path
  DATA-AUDIT  — fresh-data-block claims vs. the shared ledger (full output)
  BOUNDARY    — every touched path, set-membership against the declared scope

Input: a gate manifest JSON the gatekeeper fills from the packet under review:
{
  "packet": "<free-text id: stamp doc + section>",
  "files":  [{"path": "...", "md5": "<claimed>"}, ...],
  "data_ranges": [[lo, hi], ...],
  "scope_pathspecs": ["src/experiment-x/", ...],
  "touched_paths": ["...", ...]
}

Output: a filled stamp skeleton on stdout — every count names its derivation
(the §G.16a discipline). Exit 0 iff no FAIL (NEEDS-JUDGMENT does not fail the
tool — it fails the gate until routed and answered).

Ledger: tools/data_ledger.json (see the shipped starter file for the schema).
Selftest: tools/gate_check_selftest.py — run after ANY edit to this file.
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("GATE_CHECK_REPO") or os.path.dirname(HERE)
# Both the DATA-AUDIT leg and the standing-law form check read THIS ledger —
# deriving both from REPO keeps the two legs auditing the same file.
LEDGER = os.path.join(REPO, "tools", "data_ledger.json")


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_rehash(files):
    out = []
    for f in files:
        p, claimed = f["path"], f["md5"].lower()
        if not os.path.exists(p):
            out.append(("FAIL", p, "MISSING-AT-PATH (claimed %s)" % claimed))
            continue
        actual = md5_file(p)
        out.append(("PASS" if actual == claimed else "FAIL", p,
                    "claimed %s / actual %s" % (claimed, actual)))
    return out


def check_data(data_ranges, ledger):
    """Mechanical presence + collision audit, full output. Membership questions
    beyond exact claim matches are NEEDS-JUDGMENT, never guessed."""
    out = []
    claims = ledger.get("claims", [])
    voids = [v["range"] for v in ledger.get("void_blocks_never_reusable", [])]
    frontier = ledger.get("frontier_of_record")
    for lo, hi in data_ranges:
        hits = [c for c in claims
                if not (hi < c["range"][0] or lo > c["range"][1])]
        exact = [c for c in hits if c["range"] == [lo, hi]]
        void_hits = [v for v in voids if not (hi < v[0] or lo > v[1])]
        if void_hits:
            out.append(("FAIL", [lo, hi], "overlaps NEVER-REUSABLE void %s" % void_hits))
        elif exact:
            c = exact[0]
            out.append(("PASS", [lo, hi],
                        "exact ledger claim: owner=%s status=%s" % (
                            c.get("owner"), c.get("status"))))
        elif hits:
            out.append(("NEEDS-JUDGMENT", [lo, hi],
                        "partial overlap with claim(s) %s — membership is a ruling, route it"
                        % [(c.get("owner"), c["range"]) for c in hits]))
        else:
            out.append(("NEEDS-JUDGMENT", [lo, hi],
                        "NO ledger claim covers this range (frontier_of_record=%s) — "
                        "unclaimed consumption is a ruling, route it" % frontier))
    return out


def form_check_data_ledger(repo):
    """Standing-law form check for the shared ledger itself: claims pairwise
    disjoint, frontier strictly past every recorded range, required keys
    present. A ledger edited outside its claim tool tends to break exactly
    these invariants — which is the point of checking them at the bytes."""
    path = os.path.join(repo, "tools", "data_ledger.json")
    try:
        d = json.load(open(path))
        claims = d["claims"]
        ranges = sorted(c["range"] for c in claims)
        disjoint = all(ranges[i][1] < ranges[i + 1][0] for i in range(len(ranges) - 1))
        all_his = [c["range"][1] for c in claims] + \
                  [v["range"][1] for v in d.get("void_blocks_never_reusable", [])]
        frontier = d["frontier_of_record"]
        past_all = all(frontier > h for h in all_his)
        keys_ok = all({"range", "owner", "status"} <= set(c) for c in claims)
        ok = disjoint and past_all and keys_ok
        return ok, ("claims disjoint=%s frontier(%s)>every recorded hi=%s claim keys ok=%s "
                    "(derivation: tools/gate_check.py invariants over %d claims)"
                    % (disjoint, frontier, past_all, keys_ok, len(claims)))
    except Exception as e:
        return False, "ledger unreadable/malformed: %r" % e


# Paths written by lab-wide STANDING MACHINERY (a shared ledger maintained by
# its claim tool, the lessons ratchet) sit outside per-scope boundary checks BY
# CONSTRUCTION — but only in the machinery's MANDATED FORM. Predicate None = no
# mechanical form check exists; the row is tagged EXEMPT-PENDING-FORM-CHECK and
# the gatekeeper owes one manual form-look in the stamp. EDIT THIS DICT for
# your project; it is deliberately hardcoded — an allowlist supplied in the
# run manifest would let a packet exempt itself.
STANDING_LAW_PATHS = {
    "tools/data_ledger.json": form_check_data_ledger,
    "tasks/lessons.md": None,
}


def check_boundary(touched, pathspecs):
    """SET-MEMBERSHIP only: literal prefix match. Anything not prefix-covered
    is NEEDS-JUDGMENT — semantic interpretation of scope is a ruling."""
    out = []
    for p in touched:
        covered = [s for s in pathspecs if p == s or p.startswith(s.rstrip("/") + "/")
                   or p.startswith(s)]
        if covered:
            out.append(("PASS", p, "covered by %s" % covered))
            continue
        std = next((k for k in STANDING_LAW_PATHS
                    if p == k or p.endswith("/" + k)), None)
        if std is None:
            out.append(("NEEDS-JUDGMENT", p,
                        "NOT prefix-covered by any scope pathspec — interpretation is a ruling, route it"))
            continue
        predicate = STANDING_LAW_PATHS[std]
        if predicate is None:
            out.append(("EXEMPT-PENDING-FORM-CHECK", p,
                        "standing-law path; no mechanical form predicate — "
                        "gatekeeper owes ONE manual form-look in the stamp; hand-edits remain defects"))
            continue
        ok, detail = predicate(REPO)
        if ok:
            out.append(("EXEMPT", p, "standing-law path — form-check PASS: %s" % detail))
        else:
            out.append(("NEEDS-JUDGMENT", p,
                        "standing-law path but form-check FAILED (%s) — the exemption "
                        "covers mandated-form writes ONLY; route it" % detail))
    return out


def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    m = json.load(open(sys.argv[1]))
    ledger = json.load(open(LEDGER)) if os.path.exists(LEDGER) else {"claims": []}
    legs = {
        "REHASH": check_rehash(m.get("files", [])),
        "DATA-AUDIT": check_data(m.get("data_ranges", []), ledger),
        "BOUNDARY": check_boundary(m.get("touched_paths", []), m.get("scope_pathspecs", [])),
    }
    n_fail = sum(1 for leg in legs.values() for (v, _, _) in leg if v == "FAIL")
    n_judge = sum(1 for leg in legs.values() for (v, _, _) in leg if v == "NEEDS-JUDGMENT")
    n_pend = sum(1 for leg in legs.values() for (v, _, _) in leg
                 if v == "EXEMPT-PENDING-FORM-CHECK")
    print("GATE CHECKLIST — packet: %s" % m.get("packet", "<unnamed>"))
    print("(derivation: tools/gate_check.py %s ; ledger read at run: %s frontier=%s)"
          % (sys.argv[1], LEDGER, ledger.get("frontier_of_record")))
    for leg, rows in legs.items():
        print("\n[%s] %d checks" % (leg, len(rows)))
        for verdict, subject, detail in rows:
            print("  %-25s %s — %s" % (verdict, subject, detail))
    print("\nSUMMARY: FAIL=%d NEEDS-JUDGMENT=%d (counts derived: this run's rows above)"
          % (n_fail, n_judge))
    if n_judge:
        print("ROUTE: every NEEDS-JUDGMENT row goes to your registrar/human before any CONFORMS.")
    if n_pend:
        print("PENDING: %d EXEMPT-PENDING-FORM-CHECK row(s) — the stamp carries one "
              "manual form-look each." % n_pend)
    print("VERDICT SKELETON: %s" %
          ("HOLD (FAILs above)" if n_fail else
           "BLOCKED-ON-JUDGMENT (routed rows open)" if n_judge else
           "mechanical legs PASS — gatekeeper completes the judgment legs and stamps"))
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
