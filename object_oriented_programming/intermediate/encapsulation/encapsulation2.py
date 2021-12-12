class Motor:
    __kecepatan = 0

    def __init__(self):
        self.__kecepatan = 120

    def jalan(self):
        print("jalan dengan kecepatan {} km".format(self.__kecepatan))

    def gantiKecepatan(self, kecepatan_sekarang):
        self.__kecepatan = kecepatan_sekarang


matic = Motor()
matic.jalan()

matic.gantiKecepatan(60)
matic.jalan()
