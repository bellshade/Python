import logging
from src import IMahasiswa

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class SingletonMahasiswa(IMahasiswa):
    """Kelas Mahasiswa tidak memiliki argument or params
    akan tetapi, setiap kelas yang instance dari IPeople
    akan memiliki private variable.

    :param nama: Implementasi variable dari IPeople
    :param jurusan: Implementasi variable dari IPeople

    >>> mhs = SingletonMahasiswa('Bellshade', 'Helper')
    >>> mhs.log_instance(mhs)
    """

    __instance = None

    @staticmethod
    def get_instance(self):
        """ Fungsi ini mengambil __instance None, jika instance masih
        bertipe None maka akan di isi oleh instance object pertama kali
        karena pola Singleton ini membatasi kegunaan instance object.
        """
        if SingletonMahasiswa.__instance is None:
            SingletonMahasiswa('Bellshade', 'Helper')
        else:
            return SingletonMahasiswa.__instance

    def __init__(self, nama, jurusan):
        if SingletonMahasiswa.__instance is not None:
            raise Exception('Singleton tidak dapat membuat instance lebih dari sekali!')
        else:
            self.nama = nama
            self.jurusan = jurusan
            SingletonMahasiswa.__instance = self

    @staticmethod
    def log_instance(self):
        """
        Fungsi ini merupakan implementasi dari kelas Abstrak IMahasiswa
        """
        logging.debug(f'Nama: {SingletonMahasiswa.__instance.nama}')
        logging.debug(f'Jurusan: {SingletonMahasiswa.__instance.jurusan}')


if __name__ == '__main__':
    p = SingletonMahasiswa('Sandhika Galih', 'Dosen Informatika')
    p2 = SingletonMahasiswa('Tono', 'Mahasiswa Informatika')
    p.log_instance(p)
    p2.log_instance(p2)
