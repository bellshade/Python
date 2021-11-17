# kalkulasi nth dari angka proth
# sumber wikipedia
# https://handwiki.org/wiki/Proth_number

import math


def proth(number: int) -> int:
    """
    >>> proth(6)
    25
    >>> proth(0)
    Traceback (most recent call last):
    ...
    ValueError: input value dari [number=0] harus lebih > 0
    """
    if not isinstance(number, int):
        raise TypeError(f"input value dari [number={number}] harus integer")

    if number < 1:
        raise ValueError(f"input value dari [number={number}] harus lebih > 0")
    elif number == 1:
        return 3
    elif number == 2:
        return 5
    else:
        # +1 untuk biner mulai dari 0 yaitu 2^0, 2^1, dll.
        # +1 untuk memulai urutan pada nomor Proth ke-3
        # Oleh karena itu, kami memiliki +2 dalam pernyataan di bawah ini
        block_index = int(math.log(number // 3, 2)) + 2

        proth_list = [3, 5]
        proth_index = 2
        increment = 3
        for block in range(1, block_index):
            for move in range(increment):
                proth_list.append(2 ** (block + 1) + proth_list[proth_index - 1])
                proth_index += 1
            increment *= 2

    return proth_list[number - 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
