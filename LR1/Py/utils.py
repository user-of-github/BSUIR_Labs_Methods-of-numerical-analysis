import copy


def get_copy(some_list_or_matrix: list) -> list:
    return copy.deepcopy(some_list_or_matrix)


def multiply_matrix_by_ratio(matrix: list, ratio: int) -> list:
    response = get_copy(matrix)
    for row in range(len(response)):
        for col in range(len(response[row])):
            response[row][col] *= ratio

    return response


def sum_two_matrices(first: list, second: list) -> list:
    response = get_copy(first)
    for row in range(len(response)):
        for col in range(len(response[row])):
            response[row][col] += second[row][col]

    return response


def get_accuracy(accuracy: float) -> int:
    accuracy_copy = accuracy
    response = 0
    while accuracy_copy < 1:
        accuracy_copy *= 10
        response += 1

    return response + 1
