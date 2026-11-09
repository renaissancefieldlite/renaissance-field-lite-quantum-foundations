# Lesson 02 — Controlling Probability

Sweep seven RY rotation angles from 0° through 180° and compare the observed frequency of measuring one with the expected sine-squared probability.

## Run

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    ./run.sh
    python plot_results.py

The run uses Qiskit StatevectorSampler, 1,000 shots, and seed 67.

## Measured results

| Angle | Expected P(1) | Observed P(1) | 0 counts | 1 counts |
|---:|---:|---:|---:|---:|
| 0° | 0.000 | 0.000 | 1000 | 0 |
| 30° | 0.067 | 0.070 | 930 | 70 |
| 60° | 0.250 | 0.248 | 752 | 248 |
| 90° | 0.500 | 0.493 | 507 | 493 |
| 120° | 0.750 | 0.750 | 250 | 750 |
| 150° | 0.933 | 0.939 | 61 | 939 |
| 180° | 1.000 | 1.000 | 0 | 1000 |

## Included files

- lesson_02.py — runnable Qiskit lesson
- run.sh — portable runner
- plot_results.py — rebuilds the measured-results chart
- results/measured_results.json — structured measured values
- results/verified_run_output.txt — preserved terminal output
- captions — synchronized SRT and WebVTT
- media/lesson_02_thumbnail.png — official lesson thumbnail

## Boundary

These results come from a local ideal statevector simulation. Physical-hardware noise and calibration effects are separate validation layers.

Lesson 3 builds a two-qubit Bell pair with Hadamard and CNOT gates.

Renaissance Field Lite · Codex 67 Quantum Foundations
