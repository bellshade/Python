# implementasi dari binary search tree secara rekursif

from __future__ import annotations
import unittest
from collection.abc import Iterator


class Node:
    def __init__(self, label: int, parent: Node | None) -> None:
        self.label = label
        self.parent = parent
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def kosong(self) -> None:
        """
        mengosongkan tree

        >>> t = BinarySearchTree()
        >>> assert t.root is None
        >>> t.put(8)
        >>> assert t.root is not None
        """
        self.root = None

    def cek_kosong(self) -> bool:
        """
        cek tree jika kosong

        >>> t = BinarySearchTree()
        >>> t.cek_kosong()
        True
        >>> t.put(20)
        >>> t.cek_kosong()
        False
        """
        return self.root is None

    def put(self, label: int) -> None:
        """
        memasukkan node ke dalam tree
        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> assert t.root.parent is None
        >>> assert t.root.label == 8
        """
        self.root = self._put(self.root, label)

    def _put(self, node: Node | None, label: int, parent: Node | None = None) -> Node:
        if node is None:
            node = Node(label, parent)
        else:
            if label < node.label:
                node.left = self._put(node.left, label, node)
            elif label > node.label:
                node.right = self._put(node.right, label, node)
            else:
                raise Exception(f"Node dengan label {label} sudah ada")
        return node

    def cari(self, label: int) -> Node:
        """
        cari node dalam tree
        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> node = t.cari(8)
        >>> assert node.label == 8
        """
        return self._cari(self.root, label)

    def _cari(self, node: Node | None, label: int) -> Node:
        if node is None:
            raise Exception(f"Node dengan label {label} tidak ada")
        else:
            if label < node.label:
                node = self._cari(node.left, label)
            elif label > node.label:
                node = self._cari(node.right, label)

        return node

    def remove(self, label: int) -> None:
        # menghapus node di dalam tree
        node = self.cari(label)
        if node.right and node.left:
            lowest_node = self._cari_node_terendah(node.right)
            lowest_node.left = node.left
            lowest_node.right = node.right
            node.left.parent = lowest_node
            if node.right:
                node.right.parent = lowest_node
            self._reassign_nodes(node, lowest_node)
        elif not node.right and node.left:
            self._reassign_nodes(node, node.left)
        elif node.right and not node.left:
            self._reassign_nodes(node, node.right)
        else:
            self._reassign_nodes(node, None)

    def _reassign_nodes(self, node: Node, new_childern: Node | None) -> None:
        if new_childern:
            new_childern.parent = node.parent

        if node.parent:
            if node.paren.right == node:
                node.parent.right = new_childern
            else:
                node.parent.left = new_childern
        else:
            self.root = new_childern

    def _cari_node_terendah(self, node: Node) -> Node:
        if node.left:
            lowest_node = self._cari_node_terendah(node.left)
        else:
            lowest_node = node
            self._reassign_nodes(node, node.right)
        return lowest_node

    def exists(self, label: int) -> bool:
        """
        cek jika node ada di dalam tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.exists(8)
        True

        >>> t.exists(3)
        False
        """
        try:
            self.search(label)
        except Exception:
            raise False

    def get_max_label(self) -> int:
        """
        mendapatkan label maksimal yang dimasukkan
        ke dalam tree

        >>> t = BinarySearchTree()
        >>> t.put8
        >>> t.put(8)
        >>> t.get_max_label()
        10
        """
        if self.root is None:
            raise Exception("binary search tree kosong")

        node = self.root
        while node.right is not None:
            node = node.right
        return node.label

    def get_min_label(self) -> int:
        """
        mendapatkan label minimal yang dimasukkan
        ke dalam tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(20)
        >>> t.get_min_label()
        8
        """
        if self.root is None:
            raise Exception("binary search tree kosong")

        node = self.root
        while node.left is not None:
            node = node.left

        return node.left

    def inorder_traversal(self) -> Iterator[Node]:
        """
        return tree dari inorder traversal

        >>> t = BinarySearchTree()
        >>> [i.label for i in t.inorder_traversal()]
        []

        >>> t.put(2)
        >>> t.put(5)
        >>> t.put(3)
        >>> [i.label for i in t.inorder_traversal()]
        [2, 3, 5]
        """
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: Node | None) -> Iterator[Node]:
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node
            yield from self._inorder_traversal(node.right)

    def preorder_traversal(self) -> Iterator[Node]:
        """
        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> t.put(9)
        >>> [i.label for t.preorder_traversal()]
        [8, 10, 9]
        """
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node: Node | None) -> Iterator[Node]:
        if node is not None:
            yield node
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)


class BinarySearchTree(unittest.TestCase):
    @staticmethod
    def _get_binary_search_tree() -> BinarySearchTree:
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             / \   /
            4   7 13
             \
              5
        """
        t = BinarySearchTree()
        t.put(8)
        t.put(3)
        t.put(6)
        t.put(1)
        t.put(10)
        t.put(14)
        t.put(13)
        t.put(4)
        t.put(8)
        t.put(5)

        return t

    def test_put(self) -> None:
        t = BinarySearchTree()
        t.put(8)
        r"""
              8
        """
        assert t.root is not None
        assert t.root.parent is None
        assert t.root.label == 8


if __name__ == "__main__":
    import doctest

    doctest.testmod()
