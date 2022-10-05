<a href="../03_variable">◀ Materi Sebelumnya</a>

<center>

# Operator

</center>

<a id="1"><h2>Daftar Isi</h2></a>

---

- [Daftar Isi](#1)
- [Pendahuluan](#2)
- [Operator Aritmatika](#3)
- [Operator Penugasan](#4)
- [Operator Perbandingan](#5)
- [Operator Logika](#6)
- [Operator Keanggotaan](#7)
- [Operator Identitas](#8)
- [Operator Bitwise](#9)
- [Video Penjelasan Tentang Variabel](#10)
- [Praktikum](#11)

<a id="2"><h2>Pendahuluan</h2></a>

---

**Operator digunakan untuk melakukan operasi pada variabel atau value.** Dengan operator kita dapat memanipulasi nilai dari operan berdasarkan operator yang kita masukkan seperti `2+3` yang mana angka `2` dan `3` merupakan `operand` dan `+` merupakan `operator` untuk fungsi penjumlahan.

Python memiliki beberapa jenis operator yaitu:

- [Operator Aritmatika](#3)
- [Operator Penugasan](#4)
- [Operator Perbandingan](#5)
- [Operator Logika](#6)
- [Operator Keanggotaan](#7)
- [Operator Identitas](#8)
- [Operator Bitwise](#9)

<a id="3"><h2>Operator Aritmatika</h2></a>

---

Operator aritmatika adalah operator yang digunakan untuk melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, pembagian di antara value atau variabel.

Sebagai contoh operasi pertambahan:

```python
angka = 2
angka_kedua = 3

print(angka + angka_kedua)

# outputnya
# 5
```

Operasi tersebut menambahkan kedua variabel yang memiliki value yaitu 2 dan 3.

Berikut table dari operator aritmatika:

| operator | nama operator | contoh penggunaan |
| -------- | ------------- | ----------------- |
| +        | penambahan    | a + b             |
| -        | pengurangan   | a - b             |
| \*       | perkalian     | a \* b            |
| /        | pembagian     | a / b             |
| \* \*    | perpangkatan  | a \*\* b          |
| %        | modulus       | a % b             |
| //       | floor         | a // b            |

```py
print(6+2)      # 8
print(6-2)      # 4
print(6*2)      # 12
print(6/2)      # 3.0
print(6**2)     # 36
print(5%2)      # 1
print(10//3)    # 3
```

<a id="4"><h2>Operator Penugasan</h2></a>

---

Operator penugasan adalah operator yang digunakan untuk menetapkan suatu bilangan ke dalam variabel.

Sebagai contoh operasi penugasan:

```python
nilai = 5
nilai += 3
# operator tersebut sama dengan
# nilai = nilai + 3

print("nilai adalah", nilai)    #8
```

Operasi tersebut menambahkan sekaligus menetapkan ke dalam variabel nilai.

Berikut tabel dari operasi penugasan:

| Operator | Example     | Sama Dengan    | Hasil (jika x=5) |
| -------- | ----------- | -------------- | :--------------: |
| =        | x = 5       | x = 5          |        44        |
| +=       | x += 3      | x = x + 3      |        8         |
| -=       | x -= 3      | x = x - 3      |        2         |
| \*=      | x \*= 3     | x = x \* 3     |        15        |
| /=       | x /= 3      | x = x / 3      |       1.67       |
| %=       | x %= 3      | x = x % 3      |        2         |
| //=      | x //= 3     | x = x // 3     |        1         |
| \*\*=    | x \*\*= 3   | x = x \*\* 3   |       125        |
| &=       | x &= 3      | x = x & 3      |        1         |
| &#124;=  | x &#124;= 3 | x = x &#124; 3 |        7         |
| ^=       | x ^= 3      | x = x ^ 3      |        6         |
| <<=      | x <<= 3     | x = x << 3     |        40        |
| >>=      | x >>= 3     | x = x >> 3     |        0         |

<a id="5"><h2>Operator Perbandingan</h2></a>

---

Operator perbandingan adalah operator yang digunakan untuk membandingkan suatu nilai dengan nilai yang lain.

Sebagai contoh operasi perbandingan:

```python
print(2 < 3)  # True
```

Operasi tersebut membandingkan apakah nilai pertama lebih kecil daripada nilai kedua.

Berikut tabel dari operasi perbandingan:

| Operator | Artinya                           |
| -------- | --------------------------------- |
| ==       | Sama Dengan                       |
| !=       | Tidak Sama Dengan                 |
| >        | Lebih besar dari                  |
| <        | Lebih Kecil dari                  |
| >=       | Lebih Besar dari atau sama dengan |
| <=       | Lebih Kecil dari atau sama dengan |

```py
print(2 < 3)    # True
print(2 > 3)    # False
print(2 <= 3)   # True
print(2 >= 3)   # False
print(2 == 3)   # False
print(2 != 3)   # True
```

<a id="6"><h2>Operator Logika</h2></a>

---

Operator logika adalah operator yang digunakan untuk mengecek apakah sebuah penyataan bernilai True atau False.

Sebagai contoh operasi logika:

```python
print(3 < 5 and 5 > 3) # True
```

Operasi tersebut mengecek apakah kedua nilai yang dicek memiliki nilai True.

Berikut tabel dari operasi logika:

| Operator | Penjelasan                                                         |
| -------- | ------------------------------------------------------------------ |
| and      | Mengembalikan nilai True jika kedua nilai memiliki nilai True      |
| or       | Mengembalikan nilai True jika salah satu nilai memiliki nilai True |
| not      | Membalikkan hasil, mengembalikan False jika hasilnya True          |

```py
print(True and True)        # True
print(True and False)       # False
print(False and False)      # False
print(True or True)         # True
print(True or False)        # True
print(False or False)       # False
print((True and not True))  # False
print(True or not False)    # True
print(False and not False)  # False
```

<a id="7"><h2>Operator Keanggotaan</h2></a>

---

Operator keanggotaan adalah operator yang digunakan untuk memvalidasi anggota di dalam sebuah kumpulan data.

Contoh operasi keanggotaan:

```python
list_bahasa_pemrograman = ["javascript", "java", "Python", "Dart"]
print("Python" in list_bahasa_pemrograman)  # True
print("Indonesia" in list_bahasa_pemrograman)  # False
```

Operasi tersebut memvalidasi apakah `"Python"` ada di dalam list `list_bahasa_pemrograman`.

Berikut tabel dari operasi keanggotaan:

| Operator | Penjelasan                                                                   |
| -------- | ---------------------------------------------------------------------------- |
| in       | Mengembalikan nilai True jika nilai yang disebutkan ada di dalam objek       |
| not in   | Mengembalikan nilai True jika nilai yang disebutkan tidak ada di dalam objek |

<a id="8"><h2>Operator Identitas</h2></a>

---

Operator identitas adalah operator yang digunakan untuk membandingkan suatu data. Jika data bernilai sama dan memiliki memori yang sama, maka akan mengembalikan nilai True.

Contoh dari operasi identitas:

`contoh 1`

```python
x = 3
y = 7

print(x is y)       # False
print(x is not y)   # True
```

Hasil:

```
>> Tidak sama
```

Karena nilai dari variabel `x` dan `y` tidak memilki nilai dan memori yang sama.

`contoh 2`

```python
if (type(y) != int):
    print("Ini bukan integer")
else:
    print("Ini adalah integer")
```

Hasil:

```
>> Ini adalah integer
```

Karena tipe data yang digunakan pada variabel `y` adalah `integer`, bukan string ataupun tipe data lainnya.

Berikut tabel dari operasi identitas:

| Operator | Penjelasan                                                                                    |
| -------- | --------------------------------------------------------------------------------------------- |
| is       | Mengembalikan nilai True jika nilai yang disebutkan memiliki objek dan memori yang sama       |
| is not   | Mengembalikan nilai True jika nilai yang disebutkan tidak memiliki objek dan memori yang sama |

<a id="9"><h2>Operator Bitwise</h2></a>

---

Operator bitwise digunakan untuk melakukan operasi bilangan biner. Bilangan bulat pertama diubah menjadi biner dan kemudian operasi dilakukan pada bit demi bit, maka nama operator bitwise. Kemudian hasilnya dikembalikan dalam format desimal.

Contoh dari **bitwise not operator**:

```python
angka_saya = 10
print(~a)
```

Hasilnya:

```bash
-11
```

Penjelasannya sebagai berikut:

```
angka_saya = 10 = 1010
~a = ~1010
    = -(1010 + 1)
    = -(1011)
    = -11
```

Contoh dari **bitwise right**:

```python
angkat_saya = 10
print(angka_saya >> 1)
```

Hasilnya:

```bash
5
```

```
angka_saya = 10 = 0000 1010
a >> 1 = 0000 0101 = 5
```

Berikut tabel dari operasi identitas:

| operator | deskripsi           | sintaks |
| :------- | ------------------- | ------: |
| &        | Bitwise AND         |   x & y |
| \|       | Bitwise OR          |  x \| y |
| ~        | Bitwise NOT         |      ~x |
| ^        | Bitwise XOR         |   x ^ y |
| >>       | Bitwise right shift |     x>> |
| <<       | Bitwise left shift  |     x<< |

<a id="10"><h2>Video Penjelasan Tentang Variabel</h2></a>

---

- Operator Aritmatika
  [![sdfssadasd](https://img.youtube.com/vi/RoDGGTWbKK4/0.jpg)](https://youtu.be/RoDGGTWbKK4?list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY)
- Operator Penugasan
  [![sdfssadasd](https://img.youtube.com/vi/49KDyhzgCmA/0.jpg)](https://www.youtube.com/watch?v=49KDyhzgCmA&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=15)
- Operator Perbandingan
  [![sdfssadasd](https://img.youtube.com/vi/Kv_lDWq8kCc/0.jpg)](https://www.youtube.com/watch?v=Kv_lDWq8kCc&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=11)
- Operator Logika
  [![sdfssadasd](https://img.youtube.com/vi/Sl7zqPpC2VI/0.jpg)](https://www.youtube.com/watch?v=Sl7zqPpC2VI&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=12)
- Operator Bitwise
  [![sdfssadasd](https://img.youtube.com/vi/-VrqfCGwr88/0.jpg)](https://www.youtube.com/watch?v=-VrqfCGwr88&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=14)

<a id="11"><h2>Praktikum</h2></a>

---

Klik link dibawah untuk mencoba kode python dari pembahasan kali ini.

- [Operator Aritmatika](operator_aritmatika.py)
- [Operator Penugasan](operator_penugasan.py)
- [Operator Komparasi](operator_perbandingan.py)
- [Operator Logika](operator_logika.py)
- [Operator Identitas](operator_identitas.py)
- [Operator Bitwise](operator_bitwise.py)
- [Operator Keanggotaan](operator_keanggotaan.py)

<a href="../05_string">Materi Selanjutnya ▶</a>
