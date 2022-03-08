from sturm import get_number_of_roots_by_sturm_theorem
import data


def main() -> None:
    equation: list = [1.00, data.A, data.B, data.C]

    get_number_of_roots_by_sturm_theorem(equation)


if __name__ == '__main__':
    main()
