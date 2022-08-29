# operator logika (Logical Operator) digunakan untuk
# menggabungkan pernyataan kondisional
# bingung?
# mari kita buat contohnya


# variabel
X = 5

# operator "and" digunakan untuk mengecek
# apakah kedua pernyataan yang diberikan bernilai True

print("X < 6 and X > 1:", X < 6 and X > 1)  # True
print("X > 6 and X > 1:", X > 6 and X > 1)  # False

# operator "or" digunakan untuk mengecek
# apakah salah satu dari dua pernyataan bernilai True

print("X > 6 or X > 1:", X > 6 or X > 1)  # True
print("X > 6 or X < 1:", X > 6 or X < 1)  # False

# operator "not" digunakan untuk mengecek
# apakah nilai tersebut bernilai False

X_UNDER_6 = X < 6
X_ABOVE_10 = X > 10

print(not X_UNDER_6)  # False
print(not X_ABOVE_10)  # True
