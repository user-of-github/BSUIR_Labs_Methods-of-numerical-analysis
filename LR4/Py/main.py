import data
from demo import demonstrate_newton, demonstrate_simple_iterations


def main() -> None:
    print('Solutions by Newton method')
    for test_case in data.TEST_SUITE_FOR_NEWTON_METHOD:
        demonstrate_newton(test_case, [data.X, data.Y], data.EPSILON)

    print('Solutions by simple iterations method')
    for test_case in data.TEST_SUITE_FOR_ITERATIONS_METHOD:
        demonstrate_simple_iterations(test_case, [data.X, data.Y], data.EPSILON)


if __name__ == '__main__':
    main()
