# logika percabangan

Logika percabangan adalah salah satu operator atau fungsi dimana mengambil dan memutuskan sesuatu dari sebuah pernyataan dan kemudian menghasilkan sebuah pernyataan jika suatu solusi dapat dipenuhi sebagai contoh, ``jika kamu kehujanan maka kamu menggunakan payung``, dalam contoh kodenya adalah

```python
cuaca = "hujan"
if cuaca == "hujan":
    print("gunakan payung")
```
contoh diatas merupakan contoh sederhana dari logika percabangan dimana jika cuaca hujan maka akan menggunakan payung, dan bagaimana jika value dari ``"hujan"`` kita ganti dengan cerah?. 

jika kita mengganti variabelnya dari ``cuaca = "hujan"``, maka program tidak menghasilkan apapun karena tidak membuat sebuah fungsi atau operator apapun jika ``cerah``, maka untuk membuat fungsi atau operator logika agar dapat mengambil data value berupa ``jika cerah maka tidak menggunakan payung``.

```python
cuaca = "cerah"
if cuaca == "hujan":
    print("gunakan payung")
# menggunakan fungsi elif
elif cuaca == "cerah":
    print("tidak menggunakan payung")
```
contoh diatas merupakan contoh sederhana dari logika percabangan dimana jika cuaca cerah maka tidak menggunakan payung, dan bagaimana jika value dari ``"cerah"``, ``"hujan"`` kita ganti dengan bebas?. 

```python
# membuat variabel dari cuaca
# dan membuat value "cerah"
cuaca = "cerah"
# logika jika cuaca hujan
if cuaca == "hujan":
    print("gunakan payung")
# menggunakan fungsi elif
# jika cuaca cerah
elif cuaca == "cerah":
    print("tidak menggunakan payung")
# menggunakan else jika kedua fungsi tidak terpenhi
# if dan elif
else:
    print("gunakan pakaian renang")
```
contoh diatas merupakan contoh sederhana dari logika percabangan dimana jika selain dari cuaca hujan dan cerah maka menampilkan ``gunakan pakaian renang``

[Materi Selanjutnya](../08_perulangan)