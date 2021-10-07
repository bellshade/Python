"""
Operator Identitas adalah operator yang digunakan
untuk membandingkan suatu object. Jika object bernilai sama
dan memilii memori yang sama, maka akan mengembalikan nilai True.

contoh:
"""

# variabel
x = "piton"
y = "kobra"
list_ular = ["piton", "kobra", "sanca"]

# cek apakah nilai dari variabel x dan y ada pada memori yang sama
# jika x is y, maka cetak "Sama"
# lain jika x is not y, maka cetak "Tidak sama"
if x is y:
    print("Sama")
elif x is not y:
    print("Tidak sama")
print("\n")

# jika tipe data list_ular bukan list, maka cetak "Ini bukan list"
# jika tidak, maka cetak "Ini adalah list"
if (type(list_ular) is not list):
    print("Ini bukan list")
else:
    print("Ini adalah list")