# Atribut kelas

## Atribut kelas dan instance

Sekarang, buat kelas dari ``Pelajar`` baru dengan atribut kelas yang disebut ``jenis_kelas`` dan dua atribut instance yang berupa ``nama`` dan ``umur``.

```python
class Pelajar:
    jenis_kelas = "bahasa"
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
```

Untuk meneruskan argumen ke parameter ``nama`` dan ``umur``, masukkan nilai ke dalam tanda kurung setelah nama kelas

```python
janis = Pelajar("janis", 21)
erik = Pelajar("erik", 23)
```

Ini menciptakan contoh ``Pelajar`` baru satu untuk pelajar berusia 21 tahun bernama ``janis`` dan satu untuk yang bernama ``erik`` yang berusia 23 tahun.

Metode kelas ``pelajar``. ``__init__()`` memiliki tiga parameter, jadi mengapa hanya dua argumen yang diteruskan di dalam contoh?

Saat kita membuat instance objek ``Pelajar``, Python membuat instance baru dan meneruskannya ke parameter pertama. ``__init__()`` ini pada dasarnya menghapus ``self`` paramter, jadi kita hanya perlu khawatir pada peremter ``nama`` dan ``umur``.

Setelah kita membuat instance pelajar, ktia dapat emengakses atribut instance mereka dengan menggunakan notasi titik

```python
print(janis.umur)
print(erik.umur)
```

Kita juga dapat mengakses atribut kelas dengan cara yang sama yaitu:
```python
print(janis.jenis_kelas)
print(erik.jenis_kelaas)
```

Salah satu keuntungan terbesar menggunakan kelas untuk mengatur data adalah bahwa instance dijamin memiliki atribut yang kita harapkan. Semua objek ``pelajar`` memiliki ``jenis_kelas``,``nama`` dan ``umur``, sehingga kita dapat menggunakan atribut tersebut dengan percaya karena mengetahui bahwa mereka akan selalu mengembalikan nilai.

meskipun atribut dijamin ada, nilai dapat dirubah secara dinamis

```python
janis.umur = 22
erik.umur = 22
```

## Motede instance

Metode instance adalah fungsi yang didefinisikan di dalam kelas dan hanya dapat dipanggil dari instace kelas tersebut, eperti ``__init__()``, parameter motede instance selalu ``self``.

```python
class Pelajar:
    jenis_kelas = "bahasa"

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # metode instance
    def deksripsi(self):
        return f"{self.nama} berumur {self.umur} tahun"

janis = Pelajar("janis aneira", 22)
print(janis.deksripsi())
```
``deskripsi()`` mengembalikan string yang menampilkan nama dan usia.


Materi Selanjutnya: [mewarisi kelas](../02_mewarisi_kelas)
