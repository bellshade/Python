def pencarian_biner(array: list, batas_bawah: int, batas_atas: int, nilai: int) -> int:
    """
    fungsi ini menjalankan pencarian biner pada array 1D dan
    mengembalikan -1 jika nilai tidak ditemukan

    Parameter:
        array(list): array 1D yang sudah diurutkan
        nilai(int): nilai yang dicari dalam array

    Contoh:
    >>> matriks = [1, 4,7, 11, 15]
    >>> pencarian_biner(matriks, 0, len(matriks) - 1, 1)
    0
    >>> pencarian_biner(matriks, 0, len(matriks) - 1, 23)
    -1
    """
    # hitung indeks tengah dari array
    tengah = int((batas_bawah + batas_atas) // 2)

    # jika nilai di indeks sama dengan nilai yang dicari
    # return indeks
    if array[tengah] == nilai:
        return tengah

    # jika batas bawah sudah sama atau lebih dari batas atas
    # kembalikan -1 (nilai tidak ada)
    if batas_bawah >= batas_atas:
        return -1

    # jikai nilai di indeks tengah lebih kecil dari nilai yang
    # dicari, lakukan pencarian biner pada separuh kanan
    if array[tengah] < nilai:
        return pencarian_biner(array, tengah + 1, batas_atas, nilai)

    # jika nilai di indeks tengah lebih besar lakukan pencarian biner
    # pada separuh kiri
    else:
        return pencarian_biner(array, batas_bawah, tengah - 1, nilai)


def pencarian_matriks_biner(nilai: int, matriks: list) -> list:
    """
    fungsi ini akan menjalankan iterasi pada matriks 2D dan memanggil
    pencarian_biner pada setiap baris matriks, return [-1, -1] jika
    nilai tidak ditemukan

    Parameter:
        nilai(int): nilai yang dicari dalam matriks
        matriks(list): matriks 2D yang sudah diurutkan

    Contoh:
    >>> matriks = [[1, 4, 5, 11, 15],
    ...            [2, 5, 8, 12, 19],
    ...            [3, 6, 9, 16, 22],
    ...            [10, 13, 14, 17, 24],
    ...            [18, 21, 23, 26, 30]]
    >>> target = 1
    >>> pencarian_matriks_biner(target, matriks)
    [0, 0]
    >>> target = 34
    >>> pencarian_matriks_biner(target, matriks)
    [-1, -1]
    """

    # inisialisasi indeks baris
    indeks = 0

    # jika nilai pertama di baris pertama sama dengan nilai yang dicari
    # return indeks [0, 0]
    if matriks[indeks][0] == nilai:
        return [indeks, 0]

    # lakukan iterasi pada matriks selama indeks valid dan nilai di kolom pertama
    # lebih kecli dari nilai yang dicari
    while indeks < len(matriks) and matriks[indeks][0] < nilai:
        # cari biner pada baris saat ini
        hasil_pencarian = pencarian_biner(
            matriks[indeks], 0, len(matriks[indeks]) - 1, nilai
        )

        # jika nilai ditemukan, retunr indeks baris dan kolom
        if hasil_pencarian != -1:
            return [indeks, hasil_pencarian]

        # pindah ke baris berikutnya
        indeks += 1

    # jika tidak ditemukan maka return [-1, -1]
    return [-1, -1]


if __name__ == "__main__":
    import doctest

    # jalankan doctesting
    doctest.testmod()
