<p align="center">
  <img src="https://i.ibb.co/QQ4cfsR/generator.png" alt="Python Advance">
</p>

# Generators

Generators: Alat atau sumber daya yang akan menghasilkan jenis kode atau bahasa pemrograman komputer tertentu.

Dengan generator juga kita bisa membuat apapun baik itu Fake EmailDNS, User Fullname, HEX to RGB, dan masih banyak yang lainnya.

## Cara membuat kode generator sederhana

Kita bisa membuat angka acak mulai dari sekian ke sekian yang di kuadratkan berapapun nilai yang kita inginkan untuk di hasilkan.

### Membuat Generators dengan For

```py
from functools import wraps
from typing import Callable


# GENERATORS FOR
def Generators(func : Callable) -> Callable:


    @wraps(func)
    def start() -> int:
        i : int = 1
        for i in range(13, 50):
            i**func()
        return i
    return start


@Generators
def coba1():
    return 7


if __name__ == '__main__':
    coba1()

```

### Membuat Generators dengan While

```py
from typing import Union


# GENERATORS WHILE
class Generators:

    def __init__(self, target_int : Union[int, float], max_repeat : int = 5) -> None:
        self.tar_mul = target_int
        self.target_repeat_max = max_repeat

    def __call__(self):
        self.start_generate()

    def start_generate(self) -> Union[int, float]:
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


app = Generators(7)

if __name__ == '__main__':
    app()

```