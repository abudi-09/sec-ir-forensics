FROM python:3.11-slim

WORKDIR /app

# The agent sees only the triage artifacts. The grader and the ground-truth
# answers live in tests/ and are uploaded to /tests/ by Harbor only after the
# agent finishes, so they are never visible during analysis.
COPY artifacts/ /app/artifacts/

CMD ["sleep", "infinity"]
