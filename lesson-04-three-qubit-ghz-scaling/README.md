# Lesson 04 — Three-Qubit GHZ Scaling

Build and measure a three-qubit GHZ state with a Hadamard gate followed by two CNOT gates, then verify that the ideal simulator returns only correlated 000 and 111 outcomes.

## Run

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    ./run.sh
    python plot_results.py

The run uses Qiskit StatevectorSampler, 1,000 shots, and seed 67.

## Measured results

| Bit string | Counts |
|---:|---:|
| 000 | 507 |
| 001 | 0 |
| 010 | 0 |
| 011 | 0 |
| 100 | 0 |
| 101 | 0 |
| 110 | 0 |
| 111 | 493 |

Fully matched outcomes: 1,000 / 1,000 (100.0%)

## Included files

- lesson_04.py — runnable Qiskit lesson
- run.sh — portable runner
- plot_results.py — rebuilds the measured-results chart
- results/measured_results.json — structured measured values
- results/verified_run_output.txt — preserved terminal output
- captions — synchronized SRT and WebVTT
- media/lesson_04_thumbnail.png — official lesson thumbnail

## Boundary

These results come from a local ideal statevector simulation. Physical-hardware noise and calibration effects are separate validation layers.

Lesson 5 keeps the circuit fixed and compares sampling error across three shot counts.

Renaissance Field Lite · Codex 67 Quantum Foundations
