import numpy as np
from data import C, D


def get_matrix_according_to_my_variant(variant: int) -> np.matrix:
    return np.matrix(C) * variant + np.matrix(D)
