def rata_rata(arr: list[int | float]) -> float:
    """
    rata-rata adalah menghitung seluruh nilai pada data dengan
    panjangnya data tersebut

    **Parameter**

    ----
    :param arr:parameter ini bertipe data list mengandung bisa berupa bulat dan desimal

    **Parameter**

    ----
    **Return**
    :param return: paramater ini beroutput angka desimal
    **Contoh**
    >>> data=[1,1,2,2,2,3,3]
    >>> rata_rata(data)
    2.0
    """
    arr = arr.copy()
    panjang_data = 0
    perjumlahan = 0
    for value in arr:
        panjang_data += 1
        perjumlahan += value
    hasil = perjumlahan / panjang_data
    return hasil


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
