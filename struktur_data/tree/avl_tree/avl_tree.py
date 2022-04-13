class TreeNode:
    def __init__(self, val):
        self.val = val
        self.kiri = None
        self.kanan = None
        self.tinggi = 1


class AVL_Tree:
    # membuat fungsi rekursif untuk memasukkan
    # kunci ke subtree di root dengan node dan return
    # root baru dari sub tree
    def insert(self, root, kunci):
        # membuat binary search tre sederhana
        if not root:
            return TreeNode(kunci)
        elif kunci < root.val:
            root.kiri = self.insert(root.kiri, kunci)
        else:
            root.kanan = self.insert(root.kanan, kunci)

        # update dari tinggi simpul node
        root.tinggi = 1 + max(
            self.getTinggi(root.kiri),
            self.getTinggi(root.kanan),
        )

        # dapatkan faktor dari keseimbangan tree
        seimbang = self.getSeimbang(root)

        # jika node tidak seimbang
        # maka lakukan 4 struktur logika
        # logika 1 - kiri kiri
        if seimbang > 1 and kunci < root.kiri.val:
            return self.rotasi_kanan(root)

        # logika 2 - kanan kanan
        if seimbang < -1 and kunci > root.kanan.val:
            return self.rotasi_kiri(root)

        # logika 3 - kiri kanan
        if seimbang > 1 and kunci > root.kiri.val:
            root.kiri = self.rotasi_kiri(root.left)
            return self.rotasi_kiri

        # logika 4 - kanan kiri
        if seimbang < -1 and kunci < root.kanan.val:
            root.kanan = self.rotasi_kanan(root.kanan)
            return self.rotasi_kiri(root)

        return root

    # membuat fungsi dari rotasi kiri
    def rotasi_kiri(self, z):
        y = z.kanan
        T2 = y.kiri

        # lekukan rotasi
        y.kiri = z
        z.kanan = T2

        # update dari tinggi
        z.tinggi = 1 + max(self.getTinggi(z.kiri), self.getTinggi(z.kanan))
        y.tinggi = 1 + max(self.getTinggi(y.kiri), self.getTinggi(y.kanan))

        # mengembalikan root baru
        return y

    # membuat rotasi kanan
    def rotasi_kanan(self, z):
        y = z.kiri
        T3 = y.kanan

        # lakukan rotasi
        y.kanan = z
        z.kiri = T3

        # update dari tinggi
        z.tinggi = 1 + max(self.getTinggi(z.kiri), self.getTinggi(z.kanan))
        y.tinggi = 1 + max(self.getTinggi(y.kiri), self.getTinggi(y.kanan))

        # mengembalikan root baru
        return y

    def getTinggi(self, root):
        # jika tidak ada root mengembalikan
        # nilai 0
        if not root:
            return 0

        return root.tinggi

    def getSeimbang(self, root):
        # jika tidak ada root mengembalikan
        # nilai 0
        if not root:
            return 0

        return self.getTinggi(root.kiri) - self.getTinggi(root.kanan)

    def preOrder(self, root):
        # jika tidak ada root mengembalikan
        # nilai 0
        if not root:
            return 0

        print(f"{root.val} ", end="")
        self.preOrder(root.kiri)
        self.preOrder(root.kanan)


# menjalankan avl tree

tree_saya = AVL_Tree()
root = None

root = tree_saya.insert(root, 10)
root = tree_saya.insert(root, 20)
root = tree_saya.insert(root, 30)
root = tree_saya.insert(root, 40)
root = tree_saya.insert(root, 50)
root = tree_saya.insert(root, 25)

print("lintasan preorder dari pohon avl yang dibangun adalah ")
tree_saya.preOrder(root)
print()
