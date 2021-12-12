from math import pi


# membuat kelas induk 'Bentuk'
class Bentuk:
    # deklarasi init
    def __init__(self, nama):
        self.nama = nama

    def area(self):
        pass

    # membuat fungsi untuk menampilkan nama bentuk
    def info(self):
        return "saya adalah bentuk 2 dimensi"

    # membuat fungsinya untuk menampilkan nama bentuk
    def __str__(self):
        return self.nama


# membuat kelas persegi yang mengambil data
# dari kelas bentuk
class Persegi(Bentuk):
    def __init__(self, panjang):
        # membuat init yang mengambil data dari kelas induk
        super().__init__("Persegi")
        self.panjang = panjang

    # membuat fungsi yang menghitung area
    def area(self):
        return self.panjang ** 2

    # membuat fungsi yang menampilkan info
    def info(self):
        return "persegi memiliki sudut masing-masing 90 derajat"


# membuat kelas lingkaran yang mengambil data
# dari kelas bentuk
class Lingkaran(Bentuk):
    def __init__(self, jari):
        # membuat init yang mengambil data dari kelas induk
        super().__init__("Lingkaran")
        self.jari = jari

    # membuat fungsi yang menghitung jari jari
    def area(self):
        return pi * self.jari ** 2


# membuat objek dari kelas persegi
a = Persegi(4)
b = Lingkaran(7)

# mengoutputkan bentuk
print(b)
print(b.info())

# mengoutputkan area
print(a.info())
print(b.area())
