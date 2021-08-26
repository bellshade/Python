# Metode ini memecahkan masalah "tikus dalam labirin".
# Dalam masalah ini kita memiliki beberapa matriks n by n, titik awal dan titik akhir.
# Kami ingin pergi dari awal sampai akhir. Dalam matriks ini nol mewakili dinding
# dan jalur yang bisa kita gunakan.


from typing import List


def solve_maze(maze: List[List[int]]) -> bool:
    """
    kita bisa menggunakan parameter
    maze 2d: matrix
    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [1, 0, 1, 0, 1],
    ...         [0, 0, 1, 0, 0],
    ...         [1, 0, 0, 1, 0]]
    >>> solve_maze(maze)
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 0, 1, 1]
    [0, 0, 0, 0, 1]
    True
    >>> maze = [[0, 1, 0, 1, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 0, 0, 0, 1],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 0, 0, 0, 0]]
    >>> solve_maze(maze)
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 0, 0, 0, 0]
    [1, 1, 1, 1, 1]
    True
    >>> maze = [[0, 0, 0],
    ...         [0, 1, 0],
    ...         [1, 0, 0]]
    >>> solve_maze(maze)
    [1, 1, 1]
    [0, 0, 1]
    [0, 0, 1]
    True
    >>> maze = [[0, 1, 0],
    ...         [0, 1, 0],
    ...         [1, 0, 0]]
    >>> solve_maze(maze)
    tidak ada solusi
    False
    >>> maze = [[0, 1],
    ...         [1, 0]]
    >>> solve_maze(maze)
    tidak ada solusi
    False
    """

    size = len(maze)
    solution = [[0 for _ in range(size)] for _ in range(size)]
    solved = run_maze(maze, 0, 0, solution)
    if solved:
        print("\n".join(str(row) for row in solution))
    else:
        print("tidak ada solusi")
    return solved


def run_maze(maze: List[List[int]], i: int, j: int, solution: List[List[int]]) -> bool:
    size = len(maze)
    if i == j == (size - 1):
        solution[i][j] = 1
        return True

    lower_flag = not (i < 0) and not (j < 0)
    upper_flag = not (i >= size) and not (j >= size)
    if lower_flag and upper_flag:
        block_flag = (not (solution[i][j])) and (not (maze[i][j]))
        if block_flag:
            solution[i][j] = 1
            if (
                run_maze(maze, i + 1, j, solution)
                or run_maze(maze, i, j + 1, solution)
                or run_maze(maze, i - 1, j, solution)
                or run_maze(maze, i, j - 1, solution)
            ):
                return True

            solution[i][j] = 0
            return False
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
