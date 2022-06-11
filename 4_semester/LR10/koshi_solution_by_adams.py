def koshi_by_adams_explicit(funct, interval: tuple, step: float, initial: tuple, a, m) -> tuple[list, list]:
    f: list[float] = list()
    x: list[float] = list()
    y: list[float] = list()

    x.append(initial[0])
    y.append(initial[0])
    f.append(funct(x[0], y[0], a, m))

    # Нужна ещё одна следующая пара (x, y). Получу её через формулы Рунге-Кутты, например
    x.append(initial[0] + step)
    k1: float = funct(x[0], y[0], a, m)
    k2: float = funct(x[0] + step / 2, y[0] + step * k1 / 2, a, m)
    k3: float = funct(x[0] + step / 2, y[0] + step * k2 / 2, a, m)
    k4: float = funct(x[0] + step, y[0] + step * k3, a, m)
    dy: float = (step / 6) * (k1 + 2 * k2 + 3 * k3 + k4)
    y.append(y[0] + dy)
    f.append(funct(x[1], y[1], a, m))

    steps_count: int = int((interval[1] - interval[0]) // step)

    for counter in range(2, steps_count + 1):
        x.append(x[counter - 1] + step)
        y.append(y[counter - 1] + step * (1.5 * funct(x[counter - 1], y[counter - 1], a, m) - 0.5 * funct(x[counter - 2], y[counter - 2], a, m)))

    return x, y