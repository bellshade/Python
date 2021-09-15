"""
Operator Pada Python ada 7 jenis, yaitu:

1. Arithmetic Operators (Operator Aritmatika)
    a. + (tambah)
    b. - (kurang)
    c. * (kali)
    d. / (bagi)
    e. // (Floor Division)
    f. %% (modulo)
    g. ** (pangkat)

2. Comparison Operators (Operator Pembanding)
    a. == (sama dengan)
    b. != (tidak sama dengan)
    c. > (lebih dari)
    d. < (kurang dari)
    e. >= (lebih dari atau sama dengan)
    f. <= (kurang dari atau sama dengan)

3. Logical Operators (Operator Logika)
    a. and (akan mengembalikan True jika kedua pembanding bersifat True)
    b. or (akan mengembalikan True jika salah satu pembanding bersifat True)
    c. not (akan mengembalikan True jika kedua pembanding bersifat False)

4. Membership Operators
    a. in (akan mengembalikan True jika nilai yang ditentukan berada di dalam objek)
    b. not in (akan mengembalikan True jika nilai yang ditentukan tidak dalam objek)

5. Identity Operators (Operator Identitas)
    a. is (akan mengembalikan True jika kedua variable adalah objek yang sama)
    b. is not (akan mengembalikan True jika kedua variable bukanlah objek yang sama)

6. Bitwise Operators (Operator Binary)
    a. & (Menjadikan setiap bit 1 jika kedua bit adalah 1)
    b. | (Menjadikan setiap bit 1 jika salah satu bit adalah 1)
    c. ^ (Menjadikan setiap bit 1 hanya jika salah satunya adalah 1)
    d. ~ (Membalikkan angka bit)
    e. << (Menambahkan angka 0 di kanan dan menghapus bit di paling kiri)
    g. >> (Menambahkan salinan bit paling kiri ke kiri dan menghapus bit paling kanan)

7. Assignment Operators

    |  Operator     |  Example      |  Same As      |
    |     =         |   x = 5       |   x = 5       |
    |     +=        |   x += 3      |   x = x + 3   |
    |     -=        |   x -= 3      |   x = x - 3   |
    |     *=        |   x *= 3      |   x = x * 3   |
    |     /=        |   x /= 3      |   x = x / 3   |
    |     %=        |   x %= 3      |   x = x % 3   |
    |     //=       |   x //= 3     |   x = x // 3  |
    |     **=       |   x **= 3     |   x = x ** 3  |
    |     &=        |   x &= 3      |   x = x & 3   |
    |     |=        |   x |= 3      |   x = x | 3   |
    |     ^=        |   x ^= 3      |   x = x ^ 3   |
    |     <<=       |   x <<= 3     |   x = x << 3  |
    |     >>=       |   x >>= 3     |   x = x >> 3  |

    nb: saya tidak membuat contoh ini karena ini adalah penyingkat kode

source: https://www.w3schools.com/python/python_operators.asp
"""

a = 10
b = 4
c = False
d = True
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Variables\n")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)

# Pemisah
print("\n==================\n")

# Arithmetic Operators

print("Arithmetic Operators\n")
print("10 + 4 =", a + b)
print("10 - 4 =", a - b)
print("10 * 4 =", a * b)
print("10 / 4 =", a / b)
print("10 ** 4 =", a ** b)
print("10 // 4 =", a // b)

# Pemisah
print("\n==================\n")

# Comparison Operators

print("Comparison Operators\n")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Pemisah
print("\n==================\n")

# Logical Operators
print("Logical Operators\n")
print("c and d:", c and d)
print("c or d:", c or d)
print("not c:", not c)

# Pemisah
print("\n==================\n")

# Membership Operators
print("Membership Operators\n")
print("a in e:", a in e)
print("a not in e:", a not in e)

# Pemisah
print("\n==================\n")

# Identity Operators
print("Identity Operators\n")
print("a is b:", a is b)
print("a is a:", a is a)
print("a is not b:", a is not b)

# Pemisah
print("\n==================\n")

# Bitwise Operators
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~ a:", ~a)
print("a << b:", a << b)
print("a >> b:", a >> b)
