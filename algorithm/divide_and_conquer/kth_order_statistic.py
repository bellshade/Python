# Temukan elemen terkecil ke-k dalam waktu
# linier menggunakan metode divide and conquer.
# Ingat kita bisa melakukan ini dengan
# dalam waktu O(nlogn). Urutkan daftar dan
# mengakses elemen ke-k dalam waktu yang konstan.
# Ini adalah algoritma divide and conquer
# yang dapat menemukan solusi dalam waktu O(n).
# Untuk informasi lebih lanjut tentang algoritma ini:
# https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/08/Small08.pdf


from __future__ import annotations

from random import choice


def random_pivot(lst):
    """
    Pilih pivot acak untuk list.
    Kita dapat menggunakan algoritma
    yang lebih canggih di sini, seperti median-of-medians
    algoritma.
    """
    return choice(lst)


def kth_number(lst: list[int], k: int) -> int:
    """
    >>> kth_number([2, 1, 3, 4, 5], 3)
    3
    >>> kth_number([2, 1, 3, 4, 5], 1)
    1
    >>> kth_number([2, 1, 3, 4, 5], 5)
    5
    """
    pivot = random_pivot(lst)

    small = [e for e in lst if e < pivot]
    big = [e for e in lst if e > pivot]
    if len(small) == k - 1:
        return pivot

    elif len(small) < k - 1:
        return kth_number(big, k - len(small) - 1)
    else:
        return kth_number(small, k)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
