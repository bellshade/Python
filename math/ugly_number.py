# bilangan aneh adalah bilangan
# yang faktor primanya hanya 2, 3, 5
# urutannya
# 1, 2, 3, 4 ,5 ,6, 8, 9, 10, 12, 15, ...
# menunjukkan angka aneh pertama.
# dengan perjanjian
# 1 disertakan. deiberikan bilangan bilan n,
# kita harus menemukan bilangan aneh ke-n


def ugly_number(n: int) -> int:
    """
    return bilangan aneh
    >>> ugly_number(100)
    1536
    >>> ugly_number(0)
    1
    >>> ugly_number(20)
    36
    """
    ugly_num = [1]
    i2, i3, i5 = 0, 0, 0
    next_2 = ugly_num[i2] * 2
    next_3 = ugly_num[i3] * 3
    next_5 = ugly_num[i5] * 5

    for i in range(1, n):
        next_num = min(next_2, next_3, next_5)
        ugly_num.append(next_num)
        if next_num == next_2:
            i2 += 1
            next_2 = ugly_num[i2] * 2
        if next_num == next_3:
            i3 += 1
            next_3 = ugly_num[i3] * 3

    return ugly_num[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    print(f"{ugly_number(200)}")
