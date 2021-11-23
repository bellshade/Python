class Node:

    # Class Node digunakan untuk membangun node pada linked list.
    # Class ini memiliki properti next yang berfungsi sebagai
    # penunjuk untuk node selanjutnya dan properti val
    # sebagai properti yang menampung nilai pada node

    def __init__(self, val=None):
        self.next = None
        self.val = val


class SingleLinkedList:

    # Class SingleLinkedList digunakan untuk membuat single linked list
    # dari kumpulan node

    def __init__(self):

        # Constructor __init__ digunakan  untuk menginisialisasi
        # head dari linked list

        self.linked_list_head = None

    def insert(self, new_node):

        # Method insert digunakan untuk menambahkan node pada linked list.
        # Method ini memiliki parameter new_node di mana parameter ini
        # menerima argumen berupa class Node().

        # Method ini memiliki sebuah blok if-else, di mana blok ini akan
        # memeriksa apakah head dari linked list ini ada atau tidak (None).
        # Jika head dari linked list tidak ada, maka method ini akan
        # menginisasi Node pada argumen sebagai head dari linked list, jika
        # tidak maka Node pada argumen akan ditambah di belakang (tail)

        if self.linked_list_head is None:
            self.linked_list_head = new_node
        else:
            temp = self.linked_list_head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def insert_after(self, target_val, new_node):

        # Method insert_after digunakan untuk menambah node setelah node
        # tertentu. Method ini menerima argumen parameter target_val yang
        # berfungsi sebagai penanda di mana node yang baru akan
        # ditambahkan dan argumen new_node yang menerima class Node().

        # Variabel temp merupakan class Node, tepatnya head dari
        # linked list dan digunakan untuk mencari value dari target_val

        temp = self.linked_list_head
        while temp.val != target_val:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        # mengosongkan node temp
        temp = None  # lgtm [py/unused-local-variable]

    def delete_head(self):

        # Method delete_head digunakan untuk menghapus head dari
        # linked list

        temp = self.linked_list_head.next
        self.linked_list_head = None
        self.linked_list_head = temp

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

    def delete_node(self, target_val):

        # Method delete_node berfungsi untuk menghapus sebuah node
        # dari linked list. Method ini menerima argumen target_val, yaitu
        # nilai dari node pada linked list.

        temp = self.linked_list_head
        if temp.val == target_val:
            # jika value dari temp sama dengan value dari head
            self.delete_head()
            return

        while temp.next.val != target_val:
            temp = temp.next
        temp.next = temp.next.next

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

    linked_list = SingleLinkedList()
    linked_list.insert(Node(5))
    linked_list.insert(Node(3))
    linked_list.insert(Node(4))
    # menghasilkan 5 -> 3 -> 4
    linked_list.print_linked_list()
    linked_list.insert_after(3, Node(6))
    # menghasilkan 5 -> 3 -> 6 -> 4
    linked_list.print_linked_list()
    linked_list.delete_head()
    # menghasilkan 3 -> 6 -> 4
    linked_list.print_linked_list()
    linked_list.delete_node(6)
    # menghasilkan 3 -> 4
    linked_list.print_linked_list()
    linked_list.delete_node(3)
    # menghasilkan 4
    linked_list.print_linked_list()
    linked_list.insert(Node(5))
    # menghasilkan 4 -> 5
    linked_list.print_linked_list()
    linked_list.delete_tail()
    # menghasilkan 4
    linked_list.print_linked_list()
    linked_list.delete_tail()
    # seluruh elemen pada linked list telah dihapus
    linked_list.print_linked_list()
