<p align="center">
  <img src="https://i.ibb.co/hczmMvm/Factory.png" alt="Factory Design Pattern">
</p>

# Factory Pattern

Dalam pemrograman yang berorientasi objek, merupakan suatu pola yang biasa di sebut sebagai metode pabrik adalah pola kreasi yang menggunakan metode pabrik untuk menangani masalah pembuatan objek tanpa harus menentukan kelas pasti dari objek yang akan dibuat.

Saat kita membuat suatu pola tertentu, pasti akan erat kaitannya dengan metaclass / dataclass yang masih merupakan Blueprint sebagai landasan awal sebelum di implementasikan ke client object. Sebagai langkah awal mari sama-sama kita buat terlebih dahulu Interface dan/atau bisa di sebut juga sebagai Blueprint Class yang masih sangat abstrak.

### 1. Buatlah file dengan nama factory atau nama apapun

```py
import sys
import logging
from abc import ABCMeta, abstractstaticmethod


# FACTORY DESIGN PATTERN
class IPeople(metaclass=ABCMeta):
    __nama: str
    __posisi: str

    @abstractstaticmethod
    def major(self) -> str:
        return ''
        """ Interface IPeople Method """
```
Kedua kode diatas sama fungsinya untuk kita membuat kode program yang abstrak sama seperti bahasa program lainnya.

Karena kita ingin membuat sebuah Blueprint maka, tentu saja kita membutuhkan sebuah Blueprint Abstrak dari kelas ABC / ABCMeta. Python tidak seperti bahasa pemrograman yang lain yang bisa dengan langsung membuat sebuah program yang abstrak maupun interface.

Bagaimana cara kita untuk bisa membuat program yang masih Abstrak / Interface? Kita hanya perlu memanggil package module abc untuk melakukan penulisan kode yang abstraksi.

### 2. Kita tambahkan beberapa kelas

#### Kelas Mahasiswa
```py
class Mahasiswa(IPeople):

    __nama: str = 'Bellshade'
    __posisi: str = 'Mahasiswa UNPAS'

    def __call__(self) -> None:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.debug(f'Nama: {self.__nama}')
        logging.debug(f'Posisi: {self.major()}')

    def major(self):
        return __class__.__posisi
```

#### Kelas Dosen
```py
class Dosen(IPeople):

    __nama: str = 'Sandhika Galih'
    __posisi: str = 'Dosen UNPAS'

    def __call__(self):
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.debug(f'Nama: {self.__nama}')
        logging.debug(f'Posisi: {self.major()}')

    def major(self):
        return __class__.__posisi
```

### 3. Sekarang kita buat kelas Factory

```py
class PeopleFactory:

    @staticmethod
    def create_people(role_people):
        if role_people[0].lower() == 'mahasiswa':
            return mhs()
        elif role_people[0].lower() == 'dosen':
            return dosen()
        else:
            logging.warning('Argument tidak dikenal!')
```

Setelah semua kode kita tulis seperti diatas, sekarang kita coba buat instansiasikan dari kelas yang sudah kita buat.
```py
mhs = Mahasiswa()
dosen = Dosen()
```

Karena kita memggunakan module `sys & logging` untuk mengambil nilai argument mahasiswa dan/atau dosen dari konsol kita agar kode kita terlihat rapih.

```py
if __name__ == '__main__':
    prompt = sys.argv[1:]
    try:
        if len(prompt) >= 0:
            PeopleFactory.create_people(prompt)
    except IndexError:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.WARN)
        logging.warning('Argument mahasiswa atau dosen tidak terdeteksi!')
```

Yuk, sekarang kita coba jalankan program kita di konsol mau itu lewat CMD / Terminal lainnya.

```console
> python factory.py
```
Jika kita tidak memberikan argument mahasiswa atau dosen, maka akan muncul pesan error.

<p style="color:red;padding:5px;background:#f1f2f3;">WARNING: Argument mahasiswa atau dosen tidak terdeteksi!</p>

Lalu bagaimana jika kita memasukan argument tapi terdapat tulisan yang salah (Typo...). Sama seperti halnya di atas, jika tidak memberikan argument atau memiliki kesalahan penulisan maka akan muncul pesan error di hadapan kita.
```console
> python factory.py mahasiwa
```
Maka hasilnya adalah...
<p style="color:red;padding:5px;background:#f1f2f3;">WARNING:root:Argument tidak dikenal!</p>

Jika kita menuliskan argument dengan benar, kita tidak akan mendapatkan pesan error seperti diatas.
```console
> python factory.py mahasiwa
```

dan sekarang lihatlah hasil yang didapat jika kita menuliskannya dengan benar.
```console
DEBUG: Nama: Sandhika Galih
DEBUG: Posisi: Dosen UNPAS
```

Selanjutnya: [Proxy Pattern](proxy.md)