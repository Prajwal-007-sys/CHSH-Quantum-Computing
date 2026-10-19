import random


def classical_strategy(x, y):
    """
    One optimal classical strategy for the CHSH game.

    Alice:
        x = 0 -> a = 0
        x = 1 -> a = 1

    Bob:
        y = 0 -> b = 1
        y = 1 -> b = 0
    """

    if x == 0:
        a = 0
    else:
        a = 1

    if y == 0:
        b = 1
    else:
        b = 0

    return a, b


def chsh_game(strategy):
    """
    Run one round of the CHSH game.

    Returns:
        1 if the players win
        0 otherwise
    """

    x = random.randint(0, 1)
    y = random.randint(0, 1)

    a, b = strategy(x, y)

    if (a != b) == (x & y):
        return 1

    return 0


def simulate_classical_strategy(num_games=1000):
    """
    Simulate multiple rounds using the classical strategy.
    """

    wins = 0

    for _ in range(num_games):
        wins += chsh_game(classical_strategy)

    return {
        "total_games": num_games,
        "wins": wins,
        "losses": num_games - wins,
        "winning_probability": wins / num_games
    }