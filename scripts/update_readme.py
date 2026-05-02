#!/usr/bin/env python3
"""Regenerate the auto-activity block in README.md.

Lists the user's most-recently-pushed public, non-fork, non-archived repos
between the ACTIVITY:START and ACTIVITY:END markers. Skips the profile repo
itself.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

USER = "turfptax"
README = Path("README.md")
START = "<!-- ACTIVITY:START -->"
END = "<!-- ACTIVITY:END -->"
TOP_N = 5
EXCLUDE = {USER}  # the profile repo itself
DESC_MAX = 110


def fetch_repos() -> list[dict]:
    out = subprocess.check_output(
        [
            "gh", "repo", "list", USER,
            "--limit", "200",
            "--visibility", "public",
            "--no-archived",
            "--source",  # exclude forks
            "--json", "name,description,isFork,isArchived,pushedAt,primaryLanguage,url",
        ],
        text=True,
        encoding="utf-8",
    )
    return json.loads(out)


def render(repos: list[dict]) -> str:
    repos = [r for r in repos if r["name"] not in EXCLUDE]
    repos.sort(key=lambda r: r["pushedAt"], reverse=True)
    repos = repos[:TOP_N]

    lines = []
    for r in repos:
        lang = (r.get("primaryLanguage") or {}).get("name", "")
        lang_str = f" · `{lang}`" if lang else ""
        desc = r.get("description") or "(no description)"
        if len(desc) > DESC_MAX:
            desc = desc[: DESC_MAX - 1].rstrip() + "…"
        lines.append(f"- [`{r['name']}`]({r['url']}){lang_str} — {desc}")
    return "\n".join(lines)


def update_readme(rendered: str) -> bool:
    text = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"Markers {START} ... {END} not found in README.md")

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    block = f"{START}\n_Auto-updated {timestamp} · top {TOP_N} most recently pushed repos_\n\n{rendered}\n{END}"
    # lambda avoids re.sub interpreting backslash sequences in repo descriptions
    new_text = pattern.sub(lambda _m: block, text)

    if new_text == text:
        print("No changes to README.")
        return False

    README.write_text(new_text, encoding="utf-8")
    print("README updated.")
    return True


def main() -> int:
    repos = fetch_repos()
    rendered = render(repos)
    update_readme(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
