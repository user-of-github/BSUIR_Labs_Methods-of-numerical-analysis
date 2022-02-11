from utils import get_copy
from enum import Enum


class SolutionType(Enum):
    SCHEME_OF_THE_ONLY_SOLUTION = 'SCHEME_OF_THE_ONLY_SOLUTION',
    SCHEME_OF_PARTIAL_SELECTION = 'SCHEME_OF_PARTIAL_SELECTION',
    SCHEME_OF_FULL_SELECTION = 'SCHEME_OF_FULL_SELECTION'


def get_full_system_matrix(main_coefficients: list, free_coefficients: list) -> list:
    response = get_copy(main_coefficients)
    for row in range(len(response)):
        response[row].append(free_coefficients[row])

    return response


def triangulate(matrix: list, solution_type: SolutionType) -> None:
    def subtract_rows(out: int, what: int, ratio: float) -> None:
        for col in range(len(matrix[out])):
            matrix[out][col] -= matrix[what][col] * ratio

    def find_row_with_max_main_element(search_from: int) -> int:
        response = search_from
        for row_counter in range(search_from + 1, len(matrix)):
            if abs(matrix[row_counter][search_from]) > abs(matrix[response][search_from]):
                response = row_counter
        return response

    def found_row_with_max_left_matrix_element(search_from: int) -> int:
        maximum_element = matrix[search_from][0]
        for row_counter in range(search_from + 1, len(matrix)):
            maximum_element = max(maximum_element, max(matrix[row_counter]))

        for row_counter in range(search_from + 1, len(matrix)):
            for col_counter in range(0, len(matrix[row_counter])):
                if maximum_element == matrix[row_counter][col_counter]:
                    return row_counter

        return search_from

    def swap_rows(first: int, second: int) -> None:
        for col in range(0, len(matrix) + 1):
            matrix[first][col], matrix[second][col] = matrix[second][col], matrix[first][col]

    for row in range(len(matrix)):
        if solution_type == SolutionType.SCHEME_OF_PARTIAL_SELECTION:
            row_with_max_main_element = find_row_with_max_main_element(row)
            swap_rows(row_with_max_main_element, row)
        elif solution_type == SolutionType.SCHEME_OF_FULL_SELECTION:
            row_with_max_matrix_element = found_row_with_max_left_matrix_element(row)
            swap_rows(row_with_max_matrix_element, row)

        for lower_row in range(row + 1, len(matrix)):
            coefficient = matrix[lower_row][row] / matrix[row][row]
            subtract_rows(lower_row, row, coefficient)


def back_substitution(matrix: list) -> list:
    rows, cols = len(matrix), len(matrix[0])
    response = [0] * len(matrix)

    for current in range(rows - 1, -1, -1):
        response[current] = matrix[current][cols - 1] / matrix[current][current]
        for upper_row in range(0, current):
            matrix[upper_row][cols - 1] -= matrix[upper_row][current] * response[current]

    return response


def print_matrix(matrix: list) -> None:
    for row in matrix:
        for item in row:
            print(round(item, 3), end=' ')
        print()


def gauss(main_coefficients: list, free_coefficients: list, solution_type: SolutionType) -> list:
    full_matrix = get_full_system_matrix(main_coefficients, free_coefficients)
    triangulate(full_matrix, solution_type)
    print_matrix(full_matrix)
    return back_substitution(full_matrix)
