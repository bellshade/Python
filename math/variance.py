def rata_rata(data: list[int | float]) -> float:
    """
    rata-rata merupakan model matematika untuk mengetahui
    jumlah seluruh nilai data dibagi banyak data
    contoh input:
    >>> rata_rata([20,12,12])
    14.666666666666666
    >>> rata_rata([-20,3,12])
    -1.6666666666666667
    """
    jumlah = 0
    panjang_data = 0
    for number in data:
        panjang_data += 1
        jumlah += number
    result = jumlah / panjang_data
    return result


def variance(data: list[int | float]) -> float:
    """
    variansi atau dalam bahasa inggris disebut juga disebut variance.
    variansi ini berfungsi untuk menghitung ukuran nilai data agar,
    mengetahui sifat-sifat serta semua titik data dalam kumpulan data.
    >>> variance([10,20,20])
    33.33
    >>> variance([-20,1,2])
    154.33
    """
    n = len(data)
    jumlah = 0
    for value in data:
        hitung = (value - rata_rata(data)) ** 2
        jumlah += hitung
    result = jumlah / (n - 1)
    return round(result, 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
