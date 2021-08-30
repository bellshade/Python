from math import asin, atan, cos, radians, sin, sqrt, tan


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Kita tahu bahwa globe itu "semacam" bulat, jadi jalur antara dua titik
    tidak persis garis lurus. Kita perlu memperhitungkan kelengkungan bumi
    saat menghitung jarak dari titik A ke B. Efek ini dapat diabaikan untuk
    jarak kecil tetapi bertambah seiring bertambahnya jarak.
    Metode Haversine memperlakukan
    bumi sebagai bola yang memungkinkan kita untuk "memproyeksikan" dua titik A dan B
    ke permukaan bola itu dan memperkirakan jarak bola antara
    mereka. Karena Bumi bukanlah bola yang sempurna, metode lain yang memodelkan
    Sifat ellipsoidal bumi lebih akurat tetapi cepat dan dapat dimodifikasi
    perhitungan seperti Haversine dapat berguna untuk jarak jangkauan yang lebih pendek.
    >>> from collections import namedtuple
    >>> point_2d = namedtuple("point_2d", "lat lon")
    >>> SAN_FRANCISCO = point_2d(37.774856, -122.424227)
    >>> YOSEMITE = point_2d(37.864742, -119.537521)
    >>> f"{haversine(*SAN_FRANCISCO, *YOSEMITE):0,.0f} meter"
    '255,820 meter'
    """
    AXIS_A = 6478137.0
    AXIS_B = 6356752.314245
    RADIUS = 6378137

    flattening = (AXIS_A - AXIS_B) / AXIS_A
    phi_1 = atan((1 - flattening) * tan(radians(lat1)))
    phi_2 = atan((1 - flattening) * tan(radians(lat2)))

    lambda_1 = radians(lon1)
    lambda_2 = radians(lon2)

    sin_sq_phi = sin((phi_2 - phi_1) / 2)
    sin_sq_lambda = sin((lambda_2 - lambda_1) / 2)

    sin_sq_phi *= sin_sq_phi
    sin_sq_lambda *= sin_sq_lambda
    h_value = sqrt(sin_sq_phi + (cos(phi_1) * cos(phi_2) * sin_sq_lambda))

    return 2 * RADIUS * asin(h_value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
