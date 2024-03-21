# Contoh Decorators

## Contoh 1: Menjadikan Fungsi Sebagai Objek

Pada contoh kita yang pertama, kita akan membuat fungsi dengan nama **menyapa**.

```py
# Contoh Decorator 1
def menyapa(nama : str) -> str:
    """Contoh pada decorator yang satu ini, kita hanya cukup satu fungsi
    yang mengembalikan nilai Uppercase
    :param nama: masukan bellshade pada parameter nama
    >>> nama = "bellshade"
    >>> salam = menyapa
    >>> salam(nama)
    'BELLSHADE'
    """
    return nama.upper()

```

## Contoh 2: Menjadikan Fungsi Sebagai Parameter Fungsi

Pada contoh kita yang kedua, kita akan membuat beberapa fungsi dengan nama **wpu, terbuka, & bellshade**.

```py
from typing import Callable


# Contoh Decorator 2
def wpu(str1 : str) -> str:
    # Fungsi wpu yang mengembalikan nilai string upper
    return str1.upper()


def terbuka(str2 : str) -> str:
    # Fungsi terbuka yang mengembalikan nilai string lower
    return str2.lower()


def bellshade(func : Callable) -> str:
    """
    Fungsi ini akan menampung fungsi dari luar fungsi bellshade
    :param func: parameter fungsi yang akan menampung fungsi lainnya
    >>> mhs1 = wpu
    >>> mhs2 = terbuka
    >>> bellshade(mhs1)
    'HALO SOBAT BELLSHADE!!!'
    >>> bellshade(mhs2)
    'halo sobat bellshade!!!'
    """
    return func("Halo Sobat bellshade!!!")

```

## Contoh 3: Mengembalikan Fungsi Di Dalam Fungsi

Pada contoh kita yang ketiga, kita akan membuat beberapa fungsi dengan nama **users & belajar**.

```py
from typing import Callable


# Contoh Decorator 3
def users(nama : str) -> Callable:
    """
    Fungsi ini hanya mengembalikan sebuah fungsi
    :param name: Parameter nama dari fungsi users
    >>> nama = 'Udin'
    >>> belajar = users(nama)
    >>> belajar('Python')
    'Udin sedang belajar: Python'
    """

    def belajar(str1 : Callable) -> str:
        """
        Fungsi ini akan membungkus parameter dari users
        """

        # Return ini mengembalikan nilai untuk fungsi (belajar)
        return f'{nama} sedang belajar: {str1}'

    # Di return terluar, kita akan mengembalikan nilai berupa fungsi (belajar)
    return belajar

```