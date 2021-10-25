# Diberikan array bilangan bulat yang diurutkan,
# kembalikan indeks dari dua angka seperti
# bahwa mereka menambahkan hingga target tertentu menggunakan teknik dua pointer.
# Anda dapat berasumsi bahwa setiap input
# akan memiliki tepat satu solusi, dan Anda
# tidak boleh menggunakan elemen yang sama dua kali.
# Ini adalah solusi alternatif dari
# masalah dua jumlah, yang menggunakan
# peta untuk memecahkan masalah.
# Oleh karena itu tidak dapat menyelesaikan masalah jika ada
# kendala tidak menggunakan indeks yang sama dua kali.
# contoh
# diberikan arr = [2, 7, 11, 15] target = 9
# jadi karena arr[0] + arr[1] = 2 + 7 = 9
# maka mengembalikan nilai [0, 1]


from __future__ import annotations


def two_pointer(nums: list[int], target: int) -> list[int]:
    """
    >>> two_pointer([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_pointer([2, 7, 11, 15], 18)
    [1, 2]
    >>> two_pointer([2, 7, 11, 15], 13)
    [0, 2]
    """
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] < target:
            i = i + 1
        else:
            j = j - 1

    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
