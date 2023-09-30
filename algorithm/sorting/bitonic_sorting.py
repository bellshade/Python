from __future__ import annotations


def komparasi_swap(array: list[int], index1: int, index2: int, direction: int) -> None:
    """
    membanding nilai pada indeks 1 dan index 2 yang diberikan dalam array, kemudian swap
    sesuai dengan arah yang diberikan

    >>> arr = [12, 42, -21, 1]
    >>> komparasi_swap(arr, 1, 2, 1)
    >>> arr
    [12, -21, 42, 1]
    """
    if (direction == 1 and array[index1] > array[index2]) or (
        direction == 0 and array[index1] < array[index2]
    ):
        array[index1], array[index2] = array[index2], array[index1]


def bitonic_merge(array: list[int], low: int, length: int, direction: int) -> None:
    """
    fungsi rekursif yang mengurutkan urutan bitonic secara naik, jika arah = 1,
    dan secara menurun jika arah = 0. urutan yang akan diurutkan
    dimulai pada posisi indeks rendah, parameter panjang adalah
    jumlah elemen yang akan diurutkan

    >>> arr = [12, 42, -21, 1]
    >>> bitonic_merge(arr, 0, 4, 1)
    >>> arr
    [-21, 1, 12, 42]
    """
    if length > 1:
        mid = int(length / 2)
        for i in range(low, low + mid):
            komparasi_swap(array, i, i + mid, direction)
        bitonic_merge(array, low, mid, direction)
        bitonic_merge(array, low + mid, mid, direction)


def bitonic_sorting(array: list[int], low: int, length: int, direction: int) -> None:
    """
    fungsi ini pertama menghasilkan urutan bitonik dengan mengurutkan secara rekursif
    dua setengahnya dalam urutan yang berlawan, kemudian memanggil fungsi
    bitonic_merge untuk menggabungkan urutan yang sama

    >>> arr = [12, 34, 92, -23, 0, -121, -167, 145]
    >>> bitonic_sorting(arr, 0, 8, 0)
    >>> arr
    [145, 92, 34, 12, 0, -23, -121, -167]
    """
    if length > 1:
        mid = int(length / 2)
        bitonic_sorting(array, low, mid, 1)
        bitonic_sorting(array, low + mid, mid, 0)
        bitonic_merge(array, low, length, direction)


if __name__ == "__main__":
    import doctest

    # dat_input = input("masukkan beberapa angka menggunakan koma:").strip()
    # tidak_tersorting = [int(item.strip()) for item in dat_input.split(",")]
    # bitonic_sorting(tidak_tersorting, 0, len(tidak_tersorting), 1)
    doctest.testmod(verbose=True)
