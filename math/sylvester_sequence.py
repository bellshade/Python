# Menghitung angka ke-n dalam deret Sylvester
#  https://en.wikipedia.org/wiki/Sylvester%27s_sequence


def sylvester(number: int) -> int:
    """
    >>> sylvester(8)
    113423713055421844361000443

    >>> sylvester(-1)
    Traceback (most recent call last):
    ...
    ValueError: angka tidak boleh negatif
    """
    assert isinstance(number, int), f"nomor {number} tidak integer"

    if number == 1:
        return 2
    elif number < 1:
        raise ValueError("angka tidak boleh negatif")
    else:
        num = sylvester(number - 1)
        lower = num - 1
        upper = num
        return lower * upper + 1


if __name__ == "__main__":
    print(f"nomor ke 8 dalam deret sylvester {sylvester(8)}")
