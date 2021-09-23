"""
Bubble Sort adalah Sorting algorithm yang cara kerjanya adalah dengan
membandingkan 2 elemen array lalu menggeser kedua elemen tersebut
sesuai dengan urutan terus-menerus sampai akhir array
Langkah 1    [5, 3, 8, 4, 6] Membandingkan elemen ke 1 dengan elemen ke
              ^  ^           2.Dikarenakan nilai dari elemen ke 1 lebih 
                             besar maka posisi kedua elemen tersebut 
                             ditukar
Langkah 2    [3, 5, 8, 4, 6] Membandingkan elemen ke 2 dengan elemen 
                 ^  ^        ke 3. Dikarenakan nilai dari elemen ke 2 
                             lebih kecil maka posisi kedua elemen 
                             tidak ditukar
Langkah 3    [3, 5, 8, 4, 6] Membandingkan elemen ke 3 dengan elemen ke 4.
              ^  ^           Dikarenakan nilai dari elemen ke 3 lebih besar
                             maka posisi kedua elemen tersebut ditukar
Langkah 4    [3, 5, 4, 8, 6] Membandingkan elemen ke 4 dengan elemen ke 5.
                       ^  ^  Dikarenakan nilai dari elemen ke 4 lebih besar
                             maka posisi kedua elemen tersebut ditukar
Langkah 5    Mengulangi pengecekan dari awal sampai akhir array sampai 
tidak ada lagi yang dapat ditukar posisi
Final        [3, 4, 5, 6, 8] Array selesai diurutkan
"""


def bubble_sort(numbers: list) -> list:
    """
    >>> bubble_sort([5, 2, 1, 3, 2, 5, 7, 3, 4])
    [1, 2, 2, 3, 3, 4, 5, 5, 7]
    """
    n = len(numbers) # mendapatkan panjang list number
    for i in range(n-1, 0, -1): 
        # perulangan pertama, perulangan ini digunakan untuk
        # mengatur jumlah bari yang akan di lakukan pengecekan 
        # dan pemindahan pada loop selanjutnya
        # parameter (n, 0, -1) pada range digunakan untuk mengatur
        # proses perulangan agar i mengasilkan angka dari index terbesar
        # dari panjang n sampai ke 0
        for j in range(i):
            # perulangan kedua, perulangan ini digunakan untuk
            # melakukan proses cheking apakah elemen sekarang yang
            # diwakilkan oleh numbers[j] lebih besar dari elemen
            # selanjutnya yang di wakilkan oleh numbers[j+1] 
            if numbers[j] > numbers[j+1]:
                # proses elemen ke sekarang [j] dengan elemen ke [j+1]
                # apakah lebih besar elemen sekarang jika iya maka 
                # pindahkan elemen tersebut
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


def testing() -> None:
    """
    >>> numbers = [5, 3, 8, 4, 6]
    >>> expected_result = [3, 4, 5, 6, 8]
    >>> bubble_sort(numbers) == expected_result
    True
    """
    numbers = [5, 2, 1, 3, 2, 5, 7, 3, 4]
    print(f"\nSebelum Sort: {numbers}\n")
    result_sort = bubble_sort(numbers)
    print(f"Seteleh sort: {result_sort}\n")


if __name__ == "__main__":
    import doctest
    # testing()
    doctest.testmod()
