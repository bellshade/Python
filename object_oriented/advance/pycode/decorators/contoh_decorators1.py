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


def test_menyapa():
    assert 'BELLSHADE' == menyapa('bellshade')
