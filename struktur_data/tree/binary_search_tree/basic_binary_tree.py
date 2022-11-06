from __future__ import annotations


class Node:
    # node memiliki variabel data dan pointer
    # ke node di kiri dan kanannya

    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


def display(tree: Node | None) -> None:
    """
    >>> root = Node(1)
    >>> root.left = Node(0)
    >>> root.right = Node(2)
    >>> display(root)
    0
    1
    2
    >>> display(root.right)
    2
    """
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)


def depth_of_tree(tree: Node | None) -> int:
    """
    fungsi rekursif yang mengembalikan kedalam
    binary tree

    >>> root = Node(0)
    >>> depth_of_tree(root)
    1
    >>> root.left = Node(0)
    >>> depth_of_tree(root)
    2
    >>> root.right = Node(0)
    >>> depth_of_tree(root)
    2
    >>> root.left.right = Node(0)
    >>> depth_of_tree(root)
    3
    >>> depth_of_tree(root.left)
    2
    """
    return 1 + max(depth_of_tree(tree.left), depth_of_tree(tree.right)) if tree else 0


def is_full_binary_tree(tree: Node) -> bool:
    """
    mengembalikan True jika ini binary tree penuh

    >>> root = Node(0)
    >>> is_full_binary_tree(root)
    True
    >>> root.left = Node(0)
    >>> is_full_binary_tree(root)
    False
    >>> root.right = Node(0)
    >>> is_full_binary_tree(root)
    True
    >>> root.left.left = Node(0)
    >>> is_full_binary_tree(root)
    False
    >>> root.right.right = Node(0)
    >>> is_full_binary_tree(root)
    False
    """
    if not tree:
        return True
    if tree.left and tree.right:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return not tree.left and not tree.right


if __name__ == "__main__":
    import doctest

    doctest.testmod()
