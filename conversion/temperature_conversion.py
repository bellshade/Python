"""
Algoritma Konversi Suhu

Satuan suhu yang tersedia: celcius, reamur, fahrenheit, kelvin
(argumen dari parameter 'dari' dan 'ke' berlaku sebaliknya)

>>> konversi_suhu("celcius", "fahrenheit", 32)
'=== Konversi Suhu ===\\nDari: celcius, 32\\nKe: fahrenheit, 89.6\\n'

>>> konversi_suhu("kelvin", "fahrenheit", 100)
'Parameter Salah!\\n'
"""


def konversi_suhu(dari="celcius", ke="fahrenheit", suhu=0):
    try:
        kamus_suhu = {
            "celcius": {
                "reamur": (4 / 5) * suhu,
                "fahrenheit": (9 / 5) * suhu + 32,
                "kelvin": suhu + 273,
            },
            "reamur": {
                "celcius": (5 / 4) * suhu,
                "fahrenheit": (9 / 4) * suhu + 32,
                "kelvin": (5 / 4) * suhu + 273,
            },
            "fahrenheit": {
                "celcius": (5 / 9) * (suhu - 32),
                "reamur": (4 / 9) * (suhu - 32),
            },
            "kelvin": {
                "celcius": suhu - 273,
                "reamur": (4 / 5) * (suhu - 273),
            },
        }

        hasil = round(kamus_suhu[dari][ke], 2)
        return format_hasil(dari, ke, suhu, hasil)
    except KeyError:
        return "Parameter Salah!\n"


def format_hasil(dari, ke, suhu, hasil):
    return "=== Konversi Suhu ===\n" f"Dari: {dari}, {suhu}\n" f"Ke: {ke}, {hasil}\n"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Celcius ke Fahrenheit
    print(konversi_suhu("celcius", "fahrenheit", 32))

    # Celcius ke Reamur
    print(konversi_suhu("celcius", "reamur", 27))

    # Fahrenheit ke Celcius
    print(konversi_suhu("fahrenheit", "celcius", 60))

    # Kelvin ke Fahrenheit
    print(konversi_suhu("kelvin", "fahrenheit", 100))

    # Reamur ke Kelvin
    print(konversi_suhu("reamur", "kelvin", 18))
