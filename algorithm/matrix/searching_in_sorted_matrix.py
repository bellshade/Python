# informasi lebih lanjut tentang searching sorted
# matrix
# https://www.geeksforgeeks.org/search-element-sorted-matrix/

from __future__ import annotations


def search_in_a_sorted_matrix(
    mat: list[list], m: int, n: int, key: int | float
) -> None:
    """
    >>> search_in_a_sorted_matrix(
    ...     [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 5)
    kunci 5 ditemukan pada row 1 kolom 2
    >>> search_in_a_sorted_matrix(
    ...     [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 21)
    kunci 21 tidak ditemukan
    >>> search_in_a_sorted_matrix(
    ...     [[2.1, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 2.1)
    kunci 2.1 ditemukan pada row 1 kolom 1
    >>> search_in_a_sorted_matrix(
    ...     [[2.1, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 2.2)
    kunci 2.2 tidak ditemukan
    """
    i, j = m - 1, 0
    while i >= 0 and j < n:
        if key == mat[i][j]:
            print(f"kunci {key} ditemukan pada row {i + 1} kolom {j + 1}")
            return
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1

    print(f"kunci {key} tidak ditemukan")


def main():
    mat = [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]]
    x = int(input("masukkan element yang ingin dicari:").strip())
    print(mat)
    search_in_a_sorted_matrix(mat, len(mat), len(mat[0]), x)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
