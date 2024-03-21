<p align="center">
  <img src="https://i.ibb.co/tQXsgFK/Proxy.png" alt="Proxy Design Pattern">
</p>

# Proxy Pattern

Dalam pemrograman yang berorientasi objek, pola proxy adalah pola desain perangkat lunak. Proxy, dalam bentuknya yang paling umum adalah kelas yang berfungsi sebagai antarmuka untuk sesuatu yang lain.

Cara penulisan kode saat ini, tidaklah jauh berbeda dengan materi **[Factory Patter](factory.md)** sebelumnya, yang membedakan hanya pada Interface dan/atau Abstrak kelasnya serta ada penambahan kelas yang baru.

### 1. Buatlah file dengan nama proxy

```py
import logging
from src import IUniv
from typing import Callable

# Logging Config
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# PROXY DESIGN PATTERN
class IUniv(metaclass=ABCMeta):

    @abstractstaticmethod
    def division(self):
        """ Interface IUniv Method """
```

### 2. Lanjutkan dengan menuliskan beberapa kelas

Kelas Mahasiswa
```py
class Mahasiswa(IUniv):
    """ Kelas ini tidak memiliki parameter tetapi memiliki fungxi
    :func division: Fungsi untuk memberikan informasi
    >>> guest = Mahasiswa()
    >>> guest.division()
    """

    def division(self):
        logging.debug('Mahasiswa')
```

Kelas Dosen
```py
class Dosen(IUniv):
    """ Kelas ini tidak memiliki parameter tetapi memiliki fungxi
    :func division: Fungsi untuk memberikan informasi
    >>> guest = Dosen()
    >>> guest.division()
    """

    def division(self):
        logging.debug('Dosen')
```

Kelas Rektor
```py
class Rektor(IUniv):
    """ Kelas ini tidak memiliki parameter tetapi memiliki fungxi
    :func division: Fungsi untuk memberikan informasi
    >>> guest = Rektor()
    >>> guest.division()
    """

    def division(self):
        logging.debug('Rektor')
```

### 3. Buat kelas UnivProxy

```py
class UnivProxy(IUniv):
    """ Kelas ini tidak akan menerima parameter apapun,
    kelas ini hanya terdiri dari cunstructor init yang
    hanya memiliki attribute kelas.
    :attribute dosen: Menginstansiasikan kelas Dosen di Pattern
    :attribute rektor: Menginstansiasikan kelas Rektor di Pattern
    >>> proxy = ProxyPattern()
    >>> proxy()
    """
    def __init__(self):
        self.dosen = Dosen()
        self.rektor = Rektor()
        self.mahasiswa = Mahasiswa()

    def __call__(self) -> Callable:
        self.division()

    def division(self):
        logging.debug('ProxyPattern Functionality.\n==========')
        self.dosen.division()
        self.rektor.division()
        self.mahasiswa.division()
        logging.debug('ProxyPattern Functionality.\n==========')
```

Sebagai langkah terakhir, kita akan eksekusi kelas UnivProxy
```py
if __name__ == '__main__':
    proxy: Callable = UnivProxy()
    proxy()
```

Saat kita jalankan program di konsol kita, maka hasilnya akan kita bisa lihat seperti berikut ini.

```console
> python proxy.py
```

Hasil yang kita inginkan seperti dibawah ini
```console
> DEBUG: ProxyPattern Functionality.
> ==========
> DEBUG: Dosen
> DEBUG: Rektor
> DEBUG: Mahasiswa
> DEBUG: ProxyPattern Functionality.
> ==========
```
Sebelumnya: [Factory Pattern](factory.md) | Selanjutnya: [Singleton Pattern](singleton.md)