def digit_sum(n: int) -> int:
    """
    Fungsi ini menghitung jumlah dari digit masukan n.
    Misal digit masukan adalah 123, maka jumlah dari
    digit tersebut adalah 1 + 2 + 3.

    Hasil di atas dapat dicapai dengan menggunakan
    operasi modulo serta floor division pada Python.

    Algoritma dari fungsi ini sebagai berikut :
    1. Deklarasi variabel result yang akan menampung
    hasil
    2. Deklarasi variabel temp (temporary) sebagai
    variabel yang akan dikenakan operasi loop
    3. Loop variabel temp selama nilainya lebih dari 0
    4. Pada loop lakukan :
        4.1. Variabel dimodulo 10. Hal ini ditujukan agar
        kita mendapatkan digit paling kanan. Hasil dari modulo
        tersebut dijumlahkan dengan variabel result
        4.2. Bagi variabel temp dengan 10. Hal ini akan
        mengurangi nilai dari variabel temp.

    Contoh :
    n = 12
    Iterasi pertama
    result  = 0 + (12 % 10)
            = 0 + 2
            = 2
    temp    = 10 // 10
            = 1

    Iterasi kedua
    result  = 2 + (1 % 10)
            = 2 + 1
            = 3
    temp    = 1 // 10
            = 0

    Valid input :
    >>> digit_sum(1234)
    10

    Invalid input :
    >>> digit_sum(-12)
    Traceback (most recent call last):
    ...
    ValueError: Input tidak boleh negatif
    """
    result = 0
    temp = n

    if n < 0:
        raise ValueError("Input tidak boleh negatif")

    while temp > 0:
        result = result + temp % 10
        temp = temp // 10

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    hasil = digit_sum(123)
    print(hasil)

    hasil = digit_sum(-123)
    print(hasil)
