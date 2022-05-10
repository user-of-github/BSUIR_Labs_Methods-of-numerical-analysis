from math import exp, sinh


def calculate_function_1(argument: float) -> float:
    return exp(-argument)


def calculate_function_2(argument: float) -> float:
    return sinh(argument)


FUNCTIONS: list = [calculate_function_1, calculate_function_2]

INTERVAL: list[tuple[float, float]] = [(0, 4), (0, 2)]

NODES_COUNT: list[int] = [5, 6]


def get_x_to_count_value(index: int) -> float:
    return 0.5 * (INTERVAL[index][1] - INTERVAL[index][0])
