# kelas induk
class Siswa(object):
    # __init__ sebagai constructor
    def __init__(self, nama, kelas, jenis_kelamin):
        self.nama = nama
        self.kelas = kelas
        self.jenis_kelamin = jenis_kelamin


# child class atau kelas non induk
# membuat kategori siswa berdasarkan dari
# kelas induk
class KategoriSiswa(Siswa):
    def __init__(self):
        # memanggil constructor dari kelas induk
        Siswa.__init__(self, "arfy", 12, "laki-laki")

    # mmenampilkan hasil dari kelas induk
    def tampilkan(self):
        print(self.nama)
        print(self.kelas)
        print(self.jenis_kelamin)


# deklarasi objek
data = KategoriSiswa()
# memanggil objek
data.tampilkan()
