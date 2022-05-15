from test_run import test_run
import data


def main() -> None:
    test_run(data.TEST_EQUATION[2], -1, 1, data.ERROR)


if __name__ == '__main__':
    main()
