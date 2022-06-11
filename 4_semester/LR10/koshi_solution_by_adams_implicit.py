from scipy.optimize import fsolve
import itertools


def wrapper(x_prev: float, y_prev: float, x: float, step: float, a: float, m: float, funct):
    def func(y):
        func_current_value = ((a * (1 - (y[0] ** 2))) / ((1 + m) * x ** 2 + y[0] ** 2 + 1))
        func_previous_value: float = funct(x_prev, y_prev, a, m)

        return y_prev + 0.5 * step * func_current_value + 0.5 * step * func_previous_value - y[0]

    return func


def koshi_by_adams_implicit(funct, interval: tuple, step: float, initial: tuple, a, m) -> tuple[list, list]:
    x: list[float] = list()
    y: list = list()

    x.append(initial[0])
    y.append(initial[0])

    steps_count: int = int((interval[1] - interval[0]) // step)

    for counter in range(1, steps_count + 1):
        x.append(x[counter - 1] + step)
        y.append(fsolve(wrapper(x[counter - 1], y[counter - 1], x[counter], step, a, m, funct), [1]))

    y = list(itertools.chain(*y[1:-1]))
    y.insert(0, initial[1])

    return x[0:-1], y