# dalam aljabar linier numerik, metode jacobi adalah algoritma iteratif
# untuk menentukan solusi dari sistem persamaan linier yang dominan
# secara diagonal.setiap elemen diagonal diselesaikan, dan nilai
# perkiraan dimasukkan. proses ini kemudian diulang sampe konvergen.
# algoritma ini adalah versi stipped-down dari metode transformasi jacobi
# dari diagonalisasi matriks. metode ini dinamai carl gustav jacob jacobi


from __future__ import annotations

import numpy as np


# metode untuk mencari solusi sistem persamaan linear
def jacobi_iteration_method(
    coefficient_matrix: np.ndarray,
    constant_matrix: np.ndarry,
    init_val: list,
    iterations: int,
) -> list[float]:
    """
    algoritma iteratif untuk menentukan solusi dari
    dominan diagonal tegas sistem persamaan linear

    4x1 + x2 + x3 = 2
     x2 + 5x2 + 2x3 = -6

    >>> coefficient = np.array([[4, 1, 1], [1, 5, 2], [1, 2, 4]])
    >>> constant = np.array([[2], [-6], [-4]])
    >>> init_val = [0.5, -0.5, -0.5]
    >>> iterations = 3
    >>> jacobi_iteration_method(coefficient, constant, init_val, iterations)
    [0.909375, -1.14375, -0.7484375]
    """

    rows1, cols1 = coefficient_matrix.shape
    rows2, cols2 = constant_matrix.shape

    if rows1 != cols1:
        raise ValueError(f"koefisien matriks harus nxn tetapi sekarang {rows1}x{cols1}")

    if cols2 != 1:
        raise ValueError(f"konstanta matriks harus nx1 tetapi sekarang {rows2}x{cols2}")

    if rows1 != rows2:
        raise ValueError(
            f"""koeifisien dan konstanta matriks harus ukuran nxn dan nx1
            tetapi sekarang {rows1}x{cols1} dan {rows2}x{cols2}"""
        )

    if len(init_val) != rows1:
        raise ValueError(
            f"""jumlah nilai awal harus sama dengan jumlah baris dalam
            koefisien matriks tetapi sekarang {len(init_val)} dan {rows1}"""
        )

    if iterations <= 0:
        raise ValueError("iterasi setidaknya harus 1")

    table = np.concatenate((coefficient_matrix, constant_matrix), axis=1)
    rows, cols = table.shape

    strictly_diagonally_dominant(table)

    for i in range(iterations):
        new_val = []
        for row in range(rows):
            temp = 0
            for col in range(cols):
                if col == row:
                    denom = table[row][col]
                elif col == cols - 1:
                    val = table[row][col]
                else:
                    temp += (-1) * table[row][col] * init_val[col]
            temp = (temp + val) / denom
            new_val.append(temp)
        init_val = new_val

    return [float(i) for i in new_val]


# memeriksa apakah matriks yang diberikan benar-benar dominan diagonal
def strictly_diagonally_dominant(table: np.ndarray) -> bool:
    """
    >>> table = np.array([[4, 1, 1, 2], [1, 5, 2, -6], [1, 2, 4, -4]])
    >>> strictly_diagonally_dominant(table)
    True
    """
    rows, cols = table.shape

    is_diagonally_dominant = True

    for i in range(0, rows):
        sum = 0
        for j in range(0, cols - 1):
            if i == j:
                continue
            else:
                sum += table[i][j]

        if table[i][i] <= sum:
            raise ValueError(
                "matriks koefisien tidak sepenuhnya dominan secara diagonal"
            )

    return is_diagonally_dominant


if __name__ == "__main__":
    import doctest

    doctest.testmod()
