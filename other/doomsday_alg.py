# doomsday algo atau biasa disebut dengan aturan kiamat
# adalah algoritma daripada penentuan hari dalam seminggu
# ia menyediakan kalender abadi karena kalender georgian
# bergerak dalam siklus 400 tahun
# https://id.wikinew.wiki/wiki/Doomsday_rule

DOOMSDAY_LEAP = [4, 1, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
DOOMSDAY_NOT_LEAP = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
WEEK_DAY_NAMES = {
    0: "Minggu",
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumat",
    6: "Sabtu",
}


def get_week_day(year: int, month: int, day: int) -> str:
    """
    Mengembalikan nama hari-minggu dari tanggal tertentu.
    >>> get_week_day(2021, 8, 17)
    'Selasa'
    """
    assert len(str(year)) > 2, "tahun seharusnya dalam format yyyy"
    assert 1 <= month <= 12, "bulan seharusnya antara 1 dan 12"
    assert 1 <= day <= 31, "hari seharusnya antara 1 dan 31"

    # penerapan algoritma kiamat

    century = year // 100
    century_anchor = (5 * (century % 4) + 2) % 7
    centurian = year % 100
    centurian_m = centurian % 12
    dooms_day = (
        (centurian // 12) + centurian_m + (centurian_m // 4) + century_anchor
    ) % 7
    day_anchor = (
        DOOMSDAY_NOT_LEAP[month - 1]
        if (year % 4 != 0) or (centurian == 0 and (year % 400) == 0)
        else DOOMSDAY_LEAP[month - 1]
    )
    week_day = (dooms_day + day - day_anchor) % 7
    return WEEK_DAY_NAMES[week_day]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
