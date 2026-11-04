"""Lesson 01: compare |0>, |1>, and Hadamard superposition."""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler


SHOTS = 1_000
SEED = 67


def measured_circuit(gate_name):
    circuit = QuantumCircuit(1)
    if gate_name == "X":
        circuit.x(0)
    elif gate_name == "H":
        circuit.h(0)
    circuit.measure_all()
    return circuit


def main():
    experiments = [
        ("Start in |0>", measured_circuit("identity")),
        ("Apply X to prepare |1>", measured_circuit("X")),
        ("Apply H for superposition", measured_circuit("H")),
    ]
    sampler = StatevectorSampler(seed=SEED)
    results = sampler.run([circuit for _, circuit in experiments], shots=SHOTS).result()

    print("Lesson 01 — From bits to qubits")
    for (label, circuit), result in zip(experiments, results):
        counts = result.data.meas.get_counts()
        print(f"\n{label}")
        print(circuit.draw(output="text"))
        print("Counts:", dict(sorted(counts.items())))


if __name__ == "__main__":
    main()
