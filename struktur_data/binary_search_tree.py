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

    def preorder(self, arr: list = []):
        # Algoritma preorder adalah sebagai berikut:
        # 1. Append data pada node
        # 2. Traverse ke kiri
        # 3. Traverse ke kanan
        arr.append(self.data)  # lgtm [py/modification-of-default-value]
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
        arr.append(self.data)  # lgtm [py/modification-of-default-value]
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
        arr.append(self.data)  # lgtm [py/modification-of-default-value]
        return arr


if __name__ == "__main__":
    root = BinarySearchTree()
    root.insert(5)
    root.insert(3)
    root.insert(11)
    root.insert(4)
    preorder_result = root.preorder()
    # menghasilkan [5, 3, 4, 11]
    print(preorder_result)
    inorder_result = root.inorder()
    # menghasilkan [3, 4, 5, 11]
    print(inorder_result)
    postorder_result = root.postorder()
    # menghasilkan [4, 3, 11, 5]
    print(postorder_result)
