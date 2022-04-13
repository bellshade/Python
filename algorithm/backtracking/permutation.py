# Dalam masalah ini, kami ingin menentukan semua kemungkinan permutasi
# dari urutan yang diberikan.
# Kami menggunakan backtracking untuk memecahkan masalah ini.
# Kompleksitas waktu: O(n! * n),
# di mana n menyatakan panjang barisan yang diberikan.
from __future__ import annotations


def generate_all_permutaions(sequence: list[int | str]) -> None:
    create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])


def create_state_space_tree(
    sequence: list[int | str],
    current_sequence: list[int | str],
    index: int,
    index_used: list[int],
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
            create_state_space_tree(sequence, current_sequence, index + 1, index_used)
            current_sequence.pop()
            index_used[i] = False


if __name__ == "__main__":
    import doctest

    # sequence: List[Union[int, str]] = [3, 1, 2,4]
    # generate_permutation(sequence)
    doctest.testmod()
