from abc import ABC, abstractmethod


class Mobil(ABC):
    def __init__(self):
        self.nama = None
        self.jenis = None

    @abstractmethod
    def akselerasi(self):
        pass


class Civic(Mobil):
    def __init__(self):
        super().__init__()
        self.nama = "Honda Civic"
        self.jenis = "Sedan"

    def akselerasi(self):
        print("Akselerasi 0-100 KM/Jam dalam 10 detik! NGENGGG~")


class CivicTypeR(Civic):
    def __init__(self):
        super().__init__()
        self.nama = "Honda Civic Type R"

    def akselerasi(self):
        print("Akselerasi 0-100 KM/Jam dalam 7 detik! BRRMMM~")


# KELAS INDUK
print("=== KELAS INDUK ===")
parent = Civic()
print(f"Nama: {parent.nama}\nJenis: {parent.jenis}")
parent.akselerasi()

# KELAS ANAK
print("=== KELAS ANAK ===")
child = CivicTypeR()
print(f"Nama: {child.nama}\nJenis: {child.jenis}")
child.akselerasi()
