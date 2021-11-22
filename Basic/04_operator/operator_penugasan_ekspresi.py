"""
Operator Walrus
=== versi Python yang didukung: 3.8+ ===

Operator Walrus adalah operator jenis Assignment Expression
yang merupakan operator baru yang ditambahkan pada Python versi ke 3.8

Fungsi dari operator Walrus ini adalah melakukan pengisian
sekaligus mengembalikan nilai dan mempersingkat sintaks program

+------------+--------------+-----------------+
|   Simbol   |    Contoh    |   Sama Dengan   |
|------------|--------------|-----------------|
|    :=      |  walrus := 5 |   walrus = 5    |
|            |              |  return walrus  |
+------------+--------------+-----------------+
"""


# Contoh dibawah ini dapat dilihat perbedaannya jika melalui CLI Python
# Tidak akan mengembalikan nilai, hanya melakukan pengisian
# walrus = False


# Akan mengembalikan nilai,
# operator walrus melakukan pengisian nilai sekaligus mengembalikan nilai
# Walrus digunakan pada if statement,
# Maka dari itu jika digunakan sebagai assignment harus diberi tanda kurung ()
# Agar tidak memunculkan SyntaxError
# (walrus2 := True)


# Misal dibuat fungsi sederhana func()
def func(num):
    return num + 1


# Jika tanpa walrus, agar tidak duplikat maka fungsi func() dimasukkan ke variabel
# x = func(4)
# if x >= 5:
#     print(x)


# Jika memakai operator Walrus maka bisa langsung dipakai pada if statement
# Di bawah ini adalah contoh yang salah
# Mengembalikan nilai True
# Karena terbaca x di assign 5 >= 5
# if x := func(4) >= 5:
#     print(x)


# Di bawah ini adalah contoh yang benar
# Mengembalikan nilai 5
# x akan diisi nilai dari func(4)
# Lalu dicek apakah lebih dari sama dengan 5
# Terakhir akan print nilai dari x
if (x := func(4)) >= 5:
    print(x)
