<a href="../02_tipe_data">◀ Materi Sebelumnya</a>

<center>

# Variabel

</center>

<a id="1"><h2>Daftar Isi</h2></a>

---

- [Daftar Isi](#1)
- [Pendahuluan](#2)
- [Assign Variabel](#3)
- [Penamaan Variabel](#4)
- [Penggunaan Built-in Keyword](#5)
- [Video Penjelasan Tentang Variabel](#6)
- [Praktikum](#7)

<a id="2"><h2>Pendahuluan</h2></a>

---

**Variabel adalah referensi dari sebuah value.** Variabel sering di analogikan seperti **sebuah wadah yang menampung sebuah benda.** Seperti kita ketika ingin menyimpan suatu benda, maka perlu mencari tempat / wadah benda tersebut ingin disimpan terlebih dahulu. Dalam menentukan wadah, kita hanya perlu mencantumkan nama wadah (nama variabel) terlebih dahulu. Setelah itu, python akan secara otomatis mengambilkan wadah sesuai dengan kebutuhan kita. Contoh penggunaan variabel pada Python :

```python
angka_saya = 100
print(angka_saya)

# outputnya
# 100
```

Pada kode diatas, kita membuat sebuah variabel yang mereferensikan nilai angka `100`. Dengan penggunaan dari variabel kita bisa memanggil lebih dari sekali, misalnya:

```python
angka_saya = 20
print(angka_saya)
print(angka_saya)

# outputnya
# 20
# 20
```

<a id="3"><h2>Assign Variabel</h2></a>

---

Kita bisa assign variable dengan variabel lainnya agar mudah untuk mendeklarasikan sebuah nilai yang sama dengan variabel yang berbeda, sebagai contoh:

```python
angka_saya = 200
angka_lain = angka_saya
print(angka_saya)
print(angka_lain)

# outputnya
# 200
# 200
```

Atau bisa juga dengan cara:

```python
angka_saya = angka_lain = angka_banyak = 200
print(angka_saya)
print(angka_lain)
print(angka_banyak)

# outputnya
# 200
# 200
# 200
```

Contoh pada string:

```python
nama = nama_alias = "adams"
print(nama)
print(nama_alias)

# outputnya
# adams
# adams
```

<a id="4"><h2>Penamaan Variabel</h2></a>

---

Python memiliki beberapa peraturan dalam penulisan sebuah variabel. Jika kamu ingin melihat detail aturan tersebut bisa kunjungi laman [PEP8](https://peps.python.org/pep-0008/#type-variable-names) ini. Peraturan tersebut adalah:

1. Menggunakan kata tanpa didahuli dengan angka:

   **contoh benar** ✅

   ```python
   nama = "bob"
   ```

   **contoh salah** ❌

   ```python
   1nama = "bob"
   ```

2. Menggunakan underscore (garis bawah) jika ingin menggunakan kata yang panjang:

   **contoh yang benar** ✅

   ```python
   angka_saya = 12
   ```

   **contoh yang salah** ❌

   ```python
   12angka_saya = 12
   ```

3. Variabel pada python bersifat sensitif, penggunaan huruf besar dan kecil sangat diperhatikan:

   contoh

   ```python
   Nama_saya = "james"
   nama_saya = "joko"
   print(Nama_saya)
   print(nama_saya)

   # outputnya
   # james
   # joko
   ```

   contoh diatas akan menghasilkan 2 nama karena variabel tersebut secara kalimat sama tapi secara penulisan berbeda, Python memperhatikan hal ini.

Pada Python, penggunaan variabel disarankan menggunakan `snake_case`.

<a id="5"><h2>Penggunaan Built-in Keyword</h2></a>

---

**Built-in keyword** pada Python adalah kata-kata yang mana sudah ditetapkan/dibuat sebelumnya oleh Python. Keyword-keyword tersebut dibuat untuk melakukan suatu perintah tertentu. Maka dari itu, dalam membuat variabel kita harus menghindari kata-kata tersebut agar program kita tidak terjadi error. Ada beberapa kata yang dilarang untuk digunakan sebagai nama variabel. Contoh penggunaan kata yang dilarang pada Python:

```python
class sma_saya = "bahasa"
print(sma_saya)
```

Hasil esekusi diatas akan menyebabkan error karena `class` merupakan salah satu nama fungsi dari Python.

Kata/keywords yang dilarang:

- False
- None
- True
- and
- as
- assert
- break
- class
- continue
- def
- del
- elif
- else
- except
- finally
- for
- from
- global
- if
- import
- in
- is
- lambda
- nonlocal
- not
- or
- pass
- raise
- try
- return
- while
- with
- yield

<a id="6"><h2>Video Penjelasan Tentang Variabel</h2></a>

---

<center>

[![sdfssadasd](https://img.youtube.com/vi/gxmTFXfrMzk/0.jpg)](https://youtu.be/gxmTFXfrMzk?list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY)

</center>

<a id="7"><h2>Praktikum</h2></a>

---

Klik link ini untuk mencoba kode python dari pembahasan kali ini. [Source code](../03_variable/variable.py)

<a href="../04_operator">Materi Selanjutnya ▶</a>
