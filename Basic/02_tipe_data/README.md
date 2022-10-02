<a href="../01_introduction">◀ Materi Sebelumnya</a>

## Tipe Data

<a id="1"><h3>Daftar Isi</h3></a>

- Tipe Data
  - [Daftar Isi](#1)
  - [Pendahuluan](#2)
  - [String | `str`](#3)
  - [Integer | `int`](#4)
  - [Float | `float`](#5)
  - [Complex | `complex`](#6)
  - [List | `list`](#7)
  - [Tuple | `tuple`](#8)
  - [Set | `set`](#9)
  - [FrozenSet | `frozenset`](#10)
  - [Dictionary | `dict`](#11)
  - [Bytes | `bytes`](#12)
  - [ByteArray | `bytearray`](#13)
  - [MemoryView | `memoryview`](#14)
- [Video penjelasan tentang tipe data](#15)
- [Praktikum](#16)

<a id="2"><h3>Pendahuluan</h3></a>

Tipe data adalah klasifikasi data. Tipe data menentukan jenis sebuah variabel.
**Variabel sendiri adalah sebuah wadah untuk menyimpan data.** Dalam penulisannya, python menganut paham `dynamic typing` yang mana dalam membuat variabel kita tidak harus menuliskan tipe datanya pula. Hal tersebut sejalan dengan tujuan python dikembangkan untuk memudahkan keterbacaan kode dan memprioritaskan pengembangan konsep dalam lebih sedikit baris kode

Beberapa tipe data dalam Python:

- Berupa text

  - <a id="3">`str`</a>

    Merupakan salah satu tipe data yang berupa string, berfungsi untuk menghasilkan tipe data string seperti huruf abjad atau simbol lain.

    ```python
    nama_saya = "franklin"
    email_saya = "benjamin@franklin"
    ```

- Berupa angka

  - <a id="4">`int`</a>

    Merupakan salah satu tipe numerik yang sering dipakai dalam pemograman berupa bilangan bulat.

    ```python
    angka_saya = 25
    tahun_lahir = 1945
    ```

  - <a id="5">`float`</a>

    Merupakan salah satu tipe numerik yang menghasilkan berupa bilangan pecahan, sangat berguna dalam menghasilkan nilai secara detail.

    ```python
    nilai_saya = 95.281724
    nilai_teman = 30.25912
    ```

  - <a id="6">`complex`</a>

    Merupakan salah satu tipe data numerik yang berfungsi menghasil sebuah angka complex, contoh angka complex bisa dilihat [di sini](https://id.wikipedia.org/wiki/Bilangan_kompleks).

    ```python
    angka_kompleks_saya = complex(1.5)
    angka_teman_saya = complex(2j)
    ```

- Berupa urutan (sekuensial)

  - <a id="7">`list`</a>

    Tipe data list adalah tipe data koleksi yang berisi beberapa value yang terdapat dalam satu variabel. List menggunakan kurung kotak `[ ]`.

    ```python
    nama_siswa = ['woody', 'buzz', 'andy']
    nilai_siswa = [12, 13, 14]
    ```

  - <a id="8">`tuple`</a>

    Tipe data tuple adalah tipe data koleksi yang berisi beberap value yang terdapat dalam satu variabel. Perbedaan di antara keduanya adalah:

    - tipe data tuple jika diberi value, maka tipe data tersebut tidak dapat diubah kembali.
    - tipe data tuple menggunakan tutup kurung biasa `()`.

    ```python
    nama_siswa = ('buzz', 'andy', 'woody')
    nilai = (12, 13, 14)
    ```

  - <a id="9">`set`</a>

    Tipe data set adalah tipe data koleksi yang elemennya dapat dirubah, tidak terurut, dan bersifat unik. Sesuai dengan namanya, tipe data set memiliki operasi matematika himpunan seperti gabungan, irisan, selisih, dan lain-lain. Set menggunakan kurung kurawal `{}`.

    ```python
    nama_siswa = {'buzz', 'andy', 'woody'}
    nilai = {12, 13, 14}
    ```

  - <a id="10">`frozenset`</a>

    Tipe data frozenset adalah tipe data koleksi yang mirip dengan set, yang membedakannya dengan set adalah elemen pada frozenset tidak dapat dirubah setelah frozenset dibuat.

    ```python
    nama_siswa = frozenset(['woody', 'buzz', 'andy'])
    nilai = frozenset([12, 13, 14])
    ```

- Berupa map (kata kunci, dictionary)

  - <a id="11">`dict`</a>

    Tipe data dict atau dictionary adalah tipe data array dimana kunci atau **key** dari array bisa berbentuk string dan angka.

    ```python
    hari = {
        "sen": "senin",
        "sel": "selasa",
        "rab": "rabu"
    }
    ```

- Berupa tipe data binary (bytes, bytearray, memmoryview)

  - <a id="12">`bytes`</a>

    Merupakan sebuah object tipe data yang berisikan array tunggal.

    ```python
    angka_saya = bytes(12)
    angka_saya1 = bytes(300)
    ```

  - <a id="13">`bytearray`</a>

    Merupakan seubah object tipe data yang berisikan array byte tunggal yang tidak dapat dirubah.

    ```python
    angka_saya = bytearray(12)
    ```

  - <a id="14">`memoryview`</a>

    Memmoryview adalah cara aman untuk mengekspos protokol buffer dengan python. Ini memungkinkan untuk mengakses buffer internal suatu objek dengan membuat objek tampilan. Memmoryview mengambalikan fungsi tampilan memori daripada objek yang diberikan.

    ```python
    angka_saya = memoryview(bytes(12))
    angka_saya1 = memoryview(bytes(1212))
    ```

<a id="15"><h3>Video penjelasan tentang tipe data</h3></a>

<center>

[![sdfssadasd](https://img.youtube.com/vi/b3X0CH98Y9g/0.jpg)](https://youtu.be/b3X0CH98Y9g?list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY)

</center>

<a id="16"><h3>Praktikum</h3></a>

Klik link ini untuk mencoba kode python dari pembahasan kali ini. [Source code](../02_tipe_data/tipe_data.py)

<a href="../03_variable">Materi Selanjutnya ▶</a>
