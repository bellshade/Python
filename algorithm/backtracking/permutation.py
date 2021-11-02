# Dalam masalah ini, kami ingin menentukan semua kemungkinan permutasi
# dari urutan yang diberikan.
# Kami menggunakan backtracking untuk memecahkan masalah ini.
# Kompleksitas waktu: O(n! * n),
# di mana n menyatakan panjang barisan yang diberikan.

from typing import List, Union


def generate_permutation(sequence: List[Union[int, str]]) -> None:
    """
    >>> from typing import List, Union
    >>> sequence: List[Union[int, str]] = [3, 1, 2, 4]
    >>> generate_permutation(sequence)
    [3, 1, 2, 4]
    [3, 1, 4, 2]
    [3, 2, 1, 4]
    [3, 2, 4, 1]
    [3, 4, 1, 2]
    [3, 4, 2, 1]
    [1, 3, 2, 4]
    [1, 3, 4, 2]
    [1, 2, 3, 4]
    [1, 2, 4, 3]
    [1, 4, 3, 2]
    [1, 4, 2, 3]
    [2, 3, 1, 4]
    [2, 3, 4, 1]
    [2, 1, 3, 4]
    [2, 1, 4, 3]
    [2, 4, 3, 1]
    [2, 4, 1, 3]
    [4, 3, 1, 2]
    [4, 3, 2, 1]
    [4, 1, 3, 2]
    [4, 1, 2, 3]
    [4, 2, 3, 1]
    [4, 2, 1, 3]
    """
    state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])


def state_space_tree(
    sequence: List[Union[int, str]],
    current_sequence: List[Union[int, str]],
    index: int,
    index_used: List[int],
) -> None:

    """
    Membuat pohon ruang untuk iterasi melalui setiap cabang menggunakan DFS.
    Kita tahu bahwa setiap negara memiliki persis len (urutan) - anak-anak indeks.
    Ini berakhir ketika mencapai akhir urutan yang diberikan.
    """
    if index == len(sequence):
        print(current_sequence)
        return

    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = True
            state_space_tree(sequence, current_sequence, index + 1, index_used)
            current_sequence.pop()
            index_used[i] = False


if __name__ == "__main__":
    import doctest

    # sequence: List[Union[int, str]] = [3, 1, 2,4]
    # generate_permutation(sequence)
    doctest.testmod()
