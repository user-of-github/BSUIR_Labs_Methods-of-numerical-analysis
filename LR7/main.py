import data
from get_splines import get_cubic_splines_coefficients


def main() -> None:
    response: list[list] = get_cubic_splines_coefficients(data.FUNCTIONS[1], data.NODES_COUNT[1], data.INTERVAL[1])


if __name__ == '__main__':
    main()
