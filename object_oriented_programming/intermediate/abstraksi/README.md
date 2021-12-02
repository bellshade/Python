# Abstraksi dengan Python

Abstraksi adalah salah satu dari konsep Object-Oriented Programming, pada konsep abstraksi ada yang namanya kelas abstrak yang memiliki method yang tidak ada implementasinya, dan semua method yang ada pada kelas abstrak harus public. Secara default, python sebenarnya tidak mendukung kelas abstrak ini, untuk dapat membuat kelas abstrak harus meng-import library abc atau Abstract Base Classes agar dapat mengimplementasikan konsep abstraksi ini pada Python.

Contoh kelas abstrak:
```python
from abc import ABC, abstractmethod

class Mobil(ABC):
    
    @abstractmethod
    def akselerasi(self):
        pass

    @abstractmethod
    def deakselerasi(self):
        pass
```

Lalu untuk mengimplementasikan method yang ada harus dilakukan oleh kelas turunannya.

Contohnya seperti ini:
```python
class Xpander(Mobil):
    
    def __init__(self):
        self.__nama = "Mitsubishi Xpander"
        self.__jenis = "MPV"
        print(f"Nama: {self.__nama}\nJenis: {self.__jenis}")
    
    def akselerasi(self):
        print("Mobil semakin cepat!")

    def deakselerasi(self):
        print("Mobil semakin melambat!")
```