# Ada 3 jenis metode class, yaitu:
# metode biasa, classmethod dan, staticmethod

class SegiEmpat:

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    # metode biasa
    # metode ini harus memiliki parameter self, yang berguna
    # untuk mengakses atribut kelas, untuk menggunakannya
    # harus melalui objek
    def hitung_luas(self):
        """
        metode ini akan mengembalikan luas bangun menggunakan
        hasil perkalian panjang dan lebar
        """
        return self.panjang * self.lebar

    # classmethod
    # metode ini menggunakan deokrator @classmethod dan
    # harus memiliki parameter clf, yang berguna untuk
    # mengakses atributnya, untuk menggunakannya dapat
    # langsung dari kelasnya tanpa menggunakan objek
    @classmethod
    def kotak(cls, sisi):
        """
        metode ini akan mengembalikan suatu objek kotak
        """
        return cls(sisi, sisi)

    # staticmethod
    # metode ini menggunakan deokrator @staticmethod,
    # metode ini sama seperti classmethod namun tidak perlu
    # menggunakan parameter wajib
    @staticmethod
    def jenis_bangun(panjang, lebar):
        """
        metode ini akan mengembalikan jenis segiempat, apakah
        persegi atau persegipanjang
        """
        if panjang == lebar:
            return 'persegi'
        elif panjang != lebar:
            return 'persegi panjang'


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
