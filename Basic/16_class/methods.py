class SegiEmpat:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        """
        metode ini akan mengembalikan luas bangun menggunakan
        hasil perkalian panjang dan lebar
        """
        return self.panjang * self.lebar

    @classmethod
    def kotak(cls, sisi):
        """
        metode ini akan mengembalikan suatu objek kotak
        """
        return cls(sisi, sisi)

    @staticmethod
    def jenis_bangun(panjang, lebar):
        """
        metode ini akan mengembalikan jenis segiempat, apakah
        persegi atau persegipanjang
        """
        return "persegi" if panjang == lebar else "persegi panjang"


print(SegiEmpat.jenis_bangun(10, 5))
# output: persegi panjang

persegi_panjang = SegiEmpat(10, 5)
print(persegi_panjang.hitung_luas())
# output: 50

print(SegiEmpat.jenis_bangun(3, 3))
# output: persegi

persegi = SegiEmpat.kotak(3)
print(persegi.hitung_luas())
# output: 9
