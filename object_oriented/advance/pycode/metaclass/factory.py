import sys
import logging
from src import IPeople


class Mahasiswa(IPeople):
    """Kelas Mahasiswa tidak memiliki argument or params
    akan tetapi, setiap kelas yang instance dari IPeople
    akan memiliki private variable.

    :var __nama: Implementasi variable dari IPeople
    :var __posisi: Implementasi variable dari IPeople

    >>> mhs = Mahasiswa()
    >>> mhs.major()
    'Mahasiswa UNPAS'
"""
    __nama: str = 'Bellshade'
    __posisi: str = 'Mahasiswa UNPAS'

    def __call__(self) -> None:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.debug(f'Nama: {self.__nama}')
        logging.debug(f'Posisi: {self.major()}')

    def major(self):
        return __class__.__posisi


class Dosen(IPeople):
    """Kelas Mahasiswa tidak memiliki argument or param
    akan tetapi, setiap kelas yang instance dari IPeople
    akan memiliki private variable.
    :var __nama: Implementasi variable dari IPeople
    :var __posisi: Implementasi variable dari IPeople
    >>> mhs = Dosen()
    >>> mhs.major()
    'Dosen UNPAS'
    """
    __nama: str = 'Sandhika Galih'
    __posisi: str = 'Dosen UNPAS'

    def __call__(self):
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.debug(f'Nama: {self.__nama}')
        logging.debug(f'Posisi: {self.major()}')

    def major(self):
        return __class__.__posisi


class PeopleFactory:

    @staticmethod
    def create_people(role_people):
        if role_people[0].lower() == 'mahasiswa':
            return mhs()
        elif role_people[0].lower() == 'dosen':
            return dosen()
        else:
            logging.warning('Argument tidak dikenal!')


def test_major_mahasiswa_factories():
    mhs1 = Mahasiswa()
    assert mhs1.major() == 'Mahasiswa UNPAS'


mhs = Mahasiswa()
dosen = Dosen()

if __name__ == '__main__':
    prompt = sys.argv[1:]
    try:
        if len(prompt) >= 0:
            PeopleFactory.create_people(prompt)
    except IndexError:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.WARN)
        logging.warning('Argument mahasiswa atau dosen tidak terdeteksi!')
