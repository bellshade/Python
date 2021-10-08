class Hewan:
    def __init__(self, nama_hewan, suara):
        self.nama_hewan = nama_hewan
        self.suara = suara

    def __repr__(self):
        return "kucing {} bersuara {}".format(self.nama_hewan, self.suara)


if __name__ == "__main__":
    hewan = Hewan("sapi", "Mooo")
    print(f" {hewan.nama_hewan} bersuara :{hewan.suara}")
