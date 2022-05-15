import data
from utils import get_copy
from enum import Enum


class SimpleIterationsSolvingType(Enum):
    DEFAULT = 'DEFAULT',
    SEIDEL = 'SEIDEL'


def express_main_diagonal_variables(main_coefficients: list, free_coefficients: list) -> list:
    response = get_copy(main_coefficients)
    for row in response:
        row.append(0)

    for row in range(0, len(main_coefficients)):
        full_width = len(main_coefficients[row]) + 1
        current_variable_ratio = main_coefficients[row][row] + 0

        response[row][0] = free_coefficients[row] / current_variable_ratio
        for col in range(1, full_width):
            response[row][col] = 0 if col - 1 == row \
                else (-1) * main_coefficients[row][col - 1] / current_variable_ratio

    return response


# Подсчёт значения переменной с текущими значениями переменных с предыдущей итерации
# Например, x2 = 6 + 0.3 * x1 + 0 * x2 + 3 * x3 => при наличии с прошлой итерации переменных x1 .. x3 считаю новое значение для x3
def count_variable_value(variable_expression: list, with_variable_set: list) -> float:
    response = variable_expression[0]
    for counter in range(1, len(variable_expression)):
        response += with_variable_set[counter - 1] * variable_expression[counter]
    return response


def count_all_variables_values(variables_expressions: list, with_variables_set: list, variables: list) -> None:
    for counter in range(0, len(variables_expressions)):
        variables[counter] = count_variable_value(variables_expressions[counter], with_variables_set)


def get_accuracy_error(current_iteration: list, previous_iteration: list) -> float:
    error = 0.0
    for counter in range(0, len(current_iteration)):
        error = max(error, abs(current_iteration[counter] - previous_iteration[counter]))
    return error


def solve_by_simple_iterations(main_coefficients: list,
                               free_coefficients: list,
                               epsilon: float,
                               solving_type: SimpleIterationsSolvingType) -> (list, int):
    # выразил переменные из начальных матриц
    variables_expressions = express_main_diagonal_variables(main_coefficients, free_coefficients)

    current_iteration = get_copy(data.INITIAL_VALUES)
    previous_iteration = get_copy(current_iteration)

    # посчитал текущее значение (i + 1)-е с начальными значениями
    count_all_variables_values(variables_expressions, previous_iteration, current_iteration)

    # уже один, так как одна итерация была выше (а была выше перед while, т.к. в Python нет do while)
    iterations_count = 1

    while get_accuracy_error(current_iteration, previous_iteration) > epsilon:
        previous_iteration = get_copy(current_iteration)

        count_all_variables_values(
            variables_expressions,
            previous_iteration if solving_type == SimpleIterationsSolvingType.DEFAULT else current_iteration,
            current_iteration
        )
        iterations_count += 1

    return current_iteration, iterations_count
