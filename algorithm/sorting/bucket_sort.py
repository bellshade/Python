# Bucket Sort adalah algoritma pengurutan
# yang membagi array ke dalam beberapa bucket,
# lalu setiap bucket diurutkan secara individu
# dan akhirnya semua bucket digabungkan menjadi array akhir.

# Distribusikan elemen ke dalam bucket.
# Urutkan masing-masing bucket.
# Gabungkan semua bucket menjadi satu list terurut.

def bucket_sort(collection: list[float]) -> list[float]:
    """
    contoh
    >>> bucket_sort([0.25, 0.36, 0.58, 0.41, 0.29, 0.22, 0.45, 0.79])
    [0.22, 0.25, 0.29, 0.36, 0.41, 0.45, 0.58, 0.79]
    >>> bucket_sort([0.5, 0.3, 0.9, 0.7])
    [0.3, 0.5, 0.7, 0.9]
    """

    if len(collection) == 0:
        return collection

    # Membuat bucket kosong
    bucket_count: int = len(collection)
    buckets: list[list[float]] = [[] for _ in range(bucket_count)]

    # Menempatkan elemen ke dalam bucket
    for value in collection:
        index: int = int(value * bucket_count)
        if index != bucket_count:
            buckets[index].append(value)
        else:
            buckets[bucket_count - 1].append(value)

    # Mengurutkan setiap bucket dan menggabungkannya
    sorted_array: list[float] = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    data: list[float] = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    unsorted: list[float] = [float(item) for item in data]
    print(f"data yang belum di sorting adalah {unsorted}")
    print(f"data yang sudah di sorting {bucket_sort(unsorted)}")
