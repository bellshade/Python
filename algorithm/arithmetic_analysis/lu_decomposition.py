# informasi tentang lu decomposition bisa cek disini
# https://en.wikipedia.org/wiki/LU_decomposition

from typing import Tuple

import numpy as np


def lower_upper_decomposition(table: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    contoh:
    >>> matrix = np.array([[2, -2, 1], [0, 1, 2], [5, 3, 1]])
    >>> outcome = lower_upper_decomposition(matrix)
    >>> outcome[0]
    array([[1. , 0. , 0. ],
           [0. , 1. , 0. ],
           [2.5, 8. , 1. ]])
    >>> outcome[1]
    array([[  2. ,  -2. ,   1. ],
           [  0. ,   1. ,   2. ],
           [  0. ,   0. , -17.5]])
    >>> matrix = np.array([[2, -2, 1], [0, 1, 2]])
    >>> lower_upper_decomposition(matrix)
    Traceback (most recent call last):
    ...
    ValueError: 'table' harus dari array bentuk persegi tetapi mendapat 2x3 array :
    [[ 2 -2  1]
     [ 0  1  2]]
    """

    rows, columns = np.shape(table)
    if rows != columns:
        raise ValueError(
            f"'table' harus dari array bentuk persegi tetapi mendapat {rows}x{columns} "
            + f"array :\n{table}"
        )
    lower = np.zeros((rows, columns))
    upper = np.zeros((rows, columns))

    for i in range(columns):
        for j in range(i):
            total = 0
            for k in range(j):
                total += lower[i][k] * upper[k][j]
            lower[i][j] = (table[i][j] - total) / upper[j][j]
        lower[i][i] = 1
        for j in range(i, columns):
            total = 0
            for k in range(i):
                total += lower[i][k] * upper[k][j]
            upper[i][j] = table[i][j] - total
    return lower, upper


if __name__ == "__main__":
    import doctest

    doctest.testmod()
