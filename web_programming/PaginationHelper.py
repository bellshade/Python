from typing import Any
from math import ceil


class PaginationHelper:
    def __init__(self, collection: list[Any], items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self) -> int:
        return len(self.collection)

    def page_count(self) -> int:
        return ceil(self.item_count() / self.items_per_page)

    def page_item_count(self, page_index):
        if page_index >= self.page_count():
            return -1
        if page_index + 1 < self.page_count():
            return self.items_per_page
        return self.item_count() % self.items_per_page

    def page_index(self, item_index: int) -> int:
        if item_index < 0 or item_index >= self.item_count():
            return -1

        return item_index // self.items_per_page


if __name__ == "__main__":
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
