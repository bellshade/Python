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

# Access Modifiers
## Definisi dan Jenis Access Modifiers
Di dalam *object oriented programming* (selanjutnya disebut OOP), terdapat istilah *access modifiers*. *Access modifiers* merupakan hak akses yang dimiliki oleh suatu atribut atau method. *Access modifiers* berguna untuk menentukan apakah atribut atau method yang dimiliki oleh class dapat digunakan diluar class tersebut.

Terdapat 3 jenis serta kegunaan *access modifiers*, yaitu :
1. Public       : Memungkinkan atribut atau method dalam suatu class digunakan dimanapun.
2. Private      : Atribut atau method yang menggunakan *access modifiers* ini hanya dapat digunakan di dalam class yang mendefinisikan atribut atau method tersebut, dan tidak dapat digunakan pada class turnannya.
3. Protected    : Atribut atau method yang menggunakan *access modifiers* ini hanya dapat digunakan di dalam class yang mendifinisikan atribut atau method tersebut beserta class turunannya.

Tidak seperti bahasa pemrograman lain dengan konsep OOP yang lebih matang seperti Java atau C yang mendefinisikan *access modifiers* secara gamblang menggunakan *keyword* ``public``, ``private``, dan ``protected``, dalam bahasa Python, *access modifiers* ini menggunakan *underscore*. *Underscore* dibubuhkan sebelum nama atribut. Untuk ``public`` *access modifiers* tidak perlu menggunakan `_`, ``protected`` *access modifiers* menggunakan satu `_`, dan ``private`` *access modifiers* menggunakan dua `_`. Supaya lebih jelas, kode di bawah menunjukkan bagaimana mendefinisikan *access modifiers*.

```python
class Siswa:
    def __init__(self, nama, tanggalLahir, alamat):
        # atribut public access modifier
        self.nama = nama
        # atribut protected access modifier
        self._tanggalLahir = tanggalLahir
        # atribut private access modifier
        self.__alamat = alamat

    # method public access modifier
    def printNama(self):
        print(self.nama)

    # method protected access modifier
    def _printTanggalLahir(self):
        print(self._tanggalLahir)

    # method private access modifier
    def __printAlamat(self):
        print(self.__alamat)


# driver code
if __name__ == "__main__":
    budi = Siswa("Budi", "30 Februari", "Jalan Kemerdekaan")
    budi.printNama()
    budi._printTanggalLahir()
    budi.__printAlamat()
```

Jika kita jalankan ```driver code``` di atas, kita akan mendapatkan *output* sebagai berikut :
```python
Budi
30 Februari
AttributeError: 'orang' object has no attribute '__printAlamat'
```

Ternyata, setelah dijalankan, kita mendapat *exception* ```AttributeError```. *Exception* ini kita dapatkan karena kita mengakses ```protected``` method dengan cara yang salah. Di python, kita menggunakan *decorator* ```@property``` untuk mengakses atribut atau method yang sifatnya ```protected``` atau ```private```.

## Menggunakan Decorator Property Untuk Mengakses Private Dan Protected Access Modifiers
Seperti yang sudah dijelaskan pada bagian definisi dan jenis *access modifier*, pada bahasa Python, kita menggunakan *decorator* ```@property``` untuk mendefinisikan method *getter* dan *setter*.

Method *getter* dan *setter* merupakan method yang lazim digunakan ketika membahas OOP. Kedua method ini dapat mengambil (*get*) serta meng-*assign* (*set*) nilai dari atribut yang dimiliki class jika atribut dari kelas tersebut bersifat ```protected``` atau ```private```.

Sintaks untuk *getter* menggunakan *decorator* ```@property``` adalah sebagai berikut :

```python
@property
def nama_atribut(self):
    return self.__nama_atribut
```

Sedangkan sintaks untuk *getter* menggunakan *decorator* ```@property``` adalah sebagai berikut :

```python
@nama_atribut.setter
def nama_atribut(self, nilai_atribut_baru):
    return self.__nama_atribut = nilai_atribut_baru
```

Supaya lebih memahami bagaimana cara menggunakan *decorator* ```@property```, mari kembali ke class ```Siswa```, namun kali ini dengan sedikit perubahan.

```python
class Siswa:
    def __init__(self, nama = ""):
        # private public access modifier
        self.__nama = nama

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama_baru):
        self.__nama = nama_baru


# driver code
if __name__ == "__main__":
    siswa = Siswa("Budi")
    # menampilkan nama menggunakan getter
    print(siswa.nama)
    # mengganti nama menggunakan setter
    siswa.nama = "Andi"
    # nama dari instance siswa akan terganti dari budi menjadi andi
    print(siswa.nama)
```

Jika kita jalankan ```driver code``` di atas, kita akan mendapatkan *output* sebagai berikut :

```python
Budi
Andi
```

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
