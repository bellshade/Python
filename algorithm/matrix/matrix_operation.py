# mencari hasil dari 2dimensional matriks

from __future__ import annotations


def tambah(*matrix_s: list[list]) -> list[list]:
    """
    >>> tambah([[1,2], [3,4]], [[2,3], [4,5]])
    [[3, 5], [7, 9]]
    """
    if all(_check_not_integer(m) for m in matrix_s):
        for i in matrix_s[1:]:
            _verify_matrix_size(matrix_s[0], i)
        return [[sum(t) for t in zip(*m)] for m in zip(*matrix_s)]

    raise TypeError("masukkan tipe berupa list tidak integer")


def kurang(matrix_a: list[list], matrix_b: list[list]) -> list[list]:
    """
    >>> kurang([[1,2],[3,4]],[[2,3],[4,5]])
    [[-1, -1], [-1, -1]]
    """
    if (
        _check_not_integer(matrix_a)
        and _check_not_integer(matrix_b)
        and _verify_matrix_size(matrix_a, matrix_b)
    ):
        return [[i - j for i, j in zip(*m)] for m in zip(matrix_a, matrix_b)]

    raise TypeError("masukkan tipe berupa 2 list tidak integer")


def perkalian_scalar(matrix: list[list], n: int | float) -> list[list]:
    """
    >>> perkalian_scalar([[1,2],[3,4]],5)
    [[5, 10], [15, 20]]
    """
    return [[x * n for x in row] for row in matrix]


def perkalian(matrix_a: list[list], matrix_b: list[list]) -> list[list]:
    """
    >>> perkalian([[1,2],[3,4]],[[5,5],[7,5]])
    [[19, 15], [43, 35]]
    >>> perkalian([[1,2.5],[3,4.5]],[[5,5],[7,5]])
    [[22.5, 17.5], [46.5, 37.5]]
    >>> perkalian([[1, 2, 3]], [[2], [3], [4]])
    [[20]]
    """
    if _check_not_integer(matrix_a) and _check_not_integer(matrix_b):
        rows, cols = _verify_matrix_size(matrix_a, matrix_b)

    if cols[0] != rows[1]:
        raise ValueError(
            f"tidak bisa mengalikan dimensi matrix ({rows[0], cols[0]})"
            f" dan ({rows[1]}, {cols[1]})"
        )

    return [
        [sum(m * n for m, n in zip(i, j)) for j in zip(*matrix_b)] for i in matrix_a
    ]


def identity(n: int) -> list[list]:
    """
    >>> identity(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    n = int(n)
    return [[int(row == column) for column in range(n)] for row in range(n)]


def transpose(matrix: list[list], return_map: bool = True) -> list[list] | map[list]:
    """
    >>> transpose([[1,2],[3,4]]) # doctest: +ELLIPSIS
    <map object at ...
    >>> transpose([[1,2],[3,4]], return_map=False)
    [[1, 3], [2, 4]]
    """
    if _check_not_integer(matrix):
        if return_map:
            return map(list, zip(*matrix))
        else:
            return list(map(list, zip(*matrix)))

    raise TypeError("hanya menerima tipe data berupa list")


def minor(matrix: list[list], row: int, column: int) -> list[list]:
    """
    >>> minor([[1, 2], [3, 4]], 1, 1)
    [[1]]
    """
    minor = matrix[:row] + matrix[row + 1 :]
    return [row[:column] + row[column + 1 :] for row in minor]


def determinan(matrix: list[list]) -> int:
    """
    >>> determinan([[1, 2], [3, 4]])
    -2
    """
    if len(matrix) == 1:
        return matrix[0][0]

    return sum(
        x * determinan(minor(matrix, 0, i)) * (-1) ** i for i, x in enumerate(matrix[0])
    )


def inverse(matrix: list[list]) -> list[list] | None:
    """
    >>> inverse([[1, 2], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    """
    det = determinan(matrix)
    if det == 0:
        return None

    matrix_minor = [
        [determinan(minor(matrix, i, j)) for j in range(len(matrix))]
        for i in range(len(matrix))
    ]

    kofaktor = [
        [x * (-1) ** (row + col) for col, x in enumerate(matrix_minor[row])]
        for row in range(len(matrix))
    ]
    adjugate = list(transpose(kofaktor))

    return perkalian_scalar(adjugate, 1 / det)


def _check_not_integer(matrix: list[list]) -> bool:
    return not isinstance(matrix, int) and not isinstance(matrix[0], int)


def _shape(matrix: list[list]) -> tuple[int, int]:
    return len(matrix), len(matrix[0])


def _verify_matrix_size(
    matrix_a: list[list], matrix_b: list[list]
) -> tuple[tuple, tuple]:
    shape = _shape(matrix_a) + _shape(matrix_b)
    if shape[0] != shape[3] or shape[1] != shape[2]:
        raise ValueError(
            f"operan tidak bisa bersama dengan shape "
            f"({shape[0], shape[1], shape[2], shape[3]})"
        )
    return (shape[0], shape[2]), (shape[1], shape[3])


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
