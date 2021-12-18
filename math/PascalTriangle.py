from __future__ import annotation
from typing import List



def PascalTriangle(n: int) -> List[List[int]]:
    """Fungsi untuk mendapatkan segitiga pascal sebanyak n-baris

    Args:
        n (int): n baris bilangan yang diinginkan

    Returns:
        List[List[int]]: Kumpulan bilangan pascal

    >>> print(PascalTriangle(1))
    [[1]]

    >>> print(PascalTriangle(3))
    [[1], [1, 1], [1, 2, 1]]

    >>> print(PascalTriangle(5))
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    result = [[1] * (row + 1) for row in range(n)]

    for list_num in range(n):
        for position in range(1, list_num):
            result[list_num][position] = (
                result[list_num - 1][position - 1] + result[list_num - 1][position]
            )
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
