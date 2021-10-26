# Diberikan array bilangan bulat, kembalikan indeks dari
# dua angka sedemikian rupa sehingga jumlahnya menjadi
# target tertentu.
# Anda mungkin berasumsi bahwa setiap input
# akan memiliki tepat satu solusi,
# dan Anda tidak boleh menggunakan
# elemen yang sama dua kali. informasi tentang two sum
# https://leetcode.com/problems/two-sum/

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([15, 2, 11, 7], 13)
    [1, 2]
    """
    chk_map: dict[int, int] = {}
    for index, val in enumerate(nums):
        compl = target - val
        if compl in chk_map:
            return [chk_map[compl], index]
        chk_map[val] = index

    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{two_sum([2, 7, 11, 15], 9) = }")
