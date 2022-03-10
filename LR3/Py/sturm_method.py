import numpy as np


def get_sturm_system(polynom: list) -> list:
    sturm_system: list = [np.poly1d(polynom), np.poly1d(polynom).deriv()]

    counter: int = 1

    while sturm_system[counter][0] != 0.00:
        counter += 1
        sturm_system.append(np.polydiv(sturm_system[counter - 2], sturm_system[counter - 1])[1] * -1)

    return sturm_system


def get_number_of_sign_changes(sturm_series: list, value_to_insert: float) -> int:
    response: int = 0

    for counter in range(1, len(sturm_series)):
        if np.sign(sturm_series[counter](value_to_insert)) != np.sign(sturm_series[counter - 1](value_to_insert)):
            response += 1

    return response


def get_number_of_roots_by_sturm_theorem(source: list, range_from: float, range_to: float) -> int:
    sturm_system = get_sturm_system(source)

    left_range_side_sign_changes_number: int = get_number_of_sign_changes(sturm_system, range_from)
    right_range_side_sign_changes_number: int = get_number_of_sign_changes(sturm_system, range_to)

    return abs(left_range_side_sign_changes_number - right_range_side_sign_changes_number)
