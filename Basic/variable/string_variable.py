# String dalam Python diidentifikasi
# sebagai serangkaian karakter yang berdekatan
# yangdiwakili dalam tanda kutip.

pesan = "saya pergi ke pasar"

# s a y a   p e r g i
# 0 1 2 3 4 5 5 6 7 8 9

# k  e     p  a  s  a  r
# 10 11 12 13 14 15 16 17


print(pesan)  # print secara keseluruhan
print(pesan[0])  # print karakter 's'

# print karakter dari karakter ke 3
# ke karakter ke 5
print(pesan[2:5])

# print dimulai dari karakter ke 3
print(pesan[2:])

# print kata 2 kali
print(pesan * 2)

# gabung kata dengan kata baru
# saya pergi kepasar dengan ibu saya
print(pesan + " dengan ibu saya")

# membalikan Kata (reverse string)
print(pesan[::-1])
