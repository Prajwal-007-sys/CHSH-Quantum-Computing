from math import pi

from qiskit import QuantumCircuit


def prepare_bell_state(qc):
    """
    Prepare the Bell state:

        |Phi+> = (|00> + |11>) / sqrt(2)
    """

    qc.h(0)
    qc.cx(0, 1)


def chsh_circuit(x, y):
    """
    Create the quantum circuit for a particular CHSH
    input pair (x, y).

    Args:
        x: Alice's input, 0 or 1
        y: Bob's input, 0 or 1

    Returns:
        QuantumCircuit
    """

    qc = QuantumCircuit(2, 2)

    # Prepare entangled Bell state
    prepare_bell_state(qc)

    qc.barrier()

    # Alice's measurement operation
    if x == 0:
        qc.ry(0, 0)
    else:
        qc.ry(-pi / 2, 0)

    qc.measure(0, 0)

    # Bob's measurement operation
    if y == 0:
        qc.ry(-pi / 4, 1)
    else:
        qc.ry(pi / 4, 1)

    qc.measure(1, 1)

    return qc


def create_all_chsh_circuits():
    """
    Create the four circuits corresponding to
    all possible CHSH input combinations.
    """

    return {
        (0, 0): chsh_circuit(0, 0),
        (0, 1): chsh_circuit(0, 1),
        (1, 0): chsh_circuit(1, 0),
        (1, 1): chsh_circuit(1, 1)
    }