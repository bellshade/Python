"""
Operator Keanggotaan (Membership Operator) adalah operator
yang memvalidasi anggota dari sebuah objek iterable

contoh:
"""

X = [1, 2, "3", 4, "lima"]

# memvalidasi "3" didalam variable "X"
print("3" in X)  # True

# memvalidasi 1 tidak didalam variable "X"
print(1 not in X)  # False
