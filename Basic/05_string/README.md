# String

seperti yang dijelaskan pada materi sebelumnya, String adalah salah satu tipe data
pada python yang berfungsi untuk menghasilkan tipe data string seperti huruf abjad atau simbol lain

## Mendeklarasikan variabel string
```py
kata_pertama = "warung"
```


## Multiline String
String juga dapat dideklarasikan dengan cara berikut

```py
kata_saya = """indonesia adalah negara yang indah
berada di bawah garis khatulistiwa
aku cinta indonesia
"""
```

## Mencetak tipe data string
```py
print(kata_saya)
```

## Mengkapitalisasi setiap karakter pada string
```py
print(kata_pertama.upper())
```

## Membuat setiap karakter pada string menjadi huruf kecil
```py
print(kata_pertama.lower())
```


## Mengambil salah satu karakter dari string
```py
print(kata_pertama[0])
```

## Menghitung jumlah karatker dari string
```py
print(len(kata_pertama))
```

## Mengecek kata khusus dalam sebuah string
```py
print("indonesia" in kata_saya)
```

[Materi Selanjutnya](../06_input_output)