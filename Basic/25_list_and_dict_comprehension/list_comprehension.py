# List Comprehension
# adalah metode untuk menambahkan anggota dari suatu list melalui for loop

# Syntax dari List Comprehension adalah
# [expression for item in iterable]

# Original List

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Original : {original}")
# Output = Original : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Implementasi List Comprehension dengan Iterable

original_dua = [value for value in range(5, 11)]

print(f"Original Range : {original_dua}")
# Output = Original Range : [5, 6, 7, 8, 9, 10]

# Implementasi List Comprehension dengan Pemangkatan (Exponential)

exp_list = [item**2 for item in original]

print(f"Exponent List : {exp_list}")
# Output = Exponent List : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Implementasi List Comprehension dengan If Else

genap = [item for item in original if item % 2 == 0]

print(f"Genap : {genap}")
# Output = Genap : [2, 4, 6, 8, 10]

# Implementasi List Comprehension dengan Expression

elemen = ["Api", "Air", "Tanah", "Udara"]

huruf_awal = [item[0] for item in elemen]

print(f"Huruf Awal : {huruf_awal}")
# Output = Huruf Awal : ['A', 'A', 'T', 'U']

# Implementasi List Comprehension dengan Nested List
# Implementasi matriks 3 dimensi

matriks_3_3 = [["X" for _ in range(3)] for _ in range(3)]
# Output = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]

# Menggabungkan List Lebih dari satu dimensi

indonesia = [["Kudus", "Solo"], ["Bekasi", "Bogor"], ["Madiun", "Malang"]]

list_kota = [kota for grup_kota in indonesia for kota in grup_kota]
# Output = ['Kudus', 'Solo', 'Bekasi', 'Bogor', 'Madiun', 'Malang']
