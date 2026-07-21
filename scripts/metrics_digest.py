#!/usr/bin/env python3
"""Generate a public-safe metrics digest at data/metrics/latest.md.

Public-safe means: only data already visible on the public profile (stars,
repo metadata, language). Detailed traffic/clones/referrers are NOT included
here - those go in the private dashboards repo (see Phase 3B docs).
"""
from __future__ import annotations

import json
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

USER = "turfptax"
OUT = Path("data/metrics/latest.md")
TOP_N = 10


def fetch_repos() -> list[dict]:
    out = subprocess.check_output(
        [
            "gh", "repo", "list", USER,
            "--limit", "200",
            "--visibility", "public",
            "--json",
            "name,description,isFork,isArchived,stargazerCount,primaryLanguage,pushedAt,url",
        ],
        text=True,
        encoding="utf-8",
    )
    return json.loads(out)


def render(repos: list[dict]) -> str:
    own = [r for r in repos if not r["isFork"]]
    active = [r for r in own if not r["isArchived"]]
    archived = [r for r in own if r["isArchived"]]
    forks = [r for r in repos if r["isFork"]]

    total_stars = sum(r["stargazerCount"] for r in own)

    by_stars = sorted(own, key=lambda r: r["stargazerCount"], reverse=True)
    by_recent = sorted(active, key=lambda r: r["pushedAt"], reverse=True)[:TOP_N]

    languages: Counter[str] = Counter()
    for r in active:
        lang = (r.get("primaryLanguage") or {}).get("name")
        if lang:
            languages[lang] += 1

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = [
        "# Portfolio metrics",
        "",
        f"_Generated {timestamp}_",
        "",
        "## Totals",
        "",
        f"- Public own repos: **{len(own)}** ({len(active)} active, {len(archived)} archived)",
        f"- Public forks: **{len(forks)}**",
        f"- Total stars across own repos: **{total_stars}**",
        "",
        f"## Top by stars",
        "",
    ]
    starred = [r for r in by_stars if r["stargazerCount"] > 0][:TOP_N]
    if not starred:
        lines.append("_(no starred repos yet)_")
    else:
        for r in starred:
            lines.append(f"- [`{r['name']}`]({r['url']}) - **{r['stargazerCount']}★**")

    lines += ["", f"## Recently active ({TOP_N})", ""]
    for r in by_recent:
        date = r["pushedAt"][:10]
        lang = (r.get("primaryLanguage") or {}).get("name", "")
        lang_str = f" · {lang}" if lang else ""
        lines.append(f"- {date} · [`{r['name']}`]({r['url']}){lang_str}")

    lines += ["", "## Language distribution (active repos)", ""]
    if not languages:
        lines.append("_(no language data)_")
    else:
        for lang, count in languages.most_common():
            lines.append(f"- {lang}: {count}")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    repos = fetch_repos()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(repos), encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
