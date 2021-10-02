"""
operator logika (Logical Operator) digunakan untuk
menggabungkan pernyataan kondisional

bingung?
mari kita buat contohnya
"""

# variabel
x = 5

# operator "and" digunakan untuk mengecek
# apakah kedua pernyataan yang diberikan bernilai True

print("x < 6 and x > 1:", x < 6 and x > 1)  # True
print("x > 6 and x > 1:", x > 6 and x > 1)  # False

# operator "or" digunakan untuk mengecek
# apakah salah satu dari dua pernyataan bernilai True

print("x > 6 or x > 1:", x > 6 or x > 1)  # True
print("x > 6 or x < 1:", x > 6 or x < 1)  # False

# operator "not" digunakan untuk mengecek
# apakah nilai tersebut bernilai False

print(not(x <= 6))  # False
print(not(x >= 10))  # True
