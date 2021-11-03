# private access

Anggota kelas private menggunakan variabel deklarasi objek berupa tanda dua underscore ``__`` pada bagian depan objek dan menyatakan bahwa objek tersebut otomatis hanya akan bisa diakses oleh sebuah kelas dan turunannya saja.

```python
class PekerjaTambang:
    # private variabel
    __nama = None
    __jabatan = None

    # konstruktor
    def __init__(self, nama, jabatan):
        self.__nama = nama
        self.__jabatan = jabatan

    # membuat fungsi yang bersifat private

    def __menampilkan(self):
        # memangakses private objek
        print("Nama: ",self.__nama)
        print("Jabatan: ",self.__jabatan)
    
    # fungsi yang bersifat publik

    def menampilkan_data(self):
        self.__menampilkan()

# membuat objek dan menampilkannya
pekerja1 = PekerjaTambang("James", "Research")

# menampilkan objek yang dimana terdapat fungsi private
pekerja1.menampikan_data()
```

variabel dari ``__nama``, ``__jabatan`` adalah salah satu variabel yang hanya bisa diakses di dalam kelas (termasuk fungsi dari ``__menampilkan``, ini hanya bisa diakses di dalam kelas ``PekerjaTambang``), sementara fungsi ``menampilkan_data`` bisa diakses di luar atau di dalam kelas dikarenakan bersifat publik sehingga bisa diakses dari luar dengan membuat objek dan menampilkan hasil dari fungsi private yaitu ``__menampilkan``. jika kita menambahkan kode lagi dibawah dengan memanggil fungsi dari ``__menampilkan`` makan akan terjadi error karena kelas tersebut bersifat private. contoh error yang dihasilkan adalah
```
Traceback (most recent call last):
  File "file_saya.py", line x, in <module>
    pekerja1.__menampilkan()
AttributeError: 'PekerjaTambang' object has no attribute '__menampilkan'
```