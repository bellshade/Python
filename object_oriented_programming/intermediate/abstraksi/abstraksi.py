from abc import ABC, abstractmethod


class Mobil(ABC):
    @abstractmethod
    def akselerasi(self):
        # jika diberikan implementasi maka akan memunculkan TypeError
        pass

    @abstractmethod
    def deakselerasi(self):
        pass


class MPV(Mobil, ABC):
    def __init__(self):
        self.__jenis = "MPV"
        print(f"Jenis: {self.__jenis}")


class Xpander(MPV):
    def __init__(self):
        super().__init__()
        self.__nama = "Mitsubishi Xpander"
        print(f"Nama: {self.__nama}")

    def akselerasi(self):
        print("Akselerasi: mobil semakin cepat!")

    def deakselerasi(self):
        print("Deakselerasi: mobil melambat!")


xpander = Xpander()
xpander.akselerasi()
xpander.deakselerasi()
