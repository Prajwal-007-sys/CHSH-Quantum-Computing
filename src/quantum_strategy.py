from math import pi


ALICE_ANGLES = {
    0: 0,
    1: pi / 4
}

BOB_ANGLES = {
    0: pi / 8,
    1: -pi / 8
}


def get_alice_angle(x):
    """
    Return Alice's measurement angle for input x.
    """
    return ALICE_ANGLES[x]


def get_bob_angle(y):
    """
    Return Bob's measurement angle for input y.
    """
    return BOB_ANGLES[y]


def get_measurement_settings():
    """
    Return the complete CHSH measurement settings.
    """

    return {
        "alice": ALICE_ANGLES,
        "bob": BOB_ANGLES
    }