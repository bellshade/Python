from math import sqrt


def is_prime(num: int) -> str:
    """
    Bilangan Prima adalah bilangan yang habis dibagi
    oleh bilangan itu sendiri dan bilangan 1.

    Fungsi ini mengecek apakah parameter `num`
    merupakan sebuah bilangan prima.

    Algoritma dari fungsi ini sebagai berikut:
    1. Cek apakah `num` sama dengan 2?
            - Iya, `return "Bilangan Prima"`
    2. Cek apakah `num` kurang dari 2 atau
    `num` dapat dibagi dengan 2?
            - Iya, `return "Bukan Bilangan Prima"`
    3. Mulai perulangan `i` dari angka 3 dengan 2
    langkah tiap perulangannya hingga `sqrt(num)`.
    Untuk setiap perulangan,
            - Cek apakah `num` dapat dibagi dengan 2?
                    - Iya, `return "Bukan Bilangan Prima"`
    4. `return "Bilangan Prima"` karena `num` sudah lolos
    dari semua pengujian.

    Penjelasan algoritma:
    1. Bilangan prima genap hanya beranggotakan satu,
    yaitu angka 2, sehingga:
            * Terkecuali angka 2, bilangan yang dapat dibagi
            dengan 2 bukanlah bilangan prima.
            * Variabel `i` dalam perulangan selalu ganjil
            (dimulai dari 3, ditambah 2 tiap perulangan)
            untuk menghemat waktu komputasi.
    2. Perulangan berhenti pada akar kuadrat dari `num`
    (telah dikonversi ke `int` supaya perulangan valid)
    untuk menghemat waktu komputasi. Penjelasan lebih lanjut
    mengenai pengoptimalisasian ini:
    https://stackoverflow.com/questions/5811151/why-do-we-check-up-to-the-square-root-of-a-prime-number-to-determine-if-it-is-pr

    Contoh input:
    >>> is_prime(1)
    'Bukan Bilangan Prima'
    >>> is_prime(2)
    'Bilangan Prima'
    >>> is_prime(3)
    'Bilangan Prima'
    >>> is_prime(4)
    'Bukan Bilangan Prima'
    >>> is_prime(5)
    'Bilangan Prima'
    """
    if num == 2:
        return "Bilangan Prima"

    if num < 2 or num % 2 == 0:
        return "Bukan Bilangan Prima"

    for i in range(3, int(sqrt(num)), 2):
        if num % i == 0:
            return "Bukan Bilangan Prima"

    return "Bilangan Prima"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # basic tests
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(5))

    # custom tests
    # print(is_prime(1234))
