# Operator

Operator digunakan untuk melakukan operasi pada variabel atau value.

Python memiliki beberapa jenis operator yaitu:
- [operator aritmatika](operator_aritmatika.py)
- [operator penugasan](operator_penugasan.py)
- [operator komparasi](operator_perbandingan.py)
- [operator logika](operator_logika.py)
- [operator identitas](operator_identitas.py)
- operasi member


## Operator Aritmatika
Operator aritmatika adalah operator yang digunakan untuk melakukan operasi matematika diantara value atau variabel.

Sebagai contoh operasi pertambahan:

```python
angka = 2
angka_kedua = 3

print(angka + angka_kedua)
```

Operasi tersebut menambahkan kedua variabel yang memiliki value yaitu 2 dan 3.

Berikut table dari operator aritmatika:

| operator | nama operator | contoh penggunaan |
|----------|---------------|-------------------|
| +        | penambahan    | a + b             |
| -        | pengurangan   | a - b             |
| *        | perkalian     | a * b             |
| /        | pembagian     | a / b             |
| **       | perpangkatan  | a ** b            |
| %        | modulus       | a % b             |
| //       | floor         | a // b            |


## Operator Penugasan
Operator penugasan adalah opertor yang digunakan untuk menetapkan suatu bilangan ke dalam variabel.

Sebagai contoh operasi penugasan:

```python
nilai = 5
nilai += 3

print("nilai adalah", nilai)
```

Operasi tersebut menambahkan sekaligus menetapkan ke dalam variabel nilai.

Berikut tabel dari operasi penugasan:

|   Operator    |   Example     |  Sama Dengan  |
|---------------|---------------|---------------|
|     =         |   x = 5       |   x = 5       |
|     +=        |   x += 3      |   x = x + 3   |
|     -=        |   x -= 3      |   x = x - 3   |
|     *=        |   x *= 3      |   x = x * 3   |
|     /=        |   x /= 3      |   x = x / 3   |
|     %=        |   x %= 3      |   x = x % 3   |
|     //=       |   x //= 3     |   x = x // 3  |
|     **=       |   x **= 3     |   x = x ** 3  |
|     &=        |   x &= 3      |   x = x & 3   |
|     &#124;=        |   x &#124;= 3      |   x = x &#124; 3   |
|     ^=        |   x ^= 3      |   x = x ^ 3   |
|     <<=       |   x <<= 3     |   x = x << 3  |
|     >>=       |   x >>= 3     |   x = x >> 3  |


## Operator Perbandingan
Operator perbandingan adalah operator yang digunakan untuk membandingkan suatu nilai dengan nilai yang lain.

Sebagai contoh operasi perbandingan:

```python
print(2 < 3)  # True
```

Operasi tersebut membandingkan apakah nilai pertama lebih kecil daripada nilai kedua.

Berikut tabel dari operasi perbandingan:

|   Operator    |                Artinya                |
|---------------|---------------------------------------|
|      ==       |              Sama Dengan              |
|      !=       |           Tidak Sama Dengan           |
|      >        |           Lebih besar dari            |
|      <        |           Lebih Kecil dari            |
|      >=       |    Lebih Besar dari atau sama dengan  |
|      <=       |    Lebih Kecil dari atau sama dengan  |

## Operator Logika
Operator logika adalah operator yang digunakan untuk mengecek apakah sebuah penyataan bernilai True atau False.

Sebagai contoh operasi logika:

```python
print(3 < 5 and 5 > 3) # True
```

Operasi tersebut mengecek apakah kedua nilai yang di cek memiliki nilai True.

Berikut tabel dari operasi logika:

|   Operator    |                         Penjelasan                                    |
|---------------|-----------------------------------------------------------------------|
|     and       | Mengembalikan nilai True jika kedua nilai memiliki nilai True         |
|     or        | Mengembalikan nilai True jika salah satu nilai memiliki nilai True    |
|     not       | Membalikkan hasil, mengembalikan False jika hasilnya True             |


## Operator Keanggotaan
Operator keanggotaan adalah operator yang digunakan untuk memvalidasi anggota di dalam sebuah kumpulan data.

Contoh operasi keanggotaan:

```python
list_bahasa_pemrograman = ["javascript", "java", "Python", "Dart"]
print("Python" in list_bahasa_pemrograman)  # True
```

Operasi tersebut memvalidasi apakah `"Python"` ada di dalam list `list_bahasa_pemrograman`.

Berikut tabel dari operasi keanggotaan:

|   Operator    |                      Penjelasan                                               |
|---------------|-------------------------------------------------------------------------------|
|      in       | Mengembalikan nilai True jika nilai yang disebutkan ada di dalam objek        |
|    not in     | Mengembalikan nilai True jika nilai yang disebutkan tidak ada di dalam objek  |


## Operator Identitas
Operator identitas adalah operator yang digunakan untuk membandingkan suatu data. Jika data bernilai sama dan memilii memori yang sama, maka akan mengembalikan nilai True.

Contoh dari operasi identitas:

`contoh 1`
```python
x = 3
y = 7

if x is y:
    print("Sama")
elif x is not y:
    print("Tidak sama")
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

|   Operator    |                      Penjelasan                                               |
|---------------|-------------------------------------------------------------------------------|
|      is       | Mengembalikan nilai True jika nilai yang disebutkan memiliki objek dan memori yang sama        |
|    is not     | Mengembalikan nilai True jika nilai yang disebutkan tidak memiliki objek dan memori yang sama  |git


## Operator bitwise

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

| operator |      deskripsi      | sintaks |
|:--       |---------------------| --:     |
|&        | Bitwise AND         | x & y   |
|\|       | Bitwise OR          | x | y   |
|~        | Bitwise NOT         | ~x      |
|^        | Bitwise XOR         | x ^ y   |
|>>       | Bitwise right shift | x>>     |
|<<       | Bitwise left shift  | x<<     |


Teman-teman bisa mempelajari lebih lanjut tentang operator di link berikut:
1. [Operator Aritmatika](https://www.youtube.com/watch?v=gxmTFXfrMzk&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=5)
2. [Operator Perbandingan](https://www.youtube.com/watch?v=Kv_lDWq8kCc&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=11)
3. [Operator Logika](https://www.youtube.com/watch?v=Sl7zqPpC2VI&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=12)
4. [Operator Bitwise](https://www.youtube.com/watch?v=-VrqfCGwr88&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=14)

[Materi Selanjutnya](../05_string)