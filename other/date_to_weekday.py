from calendar import day_name
from datetime import datetime


def date_to_weekday(inp_date: str) -> str:
    """
    merubah string tanggal ke hari
    param
    - inp_date: string
    ret
    mengembalikan string dalam bentuk hari
    contoh penggunaan
    >>> date_to_weekday("7/8/2035")
    'Tuesday'
    """
    day, month, year = (int(x) for x in inp_date.split("/"))
    if year % 100 == 0:
        year = "00"
    new_base_date: str = (
        f"{day}/{month}/{year%100} 0:0:0"  # lgtm [py/percent-format/wrong-arguments]
    )
    date_time_obj: datetime.date = datetime.strptime(new_base_date, "%d/%m/%y %H:%M:%S")
    out_put_day: int = date_time_obj.weekday()
    return day_name[out_put_day]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
