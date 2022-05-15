import numpy as np


def get_root_by_newton_method(source: list[float], search_from: float, search_to: float, error: float) -> (float, int):
    polynom = np.poly1d(source)

    left_border: float = search_from
    right_border: float = search_to

    first_derivative = np.polyder(polynom)
    second_derivative = np.polyder(first_derivative)

    root: float = left_border
    iterations_count: float = 0

    if second_derivative(right_border) * polynom(right_border) > 0:
        root = right_border
    elif second_derivative(left_border) * polynom(left_border) > 0:
        root = left_border

    while abs(polynom(root)) > error:
        root = root - polynom(root) / first_derivative(root)
        iterations_count += 1

    return root, iterations_count
