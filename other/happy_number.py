# Mengecek apakah angka adalah sebuah happy number atau sad number
# https://en.wikipedia.org/wiki/Happy_number
def sum_digit(number):
    value_digit = 0
    while number > 0:
        digit = number % 10
        value_digit += digit * digit
        number = number // 10
    return value_digit


def happy_or_sad(number) -> str:
    """
    Happy number adalah sebuah angka yang dimana nanti akan kembali
    menjadi satu jika di lakukan penjumlahan kuadrat.

    13 = 1^2 + 3^2 = 10 = 1^2 + 0^2 = 1 -> Happy Number
    4 = 4^2 = 16 = 1^2 + 6^2 = 37 ... 2^2 + 0 = 4 -> Sad Number

    >>> happy_or_sad(23)
    'happy number'
    >>> happy_or_sad(44)
    'happy number'
    >>> happy_or_sad(8)
    'sad number'
    >>> happy_or_sad(20)
    'sad number'
    """
    set_value = set()
    happy, sad = "happy number", "sad number"
    while True:
        if number == 1:
            return str(happy)

        number = sum_digit(number)

        if number in set_value:
            return str(sad)

        set_value.add(number)


def main(args=None):
    import doctest

    doctest.testmod()

    # sample case
    happy_numbers = [1, 7, 23, 31, 44]
    unhappy_numbers = [2, 3, 8, 20, 4]

    for i in happy_numbers:
        print(happy_or_sad(i))

    print("\n")

    for i in unhappy_numbers:
        print(happy_or_sad(i))


if __name__ == "__main__":
    main()
