#!/usr/bin/env python3
import json
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/"results/measured_results.json").read_text())["rows"]
shots=[r["shots"] for r in rows];errors=[r["error"] for r in rows]
plt.figure(figsize=(12,6.75));plt.plot(shots,errors,marker="o",linewidth=3,color="#efbd46")
plt.xscale("log");plt.xticks(shots,[f"{s:,}" for s in shots]);plt.xlabel("Shots");plt.ylabel("Absolute error from 0.5");plt.title("Lesson 05 — Sampling Error by Shot Count")
for x,y in zip(shots,errors):plt.annotate(f"{y:.4f}",(x,y),textcoords="offset points",xytext=(0,10),ha="center",fontweight="bold")
plt.grid(alpha=.25);plt.tight_layout()
out=ROOT/"results/lesson_05_shot_error_rebuilt.png";plt.savefig(out,dpi=160);print(out)
