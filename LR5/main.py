from utils import get_matrix_according_to_my_variant
import data
from eigenvalues_by_jacobi import get_eigen_values_and_vectors_by_jacobi_method


def main() -> None:
    for variant in data.VARIANT:
        matrix = get_matrix_according_to_my_variant(variant)
        values, vectors, iterations = get_eigen_values_and_vectors_by_jacobi_method(matrix, data.ERROR)
        
        print(f'Variant {variant}')
        print('Values:\n', values)
        print('Vectors:')
        for vector in vectors:
            print(vector)
        print(f'Number of iterations: {iterations}\n')


if __name__ == '__main__':
    main()
