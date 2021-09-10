"""
Binary search adalah salah satu metode
untuk mencari index suatu elemen dalam
suatu indexable iterable, e.g., list, tuple, etc.
dengan membandingkan elemen yang ingin
dicari dengan elemen tengah dari iterable
dan mengeliminasi bagian dimana elemen
tsb. tidak mungkin ada, lalu mengulangi
tahap yang sama untuk bagian yang disisakan.

N.B. binary search hanya bekerja pada
iterable yang berurut. Aplikasi pada
iterable yang tidak berurut akan menghasilkan
UB (undefined behaviour).

N.B.B elemen dari iterable harus mengimplementasikan
operasi < dan >.

Time complexity:
    Kasus terbaik: O(log n)
    Kasus terburuk: O(n)
    Rata-rata: O(log n)

Space complexity: O(1)

https://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from typing import Protocol, TypeVar

from _types import Indexable


class Comparable(Protocol):
    def __lt__(self) -> bool:
        ...

    def __gt__(self) -> bool:
        ...


T = TypeVar("T", bound=Comparable)


def binary_search(arr: Indexable[T], value: T, /) -> int:
    """
    >>> arr = list(range(200))
    >>> binary_search(arr, 50)
    50
    >>> binary_search(arr, 201)
    Traceback (most recent call last):
    ...
    ValueError: 201 tidak ada dalam iterable
    """
    L = 0
    r = len(arr) - 1

    while L <= r:
        if (temp := arr[(m := (L + r) // 2)]) < value:
            L = m + 1
        elif temp > value:
            r = m - 1
        else:
            return m

    raise ValueError(f"{value} tidak ada dalam iterable")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
