class Node:

    # Class Node digunakan untuk membangun node pada linked list.
    # Node pada doubly linked list pada umumnya mirip dengan
    # node pada singly linked list, hanya saja terdapat sebuah
    # atribut baru, yaitu pointer prev yang menunjuk ke node
    # sebelumnya.

    def __init__(self, val=None):
        self.next = None
        self.prev = None
        self.val = val


class DoublyLinkedList:

    # Class DoublyLinkedList digunakan untuk membuat doubly linked list
    # dari kumpulan node

    def __init__(self):

        # Constructor __init__ digunakan  untuk menginisialisasi
        # head dari linked list

        self.linked_list_head = None

    def insert_head(self, new_node):

        # Method insert_head digunakan untuk menambah node pada head
        # dari linked list. Method ini menerima argumen new_node yang
        # merupakan class Node.

        # Method ini memiliki blok if-else, di mana blok if akan memeriksa
        # apakah sudah ada head dari linked list atau belum, dan blok
        # else sebaliknya.

        if self.linked_list_head is None:
            self.linked_list_head = new_node
        else:
            new_node.next = self.linked_list_head
            self.linked_list_head = new_node

    def insert(self, new_node):

        # Method insert digunakan untuk menambahkan node pada linked list.
        # Method ini memiliki parameter new_node di mana parameter ini
        # menerima argumen berupa class Node.

        # Method ini memiliki sebuah blok if-else, di mana blok ini akan
        # memeriksa apakah head dari linked list ini ada atau tidak (None).
        # Jika head dari linked list tidak ada, maka method ini akan
        # menginisasi Node pada argumen sebagai head dari linked list, jika
        # tidak maka Node pada argumen akan ditambah di belakang (tail)

        if self.linked_list_head is None:
            self.insert_head(new_node)
        else:
            temp = self.linked_list_head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_after(self, target, new_node):

        # Method insert_after digunakan untuk menambah node setelah node
        # tertentu. Method ini menerima argumen parameter target_val yang
        # berfungsi sebagai penanda di mana node yang baru akan
        # ditambahkan dan argumen new_node yang menerima class Node().

        # Variabel temp merupakan class Node, tepatnya head dari
        # linked list dan digunakan untuk mencari value dari target_val

        temp = self.linked_list_head
        while temp.val != target:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_head(self):

        # Method delete_head digunakan untuk menghapus head dari
        # linked list

        temp = self.linked_list_head
        # memindahkan head linked list ke node selanjutnya
        self.linked_list_head = temp.next
        self.linked_list_head.prev = None
        # mengosongkan head linked list
        temp = None  # lgtm [py/unused-local-variable]

    def delete_tail(self):

        # Method delete_tail digunakan untuk menghapus tail dari
        # linked list

        temp = self.linked_list_head
        if temp.next is None:
            self.delete_head()
            return

        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_node(self, target):

        # Method delete_node berfungsi untuk menghapus sebuah node
        # dari linked list. Method ini menerima argumen target_val, yaitu
        # nilai dari node pada linked list.

        temp = self.linked_list_head
        if temp.val == target:
            self.delete_head()
            return

        else:
            while temp.next.val != target:
                temp = temp.next
            temp.next = temp.next.next
            temp.next.next.prev = temp

    def print_linked_list(self):

        # Method print_linked_list berfungsi untuk mencetak linked list

        result = []
        temp = self.linked_list_head
        while temp is not None:
            result.append(str(temp.val))
            temp = temp.next
        linked_list_result = " -> ".join(result)
        print(linked_list_result)


if __name__ == "__main__":

    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insert(Node(5))
    doubly_linked_list.insert(Node(6))
    doubly_linked_list.insert(Node(2))
    # menghasilkan 5 -> 6 -> 2
    doubly_linked_list.print_linked_list()
    doubly_linked_list.insert_head(Node(1))
    # menghasilkan 1 -> 5 -> 6 -> 2
    doubly_linked_list.print_linked_list()
    doubly_linked_list.delete_head()
    # menghasilkan 5 -> 6 -> 2
    doubly_linked_list.print_linked_list()
    doubly_linked_list.delete_tail()
    # menghasilkan 5 -> 6
    doubly_linked_list.print_linked_list()
    doubly_linked_list.insert_after(6, Node(13))
    # menghasilkan 5 -> 6 -> 13
    doubly_linked_list.print_linked_list()
    doubly_linked_list.delete_node(5)
    # menghasilkan 6 -> 13
    doubly_linked_list.print_linked_list()
