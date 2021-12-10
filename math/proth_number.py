# kalkulasi nth angka proth
# https://handwiki.org/wiki/Proth_number
import math


def proth(angka: int) -> int:
    """
    >>> proth(-3)
    Traceback (most recent call last):
    ...
    ValueError: angka tidak boleh kurang dari 1
    >>> proth(6.0)
    Traceback (most recent call last):
    ...
    TypeError: Angka harus integer
    """
    if not isinstance(angka, int):
        raise TypeError("Angka harus integer")

    if angka < 1:
        raise ValueError("angka tidak boleh kurang dari 1")

    elif angka == 1:
        return 3

    elif angka == 2:
        return 5

    else:
        # +1 untuk biner yang dimulai pada 0  contoh 2 ^0, 2 ^1 dan lainnya
        block_index = int(math.log(angka // 3, 2)) + 2
        proth_list = [3, 5]
        proth_index = 2
        increment = 3

        for block in range(1, block_index):
            for _ in range(increment):
                proth_list.append(2 ** (block + 1) + proth_list[proth_index - 1])
                proth_index += 1
            increment *= 2

    return proth_list[angka - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    for angka in range(11):
        value = 0
        try:
            value = proth(angka)
        except ValueError:
            print(f"{angka}")
            continue

        print(f"{angka}, angka proth: {value}")
