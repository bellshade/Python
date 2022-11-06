from __future__ import annotations

from collections.abc import Iterator


class Node:
    # hitung jumlah semua node dalam pohon biner
    # node memiliki variable nilai dan mengarah ke
    # node kiri dan kanannya

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTreeNodeSum:
    r"""
        10
       /  \
      5   -3
     /    / \
    12   8  0
    >>> tree = Node(10)
    >>> sum(BinaryTreeNodeSum(tree))
    10
    >>> tree.left = Node(5)
    >>> sum(BinaryTreeNodeSum(tree))
    15
    >>> tree.right = Node(-3)
    >>> sum(BinaryTreeNodeSum(tree))
    12
    >>> tree.left.left = Node(12)
    >>> sum(BinaryTreeNodeSum(tree))
    24
    >>> tree.right.left = Node(8)
    >>> tree.right.right = Node(0)
    >>> sum(BinaryTreeNodeSum(tree))
    32
    """

    def __init__(self, tree: Node) -> None:
        self.tree = tree

    def depth_first_search(self, node: Node | None) -> int:
        if node is None:
            return 0
        return node.value(
            self.depth_first_search(node.left) + self.depth_first_search(node.right)
        )

    def __iter__(self) -> Iterator[int]:
        yield self.depth_first_search(self.tree)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
