def tambah(angka1: float, angka2: float) -> float:
    """
    hasil dari pertambahan antara angka1 dan angka2
    >>> tambah(3.0, 2.0)
    5.0
    """
    return angka1 + angka2


def kurang(angka1: float, angka2: float) -> float:
    """
    hasil dari pengurangan antara angka1 dan angka2
    >>> kurang(3.0, 2.0)
    1.0
    """
    return angka1 - angka2


def kali(angka1: float, angka2: float) -> float:
    """
    hasil dari perkalian antara angka1 dan angka2
    >>> kali(3.0, 2.0)
    6.0
    """
    return angka1 * angka2


def pangkat(angka1: float, angka2: float) -> float:
    """
    hasil dari pangkat antara angka1 dan angka2
    >>> pangkat(3.0, 2.0)
    9.0
    """
    return angka1 ** angka2


def bagi(angka1: float, angka2: float) -> float:
    """
    hasil dari pembagian antara angka1 dan angka2
    >>> bagi(3.0, 2.0)
    1.5
    """
    return angka1 / angka2


def modulus(angka1: float, angka2: float) -> float:
    """
    hasil dari modulus antara angka1 dan angka2
    >>> modulus(3.0, 2.0)
    1.0
    """
    return angka1 % angka2


print(tambah(3, 2))
print(kurang(12, 4))
print(kali(3, 2))
print(pangkat(3, 2))
print(bagi(12, 4))
print(modulus(12, 4))

# menggunakan input
# angka1 = float(input("Masukkan angka pertama: "))
# angka2 = float(input("Masukkan angka kedua: "))
# print(tambah(angka1, angka2))
# print(kurang(angka1, angka2))
# print(kali(angka1, angka2))
# print(pangkat(angka1, angka2))
# print(bagi(angka1, angka2))
# print(modulus(angka1, angka2))
