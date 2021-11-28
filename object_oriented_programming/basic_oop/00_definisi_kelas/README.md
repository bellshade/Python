# definisikan kelas dengan python

struktur data primitif seperti angka, string dan list dirancang untuk mewakili potongan informasi sederhana, seperti harga apel, nama puisi atau warna favorit, bagaimana jika ingin mempresentasikan suatu yang lebih kompleks ?

misalnya, kita ingin melacak karyawan di sebuah organisasi. kita perlu menyimpan beberapa informasi dasar tentang setiap karyawan, seperti nama, usia, posisi dan tahun mulai bekerja

aasalah satu car auntuk melakukannya adalah dengan mewakili setiap karyawan sebagai list

```python
sundar = ["sundar pichai", 25, "CEO", 4421]
karen = ["karen crab", 20, "officer", 2214]
lims = ["lim benjamin", "officer", 2612]
```

ada sejumlah masalah dengan pendekatan ini

pertama, ini dapat emmbuat file kode yang lebih besar dan lebih sulit untuk dikelola. jika kita mereferensikan ``sundar[0]`` beberapa baris dari tempat ``sundar`` yang di deklarasikan, apakah kita akan mengingat bahwa elemen dengan indeks ``0`` adalah nama karyawan

kedua, dapat menimbulkan kesalahan jika tidak setiap karyawan memiliki jumlah elemen yang sama dalam daftar. contoh pada ``lims`` yang tidak terdapat daftar usia. jadi jika kita memanggil ``lims[1]`` maka ``"officer"`` akan digantikan sebagai usia

car ayang bagus untuk membuat kode jenis ini lebih mudah dikelola adalah dengan menggunakan kelas

## cara mendifinisikan kelas

semua definisi kelasdimulai dengan ``class``, yang diikuti dengan nama kelas dan titik dua. setiap kode yang menjorok di bawah definisi kelas dianggap sebagai dari bagian dari badan kelas

```python
class Pelajar:
    # isi dari kelas dari "Pelajar"
    pass
```

catatan:
__nama kelas python ditulis dalam notasi **CapitalizeWords** berdasarkan python naming convention. misalnya, kelas untuk jenis pelajar seperti pelajar mahasiswa akan ditulis sebagai **PelajarMahasiswa**__

properti dari ``student`` harus dimiliki semua objek didefinisikan dalam metode yang disebut dengan ``.__init__()``. setiap kali baru student objek dibuat, ``.__init__()`` menetapkan awal dari objek dengan assign value dari objek properti. jadi, ``.__init__()`` akan menginisialisasi setiap instance baru di kelas.

kita dapat memberikan parameter di dalam ``.__init()__``, teatpi variabel pertama akan selaliu berupa variabel yang disebut dengan ``self``. ketika instance kelas beru dibuat, instance secara otomatis diteruskan ke ``self`` parameter ``.__init__()`` sehingga attribut baru dapat didefinisikan pada objek

```python
class Pelajar:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
```

di dalam ``__init__()``, tedapat dua pernyataan yang menggunakan ``selfvariabel``

1. ``self.nama = nama``, membuat atribut yang dipanggil nama dan memberikan nilai nama parameter padanya
2. ``self.umur = umur``, membatu atribut yang dipanggil umur dan memberikan nilai umur parameter padanya

attribut yang dibuat ``.__init__()`` disebut **attribut instance**. nilai atribut instance khusus untuk instance kelas tertenty, semua ``student`` objek memiliki nama dan usia, tetapi nilai atribut ``nama`` dan ``usia`` akan bervariasi tergantung pada ``student`` instance.

di sisi lain, **atribut kelas** adalah atribut yang memiliki nilai yang sama untuk semua instance kelas. kita dapat mendifinisikan atribut kelas dengan menetapkan nilai ke nama variabel di luar ``.__init__()``

misalnya, kelas ``student`` memiliiki atribut kelas yang disebut ``jenis_kelas`` dengan nilai ``bahasa``

```python
class Student:
    jenis_kelas = "bahasa"

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
```

atribut kelas didefinsikan langsung di bawah bari pertama nama kelas dan diberi indentasi oleh empat spasi. mereka harus selalu diberi nilai awal. ketika sebuah instance dari kelas dibuat. atribut kelas secara otomatis dibuat dan ditetapkan ke nilai awalnya.

gunakan atribut kelas untuk mendefinisikan properti yang harus memiliki nilai yang sama untuk setiap instanc kelas, gunakan atribut instance untuk properti yagn bervariasi dari satu instance ke instance lainnya

## membuat instansi objek dengan python

lakukan dengan cara buka terminal atau interaktif idle python, untuk pada terminal, cmd, powershell bisa dilakukan dengan cara melakukan perintah
```
python3
```
kemudian lakukan perintah
```
>>> class Pelajar:
...     pass
```
ini akan menciptakan kelas ``Pelajar`` baru tanpa atribut atau metode.

membuat objek baru dari kelas disebut ``instantiating`` objek. kita dapat membuat instance objek ``Pelajar`` bari dengan mengetikkan nama kelas, diikuti dengan tanda kurung buka dan tutup
```
>>> Pelajar
<__main__.Pelajar object at 0x7ff3b8e41640>
```

kita skearang memiliki objek ``Pelajar`` pada ``0x7ff3b8e41640``, rangkaian huruf dan angka itu adalah **alamat memori** yang menunjukkan di mana objek ``Pelajar`` tersebut disimpan dalam memori komputer kita. setiap memanggil maka kita akan mendapatkan jenis memori yang berbeda beda tiap kita memanggilnya. cara mudah untuk membedakannya adalah dengan cara berikut

```
>>> pertama = Pelajar()
>>> kedua = Pelajar()
pertama == kedua
False
```


Materi Selanjutnya: [Atribut Kelas](../01_atribut_kelas)