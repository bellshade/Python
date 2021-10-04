from abc import ABC, abstractproperty, abstractmethod


class Hewan(ABC):
    @abstractproperty
    def suara(self):
        ...

    @abstractmethod
    def bersuara(self):
        ...


# Menggunakan pewarisan dari kelas Hewan
class Kucing(Hewan):
    @property
    def suara(self):
        return('MIAWW MIAWW')

    def bersuara(self):
        print(self.suara)


# contoh membuat objek
tomcat = Kucing()

# mengakses metode bersuara
tomcat.bersuara()
# output: "MIAWW MIAWW"
