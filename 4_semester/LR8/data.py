import math

ACCURACY_DERIVATIVE: float = 0.01

FUNCTIONS: list = [lambda x: math.log10(x), lambda x: math.atan(x)]
ACCURACY_INTEGRALS: list[float] = [0.000001, 0.000001]

INTERVALS: list[tuple[float, float]] = [(1, 3), (0, 2)]

OPTIONS_COUNT: int = min(len(FUNCTIONS), len(ACCURACY_INTEGRALS), len(INTERVALS))
