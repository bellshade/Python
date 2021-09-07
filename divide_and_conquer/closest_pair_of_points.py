# Algoritma menemukan jarak antara pasangan titik terdekat
# pada n titik yang diberikan.
# Pendekatan yang digunakan -> Bagi dan taklukkan
# Poin diurutkan berdasarkan Xco-ord dan
# kemudian berdasarkan Yco-ord secara terpisah.
# Dan dengan menerapkan pendekatan membagi dan menaklukkan,
# jarak minimum diperoleh secara rekursif.

# time complexity: O(n * log n)


from typing import List, Tuple


def euclidan_distance_sqr(point1, point2):
    """
    >>> euclidan_distance_sqr([1, 2], [2, 4])
    5
    """
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def column_based_sort(array, column) -> List[tuple]:
    """
    >>> column_based_sort([(5, 1), (4, 2), (3, 0)], 1)
    [(3, 0), (5, 1), (4, 2)]
    """
    return sorted(array, key=lambda x: x[column])


def dis_between_closest_pair(points, point_count, min_dis=float("inf")) -> float:
    """
    pendekatan brute force untuk menemukan
    jarak antara titik pasangan terdekat
    >>> points = [(1, 2), (2, 4), (5, 7), (8, 9), (11, 0)]
    >>> dis_between_closest_pair(points, 5)
    5
    """
    for i in range(point_count - 1):
        for j in range(i + 1, point_count):
            current_dist = euclidan_distance_sqr(points[i], points[j])
            if current_dist < min_dis:
                min_dis = current_dist

    return min_dis


def dis_between_closest_in_strip(points, point_count, min_dis=float("inf")):
    """
    pasangan titik terdekat dalam strip
    >>> points = [(1, 2), (2, 4), (5, 7), (8, 9), (11, 0)]
    >>> dis_between_closest_in_strip(points, 5)
    85
    """

    for i in range(min(6, point_count - 1), point_count):
        for j in range(max(0, i - 6), i):
            current_dis = euclidan_distance_sqr(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis

    return min_dis


def closest_pair_of_points_sqr(points_sorted_on_x, points_sorted_on_y, point_count):

    """
    >>> points = [(1, 2), (3, 4)]
    >>> points2 = [(5,6), (7,8)]
    >>> closest_pair_of_points_sqr(points, points2, 2)
    8
    """

    if point_count <= 3:
        return dis_between_closest_pair(points_sorted_on_x, point_count)

    # rekursif
    mid = point_count // 2
    closets_in_left = closest_pair_of_points_sqr(
        points_sorted_on_y, points_sorted_on_y[mid:], mid
    )
    closets_in_right = closest_pair_of_points_sqr(
        points_sorted_on_y, points_sorted_on_y[mid:], point_count - mid
    )
    closest_pair_dis = min(closets_in_left, closets_in_right)

    cross_strip = []
    for point in points_sorted_on_x:
        if abs(point[0] - points_sorted_on_x[mid[0]]) < closest_pair_dis:
            cross_strip.append(point)

    closest_in_strip = dis_between_closest_in_strip(
        cross_strip, len(cross_strip), closest_pair_dis
    )

    return min(closest_pair_dis, closest_in_strip)


def closest_pair_of_points(points, length_points) -> float:
    """
    >>> point1 = [(2, 3), (12, 30)]
    >>> length_points = len([(2, 3), (12, 30)])
    >>> closest_pair_of_points(point1, length_points)
    28.792360097775937
    """

    point_sorted_on_x = column_based_sort(points, column=0)
    point_sorted_on_y = column_based_sort(points, column=1)

    return (
        closest_pair_of_points_sqr(point_sorted_on_x, point_sorted_on_y, length_points)
    ) ** 0.5


if __name__ == "__main__":
    import doctest

    doctest.testmod()
