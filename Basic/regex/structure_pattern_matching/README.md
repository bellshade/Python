# structure pattern matching python

structure pattern matching, diperkenalkan oleh pencipta bahasa python _guido van rossum_ dan sejumlah kontributor lainnya pada 3.10 telah mengenalkan fungsi ini. apakah itu structur pattern matching?.

pencocokan pola struktural memperkenalkan pernyataan ``match/case`` dan sintaks pola ke python. ``match/case`` memberikan struktur logika seperti pernyataan switch di C/C++/Java/Javascript. mencocokkan nilai subjek dengan satu atau lebih kasus

**hanya pada python versi 3.10**, jika tidak memilikinya kamu bisa menginstallnya [disni](https://www.python.org/downloads/release/python-3100a6/)

```python
match ekspresi:
    case pattern_pertama:
        # perintah
    case pattern_kedua:
        # perintah
```

contoh sederhana
```python
def hari(hari_ke):
    match hari_ke:
        case 1:
            return "senin"
        case 2:
            return "selasa"
        case 3:
            return "rabu"
        case 4:
            return "kamis"
        case 5:
            return "jumat"
        case 6:
            return "sabtu"
        case 7:
            return "minggu"
```

atau bisa juga penggunaan pada tipe input, dan jika pernyataan tidak terpenuhi kita bisa menggunakan pola wildcard atau underscore ``_``
```python
hari_ke = int(input("masukkan angka hari dalam seminggu"))
match hari_ke:
    case 1:
        print("senin")
    case 2:
        print("selasa")
    case 3:
        print("rabut")
    case 4:
        print("kamis")
    case 5:
        print("jumat")
    case 6:
        print("sabtu")
    case 7:
        print("minggu")
    case _:
        print("masukkan angka hari dalam seminggu")
```
