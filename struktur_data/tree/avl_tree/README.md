# Avl tree
AVL tree adalah binary search tree yang memiliki perbedaan tinggi/level maksumal 1 antar subtree kiri dan subtree kanan. AVL tree muncul untuk menyeimbangkan binary search tree. dengan AVL tree, waktu pencarian dan bentuk tree dapat dipersingkat dan disederhanakan.

## perbedaan antara binary search tree dan avl tree


**binary search tree**

- binary search tree adalah height balanced p-tree yang artinya maksimum perbedaan height antara subtree kiri dan kanan adalah p
- semua data dibagian kiri _sub-tree_ dari _node_ t selalu lebih kecil dari data dalam _node_ t itu sendiri.
- semua data dibagian kana _sub-tree_ dari _node_ t selalu lebih besar atau sama dengan data dalam node t.

**avl tree**

- avl tree adalah height balanced 1-tree yang berarti maksimum perbedaan antara subtree kiri dan kanan adalah satu.
- path pencarian lokasi untuk dilakukan operasi insert dimulai dari root.
- adanya node pada search path yang balancenya _TallLeft_(tanda -) atau _TallRight_(tanda +) dan terletak paling dekat dengan node yang baru.

## penerapan struktur data avl

penerapan struktur data avl tree digunakan pada binary search tree yang bertujuan untuk menyeimbangkan tree tersebut, sehingga waktu pencarian an struktur tree dapat disederhanakan. avl tree dapat direpresentasikan dengan menggunakan array maupun linked list. contohnya untuk membuat program tingkatan pegawi dalam perusahaan dan silsilah keluarga.

**membuat node pohon**

```python
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.kiri = None
        self.kanan = None
        self.tinggi = 1
```

**membuat kelas dari avl tree yang dimana termasuk fungsi insert**

```python
class AVL_Tree(object):
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
        z.tinggi = 1 + max(
            self.getTinggi(z.kiri),
            self.getTinggi(z.lanan)
        )
        y.tinggi = 1 + max(
            self.getTinggi(y.kiri),
            self.getTinggi(y.kanan)
        )

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
        z.tinggi = 1 + max(
            self.getTinggi(z.kiri),
            self.getTinggi(z.kanan)
        )
        y.tinggi = 1 + max(
            self.getTinggi(y.kiri),
            self.getTinggi(y.kanan)
        )

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

        print("{0} ".format(root.val), end = "")
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

print("pre order tranversal dari avl tree adalah ")
tree_saya.preOrder(root)
print()
```

## kompleksitas waktu

operasi rotasi (putar kiri dan kanan) membutuhkan waktu yang konstan karena hanya beberapa petunjuk yang diubah disana. memperbarui ketinggian dan mendpatkan faktor keseimbangan juga membutuhkan waktu yang konstan. jadi kompleksitas waktu penyisipan avl tetap sama dengan penyisipan _binary search tree_ yaitu O(h) dimana h adalah tinggi dari pohon. kerna pohon avl seimbang, tingginya adalah O(Logn). jadi kompleksitas waktu penyisipan avl tree adalah O(Logn)
