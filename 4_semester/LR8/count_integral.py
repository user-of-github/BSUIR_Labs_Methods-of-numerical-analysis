import time


def get_y_list(function, interval: tuple[float, float], step: float) -> list[float]:
    steps_count: int = int((interval[1] - interval[0]) / step)

    start_value: float = interval[0]

    response: list[float] = list()

    for counter in range(steps_count + 1):
        response.append(function(start_value))
        start_value += step

    return response


def get_x_list_for_average_rectangles(interval: tuple[float, float], step: float) -> list[float]:
    steps_count: int = int((interval[1] - interval[0]) / step)

    start_value: float = interval[0]
    response: list[float] = list()

    for counter in range(steps_count + 1):
        response.append(start_value + step / 2)
        start_value += step

    return response


def count_integral_by_trapezoid_formula(function, interval: tuple[float, float], accuracy: float) -> (float, float):
    start_time: float = time.time()

    y_list: list[float] = get_y_list(function, interval, accuracy)

    response: float = 0

    for counter in range(1, len(y_list) - 1):
        response += y_list[counter]

    response += (y_list[0] + y_list[-1]) / 2

    response *= accuracy

    return response, (time.time() - start_time)


def count_integral_by_simpson_formula(function, interval: tuple[float, float], accuracy: float) -> (float, float):
    start_time: float = time.time()
    y_list: list[float] = get_y_list(function, interval, accuracy)

    for_ratio_2: list[float] = y_list[::2][1:-1]
    for_ratio_4: list[float] = y_list[1::2]

    response: float = y_list[0] + y_list[-1] + 2 * sum(for_ratio_2) + 4 * sum(for_ratio_4)

    response *= (accuracy / 3)

    return response, (time.time() - start_time)


def count_integral_by_middle_reactangles(function, interval: tuple[float, float], accuracy: float) -> (float, float):
    start_time: float = time.time()
    x_list: list[float] = get_x_list_for_average_rectangles(interval, accuracy)

    response: float = 0

    for x in x_list:
        response += function(x)

    response *= accuracy

    return response, (time.time() - start_time)