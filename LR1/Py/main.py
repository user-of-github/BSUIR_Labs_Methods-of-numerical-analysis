import data
from utils import sum_two_matrices, multiply_matrix_by_ratio, get_copy
from gauss import gauss


def main() -> None:
    main_coefficients = sum_two_matrices(
        multiply_matrix_by_ratio(data.MATRIX_C, data.OPTION),
        data.MATRIX_D
    )

    free_coefficients = get_copy(data.VECTOR_B)

    solution = gauss(main_coefficients, free_coefficients)
    print(solution)


if __name__ == '__main__':
    main()
