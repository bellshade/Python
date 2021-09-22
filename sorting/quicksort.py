"""
Quicksort merupakan Algoritme Pembagi. Pertama quicksort membagi list
yang besar menjadi dua buah sub list yang lebih kecil: element kecil
dan element besar. Quicksort kemudian dapat menyortir sub list itu
secara rekursif. https://id.wikipedia.org/wiki/Quicksort
"""
from __future__ import annotations


def quickSort(numbers: list) -> list:
    """
    >>> quickSort([5, 3, 8, 4, 6])
    [3, 4, 5, 6, 8]
    """
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[round(len(numbers) / 2)]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    return quickSort(left) + middle + quickSort(right)


def testing():
    """
    >>> numbers = [5, 3, 8, 4, 6]
    >>> expectedResult = [3, 4, 5, 6, 8]
    >>> quickSort(numbers) == expectedResult
    True
    """
    numbers = [5, 3, 8, 4, 6]
    resultSort = quickSort(numbers)
    print(f"\nSebelum Sort: {resultSort} Seteleh sort: {resultSort}\n")


if __name__ == "__main__":
    import doctest
    # testing()
    doctest.testmod()
