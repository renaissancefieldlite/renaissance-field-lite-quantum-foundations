"""Lesson 04: scale Bell-style correlation to a three-qubit GHZ state."""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


SHOTS = 1_000
SEED = 67


def build_circuit():
    circuit = QuantumCircuit(3)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(1, 2)
    circuit.measure_all()
    return circuit


def main():
    circuit = build_circuit()
    result = StatevectorSampler(seed=SEED).run([circuit], shots=SHOTS).result()[0]
    counts = result.data.meas.get_counts()
    matched = counts.get("000", 0) + counts.get("111", 0)

    print("Lesson 04 — Three-qubit GHZ scaling")
    print(circuit.draw(output="text"))
    print("Counts:", dict(sorted(counts.items())))
    print(f"Fully matched outcomes: {matched}/{SHOTS} ({matched / SHOTS:.1%})")


if __name__ == "__main__":
    main()
