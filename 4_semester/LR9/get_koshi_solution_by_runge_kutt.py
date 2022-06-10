import matplotlib.pyplot as plt


def koshi_problem_solution_by_runge_kutt(funct, interval: tuple, step: float, initial: tuple, a, m) -> list[tuple]:
    k1: list[float] = list()
    k2: list[float] = list()
    k3: list[float] = list()
    k4: list[float] = list()

    x: list[float] = list()
    y: list[float] = list()
    dy: list[float] = list()

    x.append(initial[0])
    y.append(initial[0])

    k1.append(funct(x[0], y[0], a, m))
    k2.append(funct(x[0] + step / 2, y[0] + step * k1[0] / 2, a, m))
    k3.append(funct(x[0] + step / 2, y[0] + step * k2[0] / 2, a, m))
    k4.append(funct(x[0] + step, y[0] + step * k3[0], a, m))
    dy.append((step / 6) * (k1[0] + 2*k2[0] + 2*k3[0] + k4[0]))

    steps_count: int = int((interval[1] - interval[0]) // step)

    for counter in range(1, steps_count + 1):
        y.append(y[counter - 1] + dy[counter - 1])
        x.append(x[counter - 1] + step)
        k1.append(funct(x[counter], y[counter], a, m))
        k2.append(funct(x[counter] + step / 2, y[counter] + step * k1[counter] / 2, a, m))
        k3.append(funct(x[counter] + step / 2, y[counter] + step * k2[counter] / 2, a, m))
        k4.append(funct(x[counter] + step, y[counter] + step * k3[0], a, m))
        dy.append((step / 6) * (k1[counter] + 2*k2[counter] + 2*k3[counter] + k4[counter]))

    plt.plot(x, y, mew=2, ms=10)
    plt.show()

    return []