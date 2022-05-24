from data import ACCURACY_DERIVATIVE, ACCURACY_INTEGRALS, FUNCTIONS, INTERVALS, OPTIONS_COUNT
from count_derivative import get_first_derivative, get_second_derivative
from count_integral import count_integral_by_trapezoid_formula, count_integral_by_simpson_formula, count_integral_by_middle_reactangles


def main() -> None:
    for counter in range(OPTIONS_COUNT):
        function = FUNCTIONS[counter]
        interval: tuple[float, float] = INTERVALS[counter]
        accuracy_integral: float = ACCURACY_INTEGRALS[counter]

        diff1: float = get_first_derivative(function, (interval[1] + interval[0]) / 2, ACCURACY_DERIVATIVE)
        diff2: float = get_second_derivative(function, (interval[1] + interval[0]) / 2, ACCURACY_DERIVATIVE)

        integral_by_trapezoid, trapezoid_time = count_integral_by_trapezoid_formula(function, interval, accuracy_integral)
        integral_by_simpson, simpson_time = count_integral_by_simpson_formula(function, interval, accuracy_integral)
        integral_by_rectangles, rectangles_time = count_integral_by_middle_reactangles(function, interval, accuracy_integral)

        print(f'Function № {counter + 1}: ')
        print(f'\t1st derivative: {round(diff1, 3)}')
        print(f'\t2nd derivative: {round(diff2, 3)}')
        print(f'\tintegral by trapezoid: {round(integral_by_trapezoid, 6)} | with time {round(trapezoid_time, 5)} sec')
        print(f'\tintegral by simpson: {round(integral_by_simpson, 6)} | with time {round(simpson_time, 5)} sec')
        print(f'\tintegral by rectangles: {round(integral_by_rectangles, 6)} | with time {round(rectangles_time, 5)} sec')


if __name__ == '__main__':
    main()