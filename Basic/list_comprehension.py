# List Comprehension
# adalah metode untuk menambahkan anggota dari suatu list melalui for loop

# Syntax dari List Comprehension adalah
# [expression for item in iterable]

# Original List

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original : {}".format(original))

# Implementasi List Comprehension dengan Iterable

original_dua = [value for value in range(5, 11)]

print("Original Range : {}".format(original_dua))

# Implementasi List Comprehension dengan Pemangkatan (Exponential)

exp_list = [item ** 2 for item in original]

print("Exponent List : {}".format(exp_list))

# Implementasi List Comprehension dengan If Else

genap = [item for item in original if item % 2 == 0]

print("Genap : {}".format(genap))

# Implementasi List Comprehension dengan Expression

elemen = ["Api", "Air", "Tanah", "Udara"]

huruf_awal = [item[0] for item in elemen]

print("Huruf Awal : {}".format(huruf_awal))
