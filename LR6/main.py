from data import get_y, OPTION, X
from lagrange_interpolating_polynom import get_lagrange_polynom


def main() -> None:
    y_array: list = get_y(OPTION)
    x_array: list = list(X)
    print(y_array)
    print(get_lagrange_polynom(x_array, y_array))


if __name__ == '__main__':
    main()
