# manipulasi string

pada python kita bisa merubah, dan memanipulasi string yang sudah ada agar sesuai dengan kebutuhan yang diinginkan


- mengakses salah satu karakter dari string

    ```python
    nama_saya = "zoelfikrie"
    print(nama_saya[0])
    ```

- menghitung semua karakter string

    ```python
    nama_saya = "athallamajed"
    print(len(nama_saya))
    ```

- menghitung jumlah suatu huruf dari karakter

    ```python
    nama_saya = "carl loghmatten"
    print(nama_saya.count("l"))
    ```

- menghitung jumlah spasi pada string

    ```python
    kalimat = "program belajar indonesia"
    print(kalimat.count(' '))
    ```

- memotong karakter

    ```
    kata = "indonesia programming"
    ```

    - mengambil karakter pertama dari string
        ```python
        print(kata[0])
        ```

    - mengambil 3 karakter dari string
        ```python
        priint(kata[0:3])
        ```
        ```python
        print(kata{:3})
        ```

    - mengambil 3 karakter terakhir dari string
        ```python
        print(kata[-3:])
        ```

- mengulang sebanyak dari string
    ```python
    # mengulang sebanyak 100 kali
    print("indonesia" * 100)
    ```

- mengubah kata dari string

    ```python
    kata = "belajar memasak"
    ubah = kata.replace("belajar", "pintar")
    print(ubah)
    ```

|sintaks       | penjelasan                             | contoh kode       |
|:--        | :--:                                      | :--               |
| ``uper()``| mengubah semua huruf menjadi kapital      | ``kata.upper()``  |
| ``lower()``| mengubah semua huruf menjadi kecil       | ``kata.lower()``  |
| ``title()``| mengubah setiap awalan kata kalimat menjadi kapital | ``kata.title()``|
| ``capitalize()`` | mengubah awalan huruf utama menjadi kapital | ``kata.capitalize()`` |
| ``swapcase()``| mengubah setiap awalan kata kalimat menjadi huruf kecil | ``kata.swapcase()``|

- membalikkan string

    ```python
    kata = "bellshade python"
    # cara pertama
    print(kata[::-1])
    # cara kedua
    print(' '.join(reversed(kata)))
    ```

- penggabungan string

    ```python
    kata = "memasak"
    print("saya belajar " + kata)
    ```

    - join
        menambahkan karakter di setiap karakter
        ```python
        kata = "indonesia"
        print("x".join(kata))
        ```

- pengecekan

    - ``kata.isalnum()``
        cek kata tersebut mengandung alphanumerik atau tidak

    - ``kata.isalpha()``
        cek kata tersebut mengandung alphabet

    - ``kata.isdigit()``
        cek apakah kata mengandung digit atau angka

    - ``kata.istitle()``
        cek apakah kata mengandung title atau tidak

    - ``kata.isupper()``
        cek apakah kata mengandung huruf kapital

    - ``kata.islower()``
        cek apakah kata mengandung kata huruf kecil

    - ``kata.isspace()``
        cek apakah kata mengandung spasi atau tidak

    - ``kata.endswith('karakter')``
        cek apakah kata mengandung karakter tersebut atau tidak pada akhir

    - ``kata.startswith('karakter')``
        cek apakah kata mengandung karakter terseub atau tidak pada awal

berikut tabel method pada string

| Method         | Penjelasan                                                                                    |
|----------------|-----------------------------------------------------------------------------------------------|
| capitalize()   | Mengubah karakter pertama menjadi Kapital                                                     |
| casefold()     | Mengubah string menjadi huruf kecil                                                           |
| center()       | Mengembalikan String yang ditengahkan                                                         |
| count()        | Menghitung jumlah karakter tertentu di dalam string                                           |
| encode()       | Mengembalikan string yang sudai disandi                                                       |
| endswith()     | Mengembalikan True jika string berakhir dengan karakter tertentu                              |
| expandtabs()   | Mengatur besar Tab pada String                                                                |
| find()         | Mencari karakter tertentu dan mengembalikan letak dimana karakter itu berada                  |
| format()       | mem-format karakter tertentu di dalam string                                                  |
| format_map()   | mem-format karakter tertentu di dalam string                                                  |
| index()        | Mencari karakter tertentu dan mengembalikan letak dimana karakter itu berada                  |
| isalnum()      | Mengembalikan True jika semua karakter adalah alfanumerik                                     |
| isalpha()      | Mengembalikan True jika semua karakter adalah alfabet                                         |
| isascii()      | Mengembalikan True jika semua karakter adalah karakter ascii                                  |
| isdecimal()    | Mengembalikan True jika semua karakter adalah desimal                                         |
| isdigit()      | Mengembalikan True jika semua karakter adalah angka                                           |
| isidentifier() | Mengembalikan True jika String adalah pengidentifikasi                                        |
| islower()      | Mengembalikan True jika semua karakter adalah huruf kecil                                     |
| isnumeric()    | Mengembalikan True jika semua karakter adalah numerik                                         |
| isprintable()  | Mengembalikan True jika semua karakter dapat dicetak                                          |
| isspace()      | Mengembalikan True jika semua karakter adalah spasi                                           |
| istitle()      | Mengembalikan True jika string mengikuti aturan judul                                         |
| isupper()      | Mengembalikan True jika semua karakter adalah upper case                                      |
| join()         | masuk kedalam elemen dari suatu iterable dia akhir string                                     |
| ljust()        | Mengembalikan String yang dikirikan                                                           |
| lower()        | Mengkonversi string ke huruf kecil                                                            |
| lstrip()       | Menghapus spasi di kiri pada string                                                           |
| maketrans()    | Mengembalikan tabel translasi untuk di translasikan                                           |
| partition()    | Mengembalikan Tuple dimana string dibagi menjadi tiga bagian                                  |
| replace()      | Mengemlikan String dimana karakter tertentu di ganti dengan karakter yang lain                |
| rfind()        | Mencari karakter tertentu dan mengembalikan posisi dimana karakter itu berada terakhir        |
| rindex()       | Mencari karakter tertentu dan mengembalikan posisi dimana karakter itu berada terakhir        |
| rjust()        | Mengembalikan string yang dikanankan                                                          |
| rpartition()   | Mengembalikan Tuple dimana string dibagi menjadi tiga bagian                                  |
| rsplit()       | Membagi string pada pembagi yang ditentukan, dan mengembalikan list                           |
| rstrip()       | Menghapus spasi di kanan pada string                                                          |
| split()        | Membagi string pada pembagi yang ditentukan, dan mengembalikan list                           |
| splitlines()   | Membagi string pada baris baru, dan mengembalikan list                                        |
| startswith()   | Mengembalikan True jika string dimulai dengan karakter tertentu                               |
| strip()        | Mengembalikan String yang spasinya sudah dihapus                                              |
| swapcase()     | Mengubah kapital menjadi huruf kecil dan sebaliknya                                           |
| title()        | Mengubah huruf awal di setiap kata menjadi kapital                                            |
| translate()    | Mengembalikan string yang sudah ditranslasi                                                   |
| upper()        | Mengubah string menjadi huruf Kapital                                                         |
| zfill()        | Mengisi string dengan angka 0 sebanyak jumlah yang ditentukan di awal string                  |

video penjelasan tentang manipulasi string = [Belajar python dasar - manipulasi string](https://www.youtube.com/watch?v=ORda-LwrEwE&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=18)

[Materi Selanjutnya](../12_exception)