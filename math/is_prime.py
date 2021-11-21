from math import sqrt


def is_prime(num: int) -> str:
    if num == 2:
        return "Bilangan Prima"

    if num < 2 or num % 2 == 0:
        return "Bukan Bilangan Prima"

    for i in range(3, int(sqrt(num)), 2):
        if num % i == 0:
            return "Bukan Bilangan Prima"

    return "Bilangan Prima"


if __name__ == "__main__":
    # basic tests
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(5))

    # custom tests
    # print(is_prime(1234))
