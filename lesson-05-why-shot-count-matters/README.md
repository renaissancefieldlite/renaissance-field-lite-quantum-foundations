# Lesson 05 — Why Shot Count Matters

Run one fixed Hadamard circuit at three sample sizes, then compare each observed probability of one with the theoretical value of one half.

## Run

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    ./run.sh
    python plot_results.py

The run uses Qiskit StatevectorSampler and seed 67 at 100, 1,000, and 10,000 shots.

## Measured results

| Shots | Count of 1 | Observed P(1) | Absolute error from 0.5 |
|---:|---:|---:|---:|
| 100 | 44 | 0.4400 | 0.0600 |
| 1,000 | 493 | 0.4930 | 0.0070 |
| 10,000 | 4,971 | 0.4971 | 0.0029 |

## Included files

- lesson_05.py — runnable Qiskit lesson
- run.sh — portable runner
- plot_results.py — rebuilds the measured-results chart
- results/measured_results.json — structured measured values
- results/verified_run_output.txt — preserved terminal output
- captions — synchronized SRT and WebVTT
- media/lesson_05_thumbnail.png — official lesson thumbnail

## Boundary

This seeded run shows smaller error as the shot count grows. The general result is statistical: larger samples typically improve precision, but they do not guarantee that every individual run has smaller error.

Lesson 6 compares the same circuit idea across Qiskit and CUDA-Q.

Renaissance Field Lite · Codex 67 Quantum Foundations
