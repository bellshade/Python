# Kelas dapat diartikan sebagai kerangka untuk membuat suatu objek,
# membuat suatu kelas sama dengan membuat tipe baru, dan
# meng-inisialisasi tipe tersebut sama dengan menghasilkan objek baru.

# Kelas memiliki atribut untuk mempertahankan nilainya,
# dan memilki metode untuk mengubah nilainya.
# Untuk membuat class di python dapat menggunakan keyword class.

class Kucing:

    # Atribut adalah variable yang ada didalam kelas,
    # seluruh atribut bersifat publik dan dapat diakses
    # menggunakan tanda titik (.) dibelakang objek.
    # contoh atribut
    suara = 'MIAWW MIAWW'

    # Metode adalah fungsi yang dibuat didalam kelas,
    # metode harus memiliki parameter self, parameter ini
    # berfungsi agar dapat mengakses variable yang ada
    # didalam kelas, untuk membuat metode dapat menggunakan
    # keyword def. Untuk mengakses sebuah metode harus melalui
    # objek, menggunakan tanda titik (.) dibelakang objek.
    # contoh metode
    def bersuara(self):
        """
        metode ini berfungsi untuk menampilkan atribut suara
        """
        print(self.suara)


# contoh membuat objek
tomcat = Kucing()

# mengakses metode bersuara
tomcat.bersuara()
# output: "MIAWW MIAWW"
