# Dalam masalah ini, kami ingin menentukan semua kemungkinan kombinasi k
# nomor dari 1 ... n. Kami menggunakan backtracking untuk memecahkan masalah ini.
# Kompleksitas waktu: O(C(n,k)) yaitu O(n pilih k) = O((n!/(k! * (n - k)!)))


def generate_combination(n: int, k: int) -> list[list[int]]:
    """
    >>> generate_combination(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """

    result: list[list[int]] = []

    create_state(1, n, k, [], result)

    return result


def create_state(
    increment: int,
    total_number: int,
    level: int,
    current_list: list[int],
    total_list: list[list[int]],
) -> None:
    if level == 0:
        total_list.append(current_list[:])
        return
    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()


def print_state(total_list: list[list[int]]) -> None:
    for i in total_list:
        print(*i)


if __name__ == "__main__":
    import doctest

    # n = 4
    # k = 2
    # total_list = generate_combination(n, k)
    # print_state(total_list)
    doctest.testmod()
