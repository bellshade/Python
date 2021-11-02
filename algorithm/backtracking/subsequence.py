# Dalam masalah ini, kami ingin menentukan semua kemungkinan turunan
# dari urutan yang diberikan.
# Kami menggunakan backtracking untuk memecahkan masalah ini.
# Kompleksitas waktu: O(2^n),
# di mana n menyatakan panjang barisan yang diberikan.

from typing import Any, List


def generate_subsequence(sequence: List[Any]) -> None:
    """
    >>> seq: List[Any] = [3, 1, 2, 4]
    >>> seq.clear()
    >>> seq.extend(["A", "B", "C"])
    >>> generate_subsequence(seq)
    []
    ['C']
    ['B']
    ['B', 'C']
    ['A']
    ['A', 'C']
    ['A', 'B']
    ['A', 'B', 'C']
    """
    create_state_space_tree(sequence, [], 0)


def create_state_space_tree(
    sequence: List[Any], current_subsequence: List[Any], index: int
) -> None:
    """
    membuat state_space_tree untuk beralih melalui setiap
    cabang menggunakan DFS.
    Kita tahu bahwa setiap state bagian memiliki tepat dua anak.
    Ini berakhir ketika mencapai
    akhir dari urutan yang diberikan.
    """

    if index == len(sequence):
        print(current_subsequence)
        return

    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.pop()


if __name__ == "__main__":
    import doctest

    seq: List[Any] = [3, 1, 2, 4]
    generate_subsequence(seq)
    seq.clear()
    seq.extend(["A", "B", "C"])
    generate_subsequence(seq)
    doctest.testmod()
