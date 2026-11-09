"""Lesson 02: control measurement probability with a Y rotation."""

from math import pi, sin

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


SHOTS = 1_000
SEED = 67
ANGLES = [0, pi / 6, pi / 3, pi / 2, 2 * pi / 3, 5 * pi / 6, pi]


def build_circuit(angle):
    circuit = QuantumCircuit(1)
    circuit.ry(angle, 0)
    circuit.measure_all()
    return circuit


def main():
    circuits = [build_circuit(angle) for angle in ANGLES]
    sampler = StatevectorSampler(seed=SEED)
    results = sampler.run(circuits, shots=SHOTS).result()

    print("Lesson 02 — Controlling probability with Ry")
    print("angle_deg | expected_P(1) | observed_P(1) | counts")
    for angle, result in zip(ANGLES, results):
        counts = result.data.meas.get_counts()
        observed = counts.get("1", 0) / SHOTS
        expected = sin(angle / 2) ** 2
        print(
            f"{angle * 180 / pi:9.0f} | {expected:13.3f} | "
            f"{observed:13.3f} | {dict(sorted(counts.items()))}"
        )


if __name__ == "__main__":
    main()
