# Diberikan array dengan panjang n, max_subarray_sum() menemukan
# jumlah maksimum sub-array bersebelahan menggunakan metode bagi dan taklukkan.
# Kompleksitas waktu : O(n log n)


def max_sum_from_start(array):
    """
    Fungsi ini menemukan jumlah maksimum array yang berdekatan dari 0 indeks
    Parameter:
    array (daftar[int]) : array yang diberikan
    Return:
    max_sum (int): jumlah maksimum array bersebelahan dari 0 indeks
    """
    array_sum = 0
    max_sum = float("-inf")
    for num in array:
        array_sum += num
        if array_sum > max_sum:
            max_sum = array_sum

    return max_sum


def max_cross_array(array, left, mid, right):
    """
    Fungsi ini menemukan jumlah maksimum array kiri
    dan kanan yang berdekatan
    Parameter:
    larik, kiri, tengah, kanan (daftar[int], int, int, int)
    Return:
    (int) : jumlah maksimum dari jumlah yang
    berdekatan dari array kiri dan kanan
    """
    max_sum_of_left = max_sum_from_start(array[left : mid + 1][::-1])
    max_sum_of_right = max_sum_from_start(array[mid + 1 : right + 1])
    return max_sum_of_left + max_sum_of_right


def max_subarray_sum(array, left, right):
    """
    Jumlah sub-array bersebelahan maksimum,
    menggunakan metode bagi dan taklukkan
    Parameter:
    array, kiri, kanan (daftar[int], int, int):
    array yang diberikan, indeks kiri
    saat ini dan indeks kanan saat ini
    Return:
    int : jumlah maksimum sub-array yang berdekatan

    >>> array = [-2, -5, 6, -2, -3, 1, 5, -6]
    >>> array_length = len(array)
    >>> max_subarray_sum(array, 0, array_length - 1)
    7
    """
    if left == right:
        return array[right]

    mid = (left + right) // 2
    left_half_sum = max_subarray_sum(array, left, mid)
    right_half_sum = max_subarray_sum(array, mid + 1, right)
    cross_sum = max_cross_array(array, left, mid, right)

    return max(left_half_sum, right_half_sum, cross_sum)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
