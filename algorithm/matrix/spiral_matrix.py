# Program ini mencetak matriks dalam bentuk spiral.
# Masalah ini telah diselesaikan melalui cara rekursif.
# Matriks harus memenuhi kondisi di bawah ini
# i) matriks harus hanya satu atau dua dimensi
# ii) jumlah kolom semua baris harus sama

from collections.abc import Iterable


def check_matrix(matrix):
    if matrix and isinstance(matrix, Iterable):
        if isinstance(matrix[0], Iterable):
            prev_len = 0
            for row in matrix:
                if prev_len == 0:
                    prev_len = len(row)
                    result = True
                else:
                    result = prev_len == len(row)
        else:
            result = True
    else:
        result = False

    return result


def spiral_print(a):
    if check_matrix(a) and len(a) > 0:
        mat_row = len(a)
        if isinstance(a[0], Iterable):
            mat_col = len(a[0])
        else:
            for dat in a:
                print(dat),
            return

        # pencetakan horizontal meningkat
        for i in range(0, mat_col):
            print(a[0][i]),

        # pencetakan vertikal ke bawah
        for i in range(1, mat_row):
            print(a[i][mat_col - 1]),

        # pencetakan horizontal menurun
        if mat_row > 1:
            for i in range(mat_col - 2, -1, -1):
                print(a[mat_row - 1][i]),

        # pencetakan vertikal ke atas
        for i in range(mat_row - 2, 0, -1):
            print(a[i][0]),

        remain_mat = [row[1 : mat_col - 1] for row in a[1 : mat_row - 1]]
        if len(remain_mat) > 0:
            spiral_print(remain_mat)
        else:
            return

    else:
        print("matrix tidak valid")
        return


if __name__ == "__main__":
    a = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])
    spiral_print(a)
