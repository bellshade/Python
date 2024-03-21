class Pelajar:
    jenis_kelas = "bahasa"

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # metode instance
    def deksripsi(self):
        return f"{self.nama} berumur {self.umur} tahun"


janis = Pelajar("janis aneira", 22)
print(janis.deksripsi())
