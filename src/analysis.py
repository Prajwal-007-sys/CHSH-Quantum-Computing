def calculate_correlation_from_counts(counts, shots=None):
    """
    Calculate:

        E_xy = P(00) + P(11) - P(01) - P(10)

    Measurement convention:

        0 -> +1
        1 -> -1

    Qiskit bitstring:
        bitstring[0] -> Bob
        bitstring[1] -> Alice
    """

    if shots is None:
        shots = sum(counts.values())

    correlation_sum = 0

    for bitstring, count in counts.items():

        b = int(bitstring[0])
        a = int(bitstring[1])

        A = 1 if a == 0 else -1
        B = 1 if b == 0 else -1

        correlation_sum += A * B * count

    return correlation_sum / shots


def calculate_chsh_parameter(E00, E01, E10, E11):
    """
    Calculate the CHSH Bell parameter:

        S = E00 + E01 + E10 - E11
    """

    return E00 + E01 + E10 - E11


def calculate_winning_probability_from_counts(
    counts,
    winning_condition
):
    """
    Calculate the probability of winning for one
    CHSH input pair.

    winning_condition:
        "correlated"
        "anti-correlated"
    """

    shots = sum(counts.values())

    if winning_condition == "correlated":

        winning_count = (
            counts.get("00", 0)
            + counts.get("11", 0)
        )

    elif winning_condition == "anti-correlated":

        winning_count = (
            counts.get("01", 0)
            + counts.get("10", 0)
        )

    else:
        raise ValueError(
            "winning_condition must be "
            "'correlated' or 'anti-correlated'"
        )

    return winning_count / shots


def calculate_all_correlations(counts_list):
    """
    Calculate E00, E01, E10 and E11 from
    the four circuit count dictionaries.
    """

    E00 = calculate_correlation_from_counts(counts_list[0])
    E01 = calculate_correlation_from_counts(counts_list[1])
    E10 = calculate_correlation_from_counts(counts_list[2])
    E11 = calculate_correlation_from_counts(counts_list[3])

    return {
        "E00": E00,
        "E01": E01,
        "E10": E10,
        "E11": E11
    }


def calculate_overall_winning_probability(counts_list):
    """
    Calculate the average CHSH winning probability
    over the four equally likely input combinations.
    """

    winning_conditions = [
        "correlated",
        "correlated",
        "correlated",
        "anti-correlated"
    ]

    probabilities = []

    for counts, condition in zip(
        counts_list,
        winning_conditions
    ):
        probabilities.append(
            calculate_winning_probability_from_counts(
                counts,
                condition
            )
        )

    return sum(probabilities) / len(probabilities)


def calculate_theoretical_values():
    """
    Return the classical and ideal quantum limits.
    """

    classical_S = 2
    quantum_S = 2 * (2 ** 0.5)

    classical_P = 0.75
    quantum_P = (2 + 2 ** 0.5) / 4

    return {
        "classical_S": classical_S,
        "quantum_S": quantum_S,
        "classical_P": classical_P,
        "quantum_P": quantum_P
    }