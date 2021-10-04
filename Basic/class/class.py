class Kucing:
    suara = 'MIAWW MIAWW'

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
