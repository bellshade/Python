<p align="center">
  <img src="https://i.ibb.co/JRtmhtf/Singleton.png" alt="Singleton Design Pattern">
</p>

# Singleton Pattern

Dalam rekayasa perangkat lunak, singleton pattern atau bisa di sebut juga pola tunggal adalah pola desain perangkat lunak yang membatasi pembuatan instance kelas menjadi instance tunggal.

Pada materi-materi sebelumnya kita selalu membuat kelas yang saat di instance tanpa ada batasannya. Nah sekarang kita buat batasan pada pola supaya kelas yang di instance cukup 1x dan/atau jika melebihi akan mendapatkan pesan error.

### 1. Buatlah file dengan nama singleton

```py
import logging
from abc import ABCMeta, abstractstaticmethod

# Logging Config
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# SINGLETON DESIGN PATTERN
class IMahasiswa(metaclass=ABCMeta):

    @abstractstaticmethod
    def log_instance(self):
        """ Implement in child Class"""
```

### 2. Sekarang saatnya kita buat kelas untuk pola singleton
```py
class SingletonMahasiswa(IMahasiswa):
    """Kelas Mahasiswa tidak memiliki argument or params
    akan tetapi, setiap kelas yang instance dari IPeople
    akan memiliki private variable.

    :param nama: Implementasi variable dari IPeople
    :param jurusan: Implementasi variable dari IPeople

    >>> mhs = SingletonMahasiswa('Bellshade', 'Helper')
    >>> mhs.log_instance(mhs)
    """

    __instance = None

    @staticmethod
    def get_instance(self):
        """ Fungsi ini mengambil __instance None, jika instance masih
        bertipe None maka akan di isi oleh instance object pertama kali
        karena pola Singleton ini membatasi kegunaan instance object.
        """
        if SingletonMahasiswa.__instance is None:
            SingletonMahasiswa('Bellshade', 'Helper')
        else:
            return SingletonMahasiswa.__instance

    def __init__(self, nama, jurusan):
        if SingletonMahasiswa.__instance is not None:
            raise Exception('Singleton tidak dapat membuat instance lebih dari sekali!')
        else:
            self.nama = nama
            self.jurusan = jurusan
            SingletonMahasiswa.__instance = self

    @staticmethod
    def log_instance(self):
        """
        Fungsi ini merupakan implementasi dari kelas Abstrak IMahasiswa
        """
        logging.debug(f'Nama: {SingletonMahasiswa.__instance.nama}')
        logging.debug(f'Jurusan: {SingletonMahasiswa.__instance.jurusan}')
```

### 3. eksekusi kode kita dengan ifmain
```py
if __name__ == '__main__':
    p = SingletonMahasiswa('Sandhika Galih', 'Dosen Informatika')
    p.log_instance(p)
```

Jika kita jalankan programnya di konsol, maka kita akan mendapatkan hasil seperti di bawah:
```console
> DEBUG: Nama: Sandhika Galih
> DEBUG: Jurusan: Dosen Informatika
```

Jikalau kita paksakan instance kelas sekali lagi bisa gak yaa?
```py
if __name__ == '__main__':
    p = SingletonMahasiswa('Sandhika Galih', 'Dosen Informatika')
    p2 = SingletonMahasiswa('Tono', 'Mahasiswa Informatika')
    p.log_instance(p)
    p2.log_instance(p2)
```

Hasil yang kita dapatkan kalau kita tetap ingin memaksa untuk instance kelas sekali lagi

```console
Traceback (most recent call last):
  File "/storage/emulated/0/Dev/Python/object_oriented/advance/pycode/metaclass/singleton.py", line 51, in <module>
    p2 = SingletonMahasiswa('Tono', 'Mahasiswa Informatika')
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/storage/emulated/0/Dev/Python/object_oriented/advance/pycode/metaclass/singleton.py", line 34, in __init__
    raise Exception('Singleton tidak dapat membuat instance lebih dari sekali!')
Exception: Singleton tidak dapat membuat instance lebih dari sekali!
```
Sebelumnya: [Proxy Pattern](proxy.md) | Selanjutnya: [Composite Pattern](composite.md)