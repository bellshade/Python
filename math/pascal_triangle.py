def PascalTriangle(n: int) -> list[list[int]]:
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


def pascal_matriks(n: int) -> list[list[int]]:
    """
    Fungsi untuk membuata matriks segitiga pascal

    >>> print(pascal_matriks(3))
    [[1, 0, 0], [1, 1, 0], [1, 2, 1]]
    >>> print(pascal_matriks(4))
    [[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]]
    """
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                result[i][j] = 1
            else:
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
