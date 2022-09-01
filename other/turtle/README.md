# Python turtle

Turtle adalah package python yang digunakan untuk mengenalkan tentang pemograman kepada anak-anak dengan cara mengoding dan kemudian menghasilkan gambar yang indah.

Di folder ini terdapat berbagai macam source code dari package turtle yagn menghasilkan gambar yang indah.

Contoh dari python turtle yang membentuk matahari:

```python
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
```
