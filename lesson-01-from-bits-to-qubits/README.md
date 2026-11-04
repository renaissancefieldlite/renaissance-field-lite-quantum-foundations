# Lesson 01 — From Bits to Qubits

**Lesson 1 of 12 in Renaissance Field Lite's Introduction to Quantum Computing.**

## Learning objective

Compare a definite zero, a definite one, and an equal superposition while holding the simulator and shot count constant.

## Measured release result

| State preparation | Measured 0 | Measured 1 | Total |
|---|---:|---:|---:|
| No gate (`|0>`) | 1,000 | 0 | 1,000 |
| X gate (`|1>`) | 0 | 1,000 | 1,000 |
| Hadamard gate | 507 | 493 | 1,000 |

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
./run.sh
```

`run.sh` prints three clearly separated result blocks. The seeded local run should reproduce the included counts with Qiskit 2.6.1.

## Rebuild the chart

```bash
python plot_results.py
```

The chart script reads `results/measured_counts.json` and writes `results/lesson_01_measured_counts_chart.png`.

## Files

- `lesson_01.py` — three one-qubit circuits and the seeded 1,000-shot run
- `run.sh` — portable runner with clear result headings
- `plot_results.py` — chart recreation from the measured JSON
- `results/measured_counts.json` — machine-readable measured counts
- `results/lesson_01_measured_counts_chart.png` — visual comparison
- `captions/lesson_01_en.srt` and `.vtt` — synchronized English captions
- `media/lesson_01_thumbnail.png` — release thumbnail

## Interpretation

The first two circuits produce definite measurement outcomes. The Hadamard circuit produces a finite-sample result near an equal split. The 507/493 difference is expected sampling variation, not evidence that the ideal state preparation failed.

## Next lesson

Lesson 2 replaces the fixed Hadamard preparation with a parameterized Y rotation and observes how measurement probability changes with angle.

Follow [Renaissance Field Lite](https://renaissancefieldlite.github.io/) for the complete series.
