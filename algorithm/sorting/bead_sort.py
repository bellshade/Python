# beard sort atau juga bisa disebut dengan gravity sort
# algoritma sorting ini terinspirasi dari fenomena alam
# dan dirancang dengan mengingat object yang jatuh dibawah
# pengaruh gravitasi

# beard sort hanya berfungsi untuk urutan bilangan
# bilat non-negatif


def bead_sort(sequence: list) -> list:
    """
    >>> bead_sort([6, 11, 12, 4, 1, 5])
    [1, 4, 5, 6, 11, 12]

    >>> bead_sort("coba string")
    Traceback (most recent call last):
    ...
    TypeError: Sequence harus berupa list dari non negatif
    """
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("Sequence harus berupa list dari non negatif")
    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence


if __name__ == "__main__":
    assert bead_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
