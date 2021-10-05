# Operator

operator digunakan untuk melakukan operasi pada kedua variabel atau value

python memiliki beberapa jenis operator yaitu

- [operator aritmatika](operator_aritmatika.py)
- [operator penugasan](operator_penugasan.py)
- [operator komparasi](operator_perbandingan.py)
- [operator logika](operator_logika.py)
- operator identitas
- operasi member


## Operasi Aritmatika
operasi aritmatika adalah operasi yang digunakan untuk melakukan operasi matematika diantara kedua value atau kedua variabel

sebagai contoh operasi pertambahan
```python
angka = 2
angka_kedua = 3

print(angka + angka_kedua)
```
operasi tersebut menambahkan kedua variabel yang memiliki value yaitu 2 dan 3

berikut table dari operasi aritmatika

| operator | nama operator | contoh penggunaan |
|----------|---------------|-------------------|
| +        | penambahan    | a + b             |
| -        | pengurangan   | a - b             |
| *        | perkalian     | a * b             |
| /        | pembagian     | a / b             |
| **       | perpangkatan  | a ** b            |
| %        | modulus       | a % b             |
| //       | floor         | a // b            |

## Operasi Penugasan
operasi penugasan adalah operasi yang digunakan untuk menetapkan suatu bilangan ke dalam variabel

sebagai contoh operasi penugasan
```python
nilai = 5
nilai += 3

print("nilai adalah", nilai)
```
operasi tersebut menambahkan sekaligus menetapkan ke dalam variabel nilai

berikut tabel dari operasi penugasan

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


## Operasi Perbandingan
operasi perbandingan adalah operasi yang digunakan untuk membandingkan suatu nilai dengan nilai yang lain

sebagai contoh operasi perbandingan
```python
print(2 < 3)  # True
```

operasi tersebut membandingkan apakah nilai pertama lebih kecil daripada nilai kedua

berikut tabel dari operasi perbandingan
|   Operator    |                Artinya                |
|---------------|---------------------------------------|
|      ==       |              Sama Dengan              |
|      !=       |           Tidak Sama Dengan           |
|      >        |           Lebih besar dari            |
|      <        |           Lebih Kecil dari            |
|      >=       |    Lebih Besar dari atau sama dengan  |
|      <=       |    Lebih Kecil dari atau sama dengan  |

## Operasi Logika
operasi logika adalah operasi yang digunakan untuk mengecek pernyataan apakah True atau False

sebagai contoh operasi logika
```python
print(3 < 5 and 5 > 3) # True
```

operasi tersebut mengecek apakah kedua nilai yang di cek memiliki nilai True

berikut tabel dari operasi logika
|   Operator    |                         Penjelasan                                    |
|---------------|-----------------------------------------------------------------------|
|     and       | Mengembalikan nilai True jika kedua nilai memiliki nilai True         |
|     or        | Mengembalikan nilai True jika salah satu nilai memiliki nilai True    |
|     not       | Membalikkan hasil, mengembalikan False jika hasilnya True             |


## Operasi Keanggotaan
operasi keanggotaan adalah operasi yang digunakan untuk memvalidasi anggota di dalam sebuah objek

contoh operasi keanggotaan
```python
list_bahasa_pemrograman = ["javascript", "java", "Python", "Dart"]
print("Python" in list_bahasa_pemrograman)  # True
```

operasi tersebut memvalidasi apakah `"Python"` ada di dalam list `list_bahasa_pemrograman`

berikut tabel dari operasi keanggotaan
|   Operator    |                      Penjelasan                                               |
|---------------|-------------------------------------------------------------------------------|
|      in       | Mengembalikan nilai True jika nilai yang disebutkan ada di dalam objek        |
|    not in     | Mengembalikan nilai True jika nilai yang disebutkan tidak ada di dalam objek  |