<p align="center">
  <img src="https://i.ibb.co/rd9bDqG/Composite.png" alt="Composite Design Pattern">
</p>

# Composite Pattern

Dalam rekayasa perangkat lunak, pola komposit adalah pola desain partisi. Pola komposit mendeskripsikan sekelompok objek yang diperlakukan dengan cara yang sama seperti satu contoh objek dengan tipe yang sama.

Tujuan dari komposit adalah untuk "menyusun" objek ke dalam struktur pohon untuk mewakili hierarki sebagian-keseluruhan. Menerapkan pola komposit memungkinkan klien memperlakukan objek dan komposisi individual secara seragam.

### 1. Buatlah file dengan nama Composite

Sama seperti materi sebelumnya, bahwa kita mengharuskan membuat kelas yang abstrak untuk kita jadikan sebagai pacuan kita membuat kelas templatenya

```py
import logging
from abc import ABCMeta, abstractmethod, abstractstaticmethod

# Logging Config
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


# COMPOSITE DESIGN PATTERN
class IJurusan(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, mahasiswa):
        """ Implement in child Class """

    @abstractstaticmethod
    def jumlah_mahasiswa(self):
        pass
```

### 2. Tambahkan beberapa kelas yang dibutuhkan

Kelas Informatika
```py
class Informatika(IJurusan):
    """Kelas ini akan mengimplementasi kelas abstrak IJurusan
    yang memiliki parameter mahasiswa dari kelas abstrak
    :param mahasiswa: Parameter untuk jumlah Informatika
    ada berapa jumlah mahasiswa Informatika.
    >>> mhs1 = Informatika(30)
    >>> mhs1.jumlah_mahasiswa()
    30
    """

    def __init__(self, mahasiswa):
        self.mahasiswa = int(mahasiswa)

    def jumlah_mahasiswa(self):
        return self.mahasiswa
```

Kelas Management
```py
class Management(IJurusan):
    """Kelas ini akan mengimplementasi kelas abstrak IJurusan
    yang memiliki parameter mahasiswa dari kelas abstrak
    :param mahasiswa: Parameter untuk jumlah Management
    ada berapa jumlah mahasiswa Management.
    >>> mhs1 = Management(10)
    >>> mhs1.jumlah_mahasiswa()
    10
    """

    def __init__(self, mahasiswa):
        self.mahasiswa = int(mahasiswa)

    def jumlah_mahasiswa(self):
        return self.mahasiswa
```

### 3. Sekarang kita buat kelas Jurusan yang kita fungsikan sebagai Composite

```py
class Jurusan(IJurusan):
    """Kelas ini akan mengimplementasi kelas abstrak IJurusan
    yang memiliki parameter mahasiswa dari kelas abstrak
    :param mahasiswa: Parameter ini harus berisikan informasi
    ada berapa jumlah mahasiswa Management.
    >>> mhs1 = Informatika(30)
    >>> mhs2 = Management(20)
    >>> jurusan = Jurusan(2)
    >>> jurusan.data_jurusan(mhs1)
    >>> jurusan.data_jurusan(mhs2)
    >>> jurusan.jumlah_mahasiswa()
    """

    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa
        self.jurusan_dasar = mahasiswa
        self.jumlah_jurusan = []

    def data_jurusan(self, mahasiswa_jurusan):
        self.jumlah_jurusan.append(mahasiswa_jurusan)
        self.mahasiswa += mahasiswa_jurusan.jumlah_mahasiswa()

    def jumlah_mahasiswa(self):
        logging.debug(f'Jumlah jurusan dasar: {self.jurusan_dasar}')
        for jurusan in self.jumlah_jurusan:
            logging.debug(f'{type(jurusan).__name__}: {jurusan.jumlah_mahasiswa()}')
        logging.debug(f'Total mahasiswa: {self.mahasiswa}')
```

Jangan lupakan ifmain jika kita ingin menjalankan program ini dengan kelss yang kita inginkan agar bisa berjalan sebagai landasan awal program kita
```py
if __name__ == '__main__':
    p1 = Informatika(30)
    p2 = Management(50)
    jurusan = Jurusan(2)
    jurusan.data_jurusan(p1)
    jurusan.data_jurusan(p2)
    jurusan.jumlah_mahasiswa()
```

Saat program kita jalankan, maka kita akan mendapatkan hasil seperti dibawah ini jika penulisan program kita sudah benar

```console
DEBUG: Jumlah jurusan dasar: 2
DEBUG: Informatika: 30
DEBUG: Management: 50
DEBUG: Total mahasiswa: 82
```

Jika teman-teman ingin mengujinya menggunakan Pytest, berikut ini adalah penulisan kode yang untuk di uji oleh Pytest

```py
def test_insert_data_informatika():
    mhs = Informatika(100)
    assert 100 == mhs.jumlah_mahasiswa()
```

Sebelumnya: [Singleton Pattern](singleton.md) | Selanjutnya: [Facade Pattern (Coming Soon)](facade.md)