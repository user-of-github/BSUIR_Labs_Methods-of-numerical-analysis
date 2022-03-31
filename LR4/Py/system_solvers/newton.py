import sympy
from system_solvers.general_utils import get_norm_of_root_vectors_difference


def get_jacobi_matrix(system: tuple, variables_list: list) -> sympy.Matrix:
    response: sympy.Matrix = sympy.Matrix([[0, 0], [0, 0]])

    for row_index, equation in enumerate(system):
        for col_index, variable in enumerate(variables_list):
            response[row_index, col_index] = sympy.diff(equation, variable)

    return response


def solve_non_linear_system_by_newton_method(system: tuple, variables_list: list, epsilon: float) -> (sympy.Matrix, int):
    matrix: sympy.Matrix = sympy.Matrix(list(system[0]))
    jacobi_matrix: sympy.Matrix = get_jacobi_matrix(system[0], variables_list)

    current_iteration: sympy.Matrix = sympy.Matrix([*system[1]])
    sympy.Matrix([*system[1]])

    difference: float = 1.00
    iterations_count: int = 0

    while difference > epsilon:
        previous_iteration: sympy.Matrix = sympy.Matrix(current_iteration)

        current_iteration = previous_iteration - jacobi_matrix.subs({
            variables_list[0]: previous_iteration[0],
            variables_list[1]: previous_iteration[1]
        }).inv(method='LU') * matrix.subs({
            variables_list[0]: previous_iteration[0],
            variables_list[1]: previous_iteration[1]
        })

        difference = get_norm_of_root_vectors_difference(current_iteration, previous_iteration)
        iterations_count += 1

    return current_iteration, iterations_count
