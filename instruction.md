# Incident response: reconstruct the web01 intrusion

A monitoring alert fired for the Linux web server `web01`. Triage artifacts have
been collected into `/app/artifacts/` (see `/app/artifacts/README_artifacts.md`
for the file list and their original host paths). Everything is self-contained;
there is no live host and no network access.

Analyze the artifacts and determine how the server was compromised and what the
attacker did. Write your conclusions as JSON to **`/app/findings.json`** with
exactly these keys:

```json
{
  "initial_access": "...",
  "attacker_ip": "...",
  "compromised_account": "...",
  "persistence": "...",
  "exfiltrated_file": "..."
}
```

Field requirements:

- `initial_access` — one of:
  `ssh-brute-force`, `phishing`, `web-exploit`, `stolen-credentials`,
  `supply-chain`.
- `attacker_ip` — the single source IP of the intrusion (e.g. `192.0.2.10`).
- `compromised_account` — the local account the attacker authenticated as.
- `persistence` — one of:
  `cron-job`, `ssh-authorized-key`, `new-user`, `systemd-service`, `web-shell`.
- `exfiltrated_file` — the absolute host path of the file the attacker copied
  off the server (e.g. `/var/log/...`).

Notes:

- Choose the enum values exactly as written above (lowercase, hyphenated).
- Base every field on evidence in the artifacts. There is some benign activity
  mixed in; not every IP or login is the attacker.
- You are scored only on the contents of `/app/findings.json` (one fifth per
  correct field), not on any report text.
