import numpy as np


def get_root_by_half_division(source: list[float], search_from: float, search_to: float, error: float) -> (float, int):
    polynom = np.poly1d(source)

    left_border: float = search_from
    right_border: float = search_to

    if polynom(left_border) * polynom(right_border) > 0:
        raise Exception('Condition f(a) * f(b) is not met')

    middle_of_interval: float = (left_border + right_border) / 2
    iterations_count: int = 0

    while abs(polynom(middle_of_interval)) >= error:
        middle_of_interval = (left_border + right_border) / 2

        if polynom(left_border) * polynom(middle_of_interval) < 0:
            right_border = middle_of_interval
        elif polynom(middle_of_interval) * polynom(right_border) < 0:
            left_border = middle_of_interval

        iterations_count += 1

    return (left_border + right_border) / 2, iterations_count
