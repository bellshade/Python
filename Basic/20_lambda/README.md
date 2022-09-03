# Lambda function

Lambda function atau dikenal juga dengan anonymous function
adalah sebuah function yang bisa menerima multiple arguments
tetapi hanya bisa melakukan satu ekspresi atau satu eksekusi.

Pada contoh berikut, kita melakukan perhitungan luas persegi
dengan satu argument yaitu sisi (s) dan satu ekspresi sisi*sisi.

```python
luas_persegi = lambda s: s ** 2
print(luas_persegi(4))
```

Contoh dari lambda function yang bisa menerima multiple argument
yaitu lambda function luas segitiga

```python
luas_segitiga = lambda a, t: (a * t) / 2
print(luas_segitiga(2, 3))
```

Lambda sendiri bisa menerima argumen secara tak terbatas
seperti pada contoh:

```python
infinite = lambda *input: sum(input)
print(infinite(1, 2, 3))
print(infinite(1, 2, 3, 4))
```

Bisa juga menerima argumen dengan keyword
```python
key_inf = lambda **kwargs: sum(kwargs.values())
print(key_inf(satu=1, dua=2, tiga=3))  # 6
print(key_inf(seven=7, eight=8, nine=9, ten=10))  # 34
```

Contoh penerapannya bisa kita lihat pada fungsi ```filter()```
yaitu
```python
li = [i for i in range(10)]
beyond_five = list(filter(lambda x: (x > 5), li))
print(beyond_five)
```

[Materi Selanjutnya](../21_regex)