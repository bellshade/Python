# Diberikan array bilangan bulat dan target bilangan bulat lainnya,
# kita diminta untuk menemukan triplet dari array
# sedemikian rupa sehingga jumlahnya sama dengan
# target.

from __future__ import annotations

from itertools import permutations
from random import randint
from timeit import repeat


def make_dataset() -> tuple[list[int], int]:
    arr = [randint(-1000, 1000) for _ in range(10)]
    r = randint(-5000, 5000)

    return (arr, r)


dataset = make_dataset()


def triplet_sum1(arr: list[int], target: int) -> tuple[int, ...]:
    """
    Mengembalikan triplet dalam array dengan jumlah sama dengan target,
    lain (0, 0, 0).

    >>> triplet_sum1([13, 29, 7, 23, 5], 35)
    (5, 7, 23)

    >>> arr = [6, 47, 27, 1, 15]
    >>> target = 11
    >>> triplet_sum1(arr, target)
    (0, 0, 0)
    """
    for triplet in permutations(arr, 3):
        if sum(triplet) == target:
            return tuple(sorted(triplet))

    return (0, 0, 0)


def triplet_sum2(arr: list[int], target: int) -> tuple[int, int, int]:
    """
    Mengembalikan triplet dalam array dengan jumlah sama dengan target,
    lain (0, 0, 0).

    >>> triplet_sum2([13, 29, 7, 23, 5], 35)
    (5, 7, 23)

    >>> arr = [6, 47, 27, 1, 15]
    >>> target = 11
    >>> triplet_sum2(arr, target)
    (0, 0, 0)
    """
    arr.sort()
    n = len(arr)

    for i in range(n - 1):
        kiri, kanan = i + 1, n - 1
        while kiri < kanan:
            if arr[i] + arr[kiri] + arr[kanan] == target:
                return (arr[i], arr[kiri], arr[kanan])
            elif arr[i] + arr[kiri] + arr[kanan] < target:
                kiri += 1
            elif arr[i] + arr[kiri] + arr[kanan] > target:
                kanan -= 1

    return (0, 0, 0)


def sol_waktu() -> tuple[float, float, float]:
    setup_kode = """
from __main__ import dataset, triplet_sum1, triplet_sum2
    """
    test_kode1 = """
triplet_sum1(*dataset)
    """
    test_kode2 = """
triplet_sum2(*dataset)
    """

    waktu1 = repeat(setup=setup_kode, stmt=test_kode1, repeat=5, number=10000)
    waktu2 = repeat(setup=setup_kode, stmt=test_kode2, repeat=5, number=10000)

    return (min(waktu1), min(waktu2))


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    waktu = sol_waktu()

    print(f"solusi pertama memakan waktu : {waktu[0]}")
    print(f"sousi kedua memakan waktu : {waktu[1]}")
