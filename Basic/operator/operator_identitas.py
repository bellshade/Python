"""
Operator Identitas adalah operator yang digunakan 
untuk mengecek apakah nilai dari suatu varibel 
berada pada memori yang sama atau tidak

contoh
"""

# variabel
x = "Python"
y = "Cobra"
z = "Python"
ular1 = ["Python", "Cobra", "Sanca"]
ular2 = ["Python", "Cobra", "Sanca"]


# mengecek apakah nilai dari variabel x dan y 
# ada pada memori yang sama 
print("x is y = ", x is y) # False

# mengecek apakah nilai dari variabel x dan z 
# ada pada memori yang sama 
print("x is z = ", x is z) # True

# mengecek apakah nilai dari variabel 
# ular1 dan ular2 ada pada memori yang sama
print("ular1 is ular2 = ", ular1 is ular2) # False
print("\n")

# mengecek apakah nilai dari variabel 
# ular1 dan ular2 tidak pada memori yang sama
print("x is not y = ", x is not y) # True

# mengecek apakah nilai dari variabel 
# ular1 dan ular2 tidak pada memori yang sama
print("x is not z = ", x is not z) # False

# mengecek apakah nilai dari variabel 
# ular1 dan ular2 tidak pada memori yang sama 
print("ular1 is ular2 = ", ular1 is not ular2) # True

