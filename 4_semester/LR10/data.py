A: list[float] = [0.5, 0.7, 0.9, 1.1, 1.3, 0.5, 0.7]

M: list[float] = [1.0, 1.5, 2.0, 1.0, 1.5, 2.0, 1.0]

EPSILON: float = 0.001

INTERVAL: tuple[float, float] = (0, 1)


def function(x: float, y: float, a: float, m: float) -> float:
    return (a * (1 - y ** 2)) / ((1 + m) * x * x + y ** 2 + 1)


START_CONDITION: tuple[float, float] = (0.0, 0.0)