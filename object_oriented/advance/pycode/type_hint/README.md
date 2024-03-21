<p align="center">
  <img src="https://i.ibb.co/W0Q8GbD/typehint.png" alt="Python Advance">
</p>

# Type Hinting

_**Type Hint**_ yang merupakan petunjuk tipe adalah solusi formal untuk secara statis menunjukkan tipe data dalam kode Python Kita. Itu ditentukan di PEP 484 dan diperkenalkan di Python 3.5.

Dari segi gaya penulisan sintaks type hinting, *PEP 8* merekomendasikan seperti berikut:

- Gunakan aturan normal untuk titik dua, yaitu tidak ada spasi sebelum dan satu spasi setelah titik dua ( text: str).
- Gunakan spasi di sekitar =tanda saat menggabungkan anotasi argumen dengan nilai default ( align: bool = True).
- Gunakan spasi di sekitar -> panah ( def headline(...) -> str).

Dalam melakukan penunjuk nilai tipe data kita bisa menggunakan module bantuan `typing` di package yang di sediakan. Dan saat ini ingin mencoba menjalankan program type hints kita, maka kita membutuhkan package atau module dari luar yakni `mypy` dengan menggunakan package `mypy` kita bisa mendebug kode type hinting kita.

Instalasasi mypy secara user global Environtment Python
```console
pip install mypy
```
Instalasasi mypy secara Developer Python Mode (Editable)
```console
pip install -e mypy
```

Berikut istilah penulisan Type Hintings
```py
from typing import Any, Callable, Union, List, Dict

nama: str
umur: int
uang: float
obj: dict
arr: list
args: Any
func: Callable
ambigu: Union[str, int, float]
data: List[Any]
data_obj: Dict[Any, Any]
```

## Contoh Penulisan Type Hintings Beserta Testingnya

```py
from typing import Callable

# variable with type hint
nama: str = 'Bellshade'


# definisi function with type hint with return function
def user(nama: str) -> Callable:
    """
    Fungsi untuk menangkap value dari fungsi id
    >>> nama = 'Bellshade'
    >>> user(nama)
    'Bellshade'
    """
    return id(nama)


# definisi function with type hint and return
def id(nama: str) -> str:
    return nama


# testing code
def test_runner_code():
    nama = 'Bellshade'
    assert user(nama) == 'Bellshade'


# running
if __name__ == '__main__':
    user(nama)

```