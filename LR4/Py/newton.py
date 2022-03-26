import copy

import sympy


def get_jacobi_matrix(system: tuple, variables_list: list) -> list[list]:
    response: list = list()

    for equation in system:
        new_row: list = list()

        for variable in variables_list:
            print(equation, variable)
            new_row.append(sympy.diff(equation, variable))

        response.append(new_row)

    return response


def get_norm_of_root_vectors_difference(first: list[float], second: list[float]) -> float:
    max_difference: float = 0

    for counter in range(len(first)):
        max_difference = max(max_difference, abs(first[counter] - second[counter]))

    return max_difference


def fill_subs_for_function(variables_list: list, previous_iteration_roots: list[float]) -> list[tuple]:
    response: list[tuple] = list()

    for counter in range(len(variables_list)):
        print(variables_list[counter], previous_iteration_roots[counter])
        response.append((variables_list[counter], previous_iteration_roots[counter]))

    return response


def solve_non_linear_system_by_newton_method(system: tuple, variables_list: list, epsilon: float) -> list:
    jacobi_matrix: list[list] = get_jacobi_matrix(system[0], variables_list)

    previous_iteration_roots: list[float] = list(system[2])
    current_iteration_roots: list[float] = list(system[2])
    iterations_count: int = 0

    difference: float = 1

    while difference > epsilon:
        previous_iteration_roots = list(copy.copy(current_iteration_roots))
        variables_and_values: list[tuple] = fill_subs_for_function(variables_list, previous_iteration_roots)
        current_iteration_roots[0] = system[1][0].subs(variables_and_values)
        current_iteration_roots[1] = system[1][1].subs(variables_and_values)
        print(variables_and_values)
        difference = get_norm_of_root_vectors_difference(current_iteration_roots, previous_iteration_roots)
        iterations_count += 1

    return current_iteration_roots
