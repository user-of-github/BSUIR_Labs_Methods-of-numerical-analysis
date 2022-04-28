from data import get_points, OPTION


def main() -> None:
    points: list[tuple] = get_points(OPTION)
    print(points)


if __name__ == '__main__':
    main()
