# menangani eksepsi sederhana
try:
    # jalankan kode berikut jika berhasil
    # bilangan yang dibagi dengan nol merupakan kesalahan
    # maka tangani di dalam 'except'
    hasil = 5 / 0  # type: ignore
    print('Hasil pembagian adalah =', hasil)
except ZeroDivisionError:
    # tangani kesalahan di sini
    print('Bilangan tidak dapat dibagi dengan nol')


# menangani lebih dari satu eksepsi
# Cara 1. menggunakan lebih dari satu blok 'except'
try:
    hasil = 3 / "1"  # type: ignore
    print('Hasil pembagian adalah =', hasil)
except ZeroDivisionError:
    print("Bilangan tidak dapat dibagi dengan nol")
except TypeError:
    print("Bilangan harus bertipe numerik")

# Cara 2. menuliskannya di dalam tuple
try:
    hasil = 3 / "1"  # type: ignore
    print('Hasil pembagian adalah =', hasil)
except (ZeroDivisionError, TypeError):
    print("Terdapat kesalahan ketika melakukan pembagian")


# mencetak pesan kesalahan/eksepsi bawaan python
# gunakan keyword 'as' untuk memberi nama alias eksepsi
try:
    hasil = 5 / 0  # type: ignore
    print("Hasil pembagian adalah =", hasil)
except ZeroDivisionError as err:
    print(err)  # division by zero
except TypeError as err:
    print(err)  # unsupported operand type(s) for /: 'int' and 'str'

try:
    hasil = 3 / "1"  # type: ignore
    print('Hasil pembagian adalah =', hasil)
except (ZeroDivisionError, TypeError) as err:
    # cetak pesan error tergantung jenis error yang ditangkap
    print(err)
