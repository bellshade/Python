# lambda function atau dikenal juga dengan anonymous function
# adalah function yang bisa menerima multiple arguments
# tapi hanya bisa melakukan 1 expression

# seperti contoh pada lambda luas_persegi dibawah
# hanya input s, dan satu expresi yaitu, s * s

luas_persegi = lambda s: s ** 2
print(luas_persegi(4))  # 16

# bukti dari lambda bisa menerima multiple argument adalah
# pada luas_segitiga, argument nya itu a dan t

luas_segitiga = lambda a, t: (a * t) / 2
print(luas_segitiga(2, 3))  # 3.0

# disamping itu, lambda function juga bisa menerima
# unlimited argument seperti contoh dibawah

infinite = lambda *input: sum(input)
print(infinite(1, 2, 3))  # 6
print(infinite(1, 2, 3, 4))  # 10

# dan bisa juga unlimited argument dengan keyword

key_inf = lambda **kwargs: sum(kwargs.values())
print(key_inf(satu=1, dua=2, tiga=3))  # 6
print(key_inf(seven=7, eight=8, nine=9, ten=10))  # 34

# contoh penerapan dari lambda function yaitu
# melakukan proses filterisasi dimana yang ditampilkan hanya
# bilangan yang lebih besar dari 5, memakai filter()

li = [i for i in range(10)]
beyond_five = list(filter(lambda x: (x > 5), li))
print(beyond_five)  # [6,7,8,9]
