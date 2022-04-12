from utils import get_matrix_according_to_my_variant
import data
from eigenvalues_by_jacobi import get_eigen_values_and_vectors_by_jacobi_method


def main() -> None:
    matrix = get_matrix_according_to_my_variant(8)
    values, vectors = get_eigen_values_and_vectors_by_jacobi_method(matrix, data.ERROR)
    print(values)


if __name__ == '__main__':
    main()
