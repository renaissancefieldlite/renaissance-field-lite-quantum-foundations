#!/usr/bin/env python3
import json
from pathlib import Path
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
counts=json.loads((ROOT/"results/measured_results.json").read_text())["counts"]
labels=["00","01","10","11"];values=[counts.get(k,0) for k in labels]
plt.figure(figsize=(12,6.75));bars=plt.bar(labels,values,color=["#2fcdbd","#375d8e","#375d8e","#9274ff"])
plt.ylim(0,550);plt.xlabel("Measured bit string");plt.ylabel("Counts out of 1,000 shots");plt.title("Lesson 03 — Bell-Pair Measurement Counts")
for b,v in zip(bars,values):plt.text(b.get_x()+b.get_width()/2,v+8,str(v),ha="center",fontweight="bold")
plt.grid(axis="y",alpha=.2);plt.tight_layout()
out=ROOT/"results/lesson_03_bell_counts_rebuilt.png";plt.savefig(out,dpi=160);print(out)
