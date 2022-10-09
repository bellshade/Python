# Mengingat array 9×9 2D yang terisi sebagian,
# tujuannya adalah untuk mengisi 9×9 kotak persegi dengan angka 1 sampai 9,
# sehingga setiap baris, kolom,
# dan masing-masing dari sembilan sub-grid 3×3 berisi semua digit.
# Ini dapat diselesaikan dengan menggunakan Backtracking
# dan mirip dengan n-queens.
# Kami memeriksa untuk melihat apakah sel aman atau tidak dan secara rekursif
# memanggil berfungsi pada kolom berikutnya untuk melihat apakah mengembalikan True.
# Jika ya, kita Telah memecahkan teki">teka-teki. lain,
# kita mundur dan menempatkan nomor lain dalam sel itu dan ulangi proses ini.

from __future__ import annotations


Matrix = list[list[int]]

initial_grid: Matrix = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

no_solution: Matrix = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def safe(grid: Matrix, row: int, col: int, num: int) -> bool:
    # Fungsi ini memeriksa kisi untuk melihat apakah setiap baris,
    # kolom, dan subgrid 3x3 berisi digit 'n'.
    # Ini mengembalikan False
    # jika tidak 'aman' (digit duplikat ditemukan)
    # pengembalian lain Benar jika 'aman'

    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(col - col % 3) + j] == num:
                return False

    return True


def find_empty_location(grid: Matrix) -> tuple[int, int] | None:
    # Fungsi ini menemukan lokasi kosong sehingga
    # kita dapat menetapkan nomor untuk baris dan kolom tertentu.
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j

    return None


def sudoku(grid: Matrix) -> Matrix | None:
    """
    Mengambil grid yang terisi sebagian
    dan mencoba untuk menetapkan nilai ke semua lokasi
    yang tidak ditugaskan sedemikian rupa
    untuk memenuhi persyaratan untuk solusi Sudoku
    (non-duplikasi di baris, kolom, dan kotak)

    >>> sudoku(initial_grid)  # doctest: +NORMALIZE_WHITESPACE
    [[3, 1, 6, 5, 7, 8, 4, 9, 2],
     [5, 2, 9, 1, 3, 4, 7, 6, 8],
     [4, 8, 7, 6, 2, 9, 5, 3, 1],
     [2, 6, 3, 4, 1, 5, 9, 8, 7],
     [9, 7, 4, 8, 6, 3, 1, 2, 5],
     [8, 5, 1, 7, 9, 2, 6, 4, 3],
     [1, 3, 8, 9, 4, 7, 2, 5, 6],
     [6, 9, 2, 3, 5, 1, 8, 7, 4],
     [7, 4, 5, 2, 8, 6, 3, 1, 9]]
     >>> sudoku(no_solution) is None
     True
    """
    if location := find_empty_location(grid):
        row, column = location
    else:
        return grid

    for digit in range(1, 10):
        if safe(grid, row, column, digit):
            grid[row][column] = digit
            if sudoku(grid) is not None:
                return grid

            grid[row][column] = 0

    return None


def show_solution(grid: Matrix) -> None:
    # tampilkan solusi Sudoku dari ukuran 9x9
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


if __name__ == "__main__":
    import doctest

    # contoh
    # for example in (initial_grid, no_solution):
    #     print("\nContoh Grid:\n" + "=" *20)
    #     show_solution(example)
    #     print("\nContoh solusi grid:")
    #     solution = sudoku(example)
    #     if solution is not None:
    #         show_solution(solution)
    #     else:
    #         print("Tidak ada solusi")

    doctest.testmod()
