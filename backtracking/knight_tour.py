# informasi tentang knight tour
# https://www.youtube.com/watch?v=ab_dY3dZFHM

from __future__ import annotations


def get_valid_pos(position: tuple[int, int], n: int) -> list[tuple[int, int]]:
    """
    mencari posisi yang valid
    >>> get_valid_pos((1, 3), 4)
    [(2, 1), (0, 1), (3, 2)]
    """
    y, x = position
    positions = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]
    permission_positions = []
    for position in positions:
        y_test, x_test = position
        if 0 <= y_test < n and 0 <= x_test < n:
            permission_positions.append(position)

    return permission_positions


def is_complete(board: list[list[int]]) -> bool:
    """
    Periksa apakah papan (matriks) telah terisi penuh dengan nilai bukan nol.

    >>> is_complete([[1]])
    True

    >>> is_complete([[1, 2], [3, 0]])
    False
    """
    return not any(elem == 0 for row in board for elem in row)


def open_knight_tour_helper(
    board: list[list[int]], pos: tuple[int, int], curr: int
) -> bool:
    # fungsi untuk solver dari kngiht tour

    if is_complete(board):
        return True

    for position in get_valid_pos(pos, len(board)):
        y, x = position

        if board[y][x] == 0:
            board[y][x] = curr + 1
            if open_knight_tour_helper(board, position, curr + 1):
                return True
            board[y][x] = 0

    return False


def open_knight_tour(n: int) -> list[list[int]]:
    """
    Temukan solusi untuk masalah ksatria untuk papan berukuran n. meningkatkan
    ValueError jika tur tidak dapat dilakukan untuk ukuran tertentu.

    >>> open_knight_tour(1)
    [[1]]

    >>> open_knight_tour(2)
    Traceback (most recent call last):
    ...
    ValueError: Open Knight Tour tidak dapat dilakukan di papan berukuran 2
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            board[i][j] = 1
            if open_knight_tour_helper(board, (i, j), 1):
                return board
            board[i][j] = 0

    raise ValueError(f"Open Knight Tour tidak dapat dilakukan di papan berukuran {n}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
