# https://en.wikipedia.org/wiki/Hankel_matrix
# https://en.wikipedia.org/wiki/Toeplitz_matrix
# https://en.wikipedia.org/wiki/Pascal_matrix
# https://id.wikipedia.org/wiki/Matriks_identitas
from typing import Union


def faktorial(n) -> int:
    """
    >>> faktorial(5)
    120
    """
    if n < 0:
        raise ValueError('nilai harus positif')
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f


def kombinasi(n : int, r : int) -> int:
    """
    >>> kombinasi(5, 2)
    10.0
    """
    if n < 0 or r < 0:
        raise ValueError("Nilai Harus Positif")
    if r > n:
        return 0
    else:
        penyebut = faktorial(n)
        pembilang = faktorial(r) * faktorial(n - r)
        C = penyebut / pembilang
        return C


def identity(n : int = 2) -> list[list[Union[int]]]:
    """
    Membuat matriks identitas

    >>> identity(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            if (j == i):
                row.append(1)
            else:
                row.append(0)
        A.append(row)
    return A


def hankel(A, b=1) -> list[list[Union[int, float]]]:
    """
    Membuat matriks hankel

    >>> hankel(3)
    [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    """
    res = []
    for i in range(b, A + 1):
        row = []
        for j in range(b, A + 1):
            row.append(i + j - 1)
        res.append(row)
    return res


def toeplite(A, b=1) -> list[list[Union[int, float]]]:
    """
    Membuat matriks hankel

    >>> toeplite(3)
    [[0, -1, -2], [1, 0, -1], [2, 1, 0]]
    """
    res = []
    for i in range(b, A + 1):
        row = []
        for j in range(b, A + 1):
            row.append(i - j)
        res.append(row)
    return res


def hilbert(A, b=1) -> list[list[Union[int, float]]]:
    """
    Membuat matriks hilbert

    >>> hilbert(2)
    [[1.0, 0.5], [0.5, 0.3333333333333333]]
    """
    res = []
    for i in range(b, A + 1):
        row = []
        for j in range(b, A + 1):
            row.append(1 / (i + j - 1))
        res.append(row)
    return res


def pascal(n, kind='simetri') -> list[list[Union[int, float]]]:
    """
    Membuat matriks pascal dengan beberapa tipe

    >>> pascal(3)
    [[1.0, 1.0, 1.0], [1.0, 2.0, 3.0], [1.0, 3.0, 6.0]]
    >>> pascal(3, kind = 'lower')
    [[1.0, 0, 0], [1.0, 1.0, 0], [1.0, 2.0, 1.0]]
    """
    L_n = []
    for i in range(n):
        colum = []
        for j in range(n):
            x = kombinasi(i, j)
            colum.append(x)
        L_n.append(colum)

    r, c = len(L_n), len(L_n[0])
    t = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            t[j][i] = L_n[i][j]

    res = [[0 for _ in range(len(L_n))] for _ in range(len(L_n))]
    for i in range(len(L_n)):
        for j in range(len(t[0])):
            for k in range(len(t)):
                res[i][j] += L_n[i][k] * t[k][j]

    if kind.lower() == 'lower':
        return L_n
    elif kind.lower() == 'upper':
        return t
    else:
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
