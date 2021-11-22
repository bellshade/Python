from typing import Any
from math import ceil


class PaginationHelper:
    """
    Sebuah class yang berisi utilitas-utilitas untuk
    membantu dalam pagination.
    """

    def __init__(self, collection: list[Any], items_per_page):
        """
        Constructor class ini mengambil 2 parameter:
        1. `collection`. List berisi item-item yang ingin di
        paginate.
        2. `items_per_page`. Angka integer yang menunjukkan
        berapa item yang akan ditampilkan dalam 1 halaman.
        Contoh:
        >>> helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
        >>> helper.collection
        ['a', 'b', 'c', 'd', 'e', 'f']
        >>> helper.items_per_page
        4
        """
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self) -> int:
        """
        Method untuk mengembalikan panjang list dari
        attribut `collection`.

        Contoh:
        >>> helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
        >>> helper.item_count()
        6
        """
        return len(self.collection)

    def page_count(self) -> int:
        """
        Method untuk mengembalikan total halaman berdasarkan
        atribut yang dimiliki.

        Contoh:
        >>> helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
        >>> helper.page_count()
        2
        """
        return ceil(self.item_count() / self.items_per_page)

    def page_item_count(self, page_index):
        """
        Method untuk mengembalikan total item yang ada di
        halaman tertentu berdasarkan parameter `page_index`
        dan atribut yang dimiliki. `page_index` adalah angka
        integer yang dimulai dari 0.

        Contoh:
        >>> helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
        >>> helper.page_item_count(0)
        4
        >>> helper.page_item_count(1)
        2
        >>> helper.page_item_count(2)
        -1
        """
        if page_index >= self.page_count():
            return -1
        if page_index + 1 < self.page_count():
            return self.items_per_page
        return self.item_count() % self.items_per_page

    def page_index(self, item_index: int) -> int:
        """
        Method untuk mengembalikan nomor halaman dari sebuah item
        menggunakan index item tertentu, `item_index`.
        `item_index` adalah angka integer yang dimulai dari 0.

        Contoh:
        >>> helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
        >>> helper.page_index(2)
        0
        >>> helper.page_index(5)
        1
        >>> helper.page_index(20)
        -1
        """
        if item_index < 0 or item_index >= self.item_count():
            return -1

        return item_index // self.items_per_page


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)

    # basic tests
    print(helper.collection)
    print(helper.items_per_page)

    print(helper.item_count())

    print(helper.page_count())

    print(helper.page_item_count(0))
    print(helper.page_item_count(1))
    print(helper.page_item_count(2))

    print(helper.page_index(2))
    print(helper.page_index(5))
    print(helper.page_index(20))

    # custom tests
    # pagination_helper = PaginationHelper([
    #    (1, 'a'),
    #    (2, 'b'),
    #    (3, 'c'),
    #    (4, 'd'),
    #    (5, 'e'),
    # ], 2)
