def aliquot_sum(input_num: int) -> int:
    """
    Menemukan jumlah alikuot dari bilangan bulat input, di mana
    alikuot jumlah suatu bilangan  n
    sebagai jumlah semua
    bilangan asli kurang dari n
    yang membagi n secara merata. Untuk
    contoh, jumlah alikuot dari 15 adalah 1 + 3 + 5 = 9. Ini adalah
    implementasi O(n) sederhana.
    param input_num:
        bilangan bulat positif yang jumlah alikuotnya dapat ditemukan
    return:
        jumlah alikuot dari input_num, jika input_num positif.
    Jika tidak, naikkan ValueError
    Penjelasan Wikipedia: https://en.wikipedia.org/wiki/Aliquot_sum

    >>> aliquot_sum(19)
    1
    """
    if not isinstance(input_num, int):
        raise ValueError("input harus integer")
    if input_num <= 0:
        raise ValueError("input harus positif")

    return sum(
        divisor for divisor in range(1, input_num // 2 + 1) if input_num % divisor == 0
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
