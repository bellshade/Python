def mode(arr: list[int | float]) -> int | float:
    """
    mode atau dalam bahasa indonesia adalah modus
    modus dalam statiska merupaka nilai yang sering muncul
    dalam suatu kumpulan data.

    **Parameter**

    ---
    :param arr: parameter ini bertipe data list

    **Return**
    :param return: output ini muncul sebagai sesuai dengan item yang sering terjadi

    **Contoh**
    >>> data=[1,1,2,2,2,3,3]
    >>> mode(data)
    2
    """
    count = []
    for value in arr:
        # kita hitung jumlah frekuensi pada setiap value di array tersebut
        count.append(arr.count(value))
    combine = dict(zip(arr, count))
    memo = [a for a, b in combine.items() if b == max(count)]
    min_value = memo[0]
    result = None
    for value in memo:
        if value < min_value:
            min_value = value
    result = min_value
    if result == 1:
        raise ValueError("nan")
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
