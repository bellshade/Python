import logging
from src import IJurusan

# Logging Config
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class Informatika(IJurusan):
    """Kelas ini akan mengimplementasi kelas abstrak IJurusan
    yang memiliki parameter mahasiswa dari kelas abstrak
    :param mahasiswa: Parameter untuk jumlah Informatika
    ada berapa jumlah mahasiswa Informatika.
    >>> mhs1 = Informatika(30)
    >>> mhs1.jumlah_mahasiswa()
    30
    """

    def __init__(self, mahasiswa):
        self.mahasiswa = int(mahasiswa)

    def jumlah_mahasiswa(self):
        return self.mahasiswa


class Management(IJurusan):
    """Kelas ini akan mengimplementasi kelas abstrak IJurusan
    yang memiliki parameter mahasiswa dari kelas abstrak
    :param mahasiswa: Parameter untuk jumlah Management
    ada berapa jumlah mahasiswa Management.
    >>> mhs1 = Management(10)
    >>> mhs1.jumlah_mahasiswa()
    10
    """

    def __init__(self, mahasiswa):
        self.mahasiswa = int(mahasiswa)

    def jumlah_mahasiswa(self):
        return self.mahasiswa


class Jurusan(IJurusan):
    """Kelas ini akan mengimplementasi kelas abstrak IJurusan
    yang memiliki parameter mahasiswa dari kelas abstrak
    :param mahasiswa: Parameter ini harus berisikan informasi
    ada berapa jumlah mahasiswa Management.
    >>> mhs1 = Informatika(30)
    >>> mhs2 = Management(20)
    >>> jurusan = Jurusan(2)
    >>> jurusan.data_jurusan(mhs1)
    >>> jurusan.data_jurusan(mhs2)
    >>> jurusan.jumlah_mahasiswa()
    """

    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa
        self.jurusan_dasar = mahasiswa
        self.jumlah_jurusan = []

    def data_jurusan(self, mahasiswa_jurusan):
        self.jumlah_jurusan.append(mahasiswa_jurusan)
        self.mahasiswa += mahasiswa_jurusan.jumlah_mahasiswa()

    def jumlah_mahasiswa(self):
        logging.debug(f'Jumlah jurusan dasar: {self.jurusan_dasar}')
        for jurusan in self.jumlah_jurusan:
            logging.debug(f'{type(jurusan).__name__}: {jurusan.jumlah_mahasiswa()}')
        logging.debug(f'Total mahasiswa: {self.mahasiswa}')


def test_insert_data_informatika():
    mhs = Informatika(100)
    assert 100 == mhs.jumlah_mahasiswa()


def test_insert_data_management():
    mhs = Management(50)
    assert 50 == mhs.jumlah_mahasiswa()


if __name__ == '__main__':
    p1 = Informatika(30)
    p2 = Management(50)
    jurusan = Jurusan(2)
    jurusan.data_jurusan(p1)
    jurusan.data_jurusan(p2)
    jurusan.jumlah_mahasiswa()
