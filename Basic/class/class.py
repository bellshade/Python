# Kelas dapat diartikan sebagai kerangka untuk membuat suatu objek,
# membuat suatu kelas sama dengan membuat tipe baru, dan
# meng-inisialisasi tipe tersebut sama dengan menghasilkan objek baru.

# Kelas memiliki atribut untuk mempertahankan nilainya,
# dan memilki metode untuk mengubah nilainya.
# Untuk membuat class di python dapat menggunakan keyword class.

class Warung:

    # Atribut adalah variable yang ada didalam kelas,
    # seluruh atribut bersifat publik dan dapat diakses
    # menggunakan tanda titik (.) dibelakang objek.
    # contoh atribut
    menu_makanan = []

    # Metode adalah fungsi yang dibuat didalam kelas,
    # metode harus memiliki parameter self, parameter ini
    # berfungsi agar dapat mengakses variable yang ada
    # didalam kelas, untuk membuat metode dapat menggunakan
    # keyword def. Untuk mengakses sebuah metode harus melalui
    # objek, menggunakan tanda titik (.) dibelakang objek.
    # contoh metode
    def tambah_menu(self, makanan):
        """
        metode ini berfungsi untuk menambahkan data
        ke atribut menu_makanan
        makanan = string
        >>> Warung().tambah_menu('nasi goreng')
        menu_makanan akan bernilai ['nasi goreng']
        """
        self.menu_makanan.append(makanan)


# contoh membuat objek
depot_adem = Warung()

# contoh mengakses atribut menu_makanan dan menaruhnya divariable menu_depot_adem
menu_depot_adem = depot_adem.menu_makanan

# akan bernilai list kosong
print(menu_depot_adem)
# output: []

# mengakses metode tambah_menu untuk mengubah argumen menu_makanan
depot_adem.tambah_menu('mie goreng')
depot_adem.tambah_menu('sate ayam')

# akan berisi data yang tadi ditambahkan
print(menu_depot_adem)
# output: ['mie goreng', 'sate ayam']
