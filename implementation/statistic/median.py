def median(arr: list) -> int | float:
    """
    median adalah nilai yang dapat membagi data menjadi dua bagian yang sama.
    dengan kata lain bagaimana cara

    **Params**

    -----
    arr: tipe data ini adalah

    **Return**

    -----
    value : value ini tergantung pada ganjil atau genapnya jumlah panjang data

    **Contoh**

    ---
    >>> data=[1,2,3,4,5,6]
    >>> median(data)
    3.5
    >>> data=[1,1,2,2,2,3,3]
    >>> median(data)
    2
    """

    # mengurutkan dari terkecil ke besar
    arr.sort()
    panjang_data = len(arr)

    if panjang_data % 2 == 0:
        index = panjang_data - 1
        hasil = (arr[index // 2] + arr[(index // 2) + 1]) / 2
    else:
        index = panjang_data - 1
        hasil = arr[(index + 1) // 2]
    return hasil


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
