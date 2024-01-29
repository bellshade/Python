"""
Binary search adalah salah satu metode
untuk mencari index suatu elemen dalam
suatu indexable iterable, e.g., list, tuple, etc.
dengan membandingkan elemen yang ingin
dicari dengan elemen tengah dari iterable
dan mengeliminasi bagian dimana elemen
tsb. tidak mungkin ada, lalu mengulangi
tahap yang sama untuk bagian yang disisakan.

NB. binary search hanya bekerja pada
iterable yang berurut. Aplikasi pada
iterable yang tidak berurut akan menghasilkan
UB (undefined behaviour).

NBB. elemen dari iterable harus mengimplementasikan
operasi < dan >.

Time complexity:
    Kasus terbaik: O(log n)
    Kasus terburuk: O(n)
    Rata-rata: O(log n)

Space complexity: O(1)

https://en.wikipedia.org/wiki/Binary_search_algorithm
"""

from __future__ import annotations

from typing import Any, Protocol, TypeVar

from _types import SizedIndexable


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...

    def __le__(self, other: Any) -> bool:
        """Hanya untuk suppress LGTM alert."""

    def __gt__(self, other: Any) -> bool: ...

    def __ge__(self, other: Any) -> bool:
        """Hanya untuk suppress LGTM alert."""


T = TypeVar("T", bound=Comparable)


def _clamp(value: int, min_: int, max_: int) -> int:
    return max(min(value, max_), min_)


def binary_search(
    arr: SizedIndexable[T], value: T, start: int = 0, stop: int | None = None, /
) -> int:
    """
    >>> arr = list(range(200))
    >>> binary_search(arr, 50)
    50
    >>> binary_search(arr, 201)
    Traceback (most recent call last):
    ...
    ValueError: 201 tidak ada dalam iterable
    """
    if not isinstance(arr, SizedIndexable):
        raise TypeError(
            "tipe argumen pertama tidak memiliki implementasi "
            "`__getitem__` atau `__len__`"
        )

    r = len(arr) - 1
    r = r if stop is None else _clamp(stop, 0, r)  # batas kanan
    L = _clamp(start, 0, r)  # batas kiri

    while L <= r:
        if (temp := arr[(m := (L + r) // 2)]) < value:
            # jika elemen tengah kurang dari nilai yang kita cari
            # maka kita eliminasi bagian kiri.
            # update batas kiri.
            L = m + 1
        elif temp > value:
            # sedangkan jika elemen tengah lebih dari nilai yang kita cari
            # maka kita elminiasi bagian kanan.
            # update batas kanan.
            r = m - 1
        else:
            # elemen tengah sama dengan nilai yang kita cari.
            # return index-nya.
            return m

    # nilai tidak ditemukan.
    raise ValueError(f"{value} tidak ada dalam iterable")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
