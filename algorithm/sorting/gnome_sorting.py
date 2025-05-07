def gnome_sorting(daftar: list) -> list:
    """
    Implementasi dari algoritma gnome sorting

    fungsi yang menerima daftar yang dapat nantinya diubah
    dan diurut dengan elemen heterogen yang bisa dibandingkan,
    lalu mengembalikan list tersebut dalam urutan menaik

    Parameter:
        daftar (list): data yang ingin diberikan

    Return:
        (list): hasil sorting gnome

    Contoh:
    >>> gnome_sorting([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    """
    if len(daftar) <= 1:
        return daftar

    i = 1
    while i < len(daftar):
        if daftar[i - 1] <= daftar[i]:
            i += 1
        else:
            # tukar elemen jika tidak dalam urutan yang bener
            daftar[i - 1], daftar[i] = daftar[i], daftar[i - 1]
            i -= 1
            if i == 0:
                i = 1
    return daftar


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
