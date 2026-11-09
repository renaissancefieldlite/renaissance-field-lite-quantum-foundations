"""Lesson 03: create and measure a two-qubit Bell state."""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


SHOTS = 1_000
SEED = 67


def build_circuit():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure_all()
    return circuit


def main():
    circuit = build_circuit()
    result = StatevectorSampler(seed=SEED).run([circuit], shots=SHOTS).result()[0]
    counts = result.data.meas.get_counts()
    matched = counts.get("00", 0) + counts.get("11", 0)

    print("Lesson 03 — Bell-pair entanglement")
    print(circuit.draw(output="text"))
    print("Counts:", dict(sorted(counts.items())))
    print(f"Matched outcomes: {matched}/{SHOTS} ({matched / SHOTS:.1%})")


if __name__ == "__main__":
    main()
