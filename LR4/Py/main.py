import data
from demo import demonstrate


def main() -> None:
    demonstrate(data.TEST_SUITE_EQUATIONS_SYSTEM[0], [data.X, data.Y], data.EPSILON)


if __name__ == '__main__':
    main()
