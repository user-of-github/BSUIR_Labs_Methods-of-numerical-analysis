import math
import numpy as np


def find_max_absolute_non_diagonal_element(matrix: np.matrix) -> (int, int):
    max_element: float = matrix[0, 1]
    response_row, response_col = 0, 1
    size: int = len(matrix)

    for row in range(size):
        for col in range(size):
            if row != col:
                if abs(matrix[row, col]) > max_element:
                    max_element = abs(matrix[row, col])
                    response_row, response_col = row, col

    if response_row > response_col:
        response_row, response_col = response_col, response_row

    return response_row, response_col


def get_matrix_of_rotation(matrix: np.matrix, row_max: int, col_max: int) -> np.matrix:
    response: np.matrix = np.matrix(np.eye(len(matrix)))

    a_ii: float = matrix[row_max, row_max]
    a_jj: float = matrix[col_max, col_max]
    a_ij: float = matrix[row_max, col_max]

    if a_ii != a_jj:
        p_k: float = (2 * a_ij) / (a_ii - a_jj)
        p_k_2: float = p_k ** 2

        cosine = math.sqrt(0.5 * (1 + (1 + p_k_2) ** -0.5))
        sinus = np.sign(p_k) * math.sqrt(0.5 * (1 - (1 + p_k_2) ** -0.5))
    else:
        cosine = math.sqrt(2) / 2
        sinus = math.sqrt(2) / 2

    response[row_max, row_max] = cosine
    response[col_max, col_max] = cosine

    response[row_max, col_max] = -1 * sinus
    response[col_max, row_max] = sinus

    print(response,end='\n\n')

    return response


def get_sum_of_squares_of_non_diagonal_elements(matrix: np.matrix) -> float:
    size: int = len(matrix)
    response: float = 0.00

    for row in range(size):
        for col in range(size):
            if row != col:
                response += matrix[row, col] ** 2

    return response


def get_total_eigenvalues_of_totally_rotated_matrix(result_matrix: np.matrix) -> list[float]:
    response: list[float] = list()
    size: int = len(result_matrix)

    for row in range(size):
        response.append(result_matrix[row, row])

    return response


# list with eigen values + list with eigen vectors
def get_eigen_values_and_vectors_by_jacobi_method(source: np.matrix, error: float) -> (list[float], list):
    matrix: np.matrix = np.matrix(source)

    while get_sum_of_squares_of_non_diagonal_elements(matrix) > error:
        row_max, col_max = find_max_absolute_non_diagonal_element(matrix)

        rotation_matrix: np.matrix = get_matrix_of_rotation(matrix, row_max, col_max)
        reversed_rotation_matrix: np.matrix = np.linalg.inv(np.matrix(rotation_matrix))

        matrix = np.matrix(np.matmul(np.matmul(reversed_rotation_matrix, matrix), rotation_matrix))

    return get_total_eigenvalues_of_totally_rotated_matrix(matrix), list()
