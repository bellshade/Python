# dalam soal contoh ini kita ingin menentukan semua
# kemungkinan kombinasi dari k
# angka dari 1 ... n. kita menggunakan algoritma
# backtracking untuk memcahkan masalah

from __future__ import annotations


def generate_all_combinations(n: int, k: int) -> list[list[int]]:
    """
    >>> generate_all_combinations(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    result: list[list[int]] = []
    create_all_state(1, n, k, [], result)
    return result


def create_all_state(
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
        create_all_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()


def print_all_state(total_list: list[list[int]]) -> None:
    for i in total_list:
        print(*i)


if __name__ == "__name__":
    import doctest

    doctest.testmod()
    n = 4
    k = 2
    total_list = generate_all_combinations(n, k)
    print_all_state(total_list)
