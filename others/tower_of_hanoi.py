# tower of hanoi adalah sebuah problem
# dimana mengurutkan cakram yang tidak
# beraturan menjadi teratur
# dimulai dari yang besar ke yang kecil
# informasi tentang tower of hanoi
# https://en.wikipedia.org/wiki/Tower_of_Hanoi


from __future__ import annotations


def move_tower(height: int, from_pole: str, to_pole: str, with_pole: str) -> None:
    """
    >>> move_tower(3, 'A', 'B', 'C')
    pindah cakram dari A ke B
    pindah cakram dari A ke C
    pindah cakram dari B ke C
    pindah cakram dari A ke B
    pindah cakram dari C ke A
    pindah cakram dari C ke B
    pindah cakram dari A ke B
    """
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp: str, tp: str) -> None:
    print("pindah cakram dari", fp, "ke", tp)
