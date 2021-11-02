# dalam ilmu komputer dan teori informasi, huffman kode adalah
# adalah sebuah tipe code yang optimal yang biasanya digunakan
# untuk loseless data compression.
# https://id.wikipedia.org/wiki/Pengodean_Huffman

import sys


class Letter:
    def __init__(self, letter, freq):
        self.letter = letter
        self.freq = freq
        self.bitstring = {}

    def __repr__(self):
        return f"{self.letter}:{self.freq}"


class TreeNode:
    def __init__(self, freq, left, right):
        self.freq = freq
        self.left = left
        self.right = right


def parse_file(file_path):
    """
    Baca file dan buat dict dari semua huruf dan
    lalu ubah dict menjadi list letter.
    """
    chars = {}
    with open(file_path) as f:
        while True:
            c = f.read()
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars.keys() else 1
    return sorted([Letter(c, f) for c, f in chars.items()], key=lambda l: l.freq)


def tree(letters):
    """
    Jalankan melalui list letter dan buat tumpukan minimum
    untuk Huffman tree.
    """
    while len(letters) > 1:
        left = letters.pop(0)
        right = letters.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        letters.append(node)
        letters.sort(key=lambda l: l.freq)
    return letters[0]


def traverse_tree(root, bitstring):
    """
    Lintasi Huffman Tree secara rekursif untuk mengatur masing-masing
    Kamus bitstring Letters, dan return list letters
    """
    if type(root) is Letter:
        root.bitstring[root.letter] = bitstring
        return [root]
    letters = []
    letters += traverse_tree(root.left, bitstring + "0")
    letters += traverse_tree(root.right, bitstring + "1")
    return letters


def huffman(file_path):
    """
    Parsing file, bangun Tree, lalu jalankan file
    lagi, menggunakan kamus huruf untuk menemukan dan mencetak
    bitstring untuk setiap huruf.
    """
    letters_list = parse_file(file_path)
    root = tree(letters_list)
    letters = {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }
    print(f"huffman of {file_path} : ")
    with open(file_path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(letters[c], end=" ")
    print()


if __name__ == "__main__":
    # berikan jalur file ke fungsi huffman
    huffman(sys.argv[1])
