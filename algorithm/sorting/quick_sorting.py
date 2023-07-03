from __future__ import annotations


def partisi(array: list[int], low: int, high: int) -> int:
    """
    Partisi array menggunakan algoritma quicksort
    array dipartisi menjadi dua bagian: elemen-elemen
    yang lebih kecil dari pivot berada di sebelah kiri,
    sementara elemen-elemen yang lebih besar berada
    di sebelah kanan
    Args:
        array (list[int]): array yang akan dipartisi
        low (int): indeks rendah dari array
        high (int): indeks tinggi dari array
    Return:
        int: indeks dari pivot setlah proses partisi
    """
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array: list[int]) -> None:
    """
    Algoritma proses untuk mengrutkan
    fungsi ini menggunakan metode rekursif untuk
    mengurutkan array secara rekursif, pada setiap
    pemanggilan rekursif, elemen pivot dipilih dengan
    memanggil fungsi `partisi`
    Args:
        array (list[int]): array yang akan diurutkan
    return:
        None

    Contoh:
        >>> data = [2, 1, 5, 6, 3]
        >>> quick_sort(data)
        >>> data
        [1, 2, 3, 5, 6]
    """

    def _quick_sort(array: list[int], low: int, high: int) -> None:
        if low < high:
            pi = partisi(array, low, high)
            _quick_sort(array, low, pi - 1)
            _quick_sort(array, pi + 1, high)

    _quick_sort(array, 0, len(array) - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
