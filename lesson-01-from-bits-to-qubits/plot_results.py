#!/usr/bin/env python3
"""Rebuild the Lesson 1 measured-counts comparison chart."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results" / "measured_counts.json"
OUTPUT = ROOT / "results" / "lesson_01_measured_counts_chart.png"


def main() -> None:
    data = json.loads(RESULTS.read_text())
    counts = data["counts"]
    states = ["definite_zero", "definite_one", "equal_superposition"]
    labels = ["Definite 0", "Definite 1", "Equal superposition"]
    zeros = [counts[state]["0"] for state in states]
    ones = [counts[state]["1"] for state in states]

    x = range(len(states))
    width = 0.36
    fig, ax = plt.subplots(figsize=(12, 6), dpi=160)
    bars_zero = ax.bar([i - width / 2 for i in x], zeros, width, label="Measured 0", color="#35D0BA")
    bars_one = ax.bar([i + width / 2 for i in x], ones, width, label="Measured 1", color="#9A7BFF")
    ax.set_xticks(list(x), labels)
    ax.set_ylabel("Counts from 1,000 shots")
    ax.set_ylim(0, 1100)
    ax.grid(axis="y", alpha=0.18)
    ax.legend()
    for bars in (bars_zero, bars_one):
        ax.bar_label(bars, padding=3)
    fig.tight_layout()
    fig.savefig(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
