# diberikan root binary tree dan target bilangan bulat
# temukanjumlah jalur dimana jumlah nilai sama dengan
# target

from __future__ import annotations


class Node:
    # sebuah node memiliki variabel nilai dan
    # pointer ke node di kiri dan kanannya
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class BinaryTreePathSum:
    r"""
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1
    >>> tree = Node(10)
    >>> tree.left = Node(5)
    >>> tree.right = Node(-3)
    >>> tree.left.left = Node(3)
    >>> tree.left.right = Node(2)
    >>> tree.right.right = Node(11)
    >>> tree.left.left.left = Node(3)
    >>> tree.left.left.right = Node(-2)
    >>> tree.left.right.right = Node(1)
    >>> BinaryTreePathSum().path_sum(tree, 8)
    3
    >>> BinaryTreePathSum().path_sum(tree, 7)
    2
    >>> tree.right.right = Node(10)
    >>> BinaryTreePathSum().path_sum(tree, 8)
    2
    """
    target: int

    def __init__(self) -> None:
        self.paths = 0

    def depth_first_search(self, node: Node | None, path_sum: int) -> None:
        if node is None:
            return

        if path_sum == self.target:
            self.paths += 1

        if node.left:
            self.depth_first_search(node.left, path_sum + node.left.value)
        if node.right:
            self.depth_first_search(node.right, path_sum + node.right.value)

    def path_sum(self, node: Node | None, target: int | None = None) -> int:
        if node is None:
            return 0
        if target is not None:
            self.target = target

        self.depth_first_search(node, node.value)
        self.path_sum(node.left)
        self.path_sum(node.right)

        return self.paths


if __name__ == "__main__":
    import doctest

    doctest.testmod()
