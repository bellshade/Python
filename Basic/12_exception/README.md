# Exceptions (Eksepsi)
Saat melakukan pemrograman di bahasa _Python_, pasti sebagian besar _developer_ pernah mengalami kesalahan ketika mengeksekusi sebuah program yang dikenal dengan sebutan _error_. Hal ini terjadi karena ada kesalahan dalam menuliskan sintaks yang membuat program tersebut berhenti dan memunculkan pesan kesalahan (_error_) tersebut. Beberapa contoh kesalahan yang biasa kita lakukan ketika memprogram bahasa _Python_ diantaranya:

- Pernyataan `if` atau `for` yang tidak diikuti dengan tanda titik dua.
  ```python
  >>> if True
    File "<stdin>", line 1
      if True
            ^
  SyntaxError: invalid syntax
  ```

- Penggunaan tanda kurung yang salah.
  ```python
  >>> print('contoh penulisan yang salah'))
    File "<stdin>", line 1
      print('contoh penulisan yang salah'))
                                          ^
  SyntaxError: invalid syntax
  ```

_Error_ juga dapat terjadi saat program berjalan (_runtime_) yang disebut dengan eksepsi (_exception_). Beberapa contoh eksepsi yang biasa ditemukan adalah sebagai berikut:
- `ZeroDivisionError` : suatu bilangan numerik tidak dapat dibagi dengan nol.
  ```python
  >>> 2 / 0
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ZeroDivisionError: division by zero
  ```

- `TypeError` : operasi aritmatika pada tipe data yang tidak sesuai, misalkan tidak dapat melakukan operasi penjumlahan antara _integer_ dengan _string_.
  ```python
  >>> 5 + "5"
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: unsupported operand type(s) for +: 'int' and 'str'
  ```
## Exeption Handling (Penanganan Eksepsi)
Seperti yang sudah diketahui di awal bahwa terjadinya _error_ atau _exception_ menyebabkan program terhenti. Untuk mengantisipasi hal ini, _Python_ menyediakan penanganan kesalahan tersebut menggunakan pernyataan `try` dan `except`. Letakkan baris program yang memiliki kemungkinan _error_ di dalam blok `try`. Bila terjadi error di dalam blok `try`, tangani di dalam blok `except`. Struktur penulisan kodenya adalah sebagai berikut.
```python
try:
    # eksekusi baris ini jika tidak ada kesalahan (error)
except:
    # tangani jika terdapat kesalahan di dalam blok try
```
Pada contoh eksepsi `ZeroDivisionError` di atas, jika ingin menangani eksepsi tersebut, maka di dalam blok `try` berisi baris kode untuk melakukan operasi pembagian dua buah bilangan. Sedangkan di dalam blok `except` berisi pesan kesalahan menggunakan sintaks `print()` bahwa suatu bilangan tidak dapat dibagi dengan nol, sehingga penulisannya sebagai berikut.
```python
try:
    # karena pembaginya adalah nol, maka tangani error di except
    hasil = 5 / 0
    print('Hasil pembagian adalah =', hasil)
except:
    # tangani error di sini
    print('Bilangan tidak dapat dibagi dengan nol')
```
Pada contoh di atas, sebelum masuk ke dalam blok `except`, alangkah baiknya diikuti dengan jenis eksepsi yang ingin ditangani. Karena bisa saja terdapat lebih dari satu jenis eksepsi yang berbeda untuk ditangani. Pada contoh di atas, untuk menangani untuk eksepsi `ZeroDivisionError`, maka penulisan kodenya sebagai berikut:
```python
try:
    # karena pembaginya adalah nol, maka tangani error di except
    hasil = 5 / 0
    print('Hasil pembagian adalah =', hasil)
except ZeroDivisionError:
    # tangani error di sini
    print('Bilangan tidak dapat dibagi dengan nol')
```

Jika kita ingin menangani lebih dari satu eksepsi, maka jenis eksepsi yang ingin disebutkan menggunakan tuple. Contoh, jika ingin menangani `ZeroDivisionError` dan `TypeError`, maka struktur penulisannya menjadi sebagai berikut:
```python
try:
    # lakukan sesuatu
except (ZeroDivisionError, TypeError):
    # tangani error di sini
```

Eksepsi dapat ditangani menggunakan lebih dari satu blok `except`. Dari contoh kasus di atas, dapat dikembangkan sebagai berikut:
```python
try:
    hasil = 5 / "2"
    print("Hasil pembagian adalah =", hasil)
except ZeroDivisionError:
    # tangani error jiia ada bilangan yang dibagi dengan nol di blok try
    print("Bilangan tidak dapat dibagi dengan nol")
except TypeError:
    # tangani error jika kedua bilangan berbeda tipe data di blok try
    print("Kedua bilangan berbeda tipe")
```

Selain itu, kita dapat menampilkan pesan kesalahan atau eksepsi bawaan _Python_ dengan menambahkan _alias_ menggunakan kata kunci `as` setelah jenis eksepsinya. Kemudian cetak pesan kesalahan dengan _alias_ tersebut menggunakan `print()`. Contoh penulisannya sebagai berikut.
```python
# Bentuk 1
try:
    hasil = 5 / "2"
    print("Hasil pembagian adalah =", hasil)
except ZeroDivisionError as err:
    print(err) # division by zero
except TypeError as err:
    print(err) # unsupported operand type(s) for /: 'int' and 'str'

# Bentuk 2
try:
    hasil = 3 / "1"
    print('Hasil pembagian adalah =', hasil)
except (ZeroDivisionError, TypeError) as err:
    # cetak pesan error tergantung jenis error yang ditangkap
    print(err)
```

## Pernyataan `finally`
`finally` merupakan pernyataan yang selalu dieksekusi apapun hasil eksekusinya baik yang menghasilkan kesalahan (eksepsi) maupun tidak. Biasanya pernyataan `finally` dapat dipasangkan dengan `try` dan `except` sehingga menjadi pola `try-finally` maupun `try-except-finally`.

Contoh kode yang menggunakan pernyataan `try-finally`:
```python
try:
    print(2 / 0)
finally:
    print("Baris ini selalu dieksekusi")
```
Output:
```python
Baris ini selalu dieksekusi
Traceback (most recent call last):
  File "finally.py", line 3, in <module>
    hasil = 2 / 0
ZeroDivisionError: division by zero
```
Karena baris kode yang ada di dalam `try` terdapat kesalahan, maka baris kode yang ada di dalam `finally` dieksekusi, kemudian munculkan kesalahannya. Sebaliknya, jika baris kode yang ada di dalam `try` tidak ada masalah, maka dieksekusi dan baris kode yang ada di dalam `finally` juga dieksekusi.

Agar kesalahan dapat ditangani terlebih dahulu, gunakan pernyataan `except`.
```python
try:
    print(3 / "2")
except TypeError as err:
    print("Kesalahan :",err)
finally:
    print("Baris ini selalu dieksekusi")
```
Output:
```
Kesalahan : unsupported operand type(s) for /: 'int' and 'str'
Baris ini selalu dieksekusi
```
Karena terdapat kesalahan di dalam `try`, maka ditangani di dalam `except`. Kemudian, baris kode yang ada di dalam `finally` juga dieksekusi.

[Materi Selanjutnya](../13_module)