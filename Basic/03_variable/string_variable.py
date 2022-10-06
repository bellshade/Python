# String dalam Python diidentifikasi
# sebagai serangkaian karakter yang berdekatan
# yang diwakili dalam tanda kutip.

# Dalam membuat variabel string kita dapat
# menggunakan petik dua ("") / petik satu ('')
pesan = "saya pergi ke pasar"
pesan = "saya pergi ke pasar"

# s a y a   p e r g i
# 0 1 2 3 4 5 5 6 7 8 9

# k  e     p  a  s  a  r
# 10 11 12 13 14 15 16 17

# Dalam tipe data string, value dari
# variabel tersebut akan dianggap sebagai
# list. Maka dari kita dapat memanggil
# setiap karakter dengan urutan index

# print secara keseluruhan
print(pesan)
# print karakter pertama pada pesan
print(pesan[0])
# print karakter dari karakter ke 3 sampai 5
print(pesan[2:5])
# print dimulai dari karakter ke 3
print(pesan[2:])
# print kata 2 kali
print(pesan * 2)


# gabung kata dengan kata baru
# saya pergi kepasar dengan ibu saya
print(pesan + " dengan ibu saya")
print(pesan, " dengan ibu saya")
