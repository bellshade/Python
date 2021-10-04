# membuat list
angka = [1, 2, 3, 4, 5]


# basic for loop
for item in angka:
    print(item)

# for loop and expression
for item in angka:
    print(item * 2)

for item in angka:
    print(item)
    if item == 3:
        break

for item in angka:
    if item == 3:
        continue
    print(item)

daftar = [1, 2, 3, 4, 5]
for item in daftar:
    print(item)
    break
else:
    print("Daftar Kosong")
