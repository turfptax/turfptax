# Profile automation

This repo runs two automated workflows that keep the profile fresh and surface portfolio metrics.

## Workflows

### [`profile-readme.yml`](.github/workflows/profile-readme.yml) — daily

Runs `scripts/update_readme.py` once a day (07:17 UTC) and on every push to `main` that touches the script or workflow.

- Lists the 5 most-recently-pushed public, non-fork, non-archived own repos
- Rewrites the block between `<!-- ACTIVITY:START -->` and `<!-- ACTIVITY:END -->` in [`README.md`](README.md)
- Commits with `[skip ci]` so the auto-commit doesn't trigger more runs
- Skips the commit entirely if the rendered block is identical

### [`metrics-digest.yml`](.github/workflows/metrics-digest.yml) — weekly

Runs `scripts/metrics_digest.py` every Monday (08:23 UTC) and on every push to the script or workflow.

- Aggregates totals (own repo count, archived count, fork count, total stars)
- Top 10 by stars
- 10 most-recently-pushed active repos
- Language distribution across active repos
- Writes everything to [`data/metrics/latest.md`](data/metrics/latest.md)

This file is **public-safe** — it only includes data already visible on the public profile. No traffic, clones, or referrers.

## Manual trigger

Both workflows have `workflow_dispatch:` enabled. From the [Actions tab](https://github.com/turfptax/turfptax/actions), you can run either on demand without waiting for the schedule.

## Disable

To pause an automation, disable its workflow from the Actions tab. The README block and metrics file will simply stop refreshing — no other side effects.

## Tokens & permissions

Both workflows use the default `GITHUB_TOKEN` with `contents: write`. No personal access token (PAT) is needed — only public repo data is accessed.

For the **security** and **traffic** digests (Phase 3B, not yet shipped), a PAT will be needed to read across all repos including private ones. Those will live in a separate private repo.

## Files

| Path | Purpose |
|---|---|
| `scripts/update_readme.py` | Regenerates the activity block in `README.md` |
| `scripts/metrics_digest.py` | Generates `data/metrics/latest.md` |
| `.github/workflows/profile-readme.yml` | Schedules and runs the README update |
| `.github/workflows/metrics-digest.yml` | Schedules and runs the metrics digest |
| `data/metrics/latest.md` | Latest weekly metrics snapshot (auto-generated) |
