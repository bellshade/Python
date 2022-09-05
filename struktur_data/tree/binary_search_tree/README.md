## Definisi
*Binary search tree* (*BST*) adalah salah satu ragam dari *binary tree* yang memiliki karakteristik dimana nilai pada *node* sebelah kiri selalu lebih kecil dari *node* sebelah kanan. Dua *tree* di bawah merupakan ilustrasi dari *binary search tree*.
![Binary Search tree Example](img/bst_example.png)

## Operasi Pada *Binary Search Tree*
Ada beberapa operasi yang dapat dilakukan pada *binary search tree*, seperti *insert*, *delete*, dan *traverse/traversal*. Kebanyakan sumber menuliskan operasi-operasi ini menggunakan rekursi, jadi penting bagi kamu untuk mengerti bagaimana cara kerja fungsi rekursi.

### Insert
Algoritma untuk melakukan *insert* pada *BST* adalah sebagai berikut:
1. Mulai dari *root node*
2. Bandingkan nilai dari *node* yang ingin di-*insert* dengan nilai pada *root*. Jika nilai dari *node* yang ingin di-*insert* lebih besar daripada nilai dari *node*, lakukan *insert* pada sebelah kiri dan sebaliknya.
3. Periksa apakah *pointer* kiri dan *pointer* kanan kosong. Jika kosong lakukan *insert* pada *pointer* tersebut, dan jika tidak lakukan *insert* secara rekursif.

Berikut adalah implementasi dari algoritma di atas.
```python
class BinarySearchTree:
    # method __init__ digunakan untuk membangun Node
    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, new_data):
        if self.data is None:
            # menginisasi root jika belum ada node sama sekali
            self.data = new_data
        elif new_data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(new_data)
            else:
                # memasukkan node baru di sebelah kiri secara
                # rekursif melalui atribut left
                self.left.insert(new_data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(new_data)
            else:
                # memasukkan node baru di sebelah kanan secara
                # rekursif melalui atribut right
                self.right.insert(new_data)
```
Misalkan kita ingin membangun *BST* dengan nilai sebagai berikut : `4, 5, 3, 7`. Ilustrasi dari membangun *BST* tersebut adalah sebagai berikut.
![BST Insertion Example](img/bst_insertion.png)

### Traversal
*Traversal* adalah cara untuk mengunjungi *node* pada *tree*. Pada *binary search tree*, ada 3 cara untuk melakukan *traversal*, yaitu *preorder*, *inorder*, dan *postorder*. Ketiga *traversal* berikut dibedakan berdasarkan urutan pengunjungan dari *root node* sebagai berikut.

1. *Preorder*\
Algoritma *preorder* adalah sebagai berikut:
    1. Kunjungi *root node*
    2. Kunjungi *left subtree*
    3. Kunjungi *right subtree*

2. *Inorder*\
Algoritma *preorder* adalah sebagai berikut:
    1. Kunjungi *left subtree*
    2. Kunjungi *root node*
    3. Kunjungi *right subtree*

3. *Postorder*\
Algoritma *postorder* adalah sebagai berikut:
    1. Kunjungi *left subtree*
    2. Kunjungi *right subtree*
    3. Kunjungi *root node*

Kode di bawah ini adalah implementasi dari ketiga jenis *traversal* di atas
```python
    def preorder(self, arr: list = []):
        # Algoritma preorder adalah sebagai berikut:
        # 1. Append data pada node
        # 2. Traverse ke kiri
        # 3. Traverse ke kanan
        arr.append(self.data)
        if self.left is not None:
            self.left.preorder(arr)
        if self.right is not None:
            self.right.preorder(arr)
        return arr

    def inorder(self, arr: list = []):
        # Algoritma inorder adalah sebagai berikut:
        # 1. Traverse ke kiri
        # 2. Append data pada node
        # 3. Traverse ke kanan
        if self.left is not None:
            self.left.inorder(arr)
        arr.append(self.data)
        if self.right is not None:
            self.right.inorder(arr)
        return arr

    def postorder(self, arr: list = []):
        # Algoritma postorder adalah sebagai berikut:
        # 1. Traverse ke kiri
        # 2. Traverse ke kanan
        # 3. Append data pada node
        if self.left is not None:
            self.left.postorder(arr)
        if self.right is not None:
            self.right.postorder(arr)
        arr.append(self.data)
        return arr
```
Sebagai contoh, misalkan kita punya *binary search tree* sebagai berikut:
| *Preorder* | *Inorder*                                        | *Postorder*                                                                                                                          |
|-------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](img/preorder.png)    | ![](img/inorder.png) | ![](img/postorder.png) |