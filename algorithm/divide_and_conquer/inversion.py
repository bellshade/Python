# Diberikan struktur data seperti array A[1..n],
# berapa banyak pasangan
# (i, j) untuk semua 1 <= i < j <= n sedemikian
# hingga A[i] > A[j]? Pasangan ini adalah
# disebut inversi. Menghitung jumlah inversi seperti itu
# dalam seperti array
# objek adalah yang terpenting. Antara lain,
# menghitung inversi dapat membantu
# menentukan seberapa dekat array yang diberikan untuk diurutkan
# Dalam implementasi ini, saya menyediakan dua algoritma,
# yaitu membagi-dan-menaklukkan
# algoritma yang berjalan di nlogn dan algoritma brute-force n^2.

from __future__ import annotations

from typing import Any


def count_inversion_bf(arr: list[int]) -> int:
    """
    Menghitung jumlah inversi menggunakan algoritma brute force
    >>> count_inversion_bf([1, 4, 2, 4, 1])
    4
    """
    num_inversion = 0
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                num_inversion += 1
    return num_inversion


def count_inversion_recursive(arr: list[int]) -> Any:
    """
    Menghitung jumlah inversi menggunakan
    divide and conquer
    >>> count_inversion_recursive([1, 4, 2, 4, 1])
    ([1, 1, 2, 4, 4], 4)
    """
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        P = arr[0:mid]
        Q = arr[mid:]

        A, inversion_p = count_inversion_recursive(P)
        B, inversions_q = count_inversion_recursive(Q)
        C, cross_inversions = _count_cross_inversions(A, B)

        num_inversions = inversion_p + inversions_q + cross_inversions
        return C, num_inversions


def _count_cross_inversions(P: list[int], Q: list[int]) -> Any:
    """
    Menghitung inversi di dua larik yang diurutkan.
    Dan gabungkan dua array menjadi satu array yang diurutkan
    >>> _count_cross_inversions([1, 2, 3], [0, 2, 5])
    ([0, 1, 2, 2, 3, 5], 4)
    """
    R = []
    i = j = num_inversion = 0
    while i < len(P) and j < len(Q):
        if P[i] > Q[j]:
            num_inversion += len(P) - i
            R.append(Q[j])
            j += 1
        else:
            R.append(P[i])
            i += 1

    if i < len(P):
        R.extend(P[i:])
    else:
        R.extend(Q[j:])

    return R, num_inversion


if __name__ == "__main__":
    import doctest

    doctest.testmod()
