# rotasi matrix
# https://mathworld.wolfram.com/RotationMatrix.html

from __future__ import annotations


def make_matrix(row_size: int = 4) -> list[list]:
    """
    >>> make_matrix()
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    """
    row_size = abs(row_size) or 4
    return [[1 + x + y * row_size for x in range(row_size)] for y in range(row_size)]


def rotate_90(matrix: list[list]) -> list[list]:
    """
    >>> rotate_90(make_matrix())
    [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
    """
    return reverse_row(transpose(matrix))


def rotate_180(matrix: list[list]) -> list[list]:
    """
    >>> rotate_180(make_matrix())
    [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
    >>> rotate_180(make_matrix()) == reverse_column(reverse_row(make_matrix()))
    True
    """
    return reverse_row(reverse_column(matrix))


def rotate_270(matrix: list[list]) -> list[list]:
    """
    >>> rotate_270(make_matrix())
    [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    >>> rotate_270(make_matrix()) == transpose(reverse_row(make_matrix()))
    True
    """
    return reverse_column(transpose(matrix))


def transpose(matrix: list[list]) -> list[list]:
    matrix[:] = [list(x) for x in zip(*matrix)]
    return matrix


def reverse_row(matrix: list[list]) -> list[list]:
    matrix[:] = matrix[::-1]
    return matrix


def reverse_column(matrix: list[list]) -> list[list]:
    matrix[:] = [x[::-1] for x in matrix]
    return matrix


def print_matrix(matrix: list[list]) -> None:
    for i in matrix:
        print(*i)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
