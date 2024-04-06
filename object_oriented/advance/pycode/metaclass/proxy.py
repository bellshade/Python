import logging
from src import IUniv
from typing import Callable


# Logging Config
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class Mahasiswa(IUniv):
    """ Kelas ini tidak memiliki parameter tetapi memiliki fungxi
    :func division: Fungsi untuk memberikan informasi
    >>> guest = Mahasiswa()
    >>> guest.division()
    """

    def division(self):
        logging.debug('Mahasiswa')


class Dosen(IUniv):
    """ Kelas ini tidak memiliki parameter tetapi memiliki fungxi
    :func division: Fungsi untuk memberikan informasi
    >>> guest = Dosen()
    >>> guest.division()
    """

    def division(self):
        logging.debug('Dosen')


class Rektor(IUniv):
    """ Kelas ini tidak memiliki parameter tetapi memiliki fungxi
    :func division: Fungsi untuk memberikan informasi
    >>> guest = Rektor()
    >>> guest.division()
    """

    def division(self):
        logging.debug('Rektor')


class UnivProxy(IUniv):
    """ Kelas ini tidak akan menerima parameter apapun,
    kelas ini hanya terdiri dari cunstructor init yang
    hanya memiliki attribute kelas.
    :attribute dosen: Menginstansiasikan kelas Dosen di Pattern
    :attribute rektor: Menginstansiasikan kelas Rektor di Pattern
    >>> proxy = UnivProxy()
    >>> proxy()
    """
    def __init__(self):
        self.dosen = Dosen()
        self.rektor = Rektor()
        self.mahasiswa = Mahasiswa()

    def __call__(self):
        self.division()

    def division(self):
        logging.debug('ProxyPattern Functionality.\n==========')
        self.dosen.division()
        self.rektor.division()
        self.mahasiswa.division()
        logging.debug('ProxyPattern Functionality.\n==========')


if __name__ == '__main__':
    proxy: Callable = UnivProxy()
    proxy()
