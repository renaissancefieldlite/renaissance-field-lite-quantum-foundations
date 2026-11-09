"""Lesson 05: compare measurement estimates at increasing shot counts."""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


SEED = 67
SHOT_COUNTS = [100, 1_000, 10_000]


def build_circuit():
    circuit = QuantumCircuit(1)
    circuit.h(0)
    circuit.measure_all()
    return circuit


def main():
    circuit = build_circuit()
    print("Lesson 05 — Why shot count matters")
    print("shots | count(1) | observed_P(1) | absolute_error_from_0.5")

    for shots in SHOT_COUNTS:
        sampler = StatevectorSampler(seed=SEED)
        result = sampler.run([circuit], shots=shots).result()[0]
        counts = result.data.meas.get_counts()
        count_one = counts.get("1", 0)
        probability_one = count_one / shots
        error = abs(probability_one - 0.5)
        print(f"{shots:5d} | {count_one:8d} | {probability_one:13.4f} | {error:.4f}")


if __name__ == "__main__":
    main()
