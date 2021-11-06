class PekerjaTambang:
    # private variabel
    __nama = None
    __jabatan = None

    # konstruktor
    def __init__(self, nama, jabatan):
        self.__nama = nama
        self.__jabatan = jabatan

    # membuat fungsi yang bersifat private

    def __menampilkan(self):
        # memangakses private objek
        print("Nama: ", self.__nama)
        print("Jabatan: ", self.__jabatan)

    # fungsi yang bersifat publik

    def menampilkan_data(self):
        self.__menampilkan()


# membuat objek dan menampilkannya
pekerja1 = PekerjaTambang("James", "Research")

# menampilkan objek yang dimana terdapat fungsi private
pekerja1.menampilkan_data()
