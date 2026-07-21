#!/usr/bin/env python3
"""gate_check_selftest.py — planted-case selftest for gate_check.py.
Run after ANY edit to gate_check.py. Exit 0 iff all cases pass.
Cases exercise all verdicts on all three legs, including the standing-law
allowlist branch (form-check pass, form-check fail, no-predicate tag)."""
import hashlib, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
GC = os.path.join(HERE, "gate_check.py")
ledger = json.load(open(os.path.join(HERE, "data_ledger.json")))
claim = ledger["claims"][-1]["range"]
far = ledger["frontier_of_record"] + 10_000

td = tempfile.mkdtemp()
fx = os.path.join(td, "fixture.txt")
open(fx, "w").write("known bytes\n")
good_md5 = hashlib.md5(open(fx, "rb").read()).hexdigest()


def run(manifest, env_extra=None):
    mp = os.path.join(td, "m.json")
    json.dump(manifest, open(mp, "w"))
    env = dict(os.environ, **(env_extra or {}))
    r = subprocess.run([sys.executable, GC, mp], capture_output=True, text=True, env=env)
    return r.returncode, r.stdout


# Standing-law fixture repos: one with a well-formed ledger, one deliberately
# BAD (overlapping claims — the form-check must refuse the exemption).
def make_repo(name, claims):
    repo = os.path.join(td, name)
    os.makedirs(os.path.join(repo, "tools"))
    json.dump({"_what": "fixture", "frontier_of_record": 1010,
               "void_blocks_never_reusable": [], "claims": claims},
              open(os.path.join(repo, "tools", "data_ledger.json"), "w"))
    return {"GATE_CHECK_REPO": repo}

GOOD = make_repo("repo", [
    {"range": [1000, 1004], "owner": "x", "status": "SPENT"},
    {"range": [1005, 1009], "owner": "y", "status": "OPEN"}])
BAD = make_repo("repo_bad", [
    {"range": [1000, 1004], "owner": "x", "status": "SPENT"},
    {"range": [1003, 1009], "owner": "y", "status": "OPEN"}])

cases = [
    # (name, manifest, want_rc, want_substrings[, env])
    ("rehash-pass+exact-claim+boundary-pass",
     {"packet": "selftest", "files": [{"path": fx, "md5": good_md5}],
      "data_ranges": [claim], "scope_pathspecs": [td], "touched_paths": [fx]},
     0, ["PASS", "exact ledger claim", "mechanical legs PASS"]),
    ("rehash-fail",
     {"files": [{"path": fx, "md5": "0" * 32}]},
     1, ["FAIL", "claimed 0000"]),
    ("missing-file-fail",
     {"files": [{"path": fx + ".nope", "md5": good_md5}]},
     1, ["MISSING-AT-PATH"]),
    ("unclaimed-range-judgment",
     {"data_ranges": [[far, far + 1]]},
     0, ["NEEDS-JUDGMENT", "NO ledger claim", "route it", "BLOCKED-ON-JUDGMENT"]),
    ("boundary-uncovered-judgment",
     {"scope_pathspecs": ["src/experiment-a/"], "touched_paths": ["src/experiment-b/x.py"]},
     0, ["NEEDS-JUDGMENT", "NOT prefix-covered"]),
    ("boundary-covered-pass",
     {"scope_pathspecs": ["src/experiment-a/"], "touched_paths": ["src/experiment-a/x.md"]},
     0, ["PASS", "covered by"]),
    ("standing-lessons-pending-formcheck",
     {"scope_pathspecs": ["src/experiment-a/"], "touched_paths": ["tasks/lessons.md"]},
     0, ["EXEMPT-PENDING-FORM-CHECK", "manual form-look"], GOOD),
    ("standing-ledger-exempt-form-pass",
     {"scope_pathspecs": ["src/experiment-a/"], "touched_paths": ["tools/data_ledger.json"]},
     0, ["EXEMPT", "form-check PASS", "frontier(1010)"], GOOD),
    ("standing-ledger-overlap-judgment",
     {"scope_pathspecs": ["src/experiment-a/"], "touched_paths": ["tools/data_ledger.json"]},
     0, ["NEEDS-JUDGMENT", "form-check FAILED", "disjoint=False"], BAD),
    ("standing-path-explicit-scope-still-pass",
     {"scope_pathspecs": ["tools/"], "touched_paths": ["tools/data_ledger.json"]},
     0, ["PASS", "covered by"], GOOD),
    # pins the one-ledger law: with GATE_CHECK_REPO set, the DATA-AUDIT leg must
    # read the SAME fixture ledger as the form check (owner=x proves it did not
    # silently fall back to the shipped starter ledger)
    ("data-leg-reads-repo-ledger",
     {"data_ranges": [[1000, 1004]]},
     0, ["PASS", "owner=x"], GOOD),
]

fails = 0
for name, m, want_rc, subs, *rest in cases:
    rc, out = run(m, rest[0] if rest else None)
    bad = [s for s in subs if s not in out] + (["rc %d != %d" % (rc, want_rc)] if rc != want_rc else [])
    if bad:
        fails += 1
        print("FAIL %s: %s" % (name, bad))
print("selftest: %d/%d pass" % (len(cases) - fails, len(cases)))
sys.exit(1 if fails else 0)
