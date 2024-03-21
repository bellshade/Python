from abc import ABCMeta, abstractmethod, abstractstaticmethod


# FACTORY DESIGN PATTERN
class IPeople(metaclass=ABCMeta):
    __nama: str
    __posisi: str

    @abstractstaticmethod
    def major(self) -> str:
        return ''
        """ Interface IPeople Method """


# PROXY DESIGN PATTERN
class IUniv(metaclass=ABCMeta):

    @abstractstaticmethod
    def division(self):
        """ Interface IUniv Method """


# SINGLETON DESIGN PATTERN
class IMahasiswa(metaclass=ABCMeta):

    @abstractstaticmethod
    def log_instance(self):
        """ Implement in child Class"""


# COMPOSITE DESIGN PATTERN
class IJurusan(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, mahasiswa):
        """ Implement in child Class """

    @abstractstaticmethod
    def jumlah_mahasiswa(self):
        pass
