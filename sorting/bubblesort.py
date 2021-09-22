"""
Bubble Sort adalah Sorting algorithm yang cara kerjanya adalah dengan
membandingkan 2 elemen array lalu menggeser kedua elemen tersebut
sesuai dengan urutan terus-menerus sampai akhir array
"""

from __future__ import annotations
def bubbleSort(numbers: list) -> list:
    """
    >>> bubbleSort([5, 3, 8, 4, 6])
    [3, 4, 5, 6, 8]
    """
    for i in range(len(numbers)):
        for j in range(i):
            numbers[j], numbers[j + 1] = numbers[j + 1] , numbers[j]
    return numbers


def testing() -> None:
    """
    >>> numbers = [5, 3, 8, 4, 6]
    >>> expectedResult = [3, 4, 5, 6, 8]
    >>> bubbleSort(numbers) == expectedResult
    True
    """
    numbers = [5, 3, 8, 4, 6]
    resultSort = bubbleSort(numbers)
    print(f"\nSebelum Sort: {resultSort} Seteleh sort: {resultSort}\n")


if __name__ == "__main__":
    import doctest
    # testing()
    doctest.testmod()
