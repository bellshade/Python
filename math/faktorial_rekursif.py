def faktorial_rekursif(angka: int) -> int:
    """
    Faktorial adalah hasil perkalian dari semua bilangan positif yang dimulai
    dari 1 hingga bilangan tersebut, notasi dalam faktorial dilambangan dengan
    exclamation `angka!` / `n!` / `number!`

    pendekatan perhitungan ini menggunakan pendekatan rekursif, dengan memanggil
    fungsinya sendiri hingga mencapai base casenya.

    sebagai contoh:

    5 x 4 x 3 x 2 x 1 = 120, jika nilai yang diberikan nol maka hasilnya adalah 1

    Parameter:
        angka (int): nilai yang dikalkulasi faktorialnya

    Return:
        int: hasil nilai yang akan diberikan dari `angka!`

    Contoh:
    >>> faktorial(5)
    120
    >>> faktorial(2)
    2
    >>> faktorial(10)
    3628800
    """
    if not isinstance(angka, int):
        raise TypeError("fungsi faktorial() hanya bekerja dengan tipe data integer")

    if angka < 0:
        raise ValueError("parameter angka tidak boleh negatif")

    return 1 if angka in {0, 1} else angka * faktorial_rekursif(angka - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    angka: int = 3
    print(f"faktorial dari {angka} adalah: {faktorial_rekursif(3)}")
