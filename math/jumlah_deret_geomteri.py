# informasi tentang geometri progression
# https://en.wikipedia.org/wiki/Geometric_progression


def jumlah_deret_geometri(utama: int, rasio_umum: int, jumlah: int) -> int:
    """
    Menghitung jumlah deret geometri
    >>> jumlah_deret_geometri(1, 2, 10)
    1023.0
    >>> jumlah_deret_geometri(1, 10, 5)
    11111.0
    >>> jumlah_deret_geometri(0, 2, 10)
    0.0
    """
    if rasio_umum == 1:
        # Rumus jumlah jika rasio umum adalah 1
        return jumlah * utama

    # Rumus untuk mencari jumlah n suku dari Progresi Geometris
    return (utama / (1 - rasio_umum)) * (1 - rasio_umum**jumlah)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
