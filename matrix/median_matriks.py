def median(matriks: list[list[int]]) -> int:
    """
    menghitung nilai dari median dari sebuah matriks
    yang sudah diurutkan

    Parameter:
        matriks(list[list[int]]): matriks 2D yang berisi bilangan
                                  bulat

    Contoh:
    >>> matriks = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    >>> median(matriks)
    5
    >>> matriks = [[1, 2, 3], [4, 5, 6]]
    >>> median(matriks)
    3
    """
    # flatten matriks 2D jadi list 1D yang terurut
    linear = sorted(angka for baris in matriks for angka in baris)

    # hitung indeks tengah untuk menemukan median
    tengah = (len(linear) - 1) // 2

    # return hasil dari nilai median
    return linear[tengah]


if __name__ == "__main__":
    import doctest

    # jalankan doctesting
    doctest.testmod()
