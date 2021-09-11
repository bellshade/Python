from typing import Any

import numpy as np


def is_hermitian(matrix: np.ndarray) -> bool:
    """
    Memeriksa apakah suatu matriks adalah Hermitian.
    >>> import numpy as np
    >>> A = np.array([
    ... [2,    2+1j, 4],
    ... [2-1j,  3,  1j],
    ... [4,    -1j,  1]])
    >>> is_hermitian(A)
    True
    """
    return np.array_equal(matrix, matrix.conjugate().T)


def rayleigh_quotient(A: np.ndarray, v: np.ndarray) -> Any:
    """
    Mengembalikan hasil bagi Rayleigh dari matriks Hermitian A dan
    vektor v
    >>> import numpy as np
    >>> A = np.array([
    ... [1,  2, 4],
    ... [2,  3,  -1],
    ... [4, -1,  1]
    ... ])
    >>> v = np.array([
    ... [1],
    ... [2],
    ... [3]
    ... ])
    >>> rayleigh_quotient(A, v)
    array([[3.]])
    """
    v_star = v.conjugate().T
    v_star_dot = v_star.dot(A)
    assert isinstance(v_star_dot, np.ndarray)
    return (v_star_dot.dot(v)) / (v_star.dot(v))


def testing() -> None:
    A = np.array([[2, 2 + 1j, 4], [2 - 1j, 3, 1j], [4, -1j, 1]])
    v = np.array([[1], [2], [3]])
    assert is_hermitian(A), f"{A} tidak hermitian."
    print(rayleigh_quotient(A, v))

    A = np.array([[1, 2, 4], [2, 3, -1], [4, -1, 1]])
    assert is_hermitian(A), f"{A} tidak hermitian"
    assert rayleigh_quotient(A, v) == float(3)


if __name__ == "__main__":
    import doctest

    # testing()
    doctest.testmod()
