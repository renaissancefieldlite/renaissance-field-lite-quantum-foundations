#!/usr/bin/env python3
import json
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/"results/measured_results.json").read_text())["rows"]
angles=[r["angle"] for r in rows]
plt.figure(figsize=(12,6.75))
plt.plot(angles,[r["expected"] for r in rows],"o-",label="Expected P(1)",linewidth=2.5)
plt.plot(angles,[r["observed"] for r in rows],"s--",label="Observed P(1), 1,000 shots",linewidth=2.0)
plt.xticks(angles);plt.ylim(-0.03,1.03);plt.xlabel("RY angle (degrees)");plt.ylabel("Probability of measuring 1")
plt.title("Lesson 02 — Controlling Qubit Probability");plt.grid(alpha=.25);plt.legend();plt.tight_layout()
out=ROOT/"results/lesson_02_probability_curve_rebuilt.png";plt.savefig(out,dpi=160);print(out)
