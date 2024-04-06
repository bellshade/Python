# Enkapsulasi dengan python

Enkapsulasi adalah satu konsep dasar dalam pemograman berorientas objek (oop). Ini menggambarkan ide membungkus data dan metode yang bekerja pada data dalam satu unit, menemapatkan pembatasan dalam mengases variabel dan metode secara langsung dan dapat mencegah modifikasi data yang tidak sengaja. Untuk mencegah perubahan yang tidak disengaja, variabel objek hanya dapat diubah dengan metode objek. jenis variabel tersbut dikenal sebagai **variabel privat**.

## Anggota yang dilindungi

Anggota yang dilindungi adalah anggota kelas yang tidak dapta diakses dari luar kelas tetapi dapat diakses dari dalam keas dan subkelasnya. Untuk mencapai ini dengan python, cukup konvens dengan mengawali nama anggota dengan satu bawah ``_``

```python
class Motor:
    def __init__(self):
        self.__updatePart()

    def hidupkanMotor(self):
        print("hidupkan motor")

    def __updatePart():
        print("menambahkan part terbaru")

motor_matic = Motor()
motor_matic.hidupkanMotor()

# jika dipanggil '__updatePart' maka akan menyebabkan error
# motor_matric.__updatePart()
```

Variabel juga bisa menggunakan akses privat yang dapat berguna dalam beberapa tujuan. Variabel privat hanya dapat diubah di dalam metode kelas dan tidak di luar kelas.

Objek dapat menyimpan data penting untuk aplikasi kita dan kita tidak ingin data tersebut dapat diubah dari manapun dalam kode.

```python
class Motor:
    __kecepatan = 0
    __merk = ""

    def __init__(self):
        self.__kecepatan = 120
        self.__nama = "inter motor"

    def jalan(self):
        print("jalan dengan kecepatan {} km".format(self.__kecepatan))

matic = Motor
matic.jalan()

# variabel tidak berubah karena sebelumnya
# bersifat private
matic.__kecepatan = 300
matic.jalan()
```

Jika ingin merubah value dari private member dari kelas kita bisa menambahkan fungsi untuk meengganti serta memodifikasi dari member yang private.
```python
class Motor:
    __kecepatan = 0
    __merk = ""

    def __init__(self):
        self.__kecepatan = 120
        self.__nama = "inter motor"

    def jalan(self):
        print("jalan dengan kecepatan {} km".format(self.__kecepatan))

    def gantiKecepatan(self, kecepatan_sekarang):
        self.__kecepatan = kecepatan_sekarang

matic = Motor
matic.jalan()

matic.gantiKecepatan(60)
matic.jalan()
```

materi selanjutnya: [inheritance](../inheritance)
