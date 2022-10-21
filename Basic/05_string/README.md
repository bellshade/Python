<a href="../04_operator">[Operator] ◀ Materi Sebelumnya</a>

<center>

# String

</center>

<a id="1"><h2>Daftar Isi</h2></a>

---

- [Daftar Isi](#1)
- [Pendahuluan](#2)
- [Deklarasi Variabel String](#3)
- [Deklarasi Variabel Multistring](#4)
- [Mencetak String](#5)
- [Method String Bawaan](#6)
  - [`upper()`](#7)
  - [`lower()`](#8)
  - [Substring String](#9)
  - [`len()`](#10)
  - [`in` Keyword](#11)
- [Video Penjelasan Tentang String](#12)
- [Praktikum](#13)

<a id="2"><h2>Pendahuluan</h2></a>

---

Seperti yang dijelaskan pada materi sebelumnya [(tipe data)](../02_tipe_data/), string adalah salah satu tipe data pada Python yang berfungsi untuk menyimpan huruf abjad atau simbol lain. Penggunaan string sangat diperlukan ketika kita ingin menyimpan data seperti alamat, nama dll. Seperti pada materi sebelumnya di [tipe data](../02_tipe_data/), pendeklarasian variabel dengan tipe data string dapat dilakukan dengan cara seperti berikut :

<a id="3"><h2>Deklarasi Variabel String</h2></a>

---

```python
kata_pertama = "warung"
# String juga dapat ditulis menggunakan petik satu
# Namun hal tersebut TIDAK DISARANKAN
```

<a id="4"><h2>Deklarasi Variabel Multistring</h2></a>

---

String juga dapat dideklarasikan dengan cara berikut:

```python
kata_saya = """Indonesia adalah negara yang indah
berada di bawah garis khatulistiwa
aku cinta Indonesia
"""
```

<a id="5"><h2>Mencetak String</h2></a>

---

```python
print(kata_saya)

# outputnya
# Indonesia adalah negara yang indah
# berada di bawah garis khatulistiwa
# aku cinta Indonesia
```

<a id="6"><h2>Method String Bawaan</h2></a>

---

**Dalam membuat program, manipulasi string sangat diperlukan karena tidak semua nilai string yang kita dapatkan sesuai dengan yang kita inginkan.** Maka dari itu dibutuhkan sebuah tindakan untuk mengubah atau memanipulasi string tersebut. Dalam Python, terdapat beberapa method bawaan (built-in method) yang bisa kita gunakan untuk memanipulasi string antara lain seperti berikut :

<a id="7"><h3>`upper()`</h3></a>

---

Method ini digunakan untuk mengkapitalisasi setiap karakter pada string.

```python
print(kata_pertama.upper())

# outputnya
# WARUNG
```

<a id="8"><h3>`lower()`</h3></a>

---

Method ini digunakan untuk membuat setiap karakter pada string menjadi huruf kecil

```python
print(kata_pertama.upper().lower())

# outputnya
# WARUNG -> warung
```

<a id="9"><h3>Substring String</h3></a>

---

Dalam Python, string bisa dianggap seperti kumpulan (list) dari beberapa karakter. Maka dari itu, kita dapat mengambil salah satu karakter dari string berdasarkan urutan index paling kiri.

```python
print(kata_pertama[0])

# outputnya
# w
```

<a id="10"><h3>`len()`</h3></a>

---

Method ini digunakan untuk menghitung jumlah karatker dari string

```python
print(len(kata_pertama))

# outputnya
# 6
```

<a id="11"><h3>`in` Keyword</h3></a>

---

`in` merupakan salah satu keyword dalam Python yang digunakan utnuk mengecek kata khusus dalam sebuah string

```python
print("Indonesia" in kata_saya)
print("Indonesia" in "one")

# outputnya
# False
# True
# Perlu diperhatikan penggunaan keyword `in` harus
# memperhatikan besar kecil huruf (case sensitive)
```

Jika kamu ingin mempelajari mengenai method-method string apa saja yang dapat kita gunakan. Anda dapat langsung melihat pada materi [manipulasi string](../11_manipulasi_string/)

<a id="12"><h2>Video Penjelasan Tentang String</h2></a>

---

[![sdfssadasd](https://img.youtube.com/vi/fhAEh1Z9YuY/0.jpg)](https://www.youtube.com/watch?v=fhAEh1Z9YuY&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=16)

<a id="13"><h2>Praktikum</h2></a>

---

Klik link dibawah untuk mencoba kode python dari pembahasan kali ini. [Source code](../05_string/string_python.py)

<a href="../06_input_output">Materi Selanjutnya ▶ [Input Output]</a>
