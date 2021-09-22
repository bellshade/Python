"""
Bubble Sort adalah Sorting algorithm yang cara kerjanya adalah dengan
membandingkan 2 elemen array lalu menggeser kedua elemen tersebut
sesuai dengan urutan terus-menerus sampai akhir array
"""


def bubble_sort(numbers: list) -> list:
    """
    >>> bubble_sort([5, 2, 1, 3, 2, 5, 7, 3, 4])
    [1, 2, 2, 3, 3, 4, 5, 5, 7]
    """
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1] :
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def testing() -> None:
    """
    >>> numbers = [5, 3, 8, 4, 6]
    >>> expected_result = [3, 4, 5, 6, 8]
    >>> bubble_sort(numbers) == expected_result
    True
    """
    numbers = [5, 2, 1, 3, 2, 5, 7, 3, 4]
    print(f"\nSebelum Sort: {numbers}\n")
    resultSort = bubble_sort(numbers)
    print(f"Seteleh sort: {resultSort}\n")


if __name__ == "__main__":
    import doctest
    # testing()
    doctest.testmod()
