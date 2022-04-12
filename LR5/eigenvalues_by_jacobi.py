import math
import numpy as np

import data


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
        # if a[i][i] == a[j][j] we take sin(Pi / 4) and cos(Pi / 4)
        cosine = math.sqrt(2) / 2
        sinus = math.sqrt(2) / 2

    response[row_max, row_max] = cosine
    response[col_max, col_max] = cosine

    response[row_max, col_max] = -1 * sinus
    response[col_max, row_max] = sinus

    return response


def get_sum_of_squares_of_non_diagonal_elements(matrix: np.matrix) -> float:
    size: int = len(matrix)
    response: float = 0.00

    for row in range(size):
        for col in range(size):
            if row != col:
                response += matrix[row, col] ** 2

    return response


# in result matrix we have eigenvalues on diagonal
def get_total_eigenvalues_of_totally_rotated_matrix(result_matrix: np.matrix) -> list[float]:
    response: list[float] = list()

    for row in range(len(result_matrix)):
        response.append(result_matrix[row, row])

    return response


# multiplies all matrices of rotation and extracts columns to get eigenvectors
def get_total_eigenvectors(rotation_matrices: list[np.matrix]) -> list[list[float]]:
    multiplication_result: np.matrix = np.matrix(rotation_matrices[0])

    for counter in range(1, len(rotation_matrices)):
        multiplication_result = np.matrix(np.matmul(multiplication_result, rotation_matrices[counter]))

    response: list[list[float]] = list()

    for col in range(len(multiplication_result)):
        column: list[float] = list()

        for row in range(len(multiplication_result)):
            column.append(multiplication_result[row, col])

        response.append(column)

    return response


# for printing necessary number of digits after dot
def prettify_response(eigenvalues: list[float], eigenvectors: list[list[float]]) -> None:
    for counter in range(len(eigenvalues)):
        eigenvalues[counter] = round(eigenvalues[counter], data.ACCURACY)

    for vector in eigenvectors:
        for counter in range(len(vector)):
            vector[counter] = round(vector[counter], data.ACCURACY)


# list with eigen values + list with eigen vectors
def get_eigen_values_and_vectors_by_jacobi_method(source: np.matrix, error: float) -> (list[float], list):
    matrix: np.matrix = np.matrix(source)
    for_eigenvectors: list[np.matrix] = list()

    while get_sum_of_squares_of_non_diagonal_elements(matrix) > error:
        row_max, col_max = find_max_absolute_non_diagonal_element(matrix)

        rotation_matrix: np.matrix = get_matrix_of_rotation(matrix, row_max, col_max)
        reversed_rotation_matrix: np.matrix = np.linalg.inv(np.matrix(rotation_matrix))

        matrix = np.matrix(np.matmul(np.matmul(reversed_rotation_matrix, matrix), rotation_matrix))

        for_eigenvectors.append(rotation_matrix)

    eigenvalues: list[float] = get_total_eigenvalues_of_totally_rotated_matrix(matrix)
    eigenvectors: list[list[float]] = get_total_eigenvectors(for_eigenvectors)

    prettify_response(eigenvalues, eigenvectors)

    return eigenvalues, eigenvectors
