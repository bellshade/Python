# bubble sort adalah metode pengurutan algoritma
# dengan cara penukaran data secara terus menerus
# sampai bisa dipastikan dlam satu iterasi tertentu
# tidak ada lagi perubahan / penukaran.

# bandingkan nilai data ke 1 dan data ke 2
# jika data ke 1 lebih besar, maka tukar posisi ke data 2
# kemudian data yang lebih besar dibandingkan dengand data 3


def bubble_sort(collection):
    """
    contoh
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    """
    panjang = len(collection)

    for i in range(panjang - 1):
        swap = False
        for j in range(panjang - 1 - i):
            if collection[j] > collection[j + 1]:
                swap = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swap:
            # stop iterasi jika sudah ter sorting
            break
    return collection


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod(verbose=True)

    data = [0, 3, 5, 4, 2, 7]
    unsorted = [int(item) for item in data]
    print(f"data yang belum di sorting adalah {unsorted}")
    print(f"data yang sudah di sorting {bubble_sort(unsorted)}")
