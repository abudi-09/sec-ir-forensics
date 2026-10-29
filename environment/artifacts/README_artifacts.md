# Triage artifacts (web01)

Collected from a single Linux web server, `web01`, after an alert. All data is
synthetic; IP addresses are from the RFC 5737 documentation ranges and all
personal data uses `example.com` / `example.net`.

| File | What it is | Original host path |
|------|------------|--------------------|
| `auth.log` | sshd authentication log | `/var/log/auth.log` |
| `nginx_access.log` | web server access log | `/var/log/nginx/access.log` |
| `deploy_bash_history.txt` | shell history for user `deploy` | `/home/deploy/.bash_history` |
| `spool_cron_deploy.txt` | crontab for user `deploy` | `/var/spool/cron/crontabs/deploy` |
| `etc_passwd.txt` | account list | `/etc/passwd` |
| `var_backups_customers.csv` | a data file present on the host | `/var/backups/customers.csv` |

Your job (see the task instructions) is to reconstruct what happened and write
your conclusions to `/app/findings.json`.
