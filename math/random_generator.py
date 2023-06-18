import os


def seed(n: int = 1, byteorder: str = "little"):
    """random seed

    random seed merupakan fungsi random yang
    mengacak secara psuode code bukan value
    random seed ini di perlukan dalam untuk
    mengvalidasi hasil suatu perhitungan atau
    model dalam perhitungan
    Args:
        n (int, optional): ini merupakan size ukuran bytes.
                           Defaults to 1.
    Returns:
        type: hasil pseucode dalam ukuran besar atau kecil
    """
    bytes_need = (n + 7) // 8
    randbytes = os.urandom(bytes_need)
    bit = int.from_bytes(randbytes, byteorder=byteorder)
    return bit


def random():
    """Random
    Describe:
    merupakan algoritma yang menghasilkan angka desimal
    random ini menggunakan algoritma lcg (linear congruential
    generator)
    refence:
    https://www.firstpr.com.au/dsp/rand31/p1192-park.pdf
    """
    a = 1664525
    c = 1013904223
    m = 2**32
    result = (a * (seed() * 1000) + c) % m
    return result / m


def generator_bit(n: int | float):
    """_summary_

    Args:
        n (int | float)=input nilai yang mau ke dalam bit

    Raises:
        ValueError: inputnya harus bilangan positif

    Returns:
        _type_: float
    """
    if n <= 0:
        raise ValueError("inputnya harus bilangan positif")
    k = n.bit_length()
    return seed(k) % n


def randomint(low=0, high=1):
    """
    Fungsi ini merupakan algoritma untuk menghasilkan output acak
    yang sesuai dengan batas low dan high
    Args:
        low (int, optional): input untuk batas bawah atau mini. Defaults to 0.
        high (int, optional): _description_. Defaults to 1.

    Returns:
        int:hasil dari latihan
    """
    return generator_bit(high - low + 1) + low


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
