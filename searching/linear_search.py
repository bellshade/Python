"""
Linear search adalah salah satu metode
untuk mencari index suatu elemen dalam
suatu iterable yang dapat di-index
e.g., list, tuple, etc. dengan membandingkan
satu per satu elemen-elemennya.

Time complexity:
    Kasus terbaik: O(1)
    Kasus terburuk: O(n)
    Rata-rata: O(n/2)

Space complexity: O(1)

https://en.wikipedia.org/wiki/Linear_search
"""
from __future__ import annotations

from typing import TypeVar

from _types import SizedIndexable

T = TypeVar("T")


def linear_search(
    arr: SizedIndexable[T], value: T, start: int = 0, stop: int | None = None, /
) -> int:
    """
    >>> arr = [5, 2, 1, 6, 3, 7]
    >>> linear_search(arr, 5, 1)
    Traceback (most recent call last):
    ...
    ValueError: 5 tidak ada dalam iterable
    >>> linear_search(arr, 6)
    3
    >>> linear_search(arr, 1, 2, 3)
    2
    >>> linear_search(arr, 10)
    Traceback (most recent call last):
    ...
    ValueError: 10 tidak ada dalam iterable
    >>> linear_search((1,), 1)
    0
    """
    if not isinstance(arr, SizedIndexable):
        raise TypeError(
            "tipe argumen pertama tidak memiliki implementasi `__getitem__`"
        )

    exc = ValueError(f"{value} tidak ada dalam iterable")

    if start > len(arr) - 1:
        raise exc

    i = max(start, 0)  # set index start
    cap = min(len(arr) if stop is None else stop, len(arr))
    while i < cap:
        # cek apakah elemen ke-i adalah nilai yang kita cari
        if arr[i] == value:
            # jika ya, return index-nya
            return i

        # jika tidak, lanjut ke index selanjutnya
        i += 1

    # nilai tidak ditemukan
    raise exc


if __name__ == "__main__":
    import doctest

    doctest.testmod()
