import numpy as np


def get_sturm_system(polynom: list) -> list:
    sturm_system: list = [np.poly1d(polynom), np.poly1d(polynom).deriv()]

    counter: int = 1

    while sturm_system[counter][0] != 0.00:
        counter += 1
        sturm_system.append(np.polydiv(sturm_system[counter - 2], sturm_system[counter - 1])[1] * -1)

    return sturm_system


def get_number_of_roots_by_sturm_theorem(source: list) -> int:
    sturm_system = get_sturm_system(source)


    return 42
