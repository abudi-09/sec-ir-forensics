"""Grader. Reads the agent's /app/findings.json, compares each field to the
held-out ground truth, and writes a scalar reward (fraction of correct fields)
to /logs/verifier/reward.txt.
"""
import json
import os
import sys

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FINDINGS = "/app/findings.json"
REWARD_DIR = "/logs/verifier"
REWARD_FILE = os.path.join(REWARD_DIR, "reward.txt")

FIELDS = [
    "initial_access",
    "attacker_ip",
    "compromised_account",
    "persistence",
    "exfiltrated_file",
]


def _norm(x):
    return str(x).strip().lower()


def _write(score):
    os.makedirs(REWARD_DIR, exist_ok=True)
    with open(REWARD_FILE, "w") as f:
        f.write("%.6f\n" % score)
    print("%.6f" % score)


def main():
    with open(os.path.join(TESTS_DIR, "ground_truth.json")) as f:
        truth = json.load(f)

    try:
        with open(FINDINGS) as f:
            got = json.load(f)
        if not isinstance(got, dict):
            raise ValueError("findings.json is not a JSON object")
    except Exception as e:
        sys.stderr.write("no valid /app/findings.json: %r\n" % e)
        _write(0.0)
        return

    correct = 0
    for k in FIELDS:
        if k in got and _norm(got[k]) == _norm(truth[k]):
            correct += 1
            sys.stderr.write("  %-20s OK\n" % k)
        else:
            sys.stderr.write("  %-20s wrong/missing (got %r)\n" % (k, got.get(k)))

    _write(correct / len(FIELDS))
    sys.stderr.write("%d/%d fields correct\n" % (correct, len(FIELDS)))


if __name__ == "__main__":
    main()
