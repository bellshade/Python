# Bilangan Prima adalah Bilangan yang habis dibagi
# oleh bilangan itu sendiri dan bilangan 1
def is_prime(num):
    # Mengecek apakah num merupakan bilangan negatif dan dibawah 2
    if num < 2:
        return "Bukan Bilangan Prima"
    # Perulangan disini dimulai dari 2 dikarenakan
    # bilangan prima dimulai dari 2 dan seterusnya
    for i in range(2, num, 1):
        # Jika num habis dibagi oleh i maka bilangan tersebut bukan Bilangan prima
        if num % i == 0:
            return "Bukan Bilangan Prima"
    return "Bilangan Prima"


print(is_prime(20))  # output "Bukan Bilangan Prima"
print(is_prime(5))  # output "Bilangan Prima"
