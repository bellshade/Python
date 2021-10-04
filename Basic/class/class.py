from abc import ABC, abstractproperty, abstractmethod


# Kelas abstrak hewan, tidak dapat di-inisialisasi dan hanya berupa instance
class Hewan(ABC):

    # Properti abstrak
    @abstractproperty
    def suara(self):
        pass

    # Metode abstrak
    @abstractmethod
    def bersuara(self):
        pass


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
