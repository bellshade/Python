nama_hewan = ["gajah", "sapi", "kuda", "buaya"]

# menampilkan isi list
print(nama_hewan)

# menampilkan isi list dengan index
print(nama_hewan[0])
print(nama_hewan[1])

# mengganti satu index list
nama_hewan[0] = "kucing"
print(nama_hewan)

# menghitung jumlah list
print(len(nama_hewan))

# campur beberapa tipe data dalam satu list
list_saya = ["gajah", 12, True, "makan"]
print(list_saya)

# menggunakan konstruktor pada pembuatan list
list_hewan1 = list(("kijang", "sapi", "kucing", "ayam"))
print(list_hewan1)

# menggunakan looping untuk menampilkan list
for jenis_hewan in list_hewan1:
    print(jenis_hewan)
