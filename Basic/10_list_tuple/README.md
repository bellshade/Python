## list
list digunakan untuk menyimpan data yang banyak dengan hanya satu variable, list menggunakan square bracket atau kurung petak, contoh.
```python
nama_hewan = ["sapi", "gajah", "ayam", "bebek"]
print(nama_hewan)
```
list memiliki index, index dimulai dari 0, dan index kedua dimulai dari angka 1

kelebihan antara dari list adalah

- bisa dirubah
    list bisa dirubah dengan dengan cara
    ```python
    nama_hewan = ["sapi", "gajah", "ayam", "bebek"]
    nama_hewan[1] = "kucing"
    print(nama_hewan)
    ```
- menerima duplikasi
    list juga duplikasi item, sebagai contoh
    ```python
    nama_hewan = ["ikan", "singa", "ikan", "sapi"]
    print(nama_hewan)
    ```

## tuple
list digunakan untuk menyimpan data yang banyak dengan menggunakan satu variabel. tuple menggunakan round bracket atau kurung bulat, tuple adalah salah satu tipe data yang **tidak dapat dirubah**,contoh.
```python
nama_hewan = ("ikan", "gajah", "sapi", "paus")
print(nama_hewan)
```

buat tuple dengan hanya satu item di dalamnya, jangan lupa menggunakan koma
```python
nama_hewan = ("sapi",)
print(nama_hewan)
```

# Comprehension
Kita juga dapat membuat/membangun list atau dictionary menggunakan *comprehension*. *Comprehension* memanfaatkan *loop* untuk membangun list atau dictionary. Dengan *comprehension*, kita dapat membuat list dengan kode yang lebih ringkas.

Dalam menggunakan *comprehension*, ada 3 hal yang harus kita perhatikan, yakni :

1. Output
2. Loop
3. Condition

Ketiga hal di atas ditulis dengan notasi *comprehension* sebagai berikut :
![Desktop - 5](https://user-images.githubusercontent.com/64145699/137303996-a72bd93a-3ebb-4e00-9674-be53c41e18a8.png)
 Penjelasan diolah dari [freecodecamp](https://www.freecodecamp.org/news/list-comprehension-in-python/)

## List Comprehension
Kita dapat membangun list menggunakan *comprehension*. Kita memiliki *template* untuk list comprehension, seperti kode yang ditunjukkan di bawah :

```python 
list_comprehension = [x for x in interable]
```

Iterable di atas bisa saja elemen dari list lain, atau fungsi bawaan seperti ```range()```.

Sebagai contoh, kita ingin membuat list yang berisikan bilangan genap dari 1 sampai 10. Dengan menggunakan list comprehension, kita dapat menuliskan kode tersebut sebagai berikut : 

```python
genap = [x for x in range(11) if x % 2 == 0]
# menghasilkan [0, 2, 4, 6, 8, 10]
print(genap)

```

Kode di atas dapat kita tulis ulang menggunakan loop biasa, namun kode yang ditulis akan lebih panjang dengan kode sebagai berikut :

```python
genap = []
for x in range (11):
    if x % 2 == 0:
        genap.append(x)

# menghasilkan [0, 2, 4, 6, 8, 10]
print(genap)

```

Tidak hanya conditional menggunakan ```if```, tetapi kita juga bisa menggunakan ```if ... else``` dalam list comprehension. Kode di bawah ini menggunakan ```if ... else``` untuk menampilkan apakah nilai dalam list bernilai ganjil atau genap.

```python
ganjilGenap = ['genap' if num % 2 == 0 else 'ganjil' for num in range(5)]
# menghasilkan ['genap', 'ganjil', 'genap', 'ganjil', 'genap']
print(ganjilGenap)

```

Kita juga bisa menggunakan nested loop dalam list comprehension. Kode di bawah ini membuat matriks menggunakan list comprehension.

```python
matriks = [[i for i in range (3)] for i in range (5)]
# menghasilkan [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
print(matriks)

```

Pada kode di atas, terdapat dua buah list comprehension. List comprehension pertama ditunjukkan oleh ```[i for i in range (3)]```, sedangkan list comprehension kedua ditunjukkan oleh ```[ ... for i in range (5)]```. List comprehension pertama akan menghasilkan baris dengan elemen tiap baris adalah ```[0, 1, 2]```, dan list comprehension kedua akan menghasilkan 5 buah kolom.

## Dictionary Comprehension
Sama seperti list comprehension, kita juga dapat membangun sebuah dictionary menggunakan dictionary comprehension. Hanya saja, kita harus ingat, bahwa dictionary merupakan *key - value pair*, artinya kita mengakses elemen dictionary menggunakan *key* pada dictionary tersebut. 

Kita memiliki *template* untuk dictionary comprehension, seperti kode yang ditunjukkan di bawah :

```python 
dict_comprehension = {k:v for (k,v) in dict.items()}
```

```dict.items()``` di atas dapat kita ganti dengan iterable lain, misalnya objek yang dihasilkan dari fungsi ```range()```

Contoh di bawah ini adalah membangun dictionary pemangkatan 2 pada tiap *value* dictionary menggunakan dictionary comprehension.

```python 
awal = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
akhir = {k: v**2 for (k, v) in awal.items()}
# menghasilkan {'1': 1, '2': 4, '3': 9, '4': 16, '5': 25}
print(akhir)

```

Sama seperti list comprehension, kita juga bisa menggunakan condition dalam dictionary comprehension. Contoh di bawah ini akan menghasilkan ```ganjil``` jika *key* bernilai ganjil dan sebaliknya.

```python 
awal = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
akhir = {k: ('ganjil' if v % 2 != 0 else 'genap') for (k, v) in awal.items()}
# menghasilkan {'1': 'ganjil', '2': 'genap', '3': 'ganjil', '4': 'genap', '5': 'ganjil'}
print(akhir)

```

Kemudian, sama dengan list comprehension, kita juga bisa menggunakan dictionary comprehension di dalam dictionary comprehension, atau biasa kita sebut nested dictionary comprehension. Kode di bawah ini akan memangkatkan ```key_luar``` sebanyak ```key_dalam``` kali.

```python 
kuadrat = {
    key_luar:
        {key_dalam: key_luar ** key_dalam for key_dalam in range(1, 5)}
        for key_luar in range(2, 5)
        }
# menghasilkan {2: {1: 2, 2: 4, 3: 8, 4: 16}, 3: {1: 3, 2: 9, 3: 27, 4: 81}, 4: {1: 4, 2: 16, 3: 64, 4: 256}}
print(kuadrat)

```

Kode di atas ekuivalen dengan kode di bawah.

```python 
kuadrat = dict()
for key_luar in range(2, 5):
    kuadrat[key_luar] = {key_dalam: key_luar ** key_dalam for key_dalam in range(1,5)}

# menghasilkan {2: {1: 2, 2: 4, 3: 8, 4: 16}, 3: {1: 3, 2: 9, 3: 27, 4: 81}, 4: {1: 4, 2: 16, 3: 64, 4: 256}}
print(kuadrat)

```

[Materi Selanjutnya](../11_manipulasi_string)