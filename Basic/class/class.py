from abc import ABC, abstractproperty, abstractmethod


# Kelas abstrak hewan, tidak dapat di-inisialisasi dan hanya berupa instance
class Hewan(ABC):

    # Properti absstrak
    @abstractproperty
    def suara(self):
        ...

    # Metode abstrak
    @abstractmethod
    def bersuara(self):
        ...


# Menggunakan pewarisan dari kelas Hewan
class Kucing(Hewan):

    # Mengimplementasikan properti suara
    @property
    def suara(self):
        return('MIAWW MIAWW')

    # Mengimplementasikan atribut bersuara
    def bersuara(self):
        print(self.suara)


# contoh membuat objek
tomcat = Kucing()

# mengakses metode bersuara
tomcat.bersuara()
# output: "MIAWW MIAWW"
