# Tipe data pada Python adalah:
# tipe text yaitu str (string)
# tipe angka yaitu int, float, dan complex
# tipe data majemuk yaitu list, tuple, set, dan range
# tipe data map yaitu dict

# type() digunakan untuk memeriksa tipe data pada variabel

# contoh tipe data str
teks_string = "Halo dunia!"
teks_string_2 = 'halo dunia!'
print(teks_string)
print(teks_string_2)
print(type(teks_string))
print(type(teks_string_2))
print()  # untuk menambahkan baris baru

# contoh tipe data integer
bilangan_integer = 2
print(bilangan_integer)
print(type(bilangan_integer))
print()  # untuk menambahkan baris baru

# contoh tipe data float
bilangan_desimal = 3.13
print(bilangan_desimal)
print(type(bilangan_desimal))
print()  # untuk menambahkan baris baru

# contoh tipe data dari complex
bilangan_complex_1 = complex(1.5)
bilangan_complex_2 = complex(2j)
print(bilangan_complex_1)
print(bilangan_complex_2)
print(type(bilangan_complex_1))
print(type(bilangan_complex_2))
print()  # untuk menambahkan baris baru

# contoh tipe data dari list
nama_siswa = ["andi", "buzz", "wheezy", "army"]
print(nama_siswa)
print(nama_siswa[1])
print(nama_siswa[2])
print(type(nama_siswa))
print()  # untuk menambahkan baris baru

# contoh tipe data dari tuple
mahasiswa = ("suryadi", "sukoco", "sukijan", "sumarmi")
print(mahasiswa)
print(mahasiswa[1])
print(mahasiswa[2])
print(type(mahasiswa))
print()  # untuk menambahkan baris baru

# contoh tipe data dari set
merk_mobil = {"ferrari", "bmw", "toyota"}
print(merk_mobil)
# jika code dibawah dijalankan akan error karena
# tipe data set unsubcriptable (tidak berurutan)
# print(merk_mobil[1])
# jika code dibawah dijalankan akan error karena
# tipe data set unsubcriptable (tidak berurutan)
# print(merk_mobil[2])
print(type(merk_mobil))
print()  # untuk menambahkan baris baru

# contoh tipe data dari frozzenset
nama_desa = frozenset({"getasrejo", "karangmalang", "siti"})
print(nama_desa)
print(type(nama_desa))
print()  # untuk menambahkan baris baru

# contoh tipe data dari dict
detail_mobil = {"merk": "ferrari", "asal": "italia"}
print(detail_mobil)
print(detail_mobil["merk"])
print(detail_mobil["asal"])
print(type(detail_mobil))
print()  # untuk menambahkan baris baru

# contoh tipe data dari bytes
angka_bytes = bytes(12)
print(angka_bytes)
print(type(angka_bytes))
print()  # untuk menambahkan baris baru

# contoh tipe data dari bytearray
angka_bytearray = bytearray(12)
print(angka_bytearray)
print(type(angka_bytearray))
print()  # untuk menambahkan baris baru

# contoh tipe data dari memoryview
angka_memoryview = memoryview(bytes(12))
print(angka_memoryview)
print(type(angka_memoryview))
