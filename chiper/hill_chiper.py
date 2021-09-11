"""
urutan kunci enkripsi menjadi N (karena merupakan matriks persegi).
Teks Anda dibagi menjadi kumpulan dengan panjang N dan dikonversi ke vektor numerik
dengan pemetaan sederhana yang dimulai dengan A=0 dan seterusnya.
Kuncinya kemudian dikalikan dengan vektor batch yang baru dibuat untuk mendapatkan
vektor yang dikodekan. Setelah setiap perkalian modular 36 perhitungan dilakukan
pada vektor sehingga menghasilkan angka antara 0 dan 36 dan kemudian dipetakan dengan
alfanumerik yang sesuai.
Saat mendekripsi, kunci dekripsi ditemukan yang merupakan kebalikan dari
mengenkripsi kunci modular 36.
Proses yang sama diulang untuk mendekripsi untuk mendapatkan
pesan asli kembali.
Kendala:
Determinan matriks kunci enkripsi harus relatif prima w.r.t 36.
Catatan:
Implementasi ini hanya mempertimbangkan alfanumerik dalam teks. Jika panjang
teks yang akan dienkripsi bukan kelipatan dari kunci istirahat (panjang satu
kumpulan huruf), karakter terakhir dari teks ditambahkan ke teks sampai
panjang teks mencapai kelipatan dari break_key. Jadi teks setelah
dekripsi mungkin sedikit berbeda dari teks aslinya.
"""
import string

import numpy


def greatest_common_divisor(a: int, b: int) -> int:
    """
    >>> greatest_common_divisor(4, 8)
    4
    >>> greatest_common_divisor(8, 4)
    4
    >>> greatest_common_divisor(4, 7)
    1
    >>> greatest_common_divisor(0, 10)
    10
    """
    return b if a == 0 else greatest_common_divisor(b % a, a)


class HillCipher:
    key_string = string.ascii_uppercase + string.digits
    # ambil x dan return x % len(key_string)
    modulus = numpy.vectorize(lambda x: x % 36)

    to_int = numpy.vectorize(lambda x: round(x))

    def __init__(self, encrypt_key: numpy.ndarray) -> None:
        self.encrypt_key = self.modulus(encrypt_key)
        self.check_determinant()
        self.break_key = encrypt_key.shape[0]

    def replace_letters(self, letter: str) -> int:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_letters('T')
        19
        >>> hill_cipher.replace_letters('0')
        26
        """
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_digits(19)
        'T'
        >>> hill_cipher.replace_digits(26)
        '0'
        """
        return self.key_string[round(num)]

    def check_determinant(self) -> None:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.check_determinant()
        """
        det = round(numpy.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            raise ValueError(
                f"determinant modular {req_l} of encryption key({det}) is not co prime "
                f"w.r.t {req_l}.\nTry another key."
            )

    def process_text(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.process_text('Testing Hill Cipher')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.process_text('hello')
        'HELLOO'
        """
        chars = [char for char in text.upper() if char in self.key_string]

        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)

        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.encrypt('testing hill cipher')
        'WHXYJOLM9C6XT085LL'
        >>> hill_cipher.encrypt('hello')
        '85FF00'
        """
        text = self.process_text(text.upper())
        encrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = numpy.array([vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def make_decrypt_key(self) -> numpy.ndarray:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.make_decrypt_key()
        array([[ 6, 25],
               [ 5, 26]])
        """
        det = round(numpy.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)
        det_inv = None
        for i in range(len(self.key_string)):
            if (det * i) % len(self.key_string) == 1:
                det_inv = i
                break

        inv_key = (
            det_inv
            * numpy.linalg.det(self.encrypt_key)
            * numpy.linalg.inv(self.encrypt_key)
        )

        return self.to_int(self.modulus(inv_key))

    def decrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(numpy.array([[2, 5], [1, 6]]))
        >>> hill_cipher.decrypt('WHXYJOLM9C6XT085LL')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.decrypt('85FF00')
        'HELLOO'
        """
        decrypt_key = self.make_decrypt_key()
        text = self.process_text(text.upper())
        decrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = numpy.array([vec]).T
            batch_decrypted = self.modulus(decrypt_key.dot(batch_vec)).T.tolist()[0]
            decrypted_batch = "".join(
                self.replace_digits(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        return decrypted


if __name__ == "__main__":
    import doctest

    doctest.testmod()
