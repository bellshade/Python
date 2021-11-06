## Class (Kelas)

Kelas dapat diartikan sebagai kerangka untuk membuat suatu objek, membuat suatu kelas sama dengan membuat tipe baru, dan meng-inisialisasi tipe tersebut sama dengan menghasilkan objek baru.

Kelas memiliki atribut untuk mempertahankan nilainya, dan memilki metode untuk mengubah nilainya. Untuk membuat class di python dapat menggunakan keyword class.

# Atribut

Atribut adalah variable dan fungsi yang ada didalam kelas, seluruh atribut bersifat publik dan dapat diakses menggunakan tanda titik (.) dibelakang objek. Note: atribut yang diawali dengan `_` umumnya dianggap *private*; tidak dimaksudkan untuk digunakan di luar kelas.

# Metode 

Metode adalah fungsi yang dibuat didalam kelas, karena metode adalah fungsi maka untuk membuatnya menggunakan keyword def.

Ada 3 jenis metode class, yaitu:

- instance method

metode ini harus memiliki parameter self, yang berguna untuk mengakses atribut objek, untuk menggunakannya harus melalui objek.

- classmethod

metode ini menggunakan deokrator @classmethod dan harus memiliki parameter cls, yang berguna untuk mengakses atributnya, untuk menggunakannya dapat langsung dari kelasnya tanpa menggunakan objek.

- staticmethod

metode ini menggunakan dekorator @staticmethod, metode ini sama seperti classmethod namun tidak perlu menggunakan parameter wajib

## Konstruktor dan Destruktor

- konstruktor

Konstruktor adalah metode yang dipanggil saat membuat suatu objek, konstruktor dapat berguna untuk meminta atribut apa saja yang diperlukan saat membuat objek. Membuat konstruktor dapat menggunakan dunder-method init dan harus memiliki parameter self, juga dapat memiliki parameter tambahan.

- destruktor

Destruktor adalah metode yang dipanggil saat suatu objek dihapus, untuk membuat destruktor dapat menggunakan dunder-method del dan memiliki parameter self.


## menggunakan metode dunder atau magic method
Metode dunder atau magic method dalam Python adalah metode yang memiliki dua garis bawah awalan dan akhiran dalam nama metode. Dunder disini berarti “Double Under (Underscores)”.

contoh:
```
__add__, __repr__, __len__
```

contoh penggunaan dari dunder method
```python
class Hewan:
    def __init__(self, nama_hewan, suara):
        self.nama_hewan = nama_hewan
        self.suara = suara

    def __repr__(self):
        return "kucing {} bersuara {}".format(self.nama_hewan, self.suara)


if __name__ == "__main__":
     hewan = Hewan("sapi", "Mooo")
    print(f" {hewan.nama_hewan} bersuara :{hewan.suara}")
```