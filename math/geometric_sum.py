def geoSum(suku_pertama, rasio, jumlah_deret):
    """
    Menghitung deret geometri berhingga dari n buah suku
    dengan suku pertama a dan rasio r. Rumus umum berlaku
    jika r tidak sama dengan 1 dan a tidak sama dengan 0

    Rumus : a * ((1 -  pow(r, n)) / (1 - r))

    Mengembalikan nilai perhitungan rumus

    Valid input :
    >>> geoSum(0, 0.5, 3)
    21.0

    Invalid input :
    >>> geoSum(3, 1, 5)
    ValueError: Rasio tidak boleh sama dengan 1
    """
    a = suku_pertama
    r = rasio
    n = jumlah_deret

    if a == 0:
        raise ValueError("Suku pertama tidak boleh 0")
    elif r == 1:
        raise ValueError("Rasio tidak boleh sama dengan 1")
    else:
        result = a * ((1 - pow(r, n)) / (1 - r))
    return result


# menampilkan 93.0
hasil1 = geoSum(3, 2, 5)
print(hasil1)

# me-raise exception
hasil2 = geoSum(3, 1, 5)
print(hasil2)
