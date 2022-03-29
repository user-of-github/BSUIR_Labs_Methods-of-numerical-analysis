from sympy import symbols, tan, sqrt

X, Y = symbols('X Y')

# ((system), (transformed system (x = Ф(x))), (initial approximation (by chart))
TEST_SUITE_EQUATIONS_SYSTEM: list[tuple] = [
    ((tan(X * Y + 0.3) - X, 0.5 * (X ** 2) + 2 * (Y ** 2) - 1), (1.3, 0.4))
]
# (0.8 * X ** 2 + 2 * Y ** 2 - 1, tan(X * Y + 0.1) - X)
EPSILON: float = 0.00000001
