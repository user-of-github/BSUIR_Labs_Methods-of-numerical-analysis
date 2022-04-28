OPTION: int = 7

M: list[float] = [0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 1.8, 2.53, 3.96, 5.33, 1.96]

X: list[float] = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

P: list[float] = [0.0, 0.41, 0.79, 1.13, 1.46, 1.76, 2.04, 2.3, 2.55, 2.79, 3.01]


def get_y(option: int) -> list[float]:
    response: list = list()

    for counter in range(len(P)):
        response.append(P[counter] + ((-1) ** option) * M[option])

    return response


def get_points(option: int) -> list[tuple[float, float]]:
    response: list[tuple[float, float]] = list()

    Ys: list[float] = get_y(option)

    for counter in range(len(X)):
        response.append((X[counter], Ys[counter]))

    return response
