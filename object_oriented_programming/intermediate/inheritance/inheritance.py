class Mobil:
    def __init__(self):
        self.nama, self.warna, self.jenis, self.ukuran_ban

    def akselerasi(self):
        pass


class Civic(Mobil):
    def __init__(self):
        self.nama = "Honda Civic"
        self.warna = "Hitam"
        self.jenis = "Sedan"
        self.ukuran_ban = "20 Inci"

    def akselerasi(self):
        print("Akselerasi 0-100 KM/Jam dalam 10 detik! NGENGGG~")


class CivicTypeR(Civic):
    def __init__(self):
        super().__init__()
        self.nama = "Honda Civic Type R"
        self.warna = "Putih"
        self.ukuran_ban = "20 Inci"

    def akselerasi(self):
        print("Akselerasi 0-100 KM/Jam dalam 7 detik! BRRMMM~")


# KELAS INDUK
print("=== KELAS INDUK ===")
parent = Civic()
print(parent.nama, parent.jenis)
parent.akselerasi()

# KELAS ANAK
print("=== KELAS ANAK ===")
child = CivicTypeR()
print(child.nama, child.jenis)
child.akselerasi()
