import numpy as np


# Для выпуклой (f'' > 0)
def for_convex_function(polynom, left_border: float, right_border: float, error: float) -> (float, int):
    root: float = left_border
    iterations_count: int = 0

    while abs(polynom(root)) > error:
        root = root - (polynom(root) / (polynom(right_border) - polynom(root))) * (right_border - root)
        iterations_count += 1

    return root, iterations_count


# Для вогнутой (f'' < 0)
def for_concave_function(polynom, left_border: float, right_border: float, error: float) -> (float, int):
    root: float = right_border
    iterations_count: int = 0

    while abs(polynom(root)) > error:
        root = root - (polynom(root) / (polynom(left_border) - polynom(root))) * (left_border - root)
        iterations_count += 1

    return root, iterations_count


def get_root_by_chord_method(source: list[float], search_from: float, search_to: float, error: float) -> (float, int):
    polynom = np.poly1d(source)

    left_border: float = search_from
    right_border: float = search_to

    if polynom(left_border) * polynom(right_border) > 0:
        raise Exception('Condition f(a) * f(b) is not met')

    second_derivative = np.polyder(polynom, 2)

    if polynom(right_border) * second_derivative(right_border) > 0:
        return for_convex_function(polynom, left_border, right_border, error)
    elif polynom(left_border) * second_derivative(left_border) > 0:
        return for_concave_function(polynom, left_border, right_border, error)
