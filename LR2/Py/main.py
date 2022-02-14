from utils import sum_two_matrices, multiply_matrix_by_ratio, get_copy
import data
from simple_iterations import solve_by_simple_iterations, SimpleIterationsSolvingType


def main():
    main_coefficients = sum_two_matrices(multiply_matrix_by_ratio(data.MATRIX_C, data.OPTION), data.MATRIX_D)
    free_coefficients = get_copy(data.VECTOR_B)

    roots, iterations_count = solve_by_simple_iterations(
        main_coefficients,
        free_coefficients,
        data.ACCURACY,
        SimpleIterationsSolvingType.DEFAULT
    )

    print('Solution: ', roots)
    print('Iterations count: ', iterations_count)


if __name__ == '__main__':
    main()
