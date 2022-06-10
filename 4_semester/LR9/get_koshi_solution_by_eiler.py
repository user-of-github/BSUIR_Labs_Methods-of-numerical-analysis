import matplotlib.pyplot as plt


def koshi_problem_solution_by_euler(funct, interval: tuple, step: float, initial: tuple, a, m) -> list[tuple]:
    f: list[float] = list()
    fh: list[float] = list()
    x: list[float] = list()
    y: list[float] = list()

    x.append(initial[0])
    y.append(initial[0])

    f.append(funct(x[0], y[0], a, m))
    fh.append(f[0] * step)

    steps_count: int = int((interval[1] - interval[0]) // step)

    for counter in range(1, steps_count + 1):
        x.append(x[counter - 1] + step)
        y.append(y[counter - 1] + fh[counter - 1])
        f.append(funct(x[counter], y[counter], a, m))
        fh.append(f[counter] * step)

    print(x)
    print(y)

    plt.plot(x, y, mew=2, ms=10)
    plt.show()

    response: list[tuple[float, float]] = list()

    return response

# http://mathprofi.ru/metody_eilera_i_runge_kutty.html
