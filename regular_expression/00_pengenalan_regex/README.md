# python regex

RegEx, atau ekspresi reguler, adalah urutan karakter yang membentuk pola pencarian.

 RegEx dapat digunakan untuk memeriksa apakah string berisi pola pencarian yang ditentukan.

 python memliki module regex yang disebut dengan ``re`` yang dapat digunakan untuk bekerja dengan ekspresi reguler

 contoh penggunaan regex untuk melihat apakah sebuah string dimulai dengan kata _saya_ dan diakhiri dengan _bellshade_

 ```python
import re

kata = "saya belajar python di bellshade"
regex_saya = re.search("^saya.*bellshade$", kata)
```