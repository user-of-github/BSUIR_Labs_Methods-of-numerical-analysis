import math
import pprint
import matplotlib.pyplot as plt
import numpy as np


# a * y" + (1 + b * x^2) y = -1

# the quadratic norm. You can change to another
def get_norm(values: list[float], step: float) -> float:
    # summ: float = 0.0
    #
    # for value in values:
    #     summ += value * value * step
    #
    # return math.sqrt(summ)
    return max(*values)


# returns array for x, array for y and NORM for such grid function
def get_1_task_solution_with_number_of_dots(n: int, a: float, b: float, interval: tuple[float, float], initials: tuple[float, float]) -> tuple[list[float], list[float], float]:
    step: float = (interval[1] - interval[0]) / n

    y_k = lambda x: step * step * (1 + b * x * x) / a - 2

    b: float = step * step * (-1) / a
    # vector of free coefficients (including initial conditions for y(a) and y(b))
    free_coefficients_array: list[float] = [b] * (n + 1)
    free_coefficients_array[0] = initials[0]
    free_coefficients_array[-1] = initials[1]

    # matrix of main coefficients
    main_coefficients: list[list[float]] = [[0] * (n + 1)]
    main_coefficients[0][0] = 1

    # array of dots, on which we divide our range a..b
    x_array: list[float] = [interval[0]]

    for k in range(1, n):
        new_row: list[float] = [0] * (n + 1)
        new_row[k - 1] = 1
        x_array.append(x_array[-1] + step)
        new_row[k] = y_k(x_array[-1])
        new_row[k + 1] = 1
        main_coefficients.append(new_row)
        #print(k)
        #print(interval[0] + step * k)
        #print(new_row)
        #print('____')

    x_array.append(interval[1])

    main_coefficients.append([0] * (n + 1))
    main_coefficients[-1][-1] = 1

    #pprint.pprint(main_coefficients)
    #pprint.pprint(free_coefficients_array)

    y_array: list[float] = list(np.linalg.solve(main_coefficients, free_coefficients_array))

    #№plt.plot(x_array, y_array, mew=2, ms=10)
    #plt.show()

    return x_array, y_array, get_norm(y_array, step)


def get_1_task_solution(a: float, b: float, epsilon: float, interval: tuple[float, float], initials: tuple[float, float]) -> list:
    number_of_ranges: int = 3

    first_solution = get_1_task_solution_with_number_of_dots(number_of_ranges, a, b, interval, initials)
    print(number_of_ranges)

    number_of_ranges += number_of_ranges // 2
    print(number_of_ranges)

    second_solution = get_1_task_solution_with_number_of_dots(number_of_ranges, a, b, interval, initials)
    print(abs(first_solution[2] - second_solution[2]))

    while abs(first_solution[2] - second_solution[2]) > epsilon:
        number_of_ranges += number_of_ranges // 2
        first_solution = second_solution
        second_solution = get_1_task_solution_with_number_of_dots(number_of_ranges, a, b, interval, initials)
        print(number_of_ranges)
        print(abs(first_solution[2] - second_solution[2]))
