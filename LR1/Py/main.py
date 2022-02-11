import data
from utils import sum_two_matrices, multiply_matrix_by_ratio, get_copy
from gauss import gauss, SolutionType


def main() -> None:
    main_coefficients = sum_two_matrices(
        multiply_matrix_by_ratio(data.MATRIX_C,data.OPTION),
        data.MATRIX_D
    )

    free_coefficients = get_copy(data.VECTOR_B)

    solution = gauss(main_coefficients, free_coefficients, SolutionType.SCHEME_OF_FULL_SELECTION)

    print('Solution: ', end='')
    for root in solution:
        print(round(root, data.SIGNS_AFTER_DOT), end=' ')


if __name__ == '__main__':
    main()
