from sympy import isprime
from sympy import primerange
from sympy import randprime
from sympy import primepi
from sympy import prime
from sympy import prevprime
from sympy import nextprime


# Mengecek apakah sebuah nilai adalah bilangan prima
print("Apakah 10 angka prima?", isprime(10))
print("Apakah 11 angka prima?", isprime(11))

# Men-generate bilangan prima dalam batasan tertentu
print("Tampilkan angka prima dari 1 sampai 10:")
for i in primerange(1, 10):
    print(i)

# Mengembalikan nilai random bilangan prima dalam batasan tertentu
print("Angka prima acak antara 1 sampai 100:", randprime(1, 100))

# Mengembalikan banyaknya bilangan prima kurang dari sama dengan nilai yang diinputkan
print("Jumlah angka prima kurang dari sama dengan 10:", primepi(10))

# Mengembalikan nilai ke n
# misalkan bilangan prima pertama adalah 2
# maka input yang diberikan adalah 1
print("Angka prima ke 1:", prime(1))

# Mengembalikan 1 angka prima sebelum angka input
print("Angka prima sebelum angka 7:", prevprime(7))

# Mengembalikan 1 angka prima setelah angka input
print("Angka prima setelah angka 7:", nextprime(7))
