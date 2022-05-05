import sympy
from sympy.abc import x, y


def get_basis_polynom(current: int, x_array: list[float]) -> sympy.poly:
    response = sympy.poly(1, x)

    for counter in range(len(x_array)):
        if counter != current:
            response *= sympy.poly((x - x_array[counter]) / (x_array[current] - x_array[counter]))

    return response


def get_lagrange_polynom(x_array: list[float], y_array: list[float]) -> sympy.poly:
    print(sympy.poly(x))
    response = sympy.poly(0, x)

    for counter in range(len(x_array)):
        response += y_array[counter] * get_basis_polynom(counter, x_array)

    return response
