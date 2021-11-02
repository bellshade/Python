# inverse matrix
# https://www.mathsisfun.com/algebra/matrix-inverse.html

from __future__ import annotations

from decimal import Decimal


def inverse_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """
    Suatu matriks dikalikan dengan inversnya menghasilkan matriks identitas.
    Fungsi ini mencari invers dari matriks 2x2.
    Jika determinan suatu matriks adalah 0, inversnya tidak ada.
    >>> inverse_matrix([[2, 5], [2, 0]])
    [[0.0, 0.5], [0.2, -0.2]]
    """
    D = Decimal
    determinan = D(matrix[0][0]) * D(matrix[1][1]) - D(matrix[1][0]) * D(matrix[0][1])
    if determinan == 0:
        raise ValueError("matrix ini no inverse")

    swapped_matrix = [[0.0, 0.0], [0.0, 0.0]]
    swapped_matrix[0][0], swapped_matrix[1][1] = matrix[1][1], matrix[0][0]
    swapped_matrix[1][0], swapped_matrix[0][1] = -matrix[1][0], -matrix[0][1]

    return [[float(D(n) / determinan) or 0.0 for n in row] for row in swapped_matrix]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
