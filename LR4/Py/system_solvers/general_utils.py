import sympy


def get_norm_of_root_vectors_difference(first: sympy.Matrix, second: sympy.Matrix) -> float:
    max_difference: float = 0

    for counter in range(len(first)):
        max_difference = max(max_difference, abs(first[counter] - second[counter]))

    return max_difference
