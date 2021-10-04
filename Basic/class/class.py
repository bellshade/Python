class Hewan:
    def __init__(self, suara):
        self.suara = suara

    def bersuara(self):
        """
        metode ini berfungsi untuk menampilkan atribut suara
        """
        print(self.suara)


# contoh membuat objek
kucing = Hewan(suara="MIAWW MIAWW")

# mengakses metode bersuara
kucing.bersuara()
# output: "MIAWW MIAWW"
