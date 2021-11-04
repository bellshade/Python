import math

"""
Fungsi-fungsi di bawah mengonversi masukan dalam
satuan radian, derajat, dan gradian. Fungsi yang dibuat
adalah fungsi untuk mengonversi :
1. radian ke derajat (radian_to_degree())
2. derajat ke radian (degree_to_radian())
3. radian ke gradian (radian_to_gradian())
4. gradian ke radian (gradian_to_radian())

>>> radian_to_degree(5)
286.4788975654116

>>> degree_to_radian(60)
1.0471975511965976

>>> radian_to_gradian(3)
190.9859317102744

>>> gradian_to_radian(53)
0.8325220532012952
"""


def radian_to_degree(radian: float) -> float:
    return radian * (180 / math.pi)


def degree_to_radian(degree: float) -> float:
    return degree * (math.pi / 180)


def radian_to_gradian(radian: float) -> float:
    return radian * (200 / math.pi)


def gradian_to_radian(gradian: float) -> float:
    return gradian * (math.pi / 200)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
