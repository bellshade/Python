from __future__ import annotations


def merge_sort(data: list) -> list:
    """
    merge sort adalah algoritma sorting data yang yang bekerja
    dengan bekerja dengan membagi data menjadi dua bagian secara
    rekursif, megnrutukan kedua bagian secara terpisah, lalu
    menggabungkan kembali dua bagian tersebut dengan urutan
    yang benar

    referensi:
    https://en.wikipedia.org/wiki/Merge_sort

    Args:
        data (list): beberapa data yang bisa berubah sebanding dengan
                     item yang sebanding di dalamnya

    Return:
        (list): data hasil yang berupa ascending

    Contoh:
    >>> merge_sort([0, 6, 3, 2, 1])
    [0, 1, 2, 3, 6]
    """

    def merge(kiri: list, kanan: list) -> list:
        """
        gabungkan data kiri dan kanan

        Args:
            kiri (list): data list kiri
            kanan (kanan): data list kanan

        Return:
            (list): data gabungan dari kiri dan kanan
        """

        def _gabung():
            while kiri and kanan:
                yield (kiri if kiri[0] <= kanan[0] else kanan).pop(0)
            yield from kiri
            yield from kanan

        return list(_gabung())

    if len(data) <= 1:
        return data
    mid = len(data) // 2
    return merge(merge_sort(data[:mid]), merge_sort(data[mid:]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
