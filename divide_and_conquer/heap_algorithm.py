# Algoritma Heap mengembalikan daftar semua permutasi
# yang mungkin dari daftar.
# Ini meminimalkan gerakan dengan
# menghasilkan setiap permutasi dari yang sebelumnya
# dengan menukar hanya dua elemen.
# informasi lebih lanjut
# https://en.wikipedia.org/wiki/Heap%27s_algorithm.


def heaps(arr: list) -> list:
    """
    >>> heaps([])
    [()]
    >>> heaps([0])
    [(0,)]
    >>> heaps([-1, 1])
    [(-1, 1), (1, -1)]
    >>> heaps([1, 2, 3])
    [(1, 2, 3), (2, 1, 3), (3, 1, 2), (1, 3, 2), (2, 3, 1), (3, 2, 1)]
    >>> from itertools import permutations
    >>> sorted(heaps([1,2,3])) == sorted(permutations([1,2,3]))
    True
    >>> all(sorted(heaps(x)) == sorted(permutations(x))
    ...     for x in ([], [0], [-1, 1], [1, 2, 3]))
    True
    """

    if len(arr) <= 1:
        return [tuple(arr)]

    res = []

    def generate(k: int, arr: list):
        if k == 1:
            res.append(tuple(arr[:]))
            return

        generate(k - 1, arr)

        for i in range(k - 1):
            if k % 2 == 0:  # k genap
                arr[i], arr[k - 1] = arr[k - 1], arr[i]
            else:  # k ganjil
                arr[0], arr[k - 1] = arr[k - 1], arr[0]
            generate(k - 1, arr)

    generate(len(arr), arr)
    return res


if __name__ == "__main__":
    import doctest

    input_dat = input("masukkan nomor yang dipisahakan dengan koma").strip()
    arr = [int(item) for item in input_dat.split(",")]
    print(heaps(arr))

    doctest.testmod()
