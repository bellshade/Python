# polimorfisme

kata polimofisme berarti memiliki banyak bentik. dalam pemograman, polimorfisme berarti nama fungsi yang sama (tetapi tanda tangan yangb berbeda) digunakan untuk jenis yang berbeda

## polimorfisme sebagai operator penjumlahan

kita tahu bahwa ``+`` operator digunakan secara luas dalam program python. tapu tidak memiliki penggunaan tunggal.untuk tipe data integer, ``+`` operator digunakan untuk melakukan operasi penjumlahan aritmatika
```python
angka1 = 12
angka3 = 200
print(angka1 + angka2)
```
demikian pula untuk tipe data string, ``+`` operator digunkana untuk melakukan penggabungan
```python
pesan1 = "python"
pesan2 = "bellshade"
print(pesan1+" "+pesan2)
```
ini adalah salah satu dari polimorfimse yang paling sederhana pada python

## fungsi polimorfisme di python

ada beberapa fungsi dalam python yang kompatibel untuk dijalankan dengan beberapa tipe data

salah satu fungsi tersebut adalah ``len()``, salah satu fungsi yang bisa berjalan di banyak tipe data.
```python
print(len("bellshade python"))
print(len(["python", "programming", "indonesia"]))
print(len({"nama": "anne", "negara": "russia"}))
```
disini kita dapat melihat bahwa banyak tipe data seperti ``string``, ``list``, ``tuple``, ``set`` dan ``dictionary`` bekerja dengan fungsi ``len()``. namun, kita dapat melihat bahwa itu mengembalikan informasi spesifik tentang tipe data tertentu.

## kelas polimorfisme dengan python

kita dapat menggunakan konsep polimorfisme saat membuat metode kelas karena python memungknkan kelas yang berbeda memiliki metode dengan nama yang sama. kemudian kita dapat menggeneralisasi pemanggilan metode ini dengan mengabaikan bojke yang sedang kita kerjakan.

```python
class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"kucing saya bernama {sef.nama}, umur {self.umur}")

    def suaranya(self):
        print("meow")


class Harimau:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"harimau saya bernama {self.nama}, umur {self.umur}")

    def suaranya(self):
        pritn("arrrrg")


kucing_saya = Kucing("pico", 1.4)
harimau_saya = Harimau("trixy", 3)

for hewan in (kucing_saya, harimau_saya):
    hewan.suaranya()
    hewan.info()
    hewan.suaranya()
```

disni kita telah membuat dua kelas ``kucing`` dan ``harimau``. mereka berbagi struktur yagn sama dan memiliki nama metode yang sama ``info()`` dan ``suaranya()``, namun perhatikan bahwa kita belum membuat superclass umum atau menautkan kelas bersama sama dengan cara apapun, meski begitu, kita dapat megnemas dua objek berbeda ini ke dalam sebuah ``tuple`` dan mengulanginya menggunan persamaan ``hewan``. hal ini dimungkinkan karena polimorfisme.

## polimorfisme dan warisan

sperti dalam bahasa pemograman lain, kelas anak dalam python juga mewarisi metode dan atribut dari kelas induk. kita dapat mendifinisikan ulang metode dan atribut tertentu agar sesua dengan kelas anak, yang dikenal sebagi **metode overriding**. polimorfisme memungkinkan kita untuk mengakses metode dan atribut yang diganti ini yang memiliki nama yabg sama dengan kelas induknya.

```python
from math import pi


class Bentuk:
    def __init__(self, nama):
        self.nama = nama
    
    def area(self):
        pass

    def info(self):
        return "saya adalah bentuk 2 dimensi"

    def __str__(self):
        return self.name

class Persegi:
    def __init__(self, panjang):
        super().__init__("Persegi")
        self.panjang = panjang

    def area(self):
        return self.panjang**2

    def info(self):
        return "persegi memiliki sudut masing-masing 90 derajat"
    

class Lingkaran(Persegi):
    def __init__(self, jari):
        super().__init__("Lingkaran")
        self.jari = jari

    def area(self):
        return pi*self.radius**2

a = Persegi(4)
b = Lingkaran(7)

print(b)
print(b.info())

print(a.info())
print(a.area())
```

disini kita dapat melihat bahwa metode ``__str__()``, yang belum di override di kelas anak, digunakan dari kelas induk.

karena polimorfisme, interpreter python secara otomatis mengenali bahwa ``info()``  metode untuk objek ``a`` (kelas ``persegi``) diganti. jadi, ia menggunakan yang didefinisikan di kelas anak.

di sisi lain, karena ``info()`` metode untuk objek ``B`` tidak ditimpa, itu digunakan dari induk ``Bentuk``

contoh lain
```python
class Kakaktua:
    def terbang(self):
        print("kakaktua bisa terbang")
    
    def berenang(self):
        print("kakaktua tidak bisa berenang")


class Pinguin:
    def terbang(self):
        print("pinguin tidak bisa terbang")

    def berenang(self):
        print("pinguin bisa berenang")

def test_terbang(burung):
    burung.terbang()

jikle = Kakaktua()
megi = Pinguin()

test_terbang(jikle)
test_terbang(megi)
```