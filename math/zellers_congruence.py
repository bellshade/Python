# Kesesuaian Zeller adalah algoritma yang
# dirancang oleh Christian Zeller untuk menghitung
# hari dalam seminggu untuk setiap tanggal kalender
# Julian atau Gregorian. Ini dapat dianggap berdasarkan
# konversi antara hari Julian dan tanggal kalender.

import datetime


def zeller(date_input: str) -> str:
    """
    algoritma zellers
    Temukan hari dalam seminggu untuk hampir
    semua tanggal kalender Gregorian atau Julian
    >>> zeller('01-31-2021')
    'Tanggal kamu 01-31-2021 adalah Minggu'

    validasi jika bulan tidak sesuai
    >>> zeller('13-31-2020')
    Traceback (most recent call last):
    ...
    ValueError: bulan harus antara 1 - 12

    validasi jika tanggal tidak sesuai
    >>> zeller('01-33-2020')
    Traceback (most recent call last):
    ...
    ValueError: tanggal harus antara 1 - 31
    """
    hari = {
        "0": "Minggu",
        "1": "Senin",
        "2": "Selasa",
        "3": "Rabu",
        "4": "Kamis",
        "5": "Jumat",
        "6": "Sabtu",
    }

    # hari dalam minggu
    convert_datetime_days = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0}

    # validasi
    if not 0 < len(date_input) < 11:
        raise ValueError("harus memiliki 10 karakter string panjang")

    # mengambil data bulan
    m: int = int(date_input[0] + date_input[1])

    if not 0 < m < 13:
        raise ValueError("bulan harus antara 1 - 12")

    sep_1: str = date_input[2]

    if sep_1 not in ["-", "/"]:
        raise ValueError("tanda pemisah harus - atau /")

    # mengambil data hari
    d: int = int(date_input[3] + date_input[4])

    if not 0 < d < 32:
        raise ValueError("tanggal harus antara 1 - 31")

    sep_2: str = date_input[5]

    if sep_2 not in ["-", "/"]:
        raise ValueError("tanda pemisah harus - atau /")

    # mengambil data tahun
    y: int = int(date_input[6] + date_input[7] + date_input[8] + date_input[9])

    # validasi
    if not 45 < y < 8500:
        raise ValueError("Tahun di luar jangkauan. Harus ada semacam batasan ... kan?")

    # mengambil objek dari datetime untuk validasi
    date_ck = datetime.date(int(y), int(m), int(d))

    if m <= 2:
        y = y - 1
        m = m + 12

    c: int = int(str(y)[:2])
    k: int = int(str(y)[2:])
    t: int = int(2.6 * m - 5.39)
    u: int = int(c / 4)
    v: int = int(k / 4)
    x: int = int(d + k)
    z: int = int(t + u + v + x)
    w: int = int(z - (2 * c))
    f: int = round(w % 7)

    if f != convert_datetime_days[date_ck.weekday()]:
        raise AssertionError("tanggalnya dinilai salah. Hubungi developer.. :v")

    response: str = f"Tanggal kamu {date_input} adalah {hari[str(f)]}"

    return response


if __name__ == "__main__":
    import doctest

    doctest.testmod()
