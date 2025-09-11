# flake8: noqa

#!/usr/bin/env python3
import pathlib
import random

README = pathlib.Path("README.md")
START = "<!-- CHALLENGE:START -->"
END = "<!-- CHALLENGE:END -->"


def pick_kattis_problem():
    # Predefined list of beginner-friendly Kattis problems
    # Format: (problem_id, title, difficulty)
    beginner_problems = [
        ("hello", "Hello World!", "1.0"),
        ("carrots", "Carrots", "1.3"),
        ("potato", "Potato", "1.5"),
        ("2048", "2048", "1.7"),
        ("different", "A Different Problem", "1.8"),
        ("spavanac", "Spavanac", "2.0"),
        ("tri", "Triangle", "2.1"),
        ("rijeci", "Rijeci", "2.2"),
        ("kornislav", "Kornislav", "2.3"),
        ("pretpostavke", "Pretpostavke", "2.4"),
        ("abcd", "ABCD", "2.5"),
        ("karte", "Karte", "2.6"),
        ("trollhunt", "Troll Hunt", "2.7"),
        ("babylonian", "Babylonian Numbers", "2.8"),
        ("prva", "First", "2.9"),
        ("autori", "Autori", "3.0"),
        ("budilnik", "Budilnik", "3.1"),
        ("kockice", "Kockice", "3.2"),
        ("laptop", "Laptop", "3.3"),
        ("mali", "Mali", "3.4"),
    ]

    return random.choice(beginner_problems)


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
