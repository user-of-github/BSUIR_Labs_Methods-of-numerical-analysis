import sympy
from system_solvers.general_utils import get_norm_of_root_vectors_difference


def solve_non_linear_system_by_simple_iterations_method(transformed_system: tuple,
                                                        variables_list: list,
                                                        epsilon: float) -> (sympy.Matrix, int):
    system: sympy.Matrix = sympy.Matrix(list(transformed_system[0]))
    print(list(transformed_system[0]))

    current_iteration: sympy.Matrix = sympy.Matrix(list(transformed_system[1]))

    iterations_count: int = 0

    error: float = 1.00

    while error > epsilon:
        previous_iteration: sympy.Matrix = sympy.Matrix(current_iteration)

        for counter in range(len(current_iteration)):
            current_iteration[counter] = system[counter].subs({
                variables_list[0]: previous_iteration[0],
                variables_list[1]: previous_iteration[1]
            })

        error = get_norm_of_root_vectors_difference(current_iteration, previous_iteration)
        iterations_count += 1

    return current_iteration, iterations_count
