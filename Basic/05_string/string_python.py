# string di python bisa menggunakan
# petik satu dan petik dua
#  contoh
# "Hello World" sama dengan 'hello world'
# 'hello world' sama dengan "hello world"
# Namun disarankan menggunakan petik dua
# dalam deklarasi python


kata_pertama = "warung"

# bisa juga menggunakan multi string
# bisa menggunakan 3 tanda petik dua atau satu
kata_saya = """Indonesia adalah negara yang indah
berada di bawah garis khatulistiwa
aku cinta Indonesia
"""

# print(kata_pertama)
print(kata_saya)

# mengubah kata ke huruf besar
print(kata_pertama.upper())

# mengubah kata ke huruf kecil
print(kata_pertama.lower())

# mengambil salah satu karakter dari string
# contoh
print(kata_pertama[0])

# menghitung jumlah karatker dari string
# contoh
print(len(kata_pertama))

# kita juga dapat mengecek kata khusus dalam sebuah string
# contoh
print("Indonesia" in kata_saya)
print("Indonesia" in "one")  # lgtm [py/comparison-of-constants]
