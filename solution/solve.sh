#!/usr/bin/env bash
# Reference solution: writes the correct findings to /app/findings.json.
# The oracle agent runs this; the verifier then scores /app/findings.json.
#
# These values are derivable from the artifacts:
#   - auth.log: a burst of failed sshd passwords for several users from
#     203.0.113.37, then "Accepted password for deploy" from the same IP
#     -> initial_access=ssh-brute-force, attacker_ip=203.0.113.37,
#        compromised_account=deploy. (The later publickey login from
#        198.51.100.24 is benign admin activity.)
#   - deploy_bash_history.txt: data copied and POSTed off-box, and a new
#     crontab entry calling back to the attacker
#     -> exfiltrated_file=/var/backups/customers.csv, persistence=cron-job.
#   - spool_cron_deploy.txt: confirms the malicious cron entry.
#   - etc_passwd.txt: no account was added, ruling out new-user persistence.
set -euo pipefail
mkdir -p /app
cat > /app/findings.json <<'JSON'
{
  "initial_access": "ssh-brute-force",
  "attacker_ip": "203.0.113.37",
  "compromised_account": "deploy",
  "persistence": "cron-job",
  "exfiltrated_file": "/var/backups/customers.csv"
}
JSON
echo "reference findings written to /app/findings.json"
