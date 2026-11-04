<p align="center">
  <img src="assets/rfl-logo-silver-clean-no-tagline.png" alt="Renaissance Field Lite" width="620">
</p>

# Renaissance Field Lite + Codex 67 Quantum Foundations

A twelve-lesson Introduction to Quantum Computing built around real local code, measured simulator outputs, and one verified concept at a time.

## Available lesson

| Lesson | Topic | New concept | Measured result |
|---|---|---|---|
| 01 | [From Bits to Qubits](lesson-01-from-bits-to-qubits/) | X and Hadamard gates | 1,000 zeros; 1,000 ones; 507/493 superposition |

## Series path

1. From bits to qubits
2. Controlling probability
3. Bell-pair entanglement
4. Scaling to three qubits
5. Why shot count matters
6. Framework portability
7. Simon promise
8. Reversible oracle
9. Measurement equations
10. GF(2) recovery
11. pytket compilation
12. Qiskit interoperability

Only Lesson 1 is included in this release candidate. Later lessons remain future work until each lesson has its own code, measured outputs, captions, and review gate.

## Evidence boundary

- Simulator: Qiskit `StatevectorSampler`
- Shots per circuit: `1,000`
- Seed: `67`
- Runtime versions used for the measured release: Python `3.14.6`, Qiskit `2.6.1`, Matplotlib `3.11.2`
- Physical-hardware noise, calibration, queue time, and readout error are outside this local simulator lesson.

## Video

The captioned 1080p Lesson 1 video is a separate YouTube publication artifact. This repository and its `lesson-01-v1.0.0` release carry the runnable Lesson 1 code, measured results, captions, thumbnail, source ZIP, and checksums.

Follow [Renaissance Field Lite](https://renaissancefieldlite.github.io/) for the complete twelve-lesson Codex 67 series.

## License status

No license file is included in this approval draft. Publication terms remain an explicit owner decision before the repository is made public.
