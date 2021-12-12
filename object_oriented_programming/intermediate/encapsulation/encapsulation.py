class Motor:
    # membuat variabel yang bersifat private
    __kecepatan = 0

    def __init__(self):
        # memasukkan value dalam variabel kecepatan
        self.__kecepatan = 120

    # membuat fungsi untuk memanggil variabel
    # dari kecepatan
    def jalan(self):
        print("jalan dengan kecepatan {} km".format(self.__kecepatan))


# membuat objek dari class Motor
matic = Motor()
matic.jalan()

# variabel tidak berubah karena sebelumnya
# bersifat private
matic.__kecepatan = 300
matic.jalan()
