# flake8: noqa

#!/usr/bin/env python3
from autokattis import OpenKattis
import pathlib
import random

README = pathlib.Path("README.md")
START = "<!-- CHALLENGE:START -->"
END = "<!-- CHALLENGE:END -->"


def pick_kattis_problem():
    kt = OpenKattis("anonymous_username")  # Only needs problem suggestions
    suggested = kt.suggest()
    beginner = [p for p in suggested if 1.0 <= float(p["difficulty"]) <= 3.0]
    prob = random.choice(beginner) if beginner else random.choice(suggested)
    return prob["problem_id"], prob["title"], prob["difficulty"]


def update_readme():
    pid, title, diff = pick_kattis_problem()
    mission = f"🚀 Mission uploaded: _Solve “{title}” [{diff} pts] on Kattis_  \n[Go solve it →](https://open.kattis.com/problems/{pid})"
    text = README.read_text(encoding="utf-8")
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    new = f"{START}\n{mission}\n{END}"
    README.write_text(before + new + after, encoding="utf-8")
    print(f"Updated with Kattis problem: {title}")


if __name__ == "__main__":
    update_readme()
