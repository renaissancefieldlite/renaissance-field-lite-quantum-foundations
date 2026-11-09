# Lesson 03 — Bell-Pair Entanglement

Build and measure a two-qubit Bell state with a Hadamard gate followed by CNOT, then verify that the ideal simulator returns only correlated 00 and 11 outcomes.

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
| 00 | 507 |
| 01 | 0 |
| 10 | 0 |
| 11 | 493 |

Matched outcomes: 1,000 / 1,000 (100.0%)

## Included files

- lesson_03.py — runnable Qiskit lesson
- run.sh — portable runner
- plot_results.py — rebuilds the measured-results chart
- results/measured_results.json — structured measured values
- results/verified_run_output.txt — preserved terminal output
- captions — synchronized SRT and WebVTT
- media/lesson_03_thumbnail.png — official lesson thumbnail

## Boundary

These results come from a local ideal statevector simulation. Physical-hardware noise and calibration effects are separate validation layers.

Lesson 4 scales the same correlation pattern into a three-qubit GHZ state.

Renaissance Field Lite · Codex 67 Quantum Foundations
