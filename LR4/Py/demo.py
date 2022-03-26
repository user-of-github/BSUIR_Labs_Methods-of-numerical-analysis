from newton import solve_non_linear_system_by_newton_method


def demonstrate(transformed_equation_system: tuple, variables_list: list, epsilon: float) -> None:
    solution_by_newton = solve_non_linear_system_by_newton_method(
        transformed_equation_system,
        variables_list,
        epsilon
    )
