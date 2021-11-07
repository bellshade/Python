# Original List

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original : {}".format(original))

# Iterable

original_dua = [value for value in range(5, 11)]

print("Original Range : {}".format(original_dua))

# Exponent List Comprehension

exp_list = [item ** 2 for item in original]

print("Exponent List : {}".format(exp_list))

# If List Comprehension

genap = [item for item in original if item % 2 == 0]

print("Genap : {}".format(genap))

# Expression List Comprehension

elemen = ["Api", "Air", "Tanah", "Udara"]

huruf_awal = [item[0] for item in elemen]

print("Huruf Awal : {}".format(huruf_awal))
