import numpy.linalg.linalg


def get_nodes_array(interval: tuple[float, float], nodes_count: int) -> list[float]:
    response: list[float] = list()

    response.append(interval[0])

    step: float = (interval[1] - interval[0]) / (nodes_count - 1)

    for counter in range(1, nodes_count - 1):
        response.append(interval[0] + counter * step)

    response.append(interval[1])

    return response


def get_functions_values(function, x_array) -> list[float]:
    response: list[float] = list()

    for x in x_array:
        response.append(function(x))

    return response


# equations which link source function and my polynoms
def get_row_of_system_for_small_interval_from_source(unknowns_count: int, intervals_count: int, interval_number: int, x: float, y: float):
    response: list[float] = [0.0] * (intervals_count * unknowns_count + 1)

    degree: int = unknowns_count - 1

    for counter in range((interval_number - 1) * unknowns_count, (interval_number - 1) * unknowns_count + 4):
        response[counter] = x ** degree
        degree -= 1

    response[-1] = y

    return response


def get_row_of_system_for_small_interval_with_1_derivative(unknowns_count: int, intervals_count: int, interval_number: int, x: float):
    response: list[float] = [0.0] * (intervals_count * unknowns_count + 1)

    start_index: int = unknowns_count * (interval_number - 1)

    response[start_index] = 3 * x * x
    response[start_index + 1] = 2 * x
    response[start_index + 2] = 1
    response[start_index + 3] = 0

    response[start_index + 4] = -3 * x * x
    response[start_index + 5] = -2 * x
    response[start_index + 6] = -1
    response[start_index + 7] = 0

    return response


def get_row_of_system_for_small_interval_with_2_derivative(unknowns_count: int, intervals_count: int, interval_number: int, x: float):
    response: list[float] = [0.0] * (intervals_count * unknowns_count + 1)

    start_index: int = unknowns_count * (interval_number - 1)

    response[start_index] = 6 * x
    response[start_index + 1] = 2
    response[start_index + 2] = 0
    response[start_index + 3] = 0

    response[start_index + 4] = -6 * x
    response[start_index + 5] = -2
    response[start_index + 6] = 0
    response[start_index + 7] = 0

    return response


def get_row_of_system_with_edge_conditions(unknowns_count: int, intervals_count: int, x_first: float, x_last: float) -> tuple:
    first: list[float] = [0.0] * (intervals_count * unknowns_count + 1)
    second: list[float] = [0.0] * (intervals_count * unknowns_count + 1)

    first[0] = 6 * x_first
    first[1] = 2

    second[-2] = 2
    second[-3] = 6 * x_last

    return first, second


def extract_main_and_free_coefficients(matrix: list[list[float]]) -> tuple[list[list[float]], list[float]]:
    main_coefficients: list[list[float]] = list()
    free_coefficients: list[float] = list()

    for row in matrix:
        main_coefficients.append(row[0:-1])
        free_coefficients.append(row[-1])

    return main_coefficients, free_coefficients


def get_cubic_splines_coefficients(function, nodes_count: int, interval: tuple[float, float]) -> list[list]:
    x_array: list[float] = get_nodes_array(interval, nodes_count)

    y_array: list[float] = get_functions_values(function, x_array)

    matrix: list[list[float]] = list()

    # для начальных условий, которые именно связывают исходную функцию и новые полиномы в узлах интерполирования
    for counter in range(1, nodes_count):
        matrix.append(get_row_of_system_for_small_interval_from_source(
            4, nodes_count - 1, counter, x_array[counter - 1], y_array[counter - 1]
        ))
        matrix.append(get_row_of_system_for_small_interval_from_source(
            4, nodes_count - 1, counter, x_array[counter], y_array[counter]
        ))

    # теперь в некрайних точках первая производная у соседних полиномов в одной точке должна совпадать
    for counter in range(1, nodes_count - 1):
        matrix.append(get_row_of_system_for_small_interval_with_1_derivative(
            4, nodes_count - 1, counter, x_array[counter]
        ))

    # то же самое для второй производной
    for counter in range(1, nodes_count - 1):
        matrix.append(get_row_of_system_for_small_interval_with_2_derivative(
            4, nodes_count - 1, counter, x_array[counter]
        ))

    # и два краевых условия, так как у нас 4*n неизвестных, двух уравнений не хватает
    conditions: tuple = get_row_of_system_with_edge_conditions(4, nodes_count - 1, x_array[0], x_array[-1])

    matrix.append(conditions[0])
    matrix.append(conditions[1])
  
    result = list(numpy.linalg.linalg.solve(*extract_main_and_free_coefficients(matrix)))

    return result
