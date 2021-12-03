# membuat kelas dari kakaktua
class Kakaktua:
    # membuat fungsi
    def terbang(self):
        print("kakaktua bisa terbang")

    def berenang(self):
        print("kakaktua tidak bisa berenang")


# membuat fungsi dari penguin
class Pinguin:
    # membuat fungsi yang sama dengan kakaktua
    def terbang(self):
        print("pinguin tidak bisa terbang")

    def berenang(self):
        print("pinguin bisa berenang")


# membuat fungsi terbang dari kedua hewan
# dengan parameter burung
def test_terbang(burung):
    # memanggil fungsi terbang dari burung
    burung.terbang()


# memanggil kelas dan membuat objek dari kedua hewan
jikle = Kakaktua()
megi = Pinguin()

# memanggil fungsi terbang dari kedua hewan
test_terbang(jikle)
test_terbang(megi)
