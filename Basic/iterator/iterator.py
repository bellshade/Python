fruits = ("apple", "banana", "cherry")

# fungsi iter() disini digunakan untuk membuat iterator
fruits_iter = iter(fruits)

# mengecek tipe data fruits_iter
print("Tipe data dari fruits_iter:", fruits_iter)

# Untuk mengakses isi dari iterator kita menggunakan fungsi next
print(next(fruits_iter))
print(next(fruits_iter))
print(next(fruits_iter))

# Kita juga dapat menggunakan for loop untuk mengulang suatu objek

print("\nMenggunakan For Loop:")

# hasil kode ini sama dengan yang diatas
for fruit in fruits:
    print(fruit)


# iterator juga bisa kita kustomisasi pada class
class MyNumbers:

    # dunder method iter
    def __iter__(self):
        self.fruits = ["apple", "banana", "cherry"]
        self.counter = 0
        return self

    # dunder method next
    def __next__(self):
        if self.counter < len(self.fruits):
            x = self.fruits[self.counter]
            self.counter += 1
            return x
        else:
            # StopIteration digunakan untuk menghentikan iterator
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

print("\nMengulang menggunakan Class:")
print(next(myiter))
print(next(myiter))
print(next(myiter))
