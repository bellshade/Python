# inheritance
Warisan memungkinkan kita untuk mendefinisikan kelas yang mewarisi semua metode dan properti dari kelas lain.

Kelas induk adalah kelas yang diwarisi, juga disebut kelas dasar.

Kelas anak adalah kelas yang mewarisi dari kelas lain, juga disebut kelas turunan.

contoh

```python
class Merk(object):
    def __init__(self):
        self.nama = "calvin klein"

class Panggil(Merk):
    def __init__(self):
        Merk.__init__(self)

    def tampilkan(self):
        print(self.nama)

data = Panggil()
data.tampilkan()
```

informasi:
- ``class Merk(object)``
    merupakan parent utama dari inheritance dengan mendeklarasikan variabel nama dengan value ``"calvin klein"``
    
- ``class Panggil(Merk)``
    merupakan child parent yang memanggil parent class utama

    - ``Merk.__init__(self)``
        merupakan konstruktor pemanggil parent class atau kelas induk

    - ``def tampilkan(self)``
        memanggil dari variabel dari parent class atau kelas induk yang berupa ``self.nama`` yang berisi value string (``calvin klein``)

- ``data = Panggil()``
    deklarasi variabel baru dengan memanggil kelas ``Panggil()``
    
- ``data.tampilkan()``

    memanggil fungsi dari tampilkan dari kelas ``Panggil()``.kemudian menampilkan berupa variabel dari parent class atau kelas induk dari ``Merk`` yang berisi value berupa ``calvin klein``

[Materi Selanjutnya](../18_akses_modifikasi/public)