# Circle Sort adalah algoritma pengurutan
# berbasis rekursif yang membandingkan dan
# menukar elemen-elemen dari ujung ke tengah,
# berulang sampai array tersortir.

# Bandingkan elemen paling kiri dengan paling kanan.
# Jika elemen kiri lebih besar, tukar dengan elemen kanan.
# Lanjutkan ke tengah array, lalu lakukan rekursi.

def circle_sort(collection: list[int]) -> list[int]:
    """
    contoh
    >>> circle_sort([5, 3, 2, 8, 1, 4])
    [1, 2, 3, 4, 5, 8]
    >>> circle_sort([10, 20, -5, 7, 3])
    [-5, 3, 7, 10, 20]
    """

    def circle_sort_rec(arr: list[int], left: int, right: int) -> bool:
        if left == right:
            return False
        swapped = False
        l, r = left, right
        while l < r:
            if arr[l] > arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
                swapped = True
            l += 1
            r -= 1
        if l == r and arr[l] > arr[r + 1]:
            arr[l], arr[r + 1] = arr[r + 1], arr[l]
            swapped = True
        mid = (right - left) // 2 + left
        left_swapped = circle_sort_rec(arr, left, mid)
        right_swapped = circle_sort_rec(arr, mid + 1, right)
        return swapped or left_swapped or right_swapped

    while circle_sort_rec(collection, 0, len(collection) - 1):
        pass
    return collection


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    data: list[int] = [10, -2, 7, 4, 3]
    unsorted: list[int] = [int(item) for item in data]
    print(f"data yang belum di sorting adalah {unsorted}")
    print(f"data yang sudah di sorting {circle_sort(unsorted)}")
