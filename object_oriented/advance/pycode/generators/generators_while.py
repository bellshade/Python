from typing import Union


# GENERATORS WHILE
class Generators:
    """
    Kelas ini secara default hanya akan menghasilkan 1x generate
    :param target_int: Untuk menentukan jumlah hasil generate
    :param max_repeat: Untuk membatas perulangan agar berhenti dan tidak overloop
    Jika kamu ingin mendapatkan hasil generate secara berkala hapus [return selft.res]

    >>> app = Generators(7)
    >>> app()
    2187
    """

    def __init__(self, target_int : Union[int, float], max_repeat : int = 5) -> None:
        self.tar_mul = target_int
        self.target_repeat_max = max_repeat

    def __call__(self):
        self.start_generate()

    def start_generate(self) -> None:
        self.indeks = 2

        try:
            while True:
                self.indeks += 1
                self.res = self.indeks ** self.tar_mul
                print(self.res)

                if self.indeks == self.target_repeat_max:
                    break

                return self.res
        except Exception:
            ...


def test_generate_dengan_attribute():
    app = Generators(7)
    assert app.start_generate() == 2187


app = Generators(7)

if __name__ == '__main__':
    app()
