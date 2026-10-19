from qiskit_aer import AerSimulator

from src.circuits import chsh_circuit


def run_circuit(circuit, shots=1000):
    """
    Run one circuit on the local Aer simulator.
    """

    simulator = AerSimulator()

    result = simulator.run(
        circuit,
        shots=shots
    ).result()

    return result.get_counts()


def run_chsh_simulation(shots=1000):
    """
    Run all four CHSH circuits locally.
    """

    results = {}

    for x, y in [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]:
        circuit = chsh_circuit(x, y)

        results[(x, y)] = run_circuit(
            circuit,
            shots
        )

    return results


def quantum_strategy(x, y):
    """
    Execute one CHSH round using the local
    quantum simulator.

    Returns:
        Alice's output, Bob's output
    """

    counts = run_circuit(
        chsh_circuit(x, y),
        shots=1
    )

    bitstring = list(counts.keys())[0]

    # Qiskit returns c1 c0.
    # c1 = Bob
    # c0 = Alice
    b = bitstring[0]
    a = bitstring[1]

    return a, b