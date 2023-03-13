# diberikan m x n grid matriks yang berisi kata
# dan diberikan input kata yang diinginkan
# maka akan huruf tersebut dicari, jika huruf dalam inputan
# memenuhi maka ouput bernilai true
# contoh problem
# https://leetcode.com/problems/word-search/


def dapatkan_kata_kunci(
    panjang_papan: int, panjang_kolom_papan: int, baris: int, kolom: int
) -> int:
    """
    >>> dapatkan_kata_kunci(10, 20, 1, 0)
    200
    """
    return panjang_papan * panjang_kolom_papan * baris + kolom


def cari_kata(
    papan: list[list[str]],
    kata: str,
    baris: int,
    kolom: int,
    indeks_kata: int,
    set_poin: set[int],
) -> bool:
    """
    >>> cari_kata([["A"]], "B", 0, 0, 0, set())
    False
    """
    if papan[baris][kolom] != kata[indeks_kata]:
        return False
    if indeks_kata == len(kata) - 1:
        return True

    traverts_diversion = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    panjang_papan = len(papan)
    panjang_kolom_papan = len(papan[0])
    for direction in traverts_diversion:
        next_i = baris + direction[0]
        next_j = kolom + direction[1]
        if not (0 <= next_i < panjang_papan and 0 <= next_j < panjang_kolom_papan):
            continue

        kunci = dapatkan_kata_kunci(panjang_papan, panjang_kolom_papan, next_i, next_j)
        if kunci in set_poin:
            continue

        set_poin.add(kunci)
        if cari_kata(papan, kata, next_i, next_j, indeks_kata + 1, set_poin):
            return True

        set_poin.remove(kunci)

    return False


def cek_kata(papan: list[list[str]], kata: str) -> bool:
    """
    >>> cek_kata([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    True
    """
    pesan_error = "papan tidak boleh kosong,"
    panjang_papan = len(papan)
    if not isinstance(papan, list) or len(papan) == 0:
        raise ValueError(pesan_error)

    for baris in papan:
        if not isinstance(baris, list) or len(baris) == 0:
            raise ValueError(pesan_error)

        for item in baris:
            if not isinstance(item, str) or len(item) != 1:
                raise ValueError(pesan_error)

    if not isinstance(kata, str) or len(kata) == 0:
        raise ValueError("parameter kata tidak boleh kosong")

    panjang_kolom_papan = len(papan[0])
    for i in range(panjang_papan):
        for j in range(panjang_kolom_papan):
            if cari_kata(
                papan,
                kata,
                i,
                j,
                0,
                {dapatkan_kata_kunci(panjang_papan, panjang_kolom_papan, i, j)},
            ):
                return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.tesmod()
