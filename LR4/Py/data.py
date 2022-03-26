from sympy import symbols, tan, sqrt

TEST_SUITE: list[tuple] = [
    (7, 0.3, 0.5),
    (8, 0.4, 0.6),
    (9, 0.4, 0.7)
]

X, Y = symbols('X Y')

# ((system), (transformed system (x = Ф(x))), (initial approximation (by chart))
TEST_SUITE_EQUATIONS_SYSTEM: list[tuple] = [
    (
        (tan(X * Y + 0.3) - X, 0.5 * (X ** 2) + 2 * (Y ** 2) - 1),
        (tan(X * Y + 0.3), sqrt(0.5 - 0.25 * (X ** 2))),
        (1, 0.5)
    )
]

EPSILON: float = 0.0001
