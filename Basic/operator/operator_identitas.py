"""
Operator Identitas adalah operator yang digunakan
untuk membandingkan suatu object. Jika object bernilai sama
dan memilii memori yang sama, maka akan mengembalikan nilai True.

contoh:
"""

# variabel
x = 3
y = 7

# cek apakah nilai dari variabel x dan y ada pada memori yang sama
# jika x is y, maka cetak "Sama"
# lain jika x is not y, maka cetak "Tidak sama"
if x is y:
    print("Sama")
elif x is not y:
    print("Tidak sama")
print("\n")

# jika tipe data y bukan integer, maka cetak "Ini bukan integer"
# jika tidak, maka cetak "Ini adalah integer"
if (type(y) is not int):
    print("Ini bukan integer")
else:
    print("Ini adalah integer")
