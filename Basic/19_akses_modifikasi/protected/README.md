# protected access

Anggota kelas yang dideklarasikan protected hanya dapat diakses oleh kelas turunannya. Anggota data dari suatu kelas dinyatakan terlindungi dengan menambahkan satu simbol underscore ``_`` sebelum anggota data dari kelas tersebut. 

```python
class PekerjaTambang:
    # protected variabel
    _nama = None
    _jabatan = None
    
    # membuat konstruktor
    def __init__(self, nama, jabatan):
        self._nama = nama
        self._jabatan = jabatan

    # membuat fungsi protected
    def _menampilkan(self):
        print("jabatan: ", self._jabatan)


# kelas turunan dari pekerja tambang
class Pekerja(PekerjaTambang):

    # membuat konstruktor
    def __init__(self, nama, jabatan):
        PekerjaTambang.__init__(self, nama, jabatan)
    
    # membuat fungsi publik
    def menampilkan(self):
        print("nama: ", self._nama)
        # menampilkan fungsi protected dari kelas Pekerja Tambang
        self._menampilkan()


# membuat variabel yang membuat objek dari pekerja
pekerja1 = Pekerja("james", "driller")

# menampikan
pekerja1.menampilkan()
```

di atas, ``_nama``, ``_jabaran`` adalah anggota data yang protected dan metode ```_menampilkan()``` adalah metode yang dilindungi dari  kelas ``Pekerja``. Metode ``menampilkan()`` adalah fungsi anggota publik dari kelas ``Pekerja()`` yang diturunkan dari kelas ``PekerjaTambang``, metode ``menampilkan()`` di kelas ``Pekerja`` mengakses data anggota kelas ``PekerjaTambang`` yang protected. 