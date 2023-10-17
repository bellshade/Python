import numpy as np


def simple_convolution(arr1: np.array, arr2: np.array):
    """
    fungsi merupakan calculasi dari rumus sederhana
    dari convolution
    Args:
        arr1 (np.array): Inputan berupa array 1 dimensi
        arr2 (np.array): Inputan berupa array 1 dimensi
    """
    m, n = arr1.shape[0], arr2.shape[0]

    # indenfikasi kalau ukuran array input harus sama
    if m != n:
        raise ValueError("Dimensi array harus sama")

    # kalkulasi tersebut
    result = np.zeros(m + n - 1)
    for i in range(m):
        for j in range(n):
            result[i + j] += arr1[i] * arr2[j]
    return result
