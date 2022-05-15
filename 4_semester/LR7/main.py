import data
from get_splines import get_cubic_splines_coefficients, count_value_of_spline_in_point


def main() -> None:

    for counter in range(2):
        response, x_array = get_cubic_splines_coefficients(data.FUNCTIONS[counter], data.NODES_COUNT[counter], data.INTERVAL[counter])
        value_in_point: float = count_value_of_spline_in_point(response, data.get_x_to_count_value(counter), x_array)

        print(value_in_point - data.FUNCTIONS[counter](data.get_x_to_count_value(counter)))


if __name__ == '__main__':
    main()
