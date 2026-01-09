# https://en.wikipedia.org/wiki/LU_decomposition#Algorithms
from typing import Union


def LU(A: list[list[Union[int, float]]]) -> list[list[Union[int, float]]]:
    """
    >>> A = [[2, 3, 1], [4, 7, 7], [-2, 4, 5]]
    >>> L, U = LU(A)
    >>> L
    [[1, 0, 0], [2.0, 1, 0], [-1.0, 7.0, 1]]
    >>> U
    [[2, 3, 1], [0.0, 1.0, 5.0], [0.0, 0.0, -29.0]]
    """
    n = len(A)
    L = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    U = [[A[i][j] for j in range(n)] for i in range(n)]

    for k in range(n - 1):
        if U[k][k] == 0:
            raise ValueError("Faktorisasi LU tidak ada")
        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]
            for j in range(k, n):
                U[i][j] -= L[i][k] * U[k][j]
    return L, U


def main(args=None):
    import doctest

    doctest.testmod()
    A = [[2, 3, 1], [4, 7, 7], [-2, 4, 5]]
    L, U = LU(A)
    for row in L:
        print(row)
    print("\n")
    for row in U:
        print(row)


if __name__ == "__main__":
    main()
