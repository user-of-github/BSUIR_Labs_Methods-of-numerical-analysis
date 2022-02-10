from utils import get_copy


def get_full_system_matrix(main_coefficients: list, free_coefficients: list) -> list:
    response = get_copy(main_coefficients)
    for row in range(len(response)):
        response[row].append(free_coefficients[row])

    return response


def triangulate(matrix: list) -> None:
    def subtract_rows(out: int, what: int, ratio: float) -> None:
        for col in range(len(matrix[out])):
            matrix[out][col] -= matrix[what][col] * ratio

    for row in range(len(matrix)):
        for lower_row in range(row + 1, len(matrix)):
            ratio = matrix[lower_row][row] / matrix[row][row]
            subtract_rows(lower_row, row, ratio)


def back_substitution(matrix: list) -> list:
    rows, cols = len(matrix), len(matrix[0])
    response = [0] * len(matrix)

    for current in range(rows - 1, -1, -1):
        response[current] = matrix[current][cols - 1] / matrix[current][current]
        for upper_row in range(0, current):
            matrix[upper_row][cols - 1] -= matrix[upper_row][current] * response[current]

    return response


def gauss(main_coefficients: list, free_coefficients) -> list:
    full_matrix = get_full_system_matrix(main_coefficients, free_coefficients)
    triangulate(full_matrix)
    return back_substitution(full_matrix)
