# bubble sort adalah metode pengurutan algoritma
# dengan cara penukaran data secara terus menerus
# sampai bisa dipastikan dlam satu iterasi tertentu
# tidak ada lagi perubahan / penukaran.

# melakukan iterasi sebanyak jumlah data collection
# data collection dapat berupa kumpulan string dan/atau integer
# bandingkan data ke 1 dengan data ke 2
# jika huruf awal atau nilai data ke 1 lebih besar, maka tukar posisi ke data 2
# kemudian data yang lebih besar dibandingkan dengand data 3
# urutan data mengikuti urutan ASCII


def bubble_sort_ascii(collection: list) -> list:
    """
    contoh
    >>> bubble_sort_ascii([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort_ascii(['c', 'a', 'd', 'b', 'e'])
    ['a', 'b', 'c', 'd', 'e']
    >>> bubble_sort_ascii(['b', 3, 'a', '!', 2, 'c'])
    ['!', 2, 3, 'a', 'b', 'c']
    >>> bubble_sort_ascii([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    """
    panjang = len(collection)

    for i in range(panjang - 1):
        for j in range(panjang - 1 - i):
            if str(collection[j]) > str(collection[j + 1]):
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
    return collection


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    data = [4, "a", 2, "d", "b", "c", "$", "5"]
    unsorted = [item for item in data]
    print(f"data yang belum di sorting adalah {unsorted}")
    print(f"data yang sudah di sorting {bubble_sort_ascii(unsorted)}")
