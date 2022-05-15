from sympy import symbols, tan, sqrt

X, Y = symbols('X Y')

# ((system), (initial approximation by chart)
TEST_SUITE_FOR_NEWTON_METHOD: list[tuple] = [
    ((tan(X * Y + 0.3) - X, 0.6 * (X ** 2) + 2 * (Y ** 2) - 1), (0.8, 0.5)),
    ((0.8 * X ** 2 + 2 * Y ** 2 - 1, tan(X * Y + 0.1) - X), (0.2, 0.5)),
    ((tan(X * Y + 0.22) - X, 0.5 * (X ** 2) + 2 * (Y ** 2) - 1), (0.6, 0.5))
]

# ((already transformed system: in view: x[i] = f[i](x)), (initial approximation by chart))
TEST_SUITE_FOR_ITERATIONS_METHOD: list[tuple] = [
    ((tan(X * Y + 0.3), sqrt(0.5 - 0.25 * (X ** 2))), (1.2, 0.5))
]

EPSILON: float = 0.001
