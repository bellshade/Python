# while loop basic
a = 1

while a <= 5:
    print(a)
    a += 1
    
b = 5

while b >= 1:
    print(b)
    b -= 1
    
# break statement
c = 5

while c <= 5:
    print(c)
    if c == 3:
        break
    c += 1
    
# continue statement
d = 0

while d <= 5:
    d += 1
    if d == 3:
        continue
    print(d)
    
# else statement
e = 0

while e <= 5:
    print(e)
    e += 1
else:
    print("e tidak lebih dari 5")
    
