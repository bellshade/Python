# section 1

def hello():
    print('Hello Bellshade !')
    
hello() # Hello!

# section 2

def hello(nama):
    print('Hello '+str(nama)+' !')
    
hello('Bellshade') # Hello Bellshade !

# section 3

def triangle(alas,tinggi):
    hasil = (alas * tinggi)/2
    print(hasil)
    
triangle(2,3)

# section 4

def triangle(alas,tinggi):
    hasil = (alas * tinggi)/2
    return hasil
    
print(triangle(2,3))

# section 5

def salam(waktu="Pagi"):
    greet = "Selamat " + str(waktu)
    return greet

print(salam("Siang")) # Selamat Siang
print(salam("Malam")) # Selamat Malam
print(salam("Sore")) # Selamat Sore
print(salam()) # Selamat Pagi

# section 6

def unlimited(*args):
    for item in args:
        print(item)
        
unlimited(1,2,3,4)
unlimited([1,2],[3,4])

# section 7

def unlimitedkeyword(**infinite):
    for key, value in infinite.items():
        print("index {} memiliki nilai {}".format(key,value))
        
unlimitedkeyword(a=2,b=1,c=3)
unlimitedkeyword(fname="Harry",lname="Potter")
