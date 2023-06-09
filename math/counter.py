from heapq import nlargest
from operator import itemgetter
from typing import Any, Dict, List, Optional, Tuple


class Counter(dict):
    """
    Counter merupakan Class untuk menghitung data-data unique
    pada setiap nilai.

    Args:
        dict: parameter bersifat map.

    """

    def __init__(
        self, iterable: Optional[Dict[Any, int]] = None, **kwargs: int
    ) -> None:
        """
        counter ini bisa digunakan dalam bentuk apapun
        baik bentuk sting,list maupun yang lain
        >>> Counter("hallo")
        {'h': 1, 'a': 1, 'l': 2, 'o': 1}
        >>> Counter({'a':3,'b':2,'c':1})
        {'a': 3, 'b': 2, 'c': 1}
        """
        super().__init__()
        self.update(iterable, **kwargs)

    def update(self, iterable: Optional[Dict[Any, int]] = None, **kwargs: int) -> None:
        if iterable is not None:
            if hasattr(iterable, "items"):
                if self:
                    self_get = self.get
                    for element, count in iterable.items():
                        self[element] = self_get(element, 0) + count
                else:
                    dict.update(self, iterable)
            else:
                self_get = self.get
                for element in iterable:
                    self[element] = self_get(element, 0) + 1
        if kwargs:
            self.update(kwargs)

    def paling_muncul(self, n: Optional[int] = None) -> List[Tuple[Any, int]]:
        """
        fungsi ini merupakan menampilkan angka
        yang sering dicaribisa dikatakan bahwa
        nilai yang dominan
        Args:
            n (int, optional): ingin menampilkan sampai ke
                               berapa.
        Returns:
            _type_: berupa value di urut dari terbesar
        """
        if n is None:
            return sorted(self.items(), key=itemgetter(1), reverse=True)
        else:
            return nlargest(n, self.items(), key=itemgetter(1))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
