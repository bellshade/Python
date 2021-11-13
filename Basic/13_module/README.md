# Module (Modul)
_Module_ adalah sebuah _file_ yang berekstensi `.py` yang berisi kumpulan fungsi, _class_ maupun variabel. Keguanaan dari _module_ adalah untuk memecah kode bagian besar menjadi bagian-bagian kecil ke dalam _file_ yang terpisah berekstensi `.py` agar mudah dikelola. _Module_ bersifat _reusable_ yang artinya dapat digunakan secara berulang dimanapun sesuai dengan kebutuhan.

## Mendefinisikan modul
Misalkan, terdapat kumpulan fungsi untuk melakukan perhitungan operasi aritmatika sederhana di dalam sebuah _file_ baru, misalkan `kalkulator.py`

```python
def tambah(angka1, angka2):
    return angka1 + angka2


def kurang(angka1, angka2):
    return angka1 - angka2


def kali(angka1, angka2):
    return angka1 * angka2


def bagi(angka1, angka2):
    return angka1 / angka2

```

## Melakukan _import_ modul
_File_ `kalkulator.py` yang sudah dibuat sebelumnya dapat digunakan pada _file_ yang lain. Buat _file_ baru yang namanya `perhitungan1.py`, dimana akan dilakukan _import file_ `kalkulator.py` menggunakan kata kunci `import` di awal baris kode yang diikuti dengan nama module, yaitu _file python_ tanpa eksetensi `.py` yang ingin dipanggil. Bentuk penulisannya adalah sebagai berikut

```python
import kalkulator
```

Saat modul `kalkulator` telah di-_import_, maka fungsi-fungsi di dalam modul tersebut dapat diakses menggunakan notasi titik. Sebagai contoh, jika ingin mengakses fungsi `tambah`, maka penulisannya menjadi `kalkulator.tambah(2, 3)`. Begitu pula jika ingin mengakses fungsi-fungsi yang lainnya, maka pemanggilan fungsinya sebagai berikut.

```python
print(kalkulator.tambah(2, 3))
print(kalkulator.kurang(2, 3))
print(kalkulator.kali(2, 3))
print(kalkulator.bagi(10, 2))
```

Output:
```
5
2
18
5.0
```

Selain menggunakan kata kunci `import`, pemanggilan modul dapat dilakukan dengan menggunakan pola `from ... import ...`, dimana kata kunci `from` diikuti dengan nama modul (_file python_) yang ingin dipanggil dan dilanjutkan dengan kata kunci `import` yang diikuti dengan nama _class_, fungsi dan variabel yang ingin digunakan secara spesifik pada modul tersebut. Sebagai contoh, buat _file_ baru yang namanya `perhitungan2.py`. Di dalam _file_ tersebut, dilakukan pemanggilan _file_ `kalkulator.py` beserta fungsi di dalamnya yang akan digunakan. Penulisan di awal baris kode adalah sebagai berikut.

```python
from kalkulator import tambah, kurang, kali, bagi
```

Penggunaan fungsi yang telah di-_import_ tanpa menggunakan notasi titik, sehingga menjadi sebagai berikut
```python
print(tambah(2, 3))
print(kurang(2, 3))
print(kali(2, 3))
print(bagi(10, 2))
```

Output:
```
5
2
18
5.0
```
[Materi Selanjutnya](../14_python_datetime)