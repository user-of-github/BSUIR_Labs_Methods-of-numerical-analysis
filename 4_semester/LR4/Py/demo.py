from system_solvers.newton import solve_non_linear_system_by_newton_method
from system_solvers.simple_iterations import solve_non_linear_system_by_simple_iterations_method


def demonstrate_newton(equation_system: tuple, variables_list: list, epsilon: float) -> None:
    print(*solve_non_linear_system_by_newton_method(equation_system, variables_list, epsilon))


def demonstrate_simple_iterations(transformed_equation_system: tuple, variables_list: list, epsilon: float) -> None:
    print(*solve_non_linear_system_by_simple_iterations_method(transformed_equation_system, variables_list, epsilon))
