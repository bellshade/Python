# macam - macam operasi matriks
from typing import Union


def penjumlahan(
    matriks_1: list[list[Union[int, float]]], matriks_2: list[list[Union[int, float]]]
) -> list[list[Union[int, float]]]:
    """
    Fungsi untuk melakukan penjumlahan 2 matrriks

    >>> penjumlahan([[2, 3], [3, 4]], [[3, 2], [2, 1]])
    [[5, 5], [5, 5]]
    """
    if len(matriks_1) != len(matriks_2):
        return ValueError("Ukuran Matriks Harus Sama")
    else:
        result = []
        n = len(matriks_1)
        for i in range(n):
            row = []
            for j in range(n):
                operation = matriks_1[i][j] + matriks_2[i][j]
                row.append(operation)
            result.append(row)
        return result


def pengurangan(
    matriks_1: list[list[Union[int, float]]], matriks_2: list[list[Union[int, float]]]
) -> list[list[Union[int, float]]]:
    """
    Fungsi untuk melakukan kalkulasi pengurangan matriks

    >>> pengurangan([[3, 3], [3, 3]], [[2, 1], [2, 1]])
    [[1, 2], [1, 2]]
    """
    if len(matriks_1) != len(matriks_2):
        return ValueError("Ukuran Matriks Sama")
    else:
        result = []
        n = len(matriks_1)
        for i in range(n):
            row = []
            for j in range(n):
                operation = matriks_1[i][j] - matriks_2[i][j]
                row.append(operation)
            result.append(row)
        return result


def perkalian(
    matriks_1: list[list[Union[int, float]]], matriks_2: list[list[Union[int, float]]]
) -> list[list[Union[int, float]]]:
    """
    Fungsi untuk melakukan kalkulasi perkalian matriks

    >>> perkalian([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    """
    baris1 = len(matriks_1)
    kolom1 = len(matriks_1[0])
    baris2 = len(matriks_2)
    kolom2 = len(matriks_2[0])
    if kolom1 != baris2:
        return ValueError("Ukuran baris dan kolom mesti sama")

    result = [[0 for _ in range(kolom2)] for _ in range(baris1)]
    for i in range(baris1):
        for j in range(kolom2):
            for k in range(kolom1):
                result[i][j] += matriks_1[i][k] * matriks_2[k][j]
    return result


def perkalian_skalar_matriks(
    matriks: list[list[Union[int, float]]], x: int
) -> list[list[Union[int, float]]]:
    """
    Fungsi untuk kalkulasi skalar dan matriks

    >>> perkalian_skalar_matriks([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)
    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    """
    result = []
    n = len(matriks)
    for i in range(n):
        row = []
        for j in range(n):
            multi = x * matriks[i][j]
            row.append(multi)
        result.append(row)
    return result


def matriks_identitas(n: int) -> list[list[int]]:
    """
    Funsi untuk menghasilkan matriks identitas

    >>> matriks_identitas(2)
    [[1, 0], [0, 1]]
    >>> matriks_identitas(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    if n < 0:
        return ValueError("ukuran harus positif")
    else:
        return [[1 if j == i else 0 for j in range(int(n))] for i in range(int(n))]


def main(args=None):
    import doctest

    print(penjumlahan([[2, 3], [3, 4]], [[3, 2], [2, 1]]))
    print(pengurangan([[3, 3], [3, 3]], [[2, 1], [2, 1]]))
    print(perkalian([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(perkalian_skalar_matriks([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))
    print(matriks_identitas(3))

    doctest.testmod()


if __name__ == "__main__":
    main()
