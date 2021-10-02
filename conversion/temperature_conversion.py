"""
Algoritma Konversi Suhu
Satuan suhu yang tersedia: celcius, reamur, fahrenheit, kelvin
(argumen dari parameter 'dari' dan 'ke' berlaku sebaliknya)
Bahasa: Python
"""

def konversiSuhu(dari="celcius", ke="fahrenheit", suhu=0):
    # Celcius ke Reamur
    if (dari == "celcius" and ke == "reamur"):
        hasil = (4 / 5) * suhu
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Celcius ke Fahrenheit
    if (dari == "celcius" and ke == "fahrenheit"):
        hasil = (9 / 5) * suhu + 32
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Celcius ke Kelvin
    if (dari == "celcius" and ke == "kelvin"):
        hasil = suhu + 273
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Reamur ke Celcius
    if (dari == "reamur" and ke == "celcius"):
        hasil = (5 / 4) * suhu
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Reamur ke Fahrenheit
    if (dari == "reamur" and ke == "fahrenheit"):
        hasil = (9 / 4) * suhu + 32
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Reamure ke Kelvin
    if (dari == "reamur" and ke == "kelvin"):
        hasil = (5 / 4) * suhu + 273
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Fahrenheit ke Celcius
    if (dari == "fahrenheit" and ke == "celcius"):
        hasil = (5 / 9) * (suhu - 32)
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Fahrenheit ke Celcius
    if (dari == "fahrenheit" and ke == "celcius"):
        hasil = (4 / 9) * (suhu - 32)
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Kelvin ke Celcius
    if (dari == "kelvin" and ke == "celcius"):
        hasil = suhu - 273
        return tampilkanHasil(dari, ke, suhu, hasil)

    # Kelvin ke Reamur
    if (dari == "kelvin" and ke == "reamur"):
        hasil = (4 / 5) * (suhu - 273)
        return tampilkanHasil(dari, ke, suhu, hasil)

    return "Parameter Salah!\n"

def tampilkanHasil(dari, ke, suhu, hasil):
    return ("=== Konversi Suhu ===\n" +
            "Dari: " + dari + ", " + str(suhu) + "\n" +
            "Ke: " + ke + ", " + str(hasil) + "\n")


"""
Contoh implementasi
"""

# Celcius ke Fahrenheit
print(konversiSuhu("celcius", "fahrenheit", 32))

# Celcius ke Reamur
print(konversiSuhu("celcius", "reamur", 27))

# Fahrenheit ke Celcius
print(konversiSuhu("fahrenheit", "celcius", 60))

# Kelvin ke Fahrenheit
print(konversiSuhu("kelvin", "fahrenheit", 100))

# Reamur ke Kelvin
print(konversiSuhu("reamur", "kelvin", 18))
