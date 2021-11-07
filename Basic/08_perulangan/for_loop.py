# penggunaan for loop pada string
nama = "zoelfekre"
for tampil_nama in nama:
    print(tampil_nama)

# penggnaan for loop pada list
print("\ntampil nama siswa dalam list")
nama_siswa = ["zoelfekre", "dwi", "dian"]
for tampil_siswa in nama_siswa:
    print(tampil_siswa)

# penggunaan for loop pada tuple
print("\ntampil nama siswa dalam tuple")
nama_siswa_tuple = ("zoelfekre", "dwi", "dian")
for tampil_siswa_tuple in nama_siswa:
    print(tampil_siswa_tuple)


# penggunaan break pada looping
angka_saya = 0
for angka_saya in range(0, 10):
    print(angka_saya)
    if angka_saya == 5:
        break

# penggunaan continue pada looping
angka_saya1 = 0
for angka_saya1 in range(0, 10):
    if angka_saya1 == 5:
        continue
    print(angka_saya1)
