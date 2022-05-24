def get_first_derivative(function, x: float, step: float) -> float:
    return (function(x + step) - function(x - step)) / (2 * step)


def get_second_derivative(function, x: float, step: float) -> float:
    return (function(x + step) - 2 * function(x) + function(x - step)) / (step ** 2)
