class NamaSaya:
    def __init__(self, nama, umur):
        self.nama_saya = nama
        self.umur_saya = umur

    def tampil_nama(self):
        print(f"Apa kabar {self.nama_saya}")


objek_kelas = NamaSaya("yoga", 31)
objek_kelas.tampil_nama()
print("Umur saya adalah ", objek_kelas.umur_saya)
